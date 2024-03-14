import math
class Solution:
    def canPlaceFlowers(self, l: List[int], n: int) -> bool:
        # f= math.ceil(len(flowerbed)/2)
        # # print(f)
        # count=0
        # for i in range(len(flowerbed)):
        #     if flowerbed[i]==1:
        #         count+=1
        # if n+count<=f:
        #     return True
        # return False
        # print(l)
        x=len(l)
        cc=0
        if x==1:
            if l[0]==0 and  (n==1 or n==0):
                return 1
            elif l[0]==1 and n==0:
                return 1
            else:
                return 0    
        if l[0]==0 and l[1]==0:
            l[0]=1
            cc=cc+1
        

        for i in range (1,len(l)-1):
            if l[i]==0  and l[i-1]==0 and l[i+1]==0:
                cc+=1
                l[i]=1
        print(l) 
        if l[x-2]==0 and l[x-1]==0:
            
            cc=cc+1         
        if cc>=n:
            return 1
        else:
            return 0          


