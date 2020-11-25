import requests

BASE_URL = "https://scrapethissite.com/pages/advanced/?gotcha=headers"

headers = {
    "accept": "text/html",
    "user-agent": "Mozilla",
}

response = requests.get(BASE_URL, headers=headers)
assert "bot detected" not in response.text
