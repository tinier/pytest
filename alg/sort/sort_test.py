from randint_list import randint_list
from timeit import timeit

def sort_test(sort_func, no_count = 16, no_ext = 300, nos = None, repeat = 1000):
    def sort_copy(src):
        global last_sorted
        last_sorted = sort_func(copy_list(src))

    print('-'*32, sort_func.__name__, 'begin', '-'*32)
    print()

    unsorted = randint_list(no_count, no_ext = no_ext) if nos is None else nos
    asc_list = sorted(unsorted)
    times = []

    print_list('unsorted:', unsorted)
    t1 = timeit(lambda: sort_copy(unsorted), number = repeat)
    print_list('sorted:  ', last_sorted)
    print('time:', t1)
    print()
    assert last_sorted == asc_list
    times.append(t1)

    if len(unsorted) > 1:
        print_list('asc_list:', asc_list)
        t2 = timeit(lambda: sort_copy(asc_list), number = repeat)
        print_list('sorted:  ', last_sorted)
        print('time:', t2)
        print()
        assert last_sorted == asc_list
        times.append(t2)

        desc_list = sorted(unsorted, reverse = True)
        print_list('dsc_list:', desc_list)
        t3 = timeit(lambda: sort_copy(desc_list), number = repeat)
        print_list('sorted:  ', last_sorted)
        print('time:', t3)
        print()
        assert last_sorted == asc_list
        times.append(t3)

    print('-'*33, sort_func.__name__, 'end', '-'*33)
    print()

    return times


def print_list(msg, lst, *args):
    print(msg, show_list(lst), *args)

def show_list(lst, ceil = 16):
    count = len(lst)

    if count <= ceil:
        return str(lst)
    else:
        show = '[' \
            + ', '.join(map(str, lst[:ceil // 2])) \
            + ' ... ' \
            + ', '.join(map(str, lst[count - ceil + (ceil // 2):])) \
            + ']'

        return show

def copy_list(lst):
    return [x for x in lst]