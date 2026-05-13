class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = [0] * 26
        list2 = [0] * 26
        for i in s:
            list1[ord(i)-97] += 1
        for i in t:
            list2[ord(i)-97] += 1
        if list1 == list2:
            return True
        else:
            return False