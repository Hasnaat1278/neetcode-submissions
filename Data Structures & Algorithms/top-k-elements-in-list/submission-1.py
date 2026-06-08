class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for i in nums:
            groups[i] = groups.get(i,0) + 1
        sorted_freq = sorted(groups.items(), key=lambda item: item[1], reverse=True)
        return [sorted_freq[i][0] for i in range(k)] 
            
        