class Solution: #Brute Force
    def maxArea(self, height: List[int]) -> int:
        #loop through all indexes 1,2,3,4,5,6
        #multiply smallest height by distance from index
        maxHeight = 0
        for heights in range(len(height)):
            for width in range(len(height)):
                if height != width:
                    #Multiply smaller height or width by the distance from the two add to max
                    if height[heights] < height[width]:
                        #If the first is smaller than second
                        currHeight = (height[heights]*abs(heights-width))
                    else:
                        currHeight = (height[width]*abs(heights-width))
                    if currHeight > maxHeight:
                        maxHeight = currHeight
        return maxHeight
