# words = ["cat", "bt", "hat", "tree"], chars = "atach"
# saída: 6
"""Explicação: As palavras que podem ser formadas com os caracteres da string
               são "cat" (tamanho 3) e "hat" (tamanho 3)."""

def is_possible_format(words, chars):
    char_dict = {}
    for char in chars:
        char_dict[char] = char_dict.get(char, 0) + 1
    
    total_sum = 0
    for word in words:
        is_valid = True
        dict_copy = char_dict.copy()

        for char in word:
            if char not in dict_copy:
                is_valid = False
                break
            dict_copy[char] -= 1
            if dict_copy[char] < 0:
                is_valid = False

        if is_valid:
            total_sum += len(word)
        
    return total_sum



if __name__ == "__main__":
    print(is_possible_format(["cat", "bt", "hat", "tree"], "atach"))

