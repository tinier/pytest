import sys
from randint_list import randint_list
from timeit import timeit
from sort_test import sort_test
from buble_sort import buble_sort
from insertion_sort import insertion_sort
from shell_sort import shell_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from quick_sort import quick_sort2

sys.setrecursionlimit(10**5)
nos = randint_list(10000, no_ext = 500000)

def test(sort_func):
    return sort_test(sort_func, nos = nos, repeat = 1)

def show_times(tsmap, msg):
    print(msg)

    for x in sorted(tsmap.items(), key = lambda x: x[1]):
        print('\t', x)

    print()

if __name__ == '__main__':
    sort_funcs = [quick_sort, merge_sort, insertion_sort, shell_sort, selection_sort, buble_sort, quick_sort2]

    rand_times_map = {}
    asc_times_map = {}
    desc_times_map = {}

    for f in sort_funcs:
        times = test(f)

        rand_times_map[f.__name__] = times[0]

        if len(times) > 1:
            asc_times_map[f.__name__] = times[1]
            desc_times_map[f.__name__] = times[2]

    show_times(rand_times_map, 'random list sort times:')
    show_times(asc_times_map, 'asc list sort times:')
    show_times(desc_times_map, 'desc list sort times:')
