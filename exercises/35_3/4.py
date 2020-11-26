import requests
import parsel

BASE_URL = "http://books.toscrape.com/catalogue/the-grand-design_405/"


def make_requisition(extension="index.html"):
    return requests.get(BASE_URL + extension)


def remove_suffix(text, suffix="...more"):
    if text.endswith(suffix):
        return text[: -len(suffix)]
    return text


def take_features():
    text = make_requisition().text
    selector = parsel.Selector(text)
    title = selector.css("div.product_main > h1::text").get()
    price = selector.css("div.product_main > .price_color::text").re_first(
        r"\d+\.\d{2}"
    )
    description = remove_suffix(
        selector.css("#product_description + p::text").get()
    )
    url = selector.css("div.item img::attr(src)").get()
    return (
        title,
        price,
        description,
        BASE_URL + url,
    )


print(*take_features(), sep=", ")
