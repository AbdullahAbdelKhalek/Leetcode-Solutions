# Problem: 1672. Richest Customer Wealth
# Link: https://leetcode.com/problems/richest-customer-wealth/
# Difficulty: Easy
# Description:
#   You are given an m x n integer grid `accounts` where `accounts[i][j]` is the amount 
#   of money the i-th customer has in the j-th bank. Return the wealth that the richest
#   customer has.
#
# Example 1:
#   Input: accounts = [[1, 2, 3], [3, 2, 1]]
#   Output: 6
#
# Example 2:
#   Input: accounts = [[1, 5], [7, 3], [3, 5]]
#   Output: 10
#
# Example 3:
#   Input: accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
#   Output: 17
#
# Constraints:
#   - m == accounts.length
#   - n == accounts[i].length
#   - 1 <= m, n <= 50
#   - 1 <= accounts[i][j] <= 100

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        for i in range(len(accounts)):
            accounts[i] = sum(accounts[i])  # Calculate total wealth for each customer
        return max(accounts)  # Return the maximum wealth
