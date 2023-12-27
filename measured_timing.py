import timeit


_list_to_sort = list(range(1_000_000, 1, -1))
_data = list(range(1, 1_000_000))

def times_checking(algorithm, data):
    setup_code = f"from __main__ import {algorithm}"
    stmt = f"{algorithm}({data})"
    times = timeit.repeat(setup=setup_code, stmt=stmt, repeat=3, number=2)
    print(f"{algorithm} algorithm min time {min(times)}")

def serach_methods_time(*args):
    method, data, item = args
    setup_code = f"from __main__ import {method}"
    stmt = f"{method}({data}, {item})"
    times = timeit.repeat(setup=setup_code, stmt = stmt, repeat=3, number=3)
    print(f"{method} works at {times}")
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

def selection_sorting(lst):
    for i in range(len(lst)):
        smallest_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[smallest_idx]:
                smallest_idx = j
        lst[i], lst[smallest_idx] = lst[smallest_idx], lst[i]
    return lst

def insertion_sorting(lst):
    for i in range(1, len(lst)):
        item_to_insert = lst[i]
        j = i - 1
        while j>=0 and lst[j] > item_to_insert:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = item_to_insert
    return lst

def linear_searching(data, item):
    found = False
    start = 0
    end = len(data) - 1
    while start <= end and not found:
        if data[start] == item:
            found = True
            return found
        else:
            start += 1
    return found

def binary_searching(data, item):
    found = False
    start = 0
    end = len(data) - 1
    while start <= end and not found:
        mid = (start + end) // 2
        if data[mid] == item:
            found = True
            return found
        elif data[mid] < item:
            start = mid + 1
        else:
            end = mid - 1
    return found
# times_checking(algorithm="bubble_sorting", data=_list_to_sort)
# times_checking("quick_sorting", _list_to_sort)
# times_checking("selection_sorting", _list_to_sort)
# times_checking("insertion_sorting", _list_to_sort)

serach_methods_time("linear_searching", _data, 500_000)
serach_methods_time("binary_searching", _data, 500_000 )

