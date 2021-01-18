from deque import Deque


def palindromo(word):
    deque = Deque()
    for char in word:
        if char not in [" ", ",", ":"]:
            deque.push_front(char)
    for i in range(len(deque) // 2):
        init = deque.pop_front()
        end = deque.pop_back()
        if init.upper() != end.upper():
            return False
    return True


if __name__ == "__main__":
    print(palindromo("Sera que sou palidromo?"))
    print(palindromo("mais um teste"))
    print(palindromo("madam"))
    print(palindromo("a dama admirou o rim da amada"))
    print(palindromo("Ze de Lima, Rua Laura, Mil e Dez"))
    print(
        palindromo(
            "Luza Rocelina, a namorada do Manuel, leu na moda, da Romana: anil e cor azul"
        )
    )
