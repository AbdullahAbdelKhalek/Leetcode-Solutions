# Problem: 412. FizzBuzz
# Link: https://leetcode.com/problems/fizz-buzz/
# Difficulty: Easy
# Description: Given an integer n, return a string array answer (1-indexed) where:
# - "Fizz" is added to the array for multiples of 3.
# - "Buzz" is added for multiples of 5.
# - "FizzBuzz" is added for multiples of both 3 and 5.
# Otherwise, the string representation of the number is added.
# Example:
#   Input: n = 15
#   Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
# Constraints:
#   - 1 <= n <= 10^4

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append('FizzBuzz')
            elif i % 3 == 0:
                answer.append('Fizz')
            elif i % 5 == 0:
                answer.append('Buzz')
            else:
                answer.append(str(i))
        return answer
