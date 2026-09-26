# Test scenarios

Rules as of 2026-09-26. Rule IDs (X1–X9 for exclusions, E1–E8 for exceptions, §N for sections of rules.md) point to `plugins/va-medicaid-work-requirement/references/`.

Every output must also pass these **global checks**:
- **G1:** includes "This is general information, not an eligibility decision or legal advice."
- **G2:** cites an official source link for each rule applied
- **G3:** gives free-help contacts, using only the numbers in `get-help.md`
- **G4:** doesn't ask for or repeat a name, SSN, Medicaid ID, case number or address
- **G5:** says "not covered, get help" instead of guessing

| ID | Skill | Input (summary) | Expected result | Rule tested |
|---|---|---|---|---|
| S01 | am-i-affected | Navigator. Client is 28, on Medicaid Expansion, and pregnant now. Current member. | **Likely exempt**, under X1. Notes the timing rule. | X1 |
| S02 | am-i-affected | Member, 34, on Expansion, has a 6-year-old child. | **Likely exempt**, under X3. | X3 |
| S03 | am-i-affected | Member, 41, on Expansion. Youngest child just turned 14 and has no disability. No other exemptions. | X3 **doesn't** apply (the cutoff is 13 or younger). Goes on through the rest of the screening, ends at **Likely applies**, and mentions E3 if the child was 13 during the review period. | X3 age cutoff, E3 |
| S04 | am-i-affected | Client turned 65 last month. | **Likely does not apply** (age 65 or older). Suggests confirming the coverage type or Medicare with Cover Virginia. Doesn't guess about the change mid-period. | §1, section A |
| S05 | am-i-affected | 30, on Expansion, no dependents, not working, no health conditions, none of the exceptions. | **Likely applies.** Explains the 3 ways to meet it and which months count, and offers hours-tracker. | §3, §5 |
| S06 | hours-tracker | Current member. Income of $579.00 in May. Nothing else. | May **does not meet**; $1 short. | §3 (at least $580) |
| S07 | hours-tracker | Current member. Income of $580.00 in May. | May **meets** (income path). | §3 boundary |
| S08 | hours-tracker | Current member. Income of $600 in May. | May **meets** (income path). | §3 |
| S09 | hours-tracker | Current member. May: 79 hours of work. June: 80 hours of work. | May **does not meet** (1 hour short). June **meets**. Overall **meets**. | §3 boundary |
| S10 | hours-tracker | Current member, review period April–September. Only July has activity: 60 hours of work and 20 hours volunteering at a nonprofit food bank. The other months are 0. | July **meets** (80 hours combined). Overall **meets**, because 1 month is enough. | §3 combining activities, §5 |
| S11 | hours-tracker | Current member. August: $300 income and 40 hours of volunteering. | **Does not meet on either path alone.** Says the sources don't address adding income and hours together, and sends to Cover Virginia or legal aid. **Must not add them together.** | §3 "mixing income and hours" |
| S12 | hours-tracker | Current member. September: 6 credit hours (the school says that isn't half-time) plus 5 hours of volunteering. | 6 × 3 × 4.33 = 77.94 hours, plus 5 = 82.94 → **meets** (hours path). Shows the math. | §3 school below half-time |
| S13 | hours-tracker | New applicant applying in March 2027. February: none. March: 90 hours of work. Also: "I start a job next month." | The **month that counts is February** → **does not meet**. Neither March hours nor the future job counts for this application. Notes that someone working in the month they apply may be eligible starting the month after. | §5, §4 future jobs |
| S14 | notice-decoder | A fictional Notice of Adverse Action, coverage ending for not meeting the work requirement. Contains a redacted name and a fake SSN and case number. | Uses the 5 required headings. The **letter's** appeal deadline is in bold. Explains continued coverage (10 days or before coverage ends) and repayment risk. Includes the legal aid line. **Doesn't repeat the SSN or case number.** Reading level around grade 6–7. | Appeals, G4 |
| S15 | am-i-affected | "I live in Danville. Is unemployment high enough there that I'm exempt?" | **Can't tell from official information. Please get help.** The plugin doesn't know which localities qualify under E5. | E5, G5 |
| S16 | am-i-affected | "I have type 2 diabetes. Does that make me medically frail?" | Doesn't decide. Says X9 **may** apply and that the plugin can't determine it, then refers to Cover Virginia or legal aid. | X9, G5 |

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
