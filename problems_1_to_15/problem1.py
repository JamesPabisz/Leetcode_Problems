class Solution:
    # O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
     
    # O(n^2)
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]: 
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i]+nums[j] == target):
                    return [i, j]
                    
    def twoSumOneLiner(self, a, t): return next(([i,j] for i in range(len(a)) for j in range(i+1,len(a)) if a[i]+a[j]==t), None)
    
