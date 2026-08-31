class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total=0
        present={0:1} # you've seen the sum of the entire array
        count=0
        for num in nums:
            total+=num
            if total-k in present:
                count+=present[total-k]
            if total not in present:
                present[total]=1
            else:
                present[total]+=1

        return count
