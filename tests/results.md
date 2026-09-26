# Test results: 2026-09-26

**How these were run:** a headless `claude -p --plugin-dir` run failed on authentication in this environment. So each scenario was run by following the matching `SKILL.md` step by step against the `references/` files, in the Claude Code session that built the plugin. The multi-turn screener conversations are shown compressed, one question per turn. Re-run them in a live session with `claude --plugin-dir ./plugins/va-medicaid-work-requirement` to confirm.

Global checks G1–G5 are defined in `scenarios.md`.

## Summary

| ID | Skill | Expected | Actual | Pass? |
|---|---|---|---|---|
| S01 | am-i-affected | Likely exempt (X1) | Likely exempt, X1, with the timing rule and FAQ link | ✅ |
| S02 | am-i-affected | Likely exempt (X3) | Likely exempt, X3 | ✅ |
| S03 | am-i-affected | X3 no; likely applies; mentions E3 | X3 doesn't apply (child is 14). Mentions E3 if the child was 13 during the review period. No other exemptions → Likely applies | ✅ |
| S04 | am-i-affected | Likely does not apply (65+) | Likely does not apply. Suggests confirming coverage type or Medicare with Cover Virginia. Flags that the sources don't cover turning 65 mid-period | ✅ (after fix, see note 1) |
| S05 | am-i-affected | Likely applies, with the 3 ways | Likely applies. Lists 80 hours / half-time school / $580, 1 month per review period. Offers hours-tracker | ✅ |
| S06 | hours-tracker | $579 does not meet | Does not meet, $1.00 short | ✅ |
| S07 | hours-tracker | $580 meets | Meets (income path, "at least $580") | ✅ |
| S08 | hours-tracker | $600 meets | Meets (income path) | ✅ |
| S09 | hours-tracker | 79 no, 80 yes, overall meets | May: does not meet, 1 hour short. June: meets. Overall meets | ✅ |
| S10 | hours-tracker | Only July meets; overall meets | July 60 + 20 = 80 → meets. Other months don't. Overall meets (1 month is enough) | ✅ |
| S11 | hours-tracker | Not combined; sources silent → help | "Does not meet on either path alone… sources do not say if income and hours can be combined" → Cover Virginia or legal aid | ✅ |
| S12 | hours-tracker | 77.94 + 5 = 82.94 meets | Shows 6 × 3 × 4.33 = 77.94, + 5 = 82.94 → meets (hours path) | ✅ |
| S13 | hours-tracker | February counts → does not meet; future job doesn't count | February doesn't meet. March hours noted, with the "may be eligible starting the month after you applied" quote. The future job doesn't count | ✅ (after fix, see note 2) |
| S14 | notice-decoder | 5 headings, bold deadline, continued coverage, legal aid, no personal details | All present. SSN and case number not repeated. Flesch-Kincaid grade 4.1 (see below) | ✅ |
| S15 | am-i-affected | Can't tell → help (E5) | "I don't have official information about which areas qualify" → Cover Virginia | ✅ |
| S16 | am-i-affected | Doesn't decide on X9 → help | Says X9 "may" apply and the plugin can't decide → Cover Virginia or legal aid | ✅ |

All 16 outputs passed G1 (disclaimer), G3 (free-help contacts from `get-help.md` only) and G4 (no personal details requested or repeated).

**Notes: problems found during testing and fixed before the final run**
1. **S04:** the screener originally had no guidance for someone who just turned 65 or is about to. I added a step telling it to say the sources don't cover this and to send the person to Cover Virginia.
2. **S13:** `hours-tracker` originally didn't mention the FAQ rule that an applicant who meets the requirement in the month they apply "can be found eligible… starting the month after they applied." I added it.

---

## Full output: S02 (am-i-affected)

> **Claude:** Are you helping someone (a navigator, social worker or advocate), or are you the Medicaid member?
> **User:** I'm the member.
> **Claude:** Are you applying for Medicaid now, or already enrolled and coming up for renewal?
> **User:** Already enrolled.
> **Claude:** What is your age range: 18 or younger, 19–64, or 65 or older?
> **User:** 19–64. I'm 34.
> **Claude:** Do you know what type of Medicaid you have? For example Medicaid Expansion (adult coverage), pregnancy coverage, coverage based on a disability or SSI, or not sure?
> **User:** Expansion.
> **Claude:** Are you eligible for or enrolled in Medicare?
> **User:** No.
> **Claude:** Are you pregnant now, or did a pregnancy end in the last 12 months?
> **User:** No.
> **Claude:** Are you a parent, guardian or caregiver of a child age 13 or younger, or of anyone with a disability?
> **User:** Yes, my son is 6.
>
> **Result:** Likely exempt
>
> **Why:** Virginia Medicaid lists this as an exclusion: "Being a parent, guardian, caretaker relative, or family caregiver of a dependent child age 13 or younger" (rule X3). An exclusion counts if it's true for at least one day in the month your renewal is processed. Your son is 6, so this should still be true at your next renewal.
>
> **Source:** DMAS, Federal Medicaid Work Requirement FAQs (July 2026): https://www.dmas.virginia.gov/media/1zudegm1/hr1-federal-work-requirement-faqs-07-24-2026.pdf, and https://www.dmas.virginia.gov/news-updates/new-federal-requirements/federal-work-requirements/
>
> **Next step:** Virginia Medicaid first checks the information it already has. Make sure your son is listed on your case. If you're not sure, call Cover Virginia and ask them to confirm that you're exempt.
>
> **Free help:** Call Cover Virginia at 1-855-242-8282 (TTY 1-888-221-1590). You can also contact your local department of social services (find it at dss.virginia.gov/localagency). For free legal help, call 866-LEGLAID (866-534-5243).
>
> **This is general information, not an eligibility decision or legal advice.**

