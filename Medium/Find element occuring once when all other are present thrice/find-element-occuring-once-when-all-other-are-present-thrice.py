#User function Template for python3

#User function Template for python3

class Solution:
    def singleElement(self, a, N):
        dict={}
        for i in a:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for j in dict:
            if dict[j]==1:
                return j

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.singleElement(arr,N))
# } Driver Code Ends