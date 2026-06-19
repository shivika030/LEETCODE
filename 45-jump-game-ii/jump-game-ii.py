class Solution:
    def jump(self, nums: List[int]) -> int:
        left=0
        right=0
        jump=0
        while right<len(nums)-1:
            end=0
            for i in range(left,right+1):
                end=max(end,i+nums[i])
            left=right+1
            right=end
            jump+=1
        return jump    
        