class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        '''A.append(0)
        res=[]
        for i in range(len(A)-1):
            if max(A[i+1:])<A[i]:
                res.append(A[i])
        return res'''
        p=[]
        m=0
        for i in range(len(A)-1,-1,-1):
            if A[i]>=m:
                m=A[i]
                p.append(m)
        return p[::-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends