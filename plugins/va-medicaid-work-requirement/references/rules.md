As of 2026-09-26

# Virginia Medicaid federal work requirement: core rules

Everything below comes from the official sources in [sources.md](sources.md). Short codes in brackets say which source each rule comes from:

- **[FAQ]**: DMAS, *Federal Medicaid Work Requirement FAQs*, July 2026. https://www.dmas.virginia.gov/media/1zudegm1/hr1-federal-work-requirement-faqs-07-24-2026.pdf
- **[DMAS]**: DMAS web page, *Federal Work Requirements*. https://www.dmas.virginia.gov/news-updates/new-federal-requirements/federal-work-requirements/
- **[BULLETIN]**: DMAS provider bulletin, Sept 4, 2026. https://vamedicaid.dmas.virginia.gov/bulletin/hr-1-federal-work-requirement-six-month-renewals-and-medicaid-eligibility-changes-non
- **[COVERVA]**: Cover Virginia, *Adults 19–64 years old*. https://coverva.dmas.virginia.gov/learn/coverage-for-adults/adults-19-64-years-old/

The FAQ itself says: "all information in this document is based on current understanding. Additional forthcoming federal guidance may result in changes."

## 1. Who it applies to

- Only members enrolled in **Virginia's Medicaid Expansion**. [FAQ]
- Medicaid Expansion covers adults who are **19 to 64**, have income **under 138% of the federal poverty level**, and are **not eligible for Medicare**. [FAQ] [COVERVA]
- It "DOES NOT apply to other types of Medicaid, such as coverage for children, pregnant or postpartum individuals, or adults with a disability or who are age 65 or above." [FAQ]
- People who aren't sure whether they're in Medicaid Expansion can call Cover Virginia, use live chat at coverva.dmas.virginia.gov, or contact their local Department of Social Services. [FAQ] See [get-help.md](get-help.md).
- Expansion members were to be sent a notice by the end of September 2026. Approval notices for Expansion members will also include this information starting January 2027. [FAQ]

## 2. When it starts

- **New applicants** who apply on or after **January 1, 2027**, and who appear eligible for Medicaid Expansion, must meet the requirement or be exempt. [FAQ]
- **Current members** must meet the requirement or be exempt **starting with their first renewal in 2027**. "The new rule will not be used to redetermine eligibility for renewals that are started in 2026." [FAQ]

## 3. How to meet it (for people who are not exempt)

A person meets the requirement in a month if **any one** of these is true [FAQ] [DMAS] [BULLETIN]:

| Path | Rule |
|---|---|
| **Hours** | At least **80 hours** in the month of work, a work program, school, and/or volunteering. These activities **can be added together** to reach 80. [FAQ] [DMAS] |
| **School** | Enrolled in school **at least half-time**, as the school defines it. Half-time enrollment meets the requirement on its own. [FAQ] |
| **Income** | Monthly income of at least **$580**. [FAQ] |
| **Income (seasonal workers)** | "For a seasonal worker, the average income over the prior 6 months must be equal or higher than $580." [FAQ] |

### Numbers the skills use
- `HOURS_THRESHOLD = 80` hours per month
- `INCOME_THRESHOLD = 580` dollars per month

### How income is counted
- "Virginia Medicaid may also include income from people in your household, like your spouse. It may also include some income that is not from a job, like unemployment benefits." [DMAS]
- The sources do **not** give a full list of which non-job income counts. → **Not covered. Send to help.**

### Mixing income and hours: NOT ADDRESSED
- The sources describe income and hours as **separate** ways to meet the requirement. **They do not say whether income below $580 can be added to hours below 80** (for example, $300 plus 40 hours).
- The plugin must **not** combine income and hours. It says the sources don't address this and sends the person to Cover Virginia or legal aid.

### School below half-time
- "If they are enrolled less than half-time, the hours spent participating in one of these programs can be combined with hours spent working and/or volunteering to meet the 80 hours per month requirement." [FAQ]
- The FAQ converts credits to monthly hours: **credit hours × 3 × 4.33**. For example, 1 credit is 12.99 hours a month, and 6 credits is 77.94 hours a month. [FAQ]
- A student who applies during a regular break (such as summer) "is still considered enrolled." [FAQ]

## 4. What counts as an activity

- **Work:** "Paid work, self-employment, contract work, in-kind work and unpaid work can all be used." In-kind work means being "paid" in non-cash goods or services such as food, housing or transportation (for example, free rent in exchange for building duties). [FAQ]
- **Unpaid work:** includes "internships, work done during a trial-period, and unpaid family caregiving." It does **not** include "helping friends, family or neighbors, in an informal way or time spent doing regular chores and responsibilities for your own home." [FAQ]
- **Community service or volunteering:** must be (1) unpaid and (2) "for the direct benefit of the community," and not just helping one person. It "cannot be partisan." It "must be done through a public or nonprofit organization that supervises and is able to track the time." [FAQ]
- **Work programs:** Virginia Works programs under the Workforce Innovation and Opportunity Act (WIOA), Trade Act of 1974 programs, state-run or state-supervised work programs such as SNAP Employment and Training, and U.S. Department of Labor or Veterans Affairs programs for veterans. Supervised job search counts only if it is "less than half of the total program required hours." [FAQ]
- **Education:** high school, GED or other state-recognized equivalency programs, higher education, and career or technical education. [FAQ]
- **A future job does not count.** "Future employment does not fulfill the requirement." [FAQ]

## 5. Which months count (the review period)

- **New applicants:** must meet the requirement "in the month before the month they apply." [FAQ] [BULLETIN]
  - FAQ example: someone who applies in **February 2027** is assessed for **January 2027**.
  - Someone working in the month they apply, but not the month before, "can be found eligible for Medicaid Expansion starting the month after they applied." [FAQ]
- **Current members:** must meet it "for at least one month since their most recent eligibility renewal." [FAQ] The DMAS page says: "1 out of 6 months leading up to each renewal." [DMAS]
  - FAQ example: a member renewed in March 2027 gets coverage from April 1 to September 30, 2027. At the next renewal they must have met the requirement "in any one month between April and September." [FAQ]

## 6. Six-month renewals

- Medicaid Expansion members are reviewed **every six months** instead of every 12. This applies to applications submitted, and renewals started, on or after January 1, 2027. [BULLETIN] [FAQ]
- "American Indians and Alaska Natives are exempt from the six-month renewal requirement, and pregnant members will continue to be renewed at the end of their protected postpartum coverage period." [BULLETIN]

## 7. Exemptions

See [exemptions.md](exemptions.md). The skills must check exemptions **before** looking at hours or income.

## 8. Proof and verification

See [verification.md](verification.md).

## 9. Appeals

- "Yes, applicants and members can appeal eligibility decisions related to work requirements. Individuals who wish to appeal should follow the appeal instructions in the Notice of Adverse Action that they receive." [FAQ]
- Deadlines and how to file are in [get-help.md](get-help.md#appeals).

## 10. Notices and contact information

- "Affected members will receive letters by mail, text, or email starting in August 2026." Members should keep their contact information up to date. [FAQ]
