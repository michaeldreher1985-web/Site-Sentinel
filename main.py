from sitesentinel.scanner import scan_site
import sys

def main():
  print("=" * 50)
  print("Site Sentinel")
  print("website Security Scanner")
  print("=" * 50)

  if len(sys.argv) < 2:
    url = input("Enter a website URL (include https://): ")
  else:
    url = sys.argv[1]

  print("\nScanning...\n")

  results = scan_site(url)

  if "error" in results:
    print("Scan failed.")
    print(results["error"])
    return

  print(f"Target: {results['url']}")
  print(f"HTTP Status: {results['status']}")
  print(f"HTTPS Enabled: {results['https']}")
  print(f"Response Time: {results['response_time']} seconds")

  print("\nSecurity Headers")

  if len(results["missing_headers"]) == 0:
    print("All recommended headers found.")
  else:
    print("Missing:")
    for header in results["missing_headers"]:
      print("\nScan Complete")

if __name-- == "__main__":
  main()
