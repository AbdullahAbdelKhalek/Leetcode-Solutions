# Problem: Running Sum of 1d Array
# Link: https://leetcode.com/problems/running-sum-of-1d-array/
# Difficulty: Easy
# Description: Given an array `nums`, return the running sum of the array.
# Example:
#   Input: nums = [1, 2, 3, 4]
#   Output: [1, 3, 6, 10]
# Constraints:
#   - 1 <= nums.length <= 1000
#   - -10^6 <= nums[i] <= 10^6

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
