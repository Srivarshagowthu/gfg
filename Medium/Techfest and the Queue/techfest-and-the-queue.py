


from typing import List


class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        # code here
        factors=[*range(b+1)]
        i=2
        while i*i<=b:
            if factors[i]==i:
                for j in range(i*i,b+1,i):
                    factors[j]=i
            i+=1
        from collections import defaultdict
        ans=0
        for i in range(a,b+1):
            factor=defaultdict(int)
            while i>1:
                factor[factors[i]]+=1
                i//=factors[i]
            ans+=sum(factor.values())
        return ans



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=int(input())
        b=int(input())
        
        obj = Solution()
        res = obj.sumOfPowers(a,b)
        
        print(res)
        

# } Driver Code Ends