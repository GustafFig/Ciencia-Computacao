import requests
from parsel import Selector

BASE_URL = "https://en.wikipedia.org/wiki/"


def make_requisition(extension="Gallery_of_sovereign_state_flags"):
    return requests.get(BASE_URL + extension).text


def make_img_requisition(url):
    return requests.get("https:" + url).content


def take_flags(text):
    selector = Selector(text)
    flags = selector.css(".thumb > div > a.image > img::attr(src)").getall()
    return flags


def write_flags(*urls):
    print
    for flag in range(len(urls)):
        with open(f"images/{flag}.png", "bw") as file:
            file.write(make_img_requisition(urls[flag]))


response = make_requisition()
flags = take_flags(response)
write_flags(*flags)
