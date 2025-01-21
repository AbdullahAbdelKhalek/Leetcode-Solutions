# Problem: 383. Ransom Note
# Link: https://leetcode.com/problems/ransom-note/
# Difficulty: Easy
# Description:
#   Given two strings ransomNote and magazine, return true if ransomNote can
#   be constructed by using the letters from magazine and false otherwise.
#   Each letter in magazine can only be used once in ransomNote.
#
# Example 1:
#   Input: ransomNote = "a", magazine = "b"
#   Output: false
#
# Example 2:
#   Input: ransomNote = "aa", magazine = "ab"
#   Output: false
#
# Example 3:
#   Input: ransomNote = "aa", magazine = "aab"
#   Output: true
#
# Constraints:
#   - 1 <= ransomNote.length, magazine.length <= 10^5
#   - ransomNote and magazine consist of lowercase English letters.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Determines if ransomNote can be constructed from magazine.

        Args:
        ransomNote (str): The string representing the ransom note.
        magazine (str): The string representing the magazine.

        Returns:
        bool: True if ransomNote can be constructed, False otherwise.
        """
        chardic = {}
        
        # Count characters in magazine
        for currchar in magazine:
            if currchar in chardic:
                chardic[currchar] += 1
            else:
                chardic[currchar] = 1
        
        # Check if ransomNote can be formed
        for currchar in ransomNote:
            if currchar not in chardic or chardic[currchar] == 0:
                return False
            chardic[currchar] -= 1
        
        return True
