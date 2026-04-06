{{ config(materialized='view') }}

SELECT
    abn,
    business_name AS company_name,
    main_business_location AS address,
    postcode,
    state,
    -- Cleaning
    TRIM(UPPER(abn)) AS cleaned_abn,
    TRIM(LOWER(business_name)) AS cleaned_company_name
FROM {{ source('raw', 'abr') }}
WHERE abn IS NOT NULL
