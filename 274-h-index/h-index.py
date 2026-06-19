class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h=0
        j=1
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i]>=j:
                h=j
                j+=1
        return h        