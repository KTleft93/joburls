import streamlit as st
from backend import scrape_and_write_jobs
from csv_util import read_job_urls

st.title("Job URLs")
# Create selectboxes
sites = st.sidebar.multiselect(
    "Select job sites:",
    ["linkedin", "indeed", "glassdoor", "Google", "ZipRecruiter"],
    default=["linkedin", "indeed"]
)

search_term = st.sidebar.text_input(
    "Enter search term:",
    value="software engineer"
)

google_search_term = st.sidebar.text_input(
    "Enter Google search term (optional):",
    value=""
)

location = st.sidebar.text_input(
    "Enter the desired location",
    value="USA Remote"
)

# Button to trigger scraping
if st.sidebar.button("Scrape Jobs"):
    with st.spinner("Scraping jobs..."):
        if sites and search_term:
            scrape_and_write_jobs(sites, search_term, google_search_term, location)

            try:
                job_urls_df = read_job_urls()
                job_urls_df['job_url_direct'] = job_urls_df['job_url_direct'].replace(r'^\s*$', None, regex=True)
                job_urls_df = job_urls_df.dropna(subset=['job_url_direct','title','site'])
            except Exception as e:
                st.error(str(e))
                st.stop()
        else:
            st.error("Please select at least one site and enter a search term")

        st.success(f"Loaded {len(job_urls_df)} job URLs")

        st.dataframe(
            job_urls_df,
            column_config={
                "job_url_direct": st.column_config.LinkColumn(
                    "Job Link",
                    display_text="Link"
                ),
            },
            hide_index=True,
            use_container_width=True
        )

