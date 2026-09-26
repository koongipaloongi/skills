# Test results: 2026-09-26 (re-run after the September 2026 FAQ update)

**How these were run:** each scenario was run by following the matching `SKILL.md` step by step against the updated `references/` files, in a Claude Code session. A headless `claude -p` run couldn't sign in in this environment. The screener conversations are shown compressed. Re-run them in a live session with `claude --plugin-dir ./plugins/va-medicaid-work-requirement` (from the repo root) to confirm. The same session wrote both the expected and the actual results, so treat this as a logic check, not independent QA.

Global checks G1–G5 are defined in `scenarios.md`.

## Summary

| ID | Skill | Expected | Actual | Pass? | Changed by Sept FAQ? |
|---|---|---|---|---|---|
| S01 | am-i-affected | Likely exempt (X1, applies now) | Likely exempt, X1 | ✅ | Timing note simplified |
| S02 | am-i-affected | Likely exempt (X3) | Likely exempt, X3 | ✅ | |
| S03 | am-i-affected | X3 no → likely applies; E3 if the child was 13 at any time since the last renewal | As expected | ✅ | E3 window is now "anytime since last renewal" |
| S04 | am-i-affected | Likely does not apply (65+) | As expected, flags the mid-period gap | ✅ | |
| S05 | am-i-affected | Likely applies; 3 ways to meet it | As expected; half-time now described as "usually about 6 credit hours, as the school defines it" | ✅ | Half-time wording |
| S06 | hours-tracker | $579 → does not meet | Does not meet, $1.00 short | ✅ | |
| S07 | hours-tracker | $580 → meets | Meets (income) | ✅ | |
| S08 | hours-tracker | $600 → meets | Meets (income) | ✅ | |
| S09 | hours-tracker | 79 no / 80 yes → overall meets | As expected | ✅ | |
| S10 | hours-tracker | July 60 + 20 = 80 → meets | As expected | ✅ | |
| S11 | hours-tracker | $300 + 40 hours not combined → get help | As expected. Notes that FAQ Q19 covers combining activities but not income | ✅ | |
| S12 | hours-tracker | Eric example: 60 + 16 (estimate) + 12 = 88 → meets; no ×3 × 4.33 | 4 × 4 = 16, labeled "estimate based on DMAS's example"; 88 → meets. Adds "confirm with Cover Virginia," because without the school hours it would be 72 | ✅ | **Yes**: the formula was replaced |
| S13 | hours-tracker | February doesn't meet; FAQ silent on qualifying in the application month → ask Cover Virginia | As expected; no promise of eligibility the next month | ✅ | **Yes**: the old "month after" sentence was removed |
| S14 | notice-decoder | 5 headings, bold deadline, continued coverage, legal aid, no personal details | As expected; the appeals portal link is now the AIMS portal | ✅ | Link only |
| S15 | am-i-affected | E5 unknown → get help | As expected | ✅ | |
| S16 | am-i-affected | X9 may apply; more guidance coming; no doctor's note in 2027 | As expected | ✅ | **Yes** |
| S17 | am-i-affected | SSDI → likely exempt (X10) | Likely exempt; quotes FAQ Q9 | ✅ | **New** |
| S18 | am-i-affected | E7 may apply; how to request is to be announced; no "must request" | As expected | ✅ | **New** |
| S19 | am-i-affected | Renewal on Jan 31, 2027 → doesn't apply yet at that renewal | As expected; cites FAQ Q4 | ✅ | **New** |
| S20 | hours-tracker | 6 credits → "usually half-time," confirm with the school | As expected; month left unmarked until they confirm | ✅ | **New** |
| S21 | notice-decoder | Notice of Non-Compliance: bold response deadline, ways to send, no personal details | As expected | ✅ | **New** |
| S22 | hours-tracker | First renewal, May 2026 counts → meets | As expected; cites the "Sarah" example | ✅ | **New** |

All 22 outputs pass G1 (disclaimer), G3 (contacts only from `get-help.md`) and G4 (no personal details requested or repeated).

**Problem found while re-testing, and fixed:** for S22, `hours-tracker` step 2 only said "any one month since their last renewal." I added an explicit note that a member's first renewal under the new rule can look back over the previous 12-month coverage period, and that renewals before March 31, 2027 aren't subject to it yet.

---

## Full output: S12 (hours-tracker)

