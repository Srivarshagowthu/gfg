#User function Template for python3

class Solution:
    def findTwoElement( self,a, n): 
        # code here
        res=[]
        dict={}
        q=max(a)
        for i in a:
            if i in dict:
                dict[i]+=1
                if dict[i]==2:
                    res.append(i)
                    break
            else:
                dict[i]=1
        
        su=(q*(q+1))//2
        p=list(set(a))
        ress=su-sum(p)
        if ress==0:
            ress=q+1
        res.append(ress)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends