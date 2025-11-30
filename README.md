# Indian Startup & Investor Dataset – Venture Launcher

This repository contains the data and code produced during my work as Data Analyst Team Lead at Venture Launcher. The project focuses on scraping public data on Indian startups and investors, enriching it with state-level details, and validating it to generate clean, structured datasets.

## Project Contents
- **data/**
  - **raw/** – Original scraped data
  - **processed/** – Cleaned and standardized datasets
  - **state_wise/** – One processed file per Indian state
- **src/**
  - **scrape.py** – Scrapes public data sources
  - **enrich.py** – Cleans data, adds state mapping and classifications
  - **validate.py** – Performs schema, duplicate, and consistency checks
- **prompts/**
  - AI prompts used during scraping, enrichment, and validation

## Pipeline Overview
1. **Scraping:** Collect startup and investor data from public sources.
2. **Enrichment:** Clean fields, normalize sectors, map cities to states.
3. **Validation:** Fix missing or inconsistent entries and remove duplicates.

## Notes
- No private or confidential information is included.
- Only publicly sourced data and final cleaned outputs are provided.
- The repository is organized for clear understanding and easy reproducibility.
