#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys


# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,a, target):
        a=sorted(list(set(a)))
        def com(a,target,ds):
            if target==0:
                res.append(ds.copy())
                return 
            if target<0:
                return
            for i in range(len(a)):
                if a[i]>target:
                    break
                ds.append(a[i])
                com(a[i:],target-a[i],ds)
                ds.pop()
        res=[]
        ds=[]
        com(a,target,ds)
        return res
    
        # code here

#{ 
 # Driver Code Starts.


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        s = int(input())
        ob = Solution()
        result = ob.combinationalSum(a,s)
        if(not len(result)):
            print("Empty")
            continue
        for i in range(len(result)):
            print("(", end="")
            size = len(result[i])
            for j in range(size - 1):
                print(result[i][j], end=" ")
            if (size):
                print(result[i][size - 1], end=")")
            else:
                print(")", end="")
        print()

# } Driver Code Ends