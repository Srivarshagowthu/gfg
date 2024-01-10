#User function Template for python3

class Solution:
    #Complete this function
    M=(10**9)+7
    def power(self,n,r):
        #Your code here 
        M=(10**9)+7
        res=1
        while(r):
            if int(r)&int(1):
                r=r-1
                res=(res*n)%M
            else:
                r=r/2
                n=(n*n)%M
        return res%M

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends