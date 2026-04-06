# Australian Company Data Pipeline

This project builds a data pipeline to collect, clean, and integrate Australian company website data from Common Crawl with business information from the Australian Business Register (ABR).

## Data Sources
- **Common Crawl**: Extract Australian company websites (target: 200,000+). Data points: Website URL, Company Name, Company Industry.
- **ABR (data.gov.au)**: Enrich with ABN and other company details.

## Technology Stack
- **Python**: Data extraction and processing.
- **Apache Spark**: Distributed processing for large datasets.
- **DBT**: Data transformation, cleaning, normalization, and testing.
- **PostgreSQL**: Database for storing integrated data.

## Project Structure
- `data/`: Raw and processed data files.
- `scripts/`: Python scripts for data extraction and initial processing.
- `dbt_project/`: DBT models and configurations.
- `sql/`: PostgreSQL schema DDL.
- `notebooks/`: Jupyter notebooks for exploration and prototyping.
- `tests/`: Additional tests.

## Pipeline Execution
1. Set up PostgreSQL database and update credentials in scripts.
2. Run `python scripts/extract_abr.py` and `python scripts/extract_common_crawl.py` (or use sample data).
3. Run `python scripts/load_to_postgres.py` to load raw data.
4. Run DBT: `cd dbt_project && dbt run && dbt test`.
5. Query the `integrated_companies` table with examples in `sql/example_queries.sql`.

## Results
- **Data Loaded:** Sample Australian company data integrated.
- **Queries Demonstrated:** State distribution, industry analysis, website coverage.
- **DBT Tests:** Passed for data quality.

## GitHub Repo
https://github.com/Mangesh1998/ABR_DATA_PIPELINE