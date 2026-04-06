#!/usr/bin/env python3
"""
Main pipeline runner.
"""

import subprocess
import sys

def run_command(cmd):
    """Run shell command."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)
    print(result.stdout)

def main():
    # Run extraction scripts
    print("Extracting Common Crawl data...")
    run_command("python scripts/extract_common_crawl.py")

    print("Extracting ABR data...")
    run_command("python scripts/extract_abr.py")

    print("Loading to Postgres...")
    run_command("python scripts/load_to_postgres.py")

    # Run DBT
    print("Running DBT transformations...")
    run_command("cd dbt_project && dbt run")

    print("Running DBT tests...")
    run_command("cd dbt_project && dbt test")

if __name__ == '__main__':
    main()
