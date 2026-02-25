import csv
from jobspy import scrape_jobs

CSV_PATH = "jobs.csv"

def scrape_and_write_jobs(site_names, search_terms, google_search_terms, locations):
    """
    Scrape jobs and write them to CSV.
    Do NOT rely on return value.
    """
    jobs = scrape_jobs(
        site_name=site_names,
        search_term=search_terms,
        google_search_term=google_search_terms,
        location=locations,
        results_wanted=20,
        hours_old=72,
        is_remote=True,
        country_indeed="USA",
        linkedin_fetch_description=True,  # ensures job_url_direct
    )

    # jobspy handles writing internally when descriptions are fetched
    # If you explicitly want to control writing, uncomment below:
    jobs.to_csv(CSV_PATH, index=False)

