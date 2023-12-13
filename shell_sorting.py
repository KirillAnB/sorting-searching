def shell_sort(_list):
    if len(_list)<=1:
        return _list
    else:
        distanse = len(_list)//2
        while distanse > 0:
            for i in range(distanse, len(_list)):
                temp = _list[i]
                j = i
                while j >= distanse and _list[j - distanse] > temp:
                    _list[j] = _list[j - distanse]
                    j = j - distanse
                _list[j] = temp
            distanse = distanse//2
    print(_list)

shell_sort([5,4,3,2,1])

