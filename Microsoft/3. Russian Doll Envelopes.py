"""
Problem: 354. Russian Doll Envelopes
Platform: LeetCode
Link: https://leetcode.com/problems/russian-doll-envelopes/

Approach:
- Sort the envelopes:
   1. By width ascending.
   2. By height descending if widths are equal (to avoid invalid nesting).
- Then find the Longest Increasing Subsequence (LIS) on heights.
- This works because widths are already strictly increasing or non-overlapping.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        heights=[h for _,h in envelopes]
        lis=[]
        for h in heights:
            idx=bisect_left(lis,h)
            if idx==len(lis):
                lis.append(h)
            else:
                lis[idx]=h
        return len(lis)
