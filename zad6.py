def join_lists(first: list, second: list) -> list:
    new_set = set(first + second)
    new_list = []

    for x in new_set:
        new_list.append(x**3)

    return new_list
