class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i, n in enumerate(nums):
            bruh = target - n
            if bruh in map:
                return [map[bruh], i]
            map[n] = i
            
                
        return list1