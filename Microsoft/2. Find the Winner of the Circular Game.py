"""
Problem: 1823. Find the Winner of the Circular Game
Platform: LeetCode
Link: https://leetcode.com/problems/find-the-winner-of-the-circular-game/

Approach:
- This is a variation of the Josephus problem.
- We use a 0-based index and adjust the result to 1-based at the end.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends=list(range(1,n+1))
        idx=0
        while len(friends)>1:
            idx=(idx+k-1)%len(friends)
            friends.pop(idx)
        return friends[0]
sol=Solution()
print(sol.findTheWinner(5,2))
