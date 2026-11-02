class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        tank,start=0,0
        if sum(gas)- sum(cost)<0:
            return -1
        for i in range( len(gas)):
            tank += gas[i]-cost[i]
            if tank<0:
                tank=0
                start=i+1
        return start        