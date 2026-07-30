import requests
import time 

def scan_site(url):
  try:
    start = time.time()
    
    response = requests.get(url, timeout=10)

    end = time.time()

    headers = response.headers

    recommended_headers = [
        "Strict-Transport-Security", 
        "Content-Security-Policy", 
        "X-Frame-Options", 
        "X-Content-Type-Options",
        "Referrer-Policy"
    ]

    missing = []

    for header in recommend_headers:
      if header not in headers:
        missing.append(header)

    return {
        "url": url,
        "status": response.status_code,
        "https": url.startswith("https://"),
        "response_time": round(end - start, 3), 
        "missing_headers": missing 
    }
except Exception as e:
    return {
        "url": url, 
        "error": str(e)
    }
