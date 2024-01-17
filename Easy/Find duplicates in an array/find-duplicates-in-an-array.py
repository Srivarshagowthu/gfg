class Solution:
    def duplicates(self, a, n): 
    	# code here
    	res=[]
    	dictt={}
    	for i in a:
    	    if i in dictt:
    	        dictt[i]+=1
    	    else:
    	        dictt[i]=1
    	for key,value in dictt.items():
    	    if value>1:
    	        res.append(key)
    	if len(res)>0:
    	    return sorted(res)
    	else:
    	    res=[]
    	    res.append(-1)
    	    return res

#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends