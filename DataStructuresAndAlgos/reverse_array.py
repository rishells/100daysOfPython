# Given an array, , of  integers, print 's elements in reverse order as a single line of space-separated numbers.
# Sample Input

# 4
# 1 4 3 2
# Sample Output

# 2 3 4 1

import math
import os
import random
import re
import sys

def reverse_array(len_arr, array_elements):
    container = []
    for i in range(len_arr,0,-1):
        #container.append(array_elements[i-1])
        print(array_elements[i-1], end = ' ')
    #return container
    # for item in array_elements:
    #     print(array_elements[item])

# def fix_output(container_list):
#     for new_container in container_list:
#         print(new_container, end = ' ')
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    reverse_array(n,arr)
    # unformatted_lst = reverse_array(n,arr)
    # fix_output(unformatted_lst)
    # my_arr = {1,4,3,2}
    # print(len(my_arr))