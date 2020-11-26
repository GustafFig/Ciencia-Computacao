import requests


def make_requisition(extension=""):
    base_url = "https://httpbin.org/encoding/utf8"
    return requests.get(base_url + extension)
