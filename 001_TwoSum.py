class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d_hash = {}
        
        for i in range(len(nums)):
            if nums[i] not in d_hash:
                d_hash[target-nums[i]] = i
            else:
                return [d_hash[nums[i]],i]
        