#User function Template for python3

class Solution:

    def removeKdigits(self,s, k):
        # code here
        stack=[]
        for i in s:
            while k>0 and stack and stack[-1]>i:
                stack.pop()
                k-=1
            stack.append(i)
        while k>0:
            stack.pop()
            k-=1
        result="".join(stack).lstrip('0')
        if result:
            return result
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends