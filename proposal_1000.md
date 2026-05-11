# Proposal: Building a Verified Database of 1000 "Federer" Companies

## 1. Objective
The goal is to scale our current research from 25 companies to 1000 high-quality, verified manufacturing MSMEs (Rs. 50Cr - 500Cr revenue) within 30 days, ensuring 0% AI hallucination.

## 2. The Execution Funnel
To reach 1000 qualified companies, we will follow a multi-stage data pipeline:
- **Top of Funnel (4000+ companies):** Bulk sourcing from MCA (Ministry of Corporate Affairs) database and industry directories like Zauba Corp/Tofler.
- **Automated Filtering:** Using Python scripts to filter by Revenue (50-500Cr) and Sector (Manufacturing only).
- **AI Scoring:** Using LLM APIs (Claude/Gemini) to read company descriptions and score them on C1-C6 criteria.
- **Human Verification:** Manual spot-checks on "Evidence" columns to ensure data integrity.

## 3. 30-Day Implementation Plan

| Phase | Timeline | Key Activities |
|-------|----------|----------------|
| **Phase 1: Sourcing** | Week 1 | Extracting raw data of 4000+ MSMEs using web scraping and database subscriptions. |
| **Phase 2: Enrichment** | Week 2 | Using LinkedIn API/Apollo to find Decision Makers (DMs) and their educational backgrounds. |
| **Phase 3: AI Filtering** | Week 3 | Running an automated pipeline to score companies and generate 'Evidence' snippets. |
| **Phase 4: QA & Review** | Week 4 | Final manual verification of the top 1000 companies and formatting the final CSV. |

## 4. Tech Stack & Tools
- **Data Extraction:** Python (BeautifulSoup, Selenium), Screener.in Premium.
- **Data Processing:** Pandas, SQL for handling large datasets.
- **AI Integration:** OpenAI/Claude API for automated text analysis and scoring.
- **Verification:** LinkedIn Sales Navigator for DM profiling.

## 5. Budget Estimate
- **Data Subscriptions:** Rs. 10,000 (Tofler/LinkedIn).
- **API Credits:** Rs. 5,000 (LLM processing).
- **Total:** ~Rs. 15,000 for a fully verified 1000-company list.
