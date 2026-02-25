import pandas as pd

CSV_PATH = "jobs.csv"

def read_job_urls():
    """
    Read CSV and return only the job_url_direct column.
    """
    df = pd.read_csv(CSV_PATH)

    if "job_url_direct" and "title" not in df.columns:
        raise KeyError(
            f"'job_url_direct' not found. Available columns: {df.columns.tolist()}"
        )

    return df[["job_url_direct", "title", "site"]]
