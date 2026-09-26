# koongipaloongi skills

Free, open-source [Claude Code](https://code.claude.com/docs) plugins.

## Plugins

| Plugin | What it does | Skills |
|---|---|---|
| [va-medicaid-work-requirement](plugins/va-medicaid-work-requirement/) | Plain-language help for Virginia's federal Medicaid work requirement (Medicaid Expansion adults, starting 2027). For benefits navigators, legal aid staff and social workers. General information only, not eligibility decisions or legal advice. | `am-i-affected`, `notice-decoder`, `hours-tracker` |

## Install

Add this marketplace once, then install the plugins you want.

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

To get updates later, run `/plugin marketplace update koongipaloongi-skills`.

## Adding a plugin to this repo

1. Create `plugins/<plugin-name>/` with a `.claude-plugin/plugin.json` file (`name` must match the folder name) and one `skills/<skill-name>/SKILL.md` per skill.
2. Add an entry to [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json) with the same `name` and `"source": "./plugins/<plugin-name>"`.
3. Run `claude plugin validate .` and `claude plugin validate ./plugins/<plugin-name>`.
4. Add a row to the table above.

## License

[MIT](LICENSE)
