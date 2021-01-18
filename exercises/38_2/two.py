def with_n2(string):
    biggest = ""
    current = ""

    for char in string:
        # verify string
        insert = False
        next_string = ""

        for sub_char_ind in range(len(current)):
            sub_char = current[sub_char_ind]
            if insert:
                next_string += sub_char
            if sub_char == char:
                insert = True

        if insert:
            current = next_string

        current += char

        if len(current) > len(biggest):
            biggest = current

    return len(biggest)


def with_min_ind(string):
    min_ind = 0
    char_dict = {}
    biggest = 0

    for char_ind in range(len(string)):
        char = string[char_ind]

        if char not in char_dict:
            char_dict[char] = char_ind
            size = char_ind - min_ind + 1
            if size > biggest:
                biggest = size
            continue

        last_ind_char = char_dict[char]

        if last_ind_char >= min_ind:
            min_ind = last_ind_char + 1

        size = char_ind - min_ind + 1
        if size > biggest:
            biggest = size

        char_dict[char] = char_ind

    return biggest


if __name__ == "__main__":
    print(with_n2("bebgebakgs"))
    print(with_min_ind("bebgebakgs"))
    print(with_min_ind("abcda"))
