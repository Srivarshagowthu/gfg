#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2, n, m):
        # code here
        l=[[0 for k in range(len(s2)+1)]for h in range(len(s1)+1)]
        val=0
        for i in range(len(s1)-1,-1,-1):
            for j in range(len(s2)-1,-1,-1):
                if s1[i]==s2[j]:
                    l[i][j]=1+l[i+1][j+1]
                    val=max(val,l[i][j])
        return val

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends