
def gap_insertion_sort(nos, start, gap):
    for i in range(start + gap, len(nos), gap):
        inserted = nos[i]

        j = i - gap
        while inserted < nos[j] and j >= 0:
            nos[j + gap] = nos[j]
            j -= gap

        nos[j + gap] = inserted


def shell_sort(nos):
    gap = 3

    for i in range(0, gap):
        gap_insertion_sort(nos, i, gap)

    gap_insertion_sort(nos, 0, 1)

    return nos



if __name__ == '__main__':
    from sort_test import sort_test

    sort_test(shell_sort)
