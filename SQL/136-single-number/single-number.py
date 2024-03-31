class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictq = {}
        
        for i in nums:
            if i in dictq:
                dictq[i] += 1
            else:
                dictq[i] = 1

        for key, value in dictq.items():
            if value == 1:
                return key
