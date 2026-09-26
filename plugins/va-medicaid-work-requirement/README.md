# Virginia Medicaid Work Requirement Helper

A free, open-source Claude Code plugin. It helps people in Virginia understand the new **federal Medicaid work requirement** for **Medicaid Expansion adults**, which starts in 2027.

> **Rules last verified: 2026-09-26.** Sources are listed [below](#sources).
>
> ⚠️ **This plugin gives general information. It is not an eligibility decision or legal advice.** Only Virginia Medicaid decides eligibility. For denials, appeals or lost coverage, get free help (see [Free help](#free-help)).

## Who it's for

- Benefits navigators, legal aid staff, social workers and community health workers who help people keep their coverage
- Medicaid members themselves. Everything written for members aims for about a 6th-grade reading level.

## What it does

| Skill | Command | What it does |
|---|---|---|
| **Am I affected?** | `/va-medicaid-work-requirement:am-i-affected` | Asks one question at a time. Checks exclusions and exceptions first, then explains whether the requirement **likely** applies and why, citing the rule and the official link. |
| **Notice decoder** | `/va-medicaid-work-requirement:notice-decoder` | Paste a letter from Virginia Medicaid or local social services, **with personal details removed**. Get a plain-language explanation: what the letter is about, what it asks for, the deadline, the next step, and where to get free help. |
| **Hours tracker** | `/va-medicaid-work-requirement:hours-tracker` | Logs monthly hours or income against the **80-hour** and **$580** thresholds, shows which months meet the requirement, and builds a checklist of records to keep before renewal. |

Claude can also start these skills on its own when a question matches, for example "Is my client exempt from the Medicaid work requirement?"

### The rules in brief (as of 2026-09-26)

- **Who it applies to:** Medicaid Expansion adults aged 19–64 who aren't excluded or excepted.
- **When it starts:** for new applicants, January 1, 2027. For current members, their first renewal in 2027.
- **How to meet it, in a month:** 80 hours of work, a work program, school and/or volunteering; **or** half-time school enrollment; **or** $580 in income (seasonal workers use a 6-month average).
- **Which months count:** current members need **1 month** since their last renewal. Renewals happen every 6 months. New applicants need **the month before they apply**.
- **Exemptions:** the full list, with timing rules, is in [`references/exemptions.md`](references/exemptions.md).

### Design choices

- **All rules live in [`references/`](references/).** The skills read them and don't copy them, so updating is a one-place job.
- **When the official sources are silent, the plugin says so.** For example, the sources don't say whether income and hours can be added together, so the tracker never combines them and sends the person to Cover Virginia instead.
- **Two exclusions (meeting TANF or SNAP work rules, and being in a substance use disorder treatment program) appear only in the July 2026 DMAS FAQ.** The plugin includes them and says where they come from.
- **Appeal deadlines** come from a 2021 DMAS appeals FAQ. The plugin always says **the deadline on the notice is the one that counts**.
- **Proof checklist:** the official sources don't list the documents people need. The tracker's checklist is labeled *"Suggested records to keep. This is not an official list."*
- **Privacy:** the skills never ask for names, Social Security numbers, Medicaid ID numbers or addresses. They don't write anything to disk unless asked.

## Install

Requires [Claude Code](https://code.claude.com/docs).

Inside a Claude Code session:

```
/plugin marketplace add koongipaloongi/skills
/plugin install va-medicaid-work-requirement@koongipaloongi-skills
```

Or from your shell:

```bash
claude plugin marketplace add koongipaloongi/skills
```

```bash
claude plugin install va-medicaid-work-requirement@koongipaloongi-skills
```

To try it from a local copy without installing:

```bash
claude --plugin-dir ./plugins/va-medicaid-work-requirement   # run from the repo root
```

## Examples

**Am I affected?**
```
/va-medicaid-work-requirement:am-i-affected
> I'm a navigator. My client is 34, on Medicaid Expansion, and has a 6-year-old.
```
→ Likely exempt under exclusion X3 (parent or caregiver of a child 13 or younger), with the quote, source link, timing rule, next step and free-help contacts.

**Notice decoder**
```
/va-medicaid-work-requirement:notice-decoder
> [paste the letter with names, ID numbers and addresses removed]
```
→ Plain-language sections: *What this letter is about · What they're asking for · Deadline · What to do next · Where to get free help.*

**Hours tracker**
```
/va-medicaid-work-requirement:hours-tracker
> Current member. May: 50 hours at a job and 25 hours volunteering at a food bank. June: $610 income.
```
→ May: 75 hours, does not meet. June: meets on the income path. The member meets the requirement for the review period, and gets a checklist of records to keep.

## Free help

- **Cover Virginia:** 1-855-242-8282 (TTY 1-888-221-1590), https://coverva.dmas.virginia.gov
- **Local department of social services:** https://www.dss.virginia.gov/localagency/
- **Free legal aid:** 866-LEGLAID (866-534-5243), https://www.virginialawhelp.org
- **DMAS Appeals:** 804-371-8488, appeals@dmas.virginia.gov

## Sources

All sources were checked on **2026-09-26**. The full table is in [`references/sources.md`](references/sources.md).

- [DMAS: Federal Work Requirements](https://www.dmas.virginia.gov/news-updates/new-federal-requirements/federal-work-requirements/)
- [DMAS: Federal Medicaid Work Requirement FAQs (July 2026)](https://www.dmas.virginia.gov/media/1zudegm1/hr1-federal-work-requirement-faqs-07-24-2026.pdf)
- [DMAS provider bulletin (Sept. 4, 2026)](https://vamedicaid.dmas.virginia.gov/bulletin/hr-1-federal-work-requirement-six-month-renewals-and-medicaid-eligibility-changes-non)
- [Cover Virginia: Adults 19–64](https://coverva.dmas.virginia.gov/learn/coverage-for-adults/adults-19-64-years-old/)
- [DMAS: Applicant / Member Appeals](https://www.dmas.virginia.gov/appeals/applicant-member-appeals-resources/) and [Client Appeals FAQ (2021)](https://www.dmas.virginia.gov/media/3221/client-appeals-frequently-asked-questions-2021-05-21.pdf)

## Keeping it up to date

The FAQ says federal guidance may change. To update:

1. Fetch every source in [`references/sources.md`](references/sources.md) again, and check the [DMAS FAQ page](https://www.dmas.virginia.gov/news-updates/new-federal-requirements/member-letter-toolkit-and-faqs/) for a newer FAQ.
2. Edit the files in `references/` and change each file's "As of" line.
3. Re-run every scenario in [`tests/scenarios.md`](tests/scenarios.md).
4. Update "Rules last verified" at the top of this README, bump `version` in `plugin.json`, and run `claude plugin validate .`.

## Contributing

Corrections are welcome. Please include an official source link for any rule change.

## License

[MIT](../../LICENSE)
