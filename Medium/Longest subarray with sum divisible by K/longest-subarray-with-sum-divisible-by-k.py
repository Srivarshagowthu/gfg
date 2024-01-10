#User function Template for python3
class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, k) : 
		#Complete the function
		dic={}
		pres=0
		maxlen=0
		for i in range(len(arr)):
		    pres+=arr[i]
		    rem=pres%k
		    if rem==0:
		        maxlen=max(maxlen,i+1)
		    if rem<0:
		        rem+=k
		    if rem in dic:
		        maxlen=max(maxlen,i-dic[rem])
		    else:
		        dic[rem]=i
		return maxlen
		    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends