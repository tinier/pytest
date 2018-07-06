
def selection_sort(nos):
    for j in range(len(nos) - 1, 0, -1):
        mi = 0

        for i in range(1, j + 1):
            if nos[i] > nos[mi]:
                mi = i

        nos[j], nos[mi] = nos[mi], nos[j]

    return nos


if __name__ == '__main__':
    from sort_test import sort_test

    sort_test(selection_sort)


