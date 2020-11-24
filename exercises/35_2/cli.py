import random
import json
import csv


def name_stairs_reversed():
    name = input("Coloque seu nome, por favor: ")
    size = len(name)
    for i in range(size):
        print(name[: (size - i)])


def guess_word(file_name=None):
    words = [
        "Algum",
        "texto",
        "apenas",
        "para",
        "conseguirmos",
        "passalo",
        "e",
        "termos",
        "tamanho",
        "para",
        "ler",
    ]
    if file_name is not None:
        words = []
        with open(file_name) as file:
            for line in file:
                words.append(line.rstrip())

    print(words)
    word = random.choice(words)
    scrambled_word = "".join(random.sample(word, len(word)))
    print(scrambled_word)
    while True:
        name = input("O q vc me diz que é? ")
        if name == word:
            print("Parabéns!! Vc acertou!!")
            break
        else:
            print("A próxima vai")


def count_categories(books):
    categories = {}
    for book in books:
        for category in book["categories"]:
            if not categories.get(category):
                categories[category] = 0
            categories[category] += 1

    return categories


def get_info(file_name="books.json"):
    category_by_quantity = {}
    with open(file_name) as file:
        books = json.load(file)
        books_quantity = len(books)
        categories = count_categories(books)
        category_by_quantity = [
            (category, format(quantity / books_quantity, ".2%"))
            for category, quantity in categories.items()
        ]
    return category_by_quantity


def save_data(data, file_name="1.csv"):
    with open(file_name, "w") as file:
        writer = csv.writer(file)
        writer.writerow(("Category", "Percentage"))
        for category, percentage in data:
            writer.writerow((category, percentage))


def who_is_this_pokemon():
    with open("pokemons.json") as file:
        pokemons = [pok["name"] for pok in json.load(file)["results"]]

        pokemon = random.choice(pokemons)
        letters = 0
        while True:
            name = input(f"Qual Pokemon vc acha q é? {pokemon[:letters]} | ")
            if name == pokemon:
                return print("Voce acertou!!!")
            letters += 1


who_is_this_pokemon()
