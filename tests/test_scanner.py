from sitesentinel.scanner import scan_site


def test_scan():
  results = scan_site("https://example.com")

  assert "status" in results 
  assert "response_time" in results 
