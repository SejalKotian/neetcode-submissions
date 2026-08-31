class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total=0
        count=0
        present={0:1}
        for num in nums:
            total+=num
            if total%k in present:
                count+=present[total%k]
                present[total%k]+=1

            else:
                present[total%k]=1
        return count
