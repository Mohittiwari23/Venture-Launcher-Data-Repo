# Indian Startup & Investor Dataset – Venture Launcher

This repository contains the data and code produced during my work as Data Analyst Team Lead at Venture Launcher. The project focuses on scraping public data on Indian startups and investors, enriching it with state-level details, and validating it to generate clean, structured datasets.

## Project Contents
- **data/**
  - **raw/** – Original scraped data
  - **processed/** – Cleaned and standardized datasets
  - **state_wise/** – One processed file per Indian state
- **src/**
  - **scrapper.py** – Scrapes public data sources
  - **data_cleaning.py** – Cleans data, adds state mapping and classifications
- **prompts/**
  - AI prompts used during scraping, enrichment, and validation

## Pipeline Overview
1. **Scraping:** Collect startup and investor data from public sources.
2. **Enrichment:** Clean fields, Fix missing or inconsistent entries.
3. **Validation:** Cross checking and confirming validity of collected data.

## Notes
- No private or confidential information is included.
- Only publicly sourced data and final cleaned outputs are provided.
- The repository is organized for clear understanding and easy reproducibility.
