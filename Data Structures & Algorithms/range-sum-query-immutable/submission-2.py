class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_NumArray = [0]
        total = 0

        for num in nums:
            total += num
            self.prefix_NumArray.append(total)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_NumArray[right + 1] - self.prefix_NumArray[left]