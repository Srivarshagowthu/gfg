#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        for j in range(i,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
        return
        
    
    def selectionSort(self, arr,n):
        #code here
        if n<=1:
            return
        for i in range(n):
            self.select(arr,i)
        return
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends