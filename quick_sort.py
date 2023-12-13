def quick_sort(lst):
    if len(lst)<=1:
        return lst
    else:
        left = [ i for i in lst if i < lst[len(lst)//2]]
        right = [j for j in lst if j > lst[len(lst)//2]]
        center = [k for k in lst if k == lst[len(lst)//2]]
        return quick_sort(left) + center + quick_sort(right)


print(quick_sort([5,4,3,2,1,9,6,9,45,2]))


