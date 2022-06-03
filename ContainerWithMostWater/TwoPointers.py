class Solution: #Two Pointers
    def maxArea(self, height: List[int]) -> int:
        rPoint = len(height)-1 #Right point is last index in list
        lPoint = 0 #First index in list
        maxHeight = 0
        while rPoint > lPoint:
            if height[rPoint] < height[lPoint]:
                currHeight = height[rPoint]*(rPoint-lPoint)
                rPoint-=1
            else:
                currHeight = height[lPoint]*(rPoint-lPoint) 
                lPoint+=1
            maxHeight = max(currHeight, maxHeight)
        return maxHeight
       
