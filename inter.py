def inter(lst, item):
    lowest = 0
    highest = len(lst)-1
    found = False
    while lowest <= highest and item >= lst[lowest] and item <= lst[highest]:
        # midpoint = lowest + int(((float(highest - lowest)/lst[highest]-lst[lowest])) * (item - lst[lowest]))
        midpoint = lowest + int(((float(highest - lowest) / (lst[highest] - lst[lowest])) * (item - lst[lowest])))
        if lst[midpoint] == item:
            found = True
            return found
        if lst[midpoint] < item:
            lowest = midpoint + 1
        else:
            highest = midpoint - 1
    return found

print(inter([1,2,3,4,5], 3))
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