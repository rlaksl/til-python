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
# for website in websites:
#   if not website.startswith("https://"):
#     website = f"https://{website}"
#   response = get(website)
#   if response.status_code == 200:
#     # print(f"{website} is OK")
#     results[website] = "OK"
#   else:
#     # print(f"{website} not OK")
#     results[website] = "FAILED"

# print(results)



# BLUEPRINT | DONT EDIT

import requests

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:
for movie_id in movie_ids:
  url =f"https://nomad-movies.nomadcoders.workers.dev/movies/{movie_id}"
  response = requests.get(url)
  data = response.json()
  
  print(f"제목: {data['title']}")
  print(f"줄거리: {data['overview']}")
  print(f"평점: {data['vote_average']}")

# /YOUR CODE