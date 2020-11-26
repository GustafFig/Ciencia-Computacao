import requests
import json


BASE_URL = "http://quotes.toscrape.com/api/"


def make_requisition(extension="quotes?page=1"):
    return json.loads(requests.get(BASE_URL + extension).text)


quotes = []
for i in range(1, 13):
    for quote in make_requisition()["quotes"]:
        quotes.append(quote["text"])

print(*quotes, sep="\n")
