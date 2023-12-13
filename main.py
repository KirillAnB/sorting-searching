# import numpy as np
# import pandas as pd
#
# # myMatrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# # print(myMatrix)
# # myMatrix.transpose()
# # print(myMatrix.transpose())
#
# my_data_frame = pd.DataFrame([[1,'Kirill',39,'Phillipines'],
#                              [2,'Julia', 29, 'Russia']])
#
# my_data_frame.columns = ['id', 'name', 'age', 'country']
# print(my_data_frame)
# print(my_data_frame.iloc[1,3])
# my_data_frame.iloc[1,3] = my_data_frame.iloc[0,3]
# print(my_data_frame)

def bubble(_list: list) -> list:
    if_swapped = True
    last_elem = len(_list)-1
    while if_swapped:
        if_swapped = False
        for i in range(last_elem):
            for j in range(last_elem):
                if _list[j] > _list[j+1]:
                    _list[j], _list[j+1] = _list[j+1], _list[j]
                    if_swapped = True
    print(_list)

bubble([6,5,4,3,7,1])