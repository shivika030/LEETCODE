class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        for i in range(len(numbers)):
            n=numbers[l]+numbers[r]
            if n> target:
                r-=1
            elif n<target:
                l +=1
            else:
                return [l+1,r+1]  