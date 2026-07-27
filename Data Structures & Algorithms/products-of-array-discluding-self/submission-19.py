class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #O(n) time and O(1) space
        size=len(nums)
        result=[1]*size
        prefix=1
        for i in range(size):
            result[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(size-1,-1,-1):
            result[i]*=suffix
            suffix*=nums[i]

        return result