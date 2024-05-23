#User function Template for python3

class Solution:
    def longestPalindrome(self, S):
        # code here
        maxl=1
        res=S[0]
        for i in range(0,len(S)+1):
            for j in range(i+1,len(S)):
                if j-i+1>maxl and S[i:j+1]==S[i:j+1][::-1]:
                    maxl=j-i+1
                    res=S[i:j+1]
        return res
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        S = input().strip()
        ob=Solution()
        print(ob.longestPalindrome(S))
# } Driver Code Ends