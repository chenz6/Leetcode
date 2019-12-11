  
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        firstTime={}
        counting={}
        Time=0
        lens=0
        
        for i,n in enumerate(nums):
            firstTime.setdefault(n,i)
            counting[n]=counting.get(n,0)+1
            if counting[n] > Time:
                Time=counting[n]
                lens=i-firstTime[n]+1
            elif counting[n]== Time:
                lens=min(lens,i-firstTime[n]+1)
        
        return lens
                