> Thresholds: **80 hours** or **$580** in a month (`rules.md` §3; source: [DMAS FAQ, Sept 2026](https://www.dmas.virginia.gov/media/cyvdt2wd/hr1-work-requirement-faqs-09-15-26.pdf))
>
> | Month | Work | Volunteer | Work program | School hrs | Half-time school? | Hours total | Income | Result |
> |---|---|---|---|---|---|---|---|---|
> | September | 60 | 12 | 0 | 16* | No | 88 | n/a | ✅ Meets (hours path) |
>
> \*School hours: 4 credit hours a week × 4 = **16 monthly hours**. This is an **estimate based on DMAS's example** (FAQ Q19: "four credit hours a week" counted as "16 monthly hours of educational program credit"). DMAS doesn't give an exact formula.
>
> **What this shows:** Your work, volunteering and school add up to 88 hours, which is more than 80. DMAS says these can be added together (FAQ Q19). Without the school hours you'd have 72, so it's worth confirming how Virginia Medicaid counts your credits. Call Cover Virginia to check.
>
> **Records to keep before renewal:**
> *Suggested records to keep. This is not an official list. In 2027, what you report on your application or renewal is usually enough. If Virginia Medicaid needs more, they'll send a notice, and you'll have 30 days to respond.*
> - [ ] Pay stubs, or a letter from your employer, showing September hours
> - [ ] A signed log or letter from the nonprofit showing your volunteer dates and hours
> - [ ] An enrollment verification from your school showing your credit hours
>
> **Source:** https://www.dmas.virginia.gov/media/cyvdt2wd/hr1-work-requirement-faqs-09-15-26.pdf
>
> **Free help:** Call Cover Virginia at 1-855-242-8282 (TTY 1-888-221-1590). You can also contact your local department of social services (find it at dss.virginia.gov/localagency). For free legal help, call 866-LEGLAID (866-534-5243).
>
> **This is general information, not an eligibility decision or legal advice.**

## Full output: S17 (am-i-affected, compressed)

> Helper or member → member. Applying or enrolled → enrolled, next renewal in June 2027. Age → 19–64 (45). Coverage type → Expansion. Medicare → no. Pregnant → no. Child 13 or younger → no. SSI or SSDI → **yes, SSDI.**
>
> **Result:** Likely exempt
>
> **Why:** Virginia Medicaid's FAQ says: "Yes, you are exempt if you receive Supplemental Security Income (SSI) or Social Security Disability Insurance (SSDI)." (rule X10). In 2027, what you report on your renewal form is usually enough to show this.
>
> **Source:** DMAS FAQ, updated September 2026, Q9: https://www.dmas.virginia.gov/media/cyvdt2wd/hr1-work-requirement-faqs-09-15-26.pdf
>
> **Next step:** When your renewal form comes, fill it out fully and say that you get SSDI. If you're not sure Virginia Medicaid has this on file, call Cover Virginia.
>
> **Free help:** Call Cover Virginia at 1-855-242-8282 (TTY 1-888-221-1590). You can also contact your local department of social services (find it at dss.virginia.gov/localagency). For free legal help, call 866-LEGLAID (866-534-5243).
>
> **This is general information, not an eligibility decision or legal advice.**

## Full output: S21 (notice-decoder)

> **What this letter is about**
> Virginia Medicaid needs more information. They want to know if you met the work rule, or if you are exempt from it. If they don't get it, your coverage may end.
>
> **What they're asking for**
> - Proof of your work, school, volunteer or training hours, or your income, for any one month since your last renewal, **or**
> - Information about an exemption that applies to you (for example, pregnancy, caring for a child 13 or younger, or getting SSI or SSDI).
>
> **Deadline**
> - **Send it by June 2, 2027.** This is the date in your letter. DMAS gives 30 days to respond.
>
> **What to do next**
> 1. Pick one month when you worked, went to school or volunteered for 80 hours, or earned $580. Or pick the exemption that fits you.
> 2. Send the information in one of these ways:
>    - Mail it to Cardinal Care Correspondence Center, PO Box 1198, Richmond, VA 23218.
>    - Upload it at commonhelp.virginia.gov.
>    - Call Cover Virginia at 1-855-242-8282 (TTY 1-888-221-1590). Some information can be given over the phone.
> 3. If you can't meet the deadline or aren't sure what to send, call Cover Virginia or legal aid right away.
>
> **Where to get free help**
> Call Cover Virginia at 1-855-242-8282 (TTY 1-888-221-1590). You can also contact your local department of social services (find it at dss.virginia.gov/localagency). For free legal help, call 866-LEGLAID (866-534-5243).
>
> **Source:** [DMAS FAQ, Sept 2026, Q20](https://www.dmas.virginia.gov/media/cyvdt2wd/hr1-work-requirement-faqs-09-15-26.pdf)
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
> 1. Think back. In any one month since your last renewal, did you work, go to school, or volunteer for 80 hours? Or earn $580? Or did something like pregnancy, caring for a child 13 or younger, getting SSI or SSDI, or a serious health problem apply? If so, that may be a reason to appeal.
> 2. Call free legal aid soon at 866-LEGLAID (866-534-5243). They can help you decide.
> 3. To appeal, send a copy of this letter to DMAS. You can file online at https://dmas.virginia.gov/appeals/appeals-portal/, email appeals@dmas.virginia.gov, call 804-371-8488 (TTY 1-800-828-1120), fax 804-452-5454, or mail it to Appeals Division, DMAS, 600 E. Broad Street, Richmond, VA 23219.
>
> **Where to get free help**
> Call Cover Virginia at 1-855-242-8282 (TTY 1-888-221-1590). You can also contact your local department of social services (find it at dss.virginia.gov/localagency). For free legal help, call 866-LEGLAID (866-534-5243).
>
> *Tip: next time, please remove your Social Security number and case number before you paste a letter. I did not repeat them here.*
>
> **Source:** Appeals rules: [DMAS FAQ, Sept 2026, Q21](https://www.dmas.virginia.gov/media/cyvdt2wd/hr1-work-requirement-faqs-09-15-26.pdf); [DMAS Client Appeals FAQ (2021)](https://www.dmas.virginia.gov/media/3221/client-appeals-frequently-asked-questions-2021-05-21.pdf); [Cover Virginia Appeals](https://coverva.dmas.virginia.gov/learn/appeals/)
>
> **This is general information, not an eligibility decision or legal advice.**

### Reading level (S14)
`python3 tests/readability.py` → `words=281 sentences=30 syllables=382 FK grade=4.1`. That's at or below the 6th-grade target. It's a rough estimate: syllables are counted with a simple heuristic, and URLs, phone numbers and headings are left out.
