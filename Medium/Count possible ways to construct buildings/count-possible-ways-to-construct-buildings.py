#User function Template for python3

#User function Template for python3

#User function Template for python3

class Solution:
    def TotalWays(self, n):
        if n == 1:
            return 4
        if n == 2:
            return 9
        a = 2; b = 3
        MOD = 1000000007
        for i in range(2, n):
            a, b = b%MOD, (a%MOD + b%MOD)%MOD
        
        return (b*b)%MOD


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.TotalWays(N)
		print(ans)
# } Driver Code Ends