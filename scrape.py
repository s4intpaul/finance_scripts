
import requests
import csv
from datetime import datetime

KEYWORDS = ["lithium", "rare earth", "offtake", "jorc", 
            "resource estimate", "drilling", "spacex supply"]

def fetch_announcements():
    url = "https://www.asx.com.au/asx/1/company/announcements"
    params = {
        "count": 20,
        "market_sensitive": "false"
    }
    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    data = response.json()
    print(f"Response keys: {data.keys()}")
    print(f"First item sample: {data.get('data', [])[0] if data.get('data') else 'empty list'}")
    return data.get("data", [])
    return data.get("data", [])

def filter_by_keywords(announcements, keywords):
    results = []
    for item in announcements:
        title = item.get("header", "").lower()
        if any(kw in title for kw in keywords):
            results.append({
                "ticker": item.get("issuer_code"),
                "company": item.get("issuer_full_name"),
                "title": item.get("header"),
                "date": item.get("document_release_date"),
                "url": item.get("url")
            })
    return results

def save_to_csv(results, filename="asx_announcements.csv"):
    if not results:
        print("No matches found.")
        return
    
    with open(filename, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        if f.tell() == 0:
            writer.writeheader()
        writer.writerows(results)
    print(f"Saved {len(results)} announcements to {filename}")

def main():
    print(f"Fetching announcements at {datetime.now()}")
    announcements = fetch_announcements()
    filtered = filter_by_keywords(announcements, KEYWORDS)
    
    if filtered:
        for item in filtered:
            print(f"[{item['ticker']}] {item['company']} — {item['title']}")
    
    save_to_csv(filtered)

if __name__ == "__main__":
    main()