class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #creating hash set
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        res=0
        for num in nums:
            streak=0
            if num in count and num-1 not in count:
                i=num
                while(i) in count:
                    streak+=1
                    i+=1

            res= max(res,streak)
        return res
                