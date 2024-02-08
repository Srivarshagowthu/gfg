#User function Template for python3


class Solution:
    def factorial (self, N):
        # code here
        def fact(i):
            if i<=0:
                return 1
            if i==1:
                dp[i]=1
            if dp[i]!=-1:
                return dp[i]
            ans=1
            ans*=(i*(fact(i-1)))
            dp[i]=ans
            return dp[i]
        dp=[-1]*200
        return fact(N)
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.factorial(N))

# } Driver Code Ends