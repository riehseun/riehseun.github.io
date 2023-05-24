class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        accumulated_gas = 0
        starting_index = 0

        for i in range(n):
            accumulated_gas += (gas[i]-cost[i])
            if accumulated_gas < 0:
                accumulated_gas = 0
                starting_index = i + 1

        return starting_index