# Sourcing Methodology & AI Guardrails

## 1. Sourcing the 25 Federer Companies
- **Initial Data Pool:** Used Screener.in to extract a raw list of Indian mid-cap companies.
- **Financial Filter:** Applied strict query `Sales > 50 AND Sales < 500` to ensure revenue compliance.
- **Industry Filter:** Ignored IT, Finance, and Service sectors. Selected only pure-play physical manufacturers (Auto, Chemicals, Electronics).

## 2. Setting Guardrails Against AI Hallucination
- **Negative Prompting:** When using LLMs to structure the data, I used strict negative prompts: *"DO NOT guess revenues. Strictly reject IT and Finance companies."*
- **Human-in-the-loop QA:** AI is prone to hallucinating technical backgrounds. I verified the Decision Maker's (DM) background via LinkedIn and exact revenue figures via MCA/Screener data before adding them to the final CSV.
