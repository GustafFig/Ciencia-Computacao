def tree(people, employee):
    total = 1
    subordinateds = people[employee]
    if len(subordinateds) == 0:
        return total

    for person in subordinateds:
        total += tree(people, person)

    return total


entrada = { 1: [2, 3], 2: [4], 3: [], 4: [5, 6], 5: [7], 6: [], 7: [] }

if __name__ == "__main__":
    print(tree(entrada, 1))
