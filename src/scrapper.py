import requests
import time
import pandas as pd
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# API endpoint
API = "https://api.startupindia.gov.in/sih/api/noauth/search/profiles"

# Headers (simulate a browser)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; StartupScraper/1.0)",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json"
}

# Retry strategy
session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))

def fetch_page(page=0, size=50):
    """Fetch one page of startups"""
    payload = {
        "page": page,
        "size": size,
        "roles": ["Startup"],  # filter for startups
        "searchText": ""
    }
    response = session.post(API, headers=HEADERS, json=payload, timeout=30)
    response.raise_for_status()
    return response.json()

def scrape_startups(max_pages=100, page_size=50):
    data = []
    page = 0

    while page < max_pages:
        j = fetch_page(page=page, size=page_size)

        # Extract items (the key may vary; inspect JSON in browser)
        items = j.get("content") or j.get("profiles") or []
        if not items:
            print(f"[INFO] No more startups found on page {page}")
            break

        for item in items:
            name = item.get("entityName") or item.get("name")
            # Combine key details into a list to mimic your old "Details"
            details = []
            if item.get("registrationNo"):
                details.append(f"RegNo: {item['registrationNo']}")
            if item.get("state"):
                details.append(f"State: {item['state']}")
            if item.get("city"):
                details.append(f"City: {item['city']}")
            if item.get("industry"):
                details.append(f"Industry: {item['industry']}")
            if item.get("website"):
                details.append(f"Website: {item['website']}")

            record = {
                "Name": name,
                "Details": details
            }
            data.append(record)

        print(f"[INFO] Fetched page {page}, items: {len(items)}")
        page += 1
        time.sleep(0.5)  # be polite

    return data

if __name__ == "__main__":
    startups_data = scrape_startups(max_pages=1000, page_size=50)
    df = pd.DataFrame(startups_data)
    df.to_csv("startups_scraped_api.csv", index=False)
    print(f"[INFO] Scraping complete. Total startups scraped: {len(df)}")
    print("[INFO] Data saved to startups_scraped_api.csv")
