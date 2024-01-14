#User function Template for python3

class Solution:
    def repeatedRows(self, arr, m ,n):
        #code here
        sett=set()
        ans=[]
        for i in range(m):
            p=tuple(arr[i])
            if p in sett:
                ans.append(i)
            else:
                sett.add(p)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        arr = []
        for i in range(n):
            nums = list(map(int, input().strip().split()))
            arr.append(nums)
        ob = Solution()
        ans = ob.repeatedRows(arr, n, m)
        
        for x in ans:
            print(x, end=" ")
            
        print()
        tc -= 1

# } Driver Code Ends