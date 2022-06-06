class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        smallestIndex = -1
        smallestDistance = sys.maxsize
        for i in points:
            if(x == i[0] or y == i[1]): #Checks if valid
                distance = abs(x-i[0]+abs(y-i[1]))
                if distance<smallestDistance: #Checks if distance is smallest -> smallestIndex = distance
                    smallestIndex = points.index(i)
                    smallestDistance = distance
        return smallestIndex
                
        
