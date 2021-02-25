#!/usr/bin/env python3

'''
Author: Gene Jiang
Date: 2021-02-25 19:50:35
LastEditors: Gene Jiang
LastEditTime: 2021-02-25 20:00:11
Description: 
'''
import pytest


class Solution:

    """Docstring for . """

    def remove_elements(self, nums: list, val: int) -> int:
        if nums == None or len(nums) == 0:
            return 0
        
        left = 0
        right = len(nums)

        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                left += 1
            else:
                right -= 1
        
        return right, nums[0, right]

