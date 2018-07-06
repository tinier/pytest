
def merge_sort(nos):
    def merge(start, pivot, end):
        left = nos[start : pivot]
        right = nos[pivot : end]

        i = start
        j = 0
        k = 0

        while j < len(left) or k < len(right):
            if j == len(left) or (k < len(right) and left[j] > right[k]):
                nos[i] = right[k]
                k += 1
            else:
                nos[i] = left[j]
                j += 1

            i += 1

    def merge_sort_util(start, end):
        if end - start <= 1:
            return
        else:
            pivot = start + (end - start) // 2

            merge_sort_util(start, pivot)
            merge_sort_util(pivot, end)

            merge(start, pivot, end)


    merge_sort_util(0, len(nos))

    return nos


if __name__ == '__main__':
    from sort_test import sort_test

    sort_test(merge_sort, nos=[])