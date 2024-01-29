#User function Template for python3

class Solution:
    def AllParenthesis(self,n):
        #code here
        def para(op,cl,n,res,ds):
            if op==n and cl==n:
                t="".join(ds)
                res.append(t)
                return
            if op<n:
                ds.append("(")
                para(op+1,cl,n,res,ds)
                ds.pop()
            if op>cl:
                ds.append(")")
                para(op,cl+1,n,res,ds)
                ds.pop()
        op,cl=0,0
        res=[]
        ds=[]
        para(0,0,n,res,ds)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends