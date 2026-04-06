{{ config(materialized='view') }}

SELECT
    website_url,
    company_name,
    industry,
    -- Add cleaning logic here
    TRIM(LOWER(company_name)) AS cleaned_company_name,
    CASE
        WHEN industry IS NULL OR industry = '' THEN 'Unknown'
        ELSE TRIM(LOWER(industry))
    END AS cleaned_industry
FROM {{ source('raw', 'common_crawl') }}
WHERE website_url IS NOT NULL
