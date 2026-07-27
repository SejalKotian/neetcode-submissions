class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size=len(nums)
        leftprod =[1]*(size)
        leftprod[0]=nums[0]
        for i in range(1,size):
            leftprod[i]=nums[i]*leftprod[i-1]
        rightprod =[1]*(size)
        rightprod[-1]=nums[-1]
        for i in range(size-2,-1,-1):
            rightprod[i]=nums[i]*rightprod[i+1]
        print(rightprod)
        result=[1]*(size)
        result[0]=rightprod[1]
        for i in range(1,size-1):
            result[i]=leftprod[i-1]*rightprod[i+1]
        result[-1]=leftprod[size-2]
        return result