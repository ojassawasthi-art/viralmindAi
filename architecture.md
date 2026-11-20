# Architecture

## Design

VIRALMIND is skill-first. Its domain expertise lives in modular Agent Skills; deterministic calculations live in small scripts; live data access belongs in separately permissioned tools or MCP servers.

```text
User / Host AI
     |
     v
VIRALMIND Core Skill ----> Specialist Skills
     |                       | research / content / brand
     |                       | creative / growth
     v                       v
Tool contract (search, approved APIs, analytics exports)
     |
     v
Evidence + source metadata + campaign results
     |
     v
Human-reviewed strategy, assets and experiments
```

## Separation of concerns

- **Skills:** instructions, workflows, rubrics and domain knowledge.
- **Scripts:** deterministic calculations and validation; no network calls by default.
- **MCP/tools:** optional access to search, analytics and approved platform APIs.
- **Host model:** Claude, ChatGPT, Gemini or another compatible assistant interprets instructions and calls available tools.
- **Human:** approves publishing, outreach, account changes and ad spend.

## Research evidence model

Every external claim should carry a source URL, publisher, publication/update date, retrieval date, platform/region scope and evidence class (`official`, `independent-study`, `observed`, `hypothesis`). Preserve uncertainty and conflicting signals.

## Future MCP tool contract

Potential read-only tools:
- `search_trends(query, platform, region, date_range)`
- `get_public_content_examples(query, platform, limit)`
- `analyze_competitor_public_presence(brand, platform)`
- `get_account_analytics(account_ref, date_range)` — only with explicit account authorization
- `save_campaign_experiment(experiment)`

Potential write tools such as `publish_content` or `launch_ad_campaign` must be separate, permission-gated, and require a human confirmation step. Tool schemas must document data scope, rate limits and provenance.

## Non-goals of this initial repository

No hosted database, web dashboard, scraping engine, automated posting, model API proxy or production MCP server is included in this skill-first release. These are later modules, not features to claim as complete.
