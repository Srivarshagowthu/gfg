class Solution:
    def frequencyCount(self, arr, n, p):
        # code here
        d={}
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]]+=1
            else:
                d[arr[i]]=1
        k=0
        for i in range(1, max(p,n)+1):
            if (i not in d or i>n):
                if(i>n):
                    break
                else:
                    arr[k]=0
                    k+=1

            if (i in d):
                arr[k] = d[i]
                k+=1
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends