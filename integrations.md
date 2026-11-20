# Platform integration guide

The Agent Skills convention is a folder containing a `SKILL.md` with YAML frontmatter plus optional references and scripts. Hosts differ in how they discover, upload and execute these files. Do not assume one upload mechanism works everywhere.

## Claude

- Package a skill folder with its `SKILL.md` and references/scripts.
- Upload through the custom Skills interface where available, or install in the supported Claude Code skills directory.
- For programmatic API use, follow the current Anthropic Agent Skills API documentation and its execution/container requirements.
- Add an MCP server separately when the skill needs live search or external tools.

## ChatGPT

- Use the core skill as the instruction source for a custom GPT or compatible agent configuration.
- For external capabilities, expose an MCP server or supported app/connector and configure it in the relevant ChatGPT environment.
- A plain `SKILL.md` folder is not itself a ChatGPT plugin or automatically installable extension. Host support and account availability vary.

## Google Gemini

- Use the core skill as a Gem instruction or system-instruction template in a compatible Gemini experience.
- For tools, implement Gemini function declarations/function calling or connect through a compatible MCP host where supported.
- A `SKILL.md` folder is portable instructions, not an automatically installable Gemini extension.

## Cross-platform adapter principle

Keep the workflow and knowledge in the shared skill files. Keep model-specific setup, tool schemas, authentication and execution details in adapters. Never hard-code one provider's SDK into the shared skill layer.

## References to verify before publishing an adapter

- Anthropic Agent Skills overview: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Anthropic Skill authoring best practices: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Model Context Protocol: https://modelcontextprotocol.io/
- OpenAI platform documentation: https://platform.openai.com/docs
- Google AI for Developers: https://ai.google.dev/gemini-api/docs

Platform capabilities change. Confirm current product support, plan eligibility and API terms before release.
