
def quick_sort(nos):
    def partial(start, end):
        if end - start <= 1:
            return

        key = start + (end - start) // 2
        pivot = nos[key]
        lm, rm = start, end - 1

        while lm <= rm:
            while lm <= rm and nos[lm] <= pivot:
                lm += 1
            while nos[rm] > pivot:
                rm -= 1

            if lm < rm:
                nos[lm], nos[rm] = nos[rm], nos[lm]

                if nos[lm] == pivot:
                    key = lm

                lm += 1
                rm -= 1

        nos[key], nos[rm] = nos[rm], nos[key]

        partial(start, rm)
        partial(rm + 1, end)

    partial(0, len(nos))

    return nos


def quick_sort2(nos):
    def partial(start, end):
        if end - start <= 1:
            return

        key = start + (end - start) // 2
        pivot = nos[key]
        lm, rm = start, end - 1

        while lm < rm:
            while lm < rm and nos[rm] > pivot:
                rm -= 1
            while lm < rm and nos[lm] <= pivot:
                lm += 1

            nos[lm], nos[rm] = nos[rm], nos[lm]

            if nos[lm] == pivot:
                key = lm

        nos[key], nos[lm] = nos[lm], nos[key]

        partial(start, lm)
        partial(lm + 1, end)

    partial(0, len(nos))

    return nos


if __name__ == '__main__':
    from sort_test import sort_test

    sort_test(quick_sort)
    sort_test(quick_sort2)


