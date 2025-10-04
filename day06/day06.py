from requests import get

# 튜플
"""
websites = (
  "https://google.com",
  "airbnb.com",
  "twitter.com",
  "facebook.com",
  "https://tiktok.com"
)

# For Loops
for website in websites:
  print(website)
  print("website is equals to", website)
"""

# URL Formatting
websites = (
  "https://google.com",
  "airbnb.com",
  "twitter.com",
  "facebook.com",
  "https://tiktok.com"
)

"""
for website in websites:
  if website.startswith("https://"):
    print("good to go")
  else:
    print("we have to fix it")

for website in websites:
  if not website.startswith("https://"):
  # if website.startswith("https://") == False:
    website = f"https://{website}"
  print(website)
"""

results = {
  # "https://google.com"
}

# Requests
for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  if response.status_code == 200:
    # print(f"{website} is OK")
    results[website] = "OK"
  else:
    # print(f"{website} not OK")
    results[website] = "FAILED"

print(results)