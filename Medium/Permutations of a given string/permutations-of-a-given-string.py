#User function Template for python3

class Solution:
    def find_permutation(self, s):
        # Code here
        def perm(res,ds,s,freq):
            if len(ds)==len(s):
                r="".join(ds)
                res.append(r)
                return
            for i in range(len(s)):
                if freq[i]==0:
                    ds.append(s[i])
                    freq[i]=1
                    perm(res,ds,s,freq)
                    freq[i]=0
                    ds.pop()
        ds=[]
        res=[]
        freq=[0]*len(s)
        perm(res,ds,s,freq)
        return list(set(res))
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		ans.sort()
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends