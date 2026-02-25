# joburls
Adds Streamlit UI for a easy viewing on top of JobSpy scraper for LinkedIn, Indeed, Glassdoor, Google, ZipRecruiter &amp; more

# JobSpy Streamlit Dashboard

A sleek, web-based UI for **JobSpy** - Search across LinkedIn, Indeed, Glassdoor, and more—all in one place, concurrently.

---

## ✨ Features

* **🔍 Multi-Select Search:** Scrape LinkedIn, Indeed, Glassdoor, Google, ZipRecruiter, and more simultaneously.
* **📊 Clean Dataframe:** View your results in a clean table and search by location, search term and optional google search term.
* **🔍 Extensible Code:** Boilerplate to build a large feed and visualization tool.

---

## 🛠️ Installation

1. **Clone this repository:**
   ```bash
   git clone [https://github.com/your-username/jobspy-streamlit.git](https://github.com/your-username/jobspy-streamlit.git)
   cd jobspy-streamlit
   ```
   
Install dependencies:

 ```bash
   pip install streamlit python-jobspy pandas
```

   Run the App:
 ```bash
   streamlit run app.py
```

🖥️ Usage
Enter your Job Title (e.g., "Software Engineer").

Enter your Location (e.g., "Remote" or "Austin, TX").

Select the Job Boards you want to target.

(Optional) Add your Proxy settings in the sidebar to avoid being rate-limited.

Hit Search and watch the data roll in! 📈

🛡️ Legal & Privacy
This tool is for educational and personal use only. Please respect the Terms of Service of the job boards being scraped. Frequent or aggressive scraping may result in IP bans.

Credits & License
This project is built using the following open-source tools:

JobSpy - The engine behind the scraping (MIT License).

License: Distributed under the MIT License. See LICENSE for more information.
