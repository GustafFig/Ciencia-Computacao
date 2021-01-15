def who_wins(people_games):
    a, b = people_games.keys()  # O(2)

    # O(2n)
    a_set_game = {x for x in people_games[a]}
    b_set_game = {x for x in people_games[b]}

    # O(2n)
    a_diff_b = a_set_game.difference(b_set_game)
    b_diff_a = b_set_game.difference(a_set_game)

    if len(a_diff_b) == 0 or len(b_diff_a) == 0:
        return None

    # O(2n)
    a_lower = None
    a_bigger = None
    for i in a_diff_b:
        if not a_lower or i < a_lower:
            a_lower = i
        if not a_bigger or i > a_bigger:
            a_bigger = i

    b_lower = None
    b_bigger = None
    for i in b_diff_a:
        if not b_lower or i < b_lower:
            b_lower = i
        if not b_bigger or i > b_bigger:
            b_bigger = i

    a_score = a_bigger - a_lower
    b_score = b_bigger - b_lower

    if a_score > b_score:
        return a

    return b


# def who_wins_iterating_once(people_games):
#     (a, a_values), (b, b_values) = people_games.items()  # O(2)

#     a_ind, b_ind = 0, 0

#     a_lower = 10
#     b_lower = 10
#     a_bigger = 0
#     b_bigger = 0

#     while a_ind < len(a_values) or b_ind < len(b_values):
#         if a_ind > b_ind:


#     a_score = a_bigger - a_lower
#     b_score = b_bigger - b_lower

#     if a_score > b_score:
#         return a

#     return b


if __name__ == "__main__":
    entrada = {"Clara": [0, 1, 5, 9, 10], "Marco": [0, 2, 8, 9, 10]}

    print(who_wins(entrada))
    # print(who_wins_iterating_once(entrada))
