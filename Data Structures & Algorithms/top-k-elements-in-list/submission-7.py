class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #usinghashmap
        result={}
        for num in nums:
            if num in result:
                result[num]+=1
            else:
                result[num]=1

        sorted_result = sorted(
            result.items(), key=lambda item: item[1], reverse=True
        )
        result_topk = sorted_result[:k]
        return [num for num, freq in result_topk]