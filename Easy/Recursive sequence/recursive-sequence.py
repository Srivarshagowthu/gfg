#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        '''def rec(k,val):
            global p
            if len(prod)==n:
                return prod
            p=1
            for j in range(res[-1]+1,val+res[-1]+1):
                res.append(j)
                p=(p*j)%(10**9+7)
            prod.append(p)
            return rec(res[-1]+1,val+1)
        res=[1]
        k=res[-1]
        p=1
        prod=[1]
        w=rec(1,2)
        return sum(w)%(10**9+7)'''
        #User function Template for python3
        res=0
        mod=10**9+7
        t=1
        for i in range(1,n+1):
            p=1
            for j in range(i):
                p*=t
                t+=1
            res+=p
        return res%mod
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends