class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=0
        for i in range(k):
            summ+=nums[i]
        maxsum=summ

        start=0
        end=k

        while(end<len(nums)):
            summ-=nums[start]
            start+=1

            summ+=nums[end]
            end+=1

            maxsum=max(maxsum,summ)

        return maxsum/k
    
        

        
        