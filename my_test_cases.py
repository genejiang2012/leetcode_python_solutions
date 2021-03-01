'''
Author: Gene Jiang
Date: 2021-02-25 20:09:14
LastEditors: Gene Jiang
LastEditTime: 2021-03-01 19:37:34
Description: 
'''

from . import remove_elements

def test_remove_element():
    s = remove_elements.Solution()
    nums = [2, 2, 3, 3]
    val = 2
    assert s.remove_elements(nums, val)[0] == 2

    

