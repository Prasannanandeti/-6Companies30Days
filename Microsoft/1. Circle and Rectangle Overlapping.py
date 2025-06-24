"""
Problem: Circle and Rectangle Overlapping
Platform: LeetCode
Link: https://leetcode.com/problems/circle-and-rectangle-overlapping/

Approach:
- Clamp the circle center (xCenter, yCenter) to the rectangle boundaries.
- Find the closest point (x_closest, y_closest) inside the rectangle to the circle center.
- If the distance between this point and the circle center is less than or equal to radius, they overlap.

Time Complexity: O(1)
Space Complexity: O(1)
"""
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closestX=max(x1,min(xCenter,x2))
        closestY=max(y1,min(yCenter,y2))
        dx=xCenter-closestX
        dy=yCenter-closestY
        return dx*dx+dy*dy<=radius*radius
