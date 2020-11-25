import requests


def make_requisition(extension=""):
    base_url = "https://api.github.com/users/"
    try:
        response = requests.get(base_url + extension)
        response.raise_for_status()
    except requests.HTTPError as err:
        with open("logs.txt", "w") as file:
            print(err, file=file)
            text = "Error"
    else:
        text = response.text
    finally:
        return text


while True:
    username = input("Coloque o nome de usuário do Github: ")
    if not username:
        break
    response = make_requisition(username)
    print(response)
