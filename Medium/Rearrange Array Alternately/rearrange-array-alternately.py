#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        ##Your code here
        res=[]
        p=sorted(arr)
        t=p[::-1]
        r=p[:n//2]
        s=t[:n//2]
        for i in range(len(r)):
            res.append(s[i])
            res.append(r[i])
        if n%2!=0:
            res.append(arr[n//2])
        arr[:]=res
        return arr
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends