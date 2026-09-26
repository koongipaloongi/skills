As of 2026-09-26

# Virginia Medicaid federal work requirement: core rules

Everything below comes from the official sources in [sources.md](sources.md). Short codes in brackets say which source each rule comes from:

- **[FAQ]**: DMAS, *Federal Medicaid Work Requirement FAQs*, **Updated: September 2026** (dated 9/15/2026). https://www.dmas.virginia.gov/media/cyvdt2wd/hr1-work-requirement-faqs-09-15-26.pdf. "Q" numbers refer to its questions.
- **[DMAS]**: DMAS web page, *Federal Work Requirements*. https://www.dmas.virginia.gov/news-updates/new-federal-requirements/federal-work-requirements/
- **[BULLETIN]**: DMAS provider bulletin, Sept 4, 2026. https://vamedicaid.dmas.virginia.gov/bulletin/hr-1-federal-work-requirement-six-month-renewals-and-medicaid-eligibility-changes-non
- **[COVERVA]**: Cover Virginia, *Adults 19–64 years old*. https://coverva.dmas.virginia.gov/learn/coverage-for-adults/adults-19-64-years-old/

The FAQ itself says: "all information in this document is based on current understanding. Additional forthcoming federal guidance may result in changes." It also says: "Look for edits to this FAQ document as well as updated information on our websites."

## 1. Who it applies to

- Only members in **Virginia's Medicaid Expansion**. [FAQ Q2]
- Medicaid Expansion covers adults who are **19 to 64**, have income **under 138% of the federal poverty level** ("around $22,000/year for an individual or $45,000/year for an adult in a family of four"), and are **not eligible for Medicare**. [FAQ Q2] [COVERVA]
- It "DOES NOT apply to other types of Medicaid, such as coverage for children, pregnant or postpartum individuals, or adults with a disability or who are age 65 or above." [FAQ Q2]
- People who aren't sure whether they're in Medicaid Expansion can call Cover Virginia, use live chat at coverva.dmas.virginia.gov, or contact their local Department of Social Services. [FAQ Q3] See [get-help.md](get-help.md).
- Expansion members get a letter about the new requirement **by September 30, 2026**, by "mail, text, and/or email." That letter goes to all Expansion members, "many of whom will be exempt." Approval notices will also include this information starting January 2027. [FAQ Q3, Q22]

## 2. When it starts

"The new work requirement and six-month renewals will take effect in 2027. This means:
- Applicants applying on or after January 1, 2027.
- Members with a scheduled renewal date of March 31, 2027 or later." [FAQ Q4]

**Current members** with a scheduled renewal date **before March 31, 2027** are not yet subject to it at that renewal. The FAQ gives no more detail. For edge cases, send people to Cover Virginia.

## 3. How to meet it (for people who are not exempt)

A person meets the requirement in a month if **any one** of these is true [FAQ Q1, Q10] [DMAS]:

| Path | Rule |
|---|---|
| **Hours** | At least **80 hours** in the month of work, a work program, school, and/or volunteering. These **can be added together** (see "Combining activities" below). |
| **School** | Enrolled in school **at least half-time**, "as defined by their school/institution." This meets the requirement on its own. |
| **Income** | Monthly income of at least **$580**. |
| **Income (seasonal workers)** | "Seasonal workers can meet the requirement by having an average monthly income of at least $580 over 6 months." |

### Numbers the skills use
- `HOURS_THRESHOLD = 80` hours per month
- `INCOME_THRESHOLD = 580` dollars per month

### How income is counted
- The FAQ says "qualifying household income." [FAQ Q1] The DMAS page says: "Virginia Medicaid may also include income from people in your household, like your spouse. It may also include some income that is not from a job, like unemployment benefits." [DMAS]
- The sources do **not** give a full list of which income counts. → **Not covered. Send to help.**

### Combining activities
- "If you work, volunteer, or participate in a work program less than 80 hours in a month, or if you are enrolled in an educational program less than half-time, the hours spent in any of these activities can be combined to meet the work requirement. It is important to report all information so that we can add all of your activities together." [FAQ Q19]
- **FAQ example (Eric):** "enrolled in a community college in two courses for a total of four credit hours a week; he also works at a pet store 15 hours a week, and volunteers 3 hours a week on the weekends. Virginia Medicaid will combine his 60 monthly hours of work, his 16 monthly hours of educational program credit, and his 12 monthly hours of volunteering to equal 88 hours of combined activities. This meets the work requirement." [FAQ Q19]

### Mixing income and hours: NOT ADDRESSED
- The FAQ lists income and hours as **separate** ways to meet the requirement. Its "combine activities" answer (Q19) covers work, volunteering, work programs and school only. **It doesn't say whether income below $580 can be added to hours below 80.**
- The plugin must **not** combine income and hours. It says the sources don't address this and sends the person to Cover Virginia or legal aid.

