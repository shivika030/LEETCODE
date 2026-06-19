class Solution:
    def candy(self, arr: List[int]) -> int:
        n=len(arr)
        arr2=[1]*n
    
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                arr2[i]=arr2[i-1]+1
                
        for i in range (n-2,-1,-1):
            if arr[i]>arr[i+1]:
                arr2[i]=max(arr2[i],arr2[i+1]+1)
                
        return sum(arr2) 