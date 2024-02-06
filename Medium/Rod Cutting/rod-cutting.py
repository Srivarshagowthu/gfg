#User function Template for python3

class Solution:
    def cutRod(self, a, n):
        #code here
        '''def rod(a,n):
            if n==0:
                return 0
            if dp[n]!=-1:
                return dp[n]
            ans=float('-inf')
            for i in range(n+1):
                l=i+1
                if l<=n:
                    sub=a[i]+rod(a,n-l)
                    ans=max(ans,sub)
            dp[n]=ans
            return dp[n]
        dp=[-1]*(n+1)
        return rod(a,n)'''
        dp=[0]*(n+1)
        for i in range(1,n+1):
            ans=float("-inf")
            for j in range(1,i+1):
                ans=max(ans,a[j-1]+dp[i-j])
            dp[i]=ans
        return dp[n]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends