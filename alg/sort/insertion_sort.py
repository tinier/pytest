
def insertion_sort(nos):
    for i in range(1, len(nos)):

        inserted = nos[i]
        j = i - 1

        while j >=0 and nos[j] > inserted:
            nos[j + 1] = nos[j]
            j -= 1

        nos[j + 1] = inserted

    return nos


if __name__ == '__main__':
    from sort_test import sort_test

    sort_test(insertion_sort)