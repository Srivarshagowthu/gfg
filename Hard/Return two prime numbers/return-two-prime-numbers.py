#User function Template for python3

class Solution:
    def primeDivision(self, N):
        # code here
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
        
        a=seive(N)
        b=a[::-1]
        
        re=[]
        p=[]
        c=0
        #print(a)
        for j in range(len(b)):
            for i in range(len(a)):
                if (b[j]+a[i])==N:
                    re.append(a[i])
                    re.append(b[j])
                if len(re)==2:
                    break
        return re
                    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1,end=" ")
        print(p2)
# } Driver Code Ends