### School: half-time and credit hours
- "In most cases, your school defines your enrollment type (full time vs. half time, for example). In general, 6 credit hours in adult education per week is equivalent to half-time enrollment." [FAQ Q14] The DMAS page says: "Go to school at least half-time (this is usually 6 credit hours)." [DMAS]
- **If the school says the person is half-time or more** → meets the requirement (school path).
- **If the person has about 6 or more credit hours but doesn't know their school's definition** → likely half-time, but they should confirm with their school. Don't state it as certain.
- **Converting credit hours below half-time into monthly hours:** the FAQ **doesn't give a formula**. Its only example counts **4 credit hours a week as 16 monthly hours** (Q19). The skills may **estimate** monthly hours as *credit hours per week × 4*. They must label the result as **an estimate based on DMAS's example** and tell the person to confirm with Cover Virginia whenever the estimate decides whether they meet 80 hours.
- ⚠️ The **July 2026** FAQ used a different conversion (credits × 3 × 4.33). The September FAQ **removed** it. Don't use it.
- **Breaks:** "If a person enrolled in an education program applies or is renewed for Medicaid during a regular break (ex: summer break), they are still considered enrolled in the education program. This is true even if the person is moving from one type of education to another (e.g., from high school to college)." [FAQ Q15]

## 4. What counts as an activity [FAQ Q12, Q13, Q16, Q17, Q18]

- **Work:** paid work, self-employment, contract work, in-kind work (being "paid" in non-cash goods or services such as food, housing or transportation; for example, "a property manager who receives free rent in exchange for building duties"), and unpaid work.
- **Unpaid work:** includes "internships, work done during a trial-period, and unpaid family caregiving." It does **not** include "helping friends, family or neighbors, in an informal way or time spent doing regular chores and responsibilities for your own home."
- **Community service or volunteering:** must be unpaid and done "for the direct benefit of the community," not only to help one person. It "cannot be partisan," and must be "done through a public or nonprofit organization that supervises and is able to track the time."
- **Work programs:** Virginia Works programs under the Workforce Innovation and Opportunity Act (WIOA), Trade Act of 1974 programs, state-run or state-supervised work programs "such the SNAP Employment and Training program," and U.S. Department of Labor or Veterans Affairs programs for veterans. Supervised job search counts only if it is "less than half of the total program required hours."
- **Education:** high school, GED or other state-recognized equivalency programs, higher education ("associate's degree program, college, or graduate or professional degree"), and technical or career education.
- **A future job doesn't count.** "No, future employment does not fulfill the requirement." [Q18]

## 5. Which months count (the review period) [FAQ Q11]

- **New applicants:** "the month before they apply."
  - FAQ example: "James applies for coverage in February 2027. He must have worked, gone to school, or had another qualifying activity in January 2027 to have coverage effective February 1."
  - The September FAQ **doesn't say** what happens to someone who qualifies in the month they apply but not the month before. (The July FAQ did; that sentence was removed.) → **Not covered. Send to help.**
- **Current members:** "for one month since their most recent eligibility renewal."
  - FAQ example: "Sarah's coverage is effective April 1, 2026-March 31, 2027. To continue to be eligible for Medicaid Expansion at her next renewal in March 2027, if she is not exempt, she must have worked, gone to school, or had another qualifying activity for at least 1 month since April 1, 2026." After that she's renewed for six months, April 1 to September 30, 2027, and at the September renewal she needs "at least 1 month since April 1, 2027."
  - So at a member's **first** renewal under the new rule, the lookback can cover their whole previous **12-month** coverage period.

## 6. Six-month renewals

- Medicaid Expansion members are reviewed **every six months** instead of every 12. [FAQ Q1] [BULLETIN]
- "American Indians and Alaska Natives are exempt from the six-month renewal requirement, and pregnant members will continue to be renewed at the end of their protected postpartum coverage period." [BULLETIN]

## 7. Exemptions

See [exemptions.md](exemptions.md). The skills must check exemptions **before** looking at hours or income.

## 8. Showing that you qualify, and proof

See [verification.md](verification.md). In short: **in 2027, what people report on their application or renewal is usually enough** ("self-attestation"), and additional requirements start in 2028. [FAQ Q5]

## 9. Appeals

- "Yes, applicants and members can appeal eligibility decisions related to work requirements. Individuals who wish to appeal should follow the appeal instructions in the Notice of Adverse Action that they receive." [FAQ Q21]
- Deadlines and how to file are in [get-help.md](get-help.md#appeals).

## 10. Staying covered and getting updates [FAQ Q23, Q24]

- Keep contact information current at commonhelp.virginia.gov or by calling Cover Virginia.
- DMAS is holding **virtual town halls** this fall; recordings are posted online. See [get-help.md](get-help.md).
- "In the coming months, Virginia Medicaid will provide more information about a new online portal to help Virginians report, track, and submit information regarding work requirements and exemptions." [FAQ Q20]
