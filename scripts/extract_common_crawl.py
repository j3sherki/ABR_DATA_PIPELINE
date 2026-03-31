#!/usr/bin/env python3
"""
Extract Australian company websites from Common Crawl using boto3 and warcio.
"""

import boto3
from warcio import ArchiveIterator
import requests
from bs4 import BeautifulSoup
import csv
import os

def extract_company_info(html_content, url):
    """Extract company name and industry from HTML."""
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.title.string if soup.title else ''
        # Simple heuristics
        company_name = title.split(' - ')[0] if ' - ' in title else title
        industry = None  # Placeholder for ML-based extraction
        return company_name, industry
    except:
        return None, None

def process_warc_from_s3(bucket, key):
    """Process a single WARC file from S3."""
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
    records = []
    for record in ArchiveIterator(response['Body']):
        if record.rec_type == 'response':
            url = record.rec_headers.get_header('WARC-Target-URI')
            if url and '.au' in url.lower():  # Australian domain
                content = record.content_stream.read().decode('utf-8', errors='ignore')
                company_name, industry = extract_company_info(content, url)
                if company_name:
                    records.append([url, company_name, industry])
                    if len(records) >= 1000:  # Limit for demo
                        break
    return records

def main():
    # Common Crawl bucket
    bucket = 'commoncrawl'
    # Sample WARC path (update to latest)
    key = 'crawl-data/CC-MAIN-2024-10/segments/1707940200/warc/CC-MAIN-20240102000000-20240102010000-00000.warc.gz'  # Example

    records = process_warc_from_s3(bucket, key)
    
    os.makedirs('data', exist_ok=True)
    with open('data/common_crawl_raw.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['website_url', 'company_name', 'industry'])
        writer.writerows(records)
    
    print(f"Extracted {len(records)} Australian websites.")

if __name__ == '__main__':
    main()