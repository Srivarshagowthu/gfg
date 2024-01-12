#User function Template for python3
import math
class Solution:        
    def primeRange(self,M,N):
        #code here
        def seive(n):
            q=[]
            l=[True for i in range(n+1)]
            p=2
            while(p*p<=n):
                if l[p]:
                    for i in range(p*p,n+1,p):
                        l[i]=False
                p+=1
            for j in range(2,n+1):
                if l[j]:
                    q.append(j)
            return q
        def seg(l,r):
            ans=[]
            k=int(math.floor(math.sqrt(r))+1)#4
            primes=seive(k)
            array=[True for i in range(r-l+1)]
            for j in (primes):
                w=(l//j)*j
                if(w<l):
                    w+=j
                if(j*j > w): w = j* j;#
                while(w<=r):
                    array[w-l]=False
                    w+=j
            for b in range(l,r+1):
                if array[b-l]:
                    ans.append(b)
            if l==1:
                return ans[1::]
            else:
                return ans
            
        return seg(M,N)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        M,N=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.primeRange(M,N)
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends