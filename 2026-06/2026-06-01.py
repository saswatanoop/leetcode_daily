# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/?envType=daily-question&envId=2026-06-01

from typing import List
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        min_cost=0
        i=1
        n=len(cost)
        while n-i>=0:
            if i%3!=0:
                min_cost+=cost[n-i]
            i+=1
        return min_cost