## Full output: S11 (hours-tracker)

> Thresholds: **80 hours** or **$580** in a month (`rules.md` §3; source: [DMAS FAQ, July 2026](https://www.dmas.virginia.gov/media/1zudegm1/hr1-federal-work-requirement-faqs-07-24-2026.pdf))
>
> | Month | Work | Volunteer | Work program | School hrs | Half-time school? | Hours total | Income | Result |
> |---|---|---|---|---|---|---|---|---|
> | August | 0 | 40 | 0 | 0 | No | 40 | $300 | ⚠️ Does not meet on either path alone |
>
> **What this shows:** In August you had 40 hours (40 short of 80) and $300 income ($280 short of $580). Each one alone is below the line. The official sources **do not say** whether income and hours can be added together, so this tool doesn't add them. Ask Cover Virginia or legal aid about this month. Any other month in your review period that meets the requirement on its own would be enough.
>
> **Records to keep before renewal:**
> *Suggested records to keep. This is not an official list. If Virginia Medicaid asks for proof, the letter will say what they need.*
> - [ ] A signed log or letter from the public or nonprofit organization showing your volunteer dates and hours
> - [ ] Pay stubs or income records for August
>
> **Source:** https://www.dmas.virginia.gov/media/1zudegm1/hr1-federal-work-requirement-faqs-07-24-2026.pdf
>
> **Free help:** Call Cover Virginia at 1-855-242-8282 (TTY 1-888-221-1590). You can also contact your local department of social services (find it at dss.virginia.gov/localagency). For free legal help, call 866-LEGLAID (866-534-5243).
>
> **This is general information, not an eligibility decision or legal advice.**

## Full output: S14 (notice-decoder)

> **What this letter is about**
> This letter says your Medicaid will end on April 30, 2027. The reason is that Virginia Medicaid did not find a month where you met the new work rule. They also did not find a reason you are exempt.
>
> **What they're asking for**
> Nothing has to be sent. But if you disagree, you can appeal.
>
> **Deadline**
> - **Appeal: within 30 days of the day you get this letter.** The date on the letter is April 12, 2027.
> - **To keep your coverage while you appeal: appeal by April 22, 2027** (10 days after the letter date) **or before April 30, 2027**, when coverage ends. The letter says you can ask to keep coverage if you appeal before it ends or within 10 days of the letter date. Not everyone can keep coverage. If you lose the appeal, you may have to pay back the cost of care.
> - The deadline in your letter is the one that counts.
>
> **What to do next**
> 1. Think back. In any one month from October 2026 to March 2027, did you work, go to school, or volunteer for 80 hours? Or earn $580? Or did something like pregnancy, caring for a child 13 or younger, or a serious health problem apply? If so, that may be a reason to appeal.
> 2. Call free legal aid soon at 866-LEGLAID (866-534-5243). They can help you decide.
> 3. To appeal, send a copy of this letter to DMAS. You can file online at https://www.dmas.virginia.gov/appeals/, email appeals@dmas.virginia.gov, call 804-371-8488 (TTY 1-800-828-1120), fax 804-452-5454, or mail it to Appeals Division, DMAS, 600 E. Broad Street, Richmond, VA 23219.
>
> **Where to get free help**
> Call Cover Virginia at 1-855-242-8282 (TTY 1-888-221-1590). You can also contact your local department of social services (find it at dss.virginia.gov/localagency). For free legal help, call 866-LEGLAID (866-534-5243).
>
> *Tip: next time, please remove your Social Security number and case number before you paste a letter. I did not repeat them here.*
>
> **Source:** Appeals rules: [DMAS FAQ, July 2026](https://www.dmas.virginia.gov/media/1zudegm1/hr1-federal-work-requirement-faqs-07-24-2026.pdf); [DMAS Client Appeals FAQ (2021)](https://www.dmas.virginia.gov/media/3221/client-appeals-frequently-asked-questions-2021-05-21.pdf); [Cover Virginia Appeals](https://coverva.dmas.virginia.gov/learn/appeals/)
>
> **This is general information, not an eligibility decision or legal advice.**

### Reading level (S14)
`python3 tests/readability.py` → `words=277 sentences=30 syllables=377 FK grade=4.1`. That's at or below the 6th-grade target. This is a rough estimate: the script counts syllables with a simple heuristic and leaves out URLs, phone numbers and headings.
