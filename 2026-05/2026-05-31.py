# https://leetcode.com/problems/destroying-asteroids/?envType=daily-question&envId=2026-05-31


from typing import List

# T:O(NlogN) S:O(1)
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for a in asteroids:
            if a>mass:
                return False
            mass+=a
        return True