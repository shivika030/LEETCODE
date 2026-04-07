class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        strs=[list(word)for word in strs]
        strs.sort(key=len)
        n=len(strs[0])
        m=len(strs)
        for i in range(n):
            for j in range(1,m):
                if strs[0][i]!=strs[j][i]:
                    return res  
            res+=strs[0][i]
        return res                    
            