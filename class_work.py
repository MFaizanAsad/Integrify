#!/usr/bin/env python
# coding: utf-8

# In[1]:


# min_split_diff.py, june 14
"""


Gets the minimum absolute difference of the sums of two subsets of 
an array that can be obtained 
"""

def get_diff(sum_left,sum_right,value):
    """
    Gets the absolute difference between two halves of an array given
    the sums of the left and right halves and the value of the
    current index
    """
    
    left = sum_left + value
    right = sum_right - value
    return left,right, abs(left-right)


def get_min_diff_split(input_list = []):
    """
    Finds the minimum absolute difference of the sums of any two subsets
    of the input array 
    """

    # initial problem setup
    left = 0
    right = sum(input_list)
    diffs = []
    diffs.append(abs(right))

    # memoization of possible solutions
    for i in range(len(input_list)-2):
        left,right,diff = get_diff(left,right,input_list[i])
        diffs.append(diff)

    # getting the first occurrence of best solution
    split_min, _ = min((v,i) for i,v in enumerate(diffs))

    return split_min #, left_arr, right_arr


def test():
    test_list = [3,1,2,4,3]
    s_min = get_min_diff_split(test_list)
    print(s_min)


if __name__ == "__main__":
    test()


# In[ ]:




