from pymongo import MongoClient


# def take_


def take_value(key_value):
    return -key_value[1]


with MongoClient() as client:
    book_db = client.library.books
    book_by_category = {}
    for book in book_db.find({"status": "PUBLISH"}):
        for category in book["categories"]:
            cat = category.lower()
            book_by_category[cat] = book_by_category.get(cat, 0) + 1

    print(*sorted(book_by_category.items(), key=take_value), sep="\n")
