class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list1 = [0]*2
        count1 = -1
        for i in nums:
            count1 += 1
            count2 = len(nums)
            for j in reversed(nums):
                count2 -= 1
                if count1 == count2:
                    break
                if i + j == target:
                    list1[0] = count1
                    list1[1] = count2
                
        return list1