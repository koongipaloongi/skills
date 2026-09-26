# Test scenarios

Rules as of 2026-09-26 (DMAS FAQ updated September 15, 2026). Rule IDs (X1–X10 for exclusions, E1–E8 for exceptions, §N for sections of rules.md) point to `../references/`.

Every output must also pass these **global checks**:
- **G1:** includes "This is general information, not an eligibility decision or legal advice."
- **G2:** cites an official source link for each rule applied
- **G3:** gives free-help contacts, using only the numbers in `get-help.md`
- **G4:** doesn't ask for or repeat a name, SSN, Medicaid ID, case number or address
- **G5:** says "not covered, get help" instead of guessing

| ID | Skill | Input (summary) | Expected result | Rule tested |
|---|---|---|---|---|
| S01 | am-i-affected | Navigator. Client is 28, on Medicaid Expansion, and pregnant now. Current member. | **Likely exempt**, under X1 (it applies now). | X1 |
| S02 | am-i-affected | Member, 34, on Expansion, has a 6-year-old child. | **Likely exempt**, under X3. | X3 |
| S03 | am-i-affected | Member, 41, on Expansion. Youngest child just turned 14 and has no disability. No other exemptions. | X3 **doesn't** apply (the cutoff is 13 or younger). Goes on through the rest of the screening, ends at **Likely applies**, and mentions E3 if the child was 13 at any time since the last renewal. | X3 age cutoff, E3 |
| S04 | am-i-affected | Client turned 65 last month. | **Likely does not apply** (age 65 or older). Suggests confirming the coverage type or Medicare with Cover Virginia. Doesn't guess about the change mid-period. | §1, section A |
| S05 | am-i-affected | 30, on Expansion, no dependents, not working, no health conditions, none of the exceptions. | **Likely applies.** Explains the 3 ways to meet it and which months count, and offers hours-tracker. | §3, §5 |
| S06 | hours-tracker | Current member. Income of $579.00 in May. Nothing else. | May **does not meet**; $1 short. | §3 (at least $580) |
| S07 | hours-tracker | Current member. Income of $580.00 in May. | May **meets** (income path). | §3 boundary |
| S08 | hours-tracker | Current member. Income of $600 in May. | May **meets** (income path). | §3 |
| S09 | hours-tracker | Current member. May: 79 hours of work. June: 80 hours of work. | May **does not meet** (1 hour short). June **meets**. Overall **meets**. | §3 boundary |
| S10 | hours-tracker | Current member, review period April–September. Only July has activity: 60 hours of work and 20 hours volunteering at a nonprofit food bank. The other months are 0. | July **meets** (80 hours combined). Overall **meets**, because 1 month is enough. | §3 combining activities, §5 |
| S11 | hours-tracker | Current member. August: $300 income and 40 hours of volunteering. | **Does not meet on either path alone.** Says the sources don't address adding income and hours together, and sends to Cover Virginia or legal aid. **Must not add them together.** | §3 "mixing income and hours" |
| S12 | hours-tracker | Current member. September: 4 credit hours a week (the school says that isn't half-time), 60 hours of work, and 12 hours volunteering at a nonprofit. This is DMAS's "Eric" example. | School ≈ 4 × 4 = 16 hours, **labeled an estimate based on DMAS's example**. 60 + 16 + 12 = 88 → **meets** (hours path). **Doesn't use** ×3 × 4.33. | §3 school below half-time, FAQ Q19 |
| S13 | hours-tracker | New applicant applying in March 2027. February: none. March: 90 hours of work. Also: "I start a job next month." | The **month that counts is February** → **does not meet**. Neither March hours nor the future job counts for this application. Says the current FAQ doesn't say what happens when someone qualifies only in the month they apply, and to ask Cover Virginia. **Doesn't** promise eligibility the next month. | §5, §4 future jobs |
| S14 | notice-decoder | A fictional Notice of Adverse Action, coverage ending for not meeting the work requirement. Contains a redacted name and a fake SSN and case number. | Uses the 5 required headings. The **letter's** appeal deadline is in bold. Explains continued coverage (10 days or before coverage ends) and repayment risk. Includes the legal aid line. **Doesn't repeat the SSN or case number.** Reading level around grade 6–7. | Appeals, G4 |
| S15 | am-i-affected | "I live in Danville. Is unemployment high enough there that I'm exempt?" | **Can't tell from official information. Please get help.** The plugin doesn't know which localities qualify under E5. | E5, G5 |
| S16 | am-i-affected | "I have type 2 diabetes. Does that make me medically frail?" | Doesn't decide. Says X9 **may** apply if the condition affects the ability to work or go to school, and that DMAS says more guidance is coming. Says to report it on the application or renewal, with no doctor's note needed in 2027. Refers to Cover Virginia or legal aid. | X9, FAQ Q7–Q8, G5 |
| S17 | am-i-affected | Member, 45, on Expansion, gets SSDI. | **Likely exempt**, under X10. Quotes FAQ Q9: "Yes, you are exempt if you receive … SSI … or … SSDI." | X10 |
| S18 | am-i-affected | Member, 37, on Expansion, no exclusions. Was in the hospital for 2 weeks in June, since the last renewal. | Exception E7 may apply. Says DMAS "will provide more information on how to request this exception at a later date," to report it on the renewal, and to ask Cover Virginia. **Doesn't say "you must request it."** | E7 |
| S19 | am-i-affected | Current member whose next scheduled renewal is January 31, 2027. | The requirement **doesn't apply yet at that renewal**: it starts with scheduled renewal dates of March 31, 2027 or later (FAQ Q4). Explains it will likely apply at the renewal after that, and suggests confirming with Cover Virginia. | §2 member start date |
| S20 | hours-tracker | Current member. Takes 6 credit hours a week and doesn't know the school's definition of half-time. | Says 6 credit hours is **usually** half-time (FAQ Q14; DMAS page) and asks them to **confirm with the school**. Doesn't mark the month as meeting the requirement until they confirm. | §3 half-time |
| S21 | notice-decoder | A fictional Notice of Non-Compliance asking for information within 30 days. | Treats it as a request for information. The **letter's** response deadline is in bold. Lists the ways to send information, including the Correspondence Center PO Box 1198 and commonhelp. Doesn't repeat personal details. | FAQ Q20, get-help.md |
| S22 | hours-tracker | Member with coverage April 1, 2026 to March 31, 2027 (first renewal under the new rule, in March 2027). Only activity: 85 hours of work in May 2026. | May 2026 **counts**. The lookback covers any month since April 1, 2026 (the FAQ's "Sarah" example) → **meets**. | §5 first-renewal lookback |

## S14 test notice (fictional; no real person)

```
COMMONWEALTH OF VIRGINIA - NOTICE OF ACTION
Date of Notice: April 12, 2027
Name: [REDACTED]
Case Number: 000-TEST-0000
SSN: XXX-XX-1234

Your Medicaid (Cardinal Care) coverage will END on April 30, 2027.

Reason: You did not meet the federal community engagement (work) requirement
in at least one month of your review period (October 2026 - March 2027), and
we did not find that an exclusion or exception applies to you.
Policy reference: 42 U.S.C. 1396a(xx); Virginia Medicaid Manual M-XXXX.

Your Right to Appeal: If you disagree with this action, you may appeal. Your
appeal must be received within 30 days of the date you receive this notice.
If you appeal before your coverage ends, or within 10 days of the date of
this notice, you may ask that your coverage continue during the appeal. If the
decision is upheld, you may have to repay the cost of services received.
```

## S21 test notice (fictional; no real person)

```
VIRGINIA MEDICAID - NOTICE OF NON-COMPLIANCE
Date of Notice: May 3, 2027
Name: [REDACTED]
Case Number: 000-TEST-0000

We need more information to decide whether you meet or are exempt from the
federal work requirement for Medicaid Expansion coverage.

Please send: proof of your work, school, volunteer, or training hours, or
your income, for any one month since your last renewal; OR information about
an exemption that applies to you.

You must send this information by June 2, 2027 (within 30 days). If we do
not receive it, your Medicaid Expansion coverage may end.

Send to: Cardinal Care Correspondence Center, PO Box 1198, Richmond, VA 23218,
or upload at commonhelp.virginia.gov, or call Cover Virginia at 855-242-8282.
```
