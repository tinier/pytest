
def buble_sort(nos):
    def swap(i):
        if nos[i] > nos[i + 1]:
            nos[i], nos[i + 1] = nos[i + 1], nos[i]

            return True
        else:
            return False

    i = 0
    j = len(nos) - 1

    while i < j:
        any_swapped = False

        for si in range(i, j):
            swapped = swap(si)

            if swapped:
                if not any_swapped and si > 0:
                    i = si - 1

                any_swapped = True

        j -= 1

        if not any_swapped:
            return nos

    return nos


if __name__ == '__main__':
    from sort_test import sort_test

    sort_test(buble_sort)