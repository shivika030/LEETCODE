class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sums = 0
        length = float('inf')

        for right in range(len(nums)):
            sums += nums[right]

            while sums >= target:
                length = min(length, right - left + 1)
                sums -= nums[left]
                left += 1

        if length == float('inf'):
            return 0
        return length