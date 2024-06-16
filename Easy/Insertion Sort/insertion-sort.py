#Sort the array using insertion sort

class Solution:

    
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        for i in range(1,n):
            j=i
            while j>0 and arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                j-=1
            


#{ 
 # Driver Code Starts

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends