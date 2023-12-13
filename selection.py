def selection(some_list):
    for i in range(len(some_list)):
        smallest = i
        for j in range(i+1, len(some_list)):
            if some_list[j] < some_list[smallest]:
                smallest = j
        some_list[i], some_list[smallest] = some_list[smallest], some_list[i]
    print(some_list)

selection([5,4,3,2,1])
