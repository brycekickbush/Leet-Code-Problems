class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lastSum = nums[0] #Last sum = first num in list
        maxCount = nums[0] #maxCount = first num in list
        for i in nums: #Loops through all nums in list
            if lastSum >= 0: #If number greater than 0 add it to sum
                lastSum += i
            else: #If number is less than 0 make that the current sum
                lastSum = i
            maxCount = max(lastSum, maxCount)
        return maxCount
