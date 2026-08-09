class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #creating hash set
        numsSet=set(nums)
        res=0
        for num in numsSet:
            streak=0
            if num-1 not in numsSet:
                i=num
                while(i) in numsSet:
                    streak+=1
                    i+=1

            res= max(res,streak)
        return res
                