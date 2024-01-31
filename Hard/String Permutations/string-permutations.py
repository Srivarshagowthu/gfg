#User function Template for python3
import itertools
class Solution:
    def permutation(self,s):
        '''def perm(s,ds,ans,freq):
            if len(ds)==len(s):
                f="".join(ds)
                res.append(f)
                return
            for i in range(len(s)):
                if freq[i]==0:
                    ds.append(s[i])
                    freq[i]=1
                    perm(s,ds,ans,freq)
                    freq[i]=0
                    ds.pop()
        res=[]
        ds=[]
        n=len(s)
        freq=[0]*len(s)
        ans=[]
        perm(s,ds,ans,freq)
        return sorted(res)'''
        res=[]
        p=list(itertools.permutations(s))
        p.sort()
        for i in p:
            res.append("".join(i))
        return res
                    
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    while(T>0):
        s=input()
        ob=Solution()
        ans=ob.permutation(s)
        for i in ans:
            print(i,end=" ")
        print()
        
        T-=1
# } Driver Code Ends