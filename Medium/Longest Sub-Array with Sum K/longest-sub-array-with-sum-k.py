#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        s=0
        premap={}
        maxl=0
        for i in range(len(arr)):
            s+=arr[i]
            if s==k:
                maxl=max(maxl,i+1)
            p=s-k
            if p in premap:
                maxl=max(maxl,i-premap[p])
            if s not in premap:
                premap[s]=i
        return maxl



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends