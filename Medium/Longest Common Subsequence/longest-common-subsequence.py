#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        '''def Lcs(x,y,s1,s2,dp):
            if x==0 or y==0:
                return 0
            if dp[x][y]!=-1:
                return dp[x][y]
            elif s1[x-1]==s2[y-1]:
                dp[x][y]=1+Lcs(x-1,y-1,s1,s2,dp)
                return dp[x][y]
            
            dp[x][y]=max(Lcs(x,y-1,s1,s2,dp),Lcs(x-1,y,s1,s2,dp))
            return dp[x][y]
        dp=[[-1 for i in range(x+ 1)]for j in range(y+ 1)]
        return Lcs(x,y,s1,s2,dp)'''
        l=[[0 for k in range(len(s2)+1)]for h in range(len(s1)+1)]
        for i in range(len(s1)-1,-1,-1):
            for j in range(len(s2)-1,-1,-1):
                if s1[i]==s2[j]:
                    l[i][j]=1+l[i+1][j+1]
                else:
                    l[i][j]=max(l[i+1][j],l[i][j+1])
        return l[0][0]
        
    
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends