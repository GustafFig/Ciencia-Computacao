def find_biggest_substring(string):
    set_str = set(string)
    set_str_sub = set(string)
    size = 0
    size_try = 0
    for letter in string:
        if letter not in set_str:
            set_str = set_str_sub
            size_try = 0
        if letter in set_str:
            size_try += 1
            set_str.discard(letter)
        if size_try > size:
            size = size_try

    return size


def biggest_distinct_substring(string):
    biggest_subs, candidate_subs = "", ""
    for letter in string:
        if letter not in candidate_subs:
            candidate_subs += letter
            if candidate_subs > biggest_subs:
                biggest_subs = candidate_subs
    return len(biggest_subs)


if __name__ == "__main__":
    # print(find_biggest_substring("ABCABCBB"))
    # print(find_biggest_substring("geeksforgeeks"))
    print(find_biggest_substring("eaaagebaks"))
    print(biggest_distinct_substring("eaaagebaks"))
