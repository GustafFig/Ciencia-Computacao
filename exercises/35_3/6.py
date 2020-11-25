from pymongo import MongoClient
import json

# with MongoClient() as client:
#     db = client.library
#     with open("books.json") as file:
#         books = json.load(file)
#         db.books.insert_many(books)


def take_books_by_categories():
    with MongoClient() as client:
        category = input("Nome da categoria: ")
        db = client.library
        for cat in db.books.find({"categories": category}):
            print(cat["title"])


take_books_by_categories()
