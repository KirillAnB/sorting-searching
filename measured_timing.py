import timeit


_list_to_sort = list(range(1000, 1, -1))

def times_checking(algorithm, data):
    setup_code = f"from __main__ import {algorithm}"
    stmt = f"{algorithm}({data})"
    times = timeit.repeat(setup=setup_code, stmt=stmt, repeat=3, number=2)
    print(f"{algorithm} algotithm min time {min(times)}")

def bubble_sorting(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
    return lst

def quick_sorting(lst):
    if len(lst) < 2:
        return lst
    left = [i for i in lst if i < lst[len(lst)//2]]
    center = [i for i in lst if i == lst[len(lst)//2]]
    right = [i for i in lst if i > lst[len(lst)//2]]
    return quick_sorting(left) + center + quick_sorting(right)


times_checking(algorithm="bubble_sorting", data=_list_to_sort)
times_checking("quick_sorting", _list_to_sort)
