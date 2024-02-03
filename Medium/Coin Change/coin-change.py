#User function Template for python3
class Solution:
    def count(self, l, n, summ):
        # code here
        '''def coin(i,l,summ,dp):
            if i>=n:
                if summ==0:
                    return 1
                return 0
            if summ<0:
                return 0
            if dp[i][summ]!=-1:
                return dp[i][summ]
        
            dp[i][summ]=coin(i,l,summ-l[i],dp)+coin(i+1,l,summ,dp)
            return dp[i][summ]
        dp=[[-1]*(summ+1)for h in range(n)]
        res=coin(0,l,summ,dp)
        return res'''
        # code here
        dp=[[-1]*(summ+1)for h in range(n)]
        def coin(i,l,summ):
            if summ==0:
                return 1
            if summ<0 or i==n:
                return 0
            if dp[i][summ]!=-1:
                return dp[i][summ]
            ic=0
            if l[i]<=summ:
                ic=coin(i,l,summ-l[i])
            ec=coin(i+1,l,summ)
            dp[i][summ]=ic+ec
            return dp[i][summ]
        
        res=coin(0,l,summ)
        return res
         
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends