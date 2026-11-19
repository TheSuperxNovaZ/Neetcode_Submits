from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if len(s1) > len(s2):
        #     return False
        # count1 = [0] * 26
        # count2 = [0] * 26
        # for char in s1:
        #     count1[ord(char) - ord('a')] += 1
        # for i in range(len(s1)):
        #     count2[ord(s2[i]) - ord('a')] += 1
        # if count1 == count2:
        #     return True
        # left = 0
        # for right in range(len(s1), len(s2)):
        #     count2[ord(s2[right]) - ord('a')] += 1
        #     count2[ord(s2[left]) - ord('a')] -= 1
        #     left += 1
        #     if count1 == count2:
        #         return True
        # return False
        ss1 = ''.join(sorted(s1))
        lens1 = len(s1)
        lens2 = len(s2)
        if lens1>lens2:
            return False
        for left in range(lens2):
            if s2[left] in s1:
                if ''.join(sorted(s2[left:left+lens1]))==ss1:
                    return True
        return False