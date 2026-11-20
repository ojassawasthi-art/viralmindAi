# VIRALMIND AI

**An open-source, modular AI marketing agency skill system.** VIRALMIND helps creators, founders and teams research audiences, analyze content opportunities, develop brands, create campaigns and improve growth through measurable experiments.

> VIRALMIND does not promise guaranteed virality or a fixed growth percentage. Its scores are structured heuristics, not calibrated probabilities, until validated against a user's own campaign data.

## What is included

- Six modular Agent Skills using the `SKILL.md` convention.
- A reusable virality scoring CLI with transparent weighted dimensions.
- Platform adapter guides for Claude, ChatGPT and Gemini.
- A portable MCP integration contract for future live research tools.
- Examples, tests, architecture notes and release workflow.

## Quick start

1. Open `skills/viralmind-core/SKILL.md` and follow its workflow.
2. Add the specialist skill folders when a task needs deeper research, content, branding, design or growth expertise.
3. Score a draft with the deterministic helper:

```bash
python scripts/score_content.py examples/sample_content.json
```

4. Run tests:

```bash
python -m unittest discover -s tests -v
```

No API key is required for the skills or scoring helper. Live trend research requires a search provider or approved platform API configured by the host environment.

## Install as a skill

### Claude

Zip the `skills/viralmind-core` folder (or the entire `skills/` folder for the full suite) and upload it through Claude's Skills settings where custom skills are supported. In Claude Code, place the skill folders in the supported skills directory for your installation.

### ChatGPT

Use the core skill text as the instructions for a custom GPT or compatible agent workflow. For live external tools, expose a separately hosted MCP server or supported app/connector. A `SKILL.md` file is not, by itself, a ChatGPT plugin installation.

### Google Gemini

Use the core instructions as the system instruction for a Gemini Gem or compatible agent. For tool access, implement Gemini function calling or connect an MCP-compatible host where supported. The skill folder is portable source material, not an automatic Gemini extension install.

See [`docs/integrations.md`](docs/integrations.md) for details and limitations.

## Project layout

```text
viralmind-ai/
├── skills/                 # Modular agent skills
├── integrations/           # Platform-specific setup guidance
├── scripts/                # Deterministic utilities
├── tests/                  # Automated tests
├── examples/               # Input/output examples
├── docs/                   # Architecture, scoring, roadmap
└── .github/workflows/      # CI
```

## Principles

- Evidence before claims: distinguish official platform guidance, observed patterns and hypotheses.
- Ethical persuasion: no fake scarcity, fake testimonials, impersonation, spam or deceptive engagement schemes.
- Privacy by design: use public, authorized or user-provided data; minimize personal data.
- Human approval: users approve publishing, spending, outreach and account changes.
- Transparent measurement: separate reach, views, watch time, saves, shares, leads and revenue.
- Platform compliance: do not scrape behind access controls or bypass rate limits.

## Current status

This repository is a usable skill-and-toolkit foundation. It is not yet a hosted SaaS, a live social-listening backend, or a published MCP server. Those require provider credentials, infrastructure and platform-specific implementation. See [`docs/roadmap.md`](docs/roadmap.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Please include sources for platform-specific claims and tests for deterministic code changes.

## License

MIT. See [LICENSE](LICENSE).
