
class Solution:
    def isMaxHeap(self,arr,n):
        # Your code goes here      
        c=0
        for i in range(len(arr)):
            l=2*i+1
            p=2*i+2
            if l<n and arr[i]<arr[l]:
                c+=1
            if p<n and arr[i]<arr[p]:
                c+=1
        if c>0:
            return 0
        else:
            return 1


#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends