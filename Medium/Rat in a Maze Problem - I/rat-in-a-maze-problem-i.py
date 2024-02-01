#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        def rm(i,j,n,m,res,path,current):
            if i<0 or i>=n or j<0 or j>=n or path[i][j]==1 or m[i][j]==0:
                return
            if i==n-1 and j==n-1:
                res.append(current)
                return
            path[i][j]=1
            rm(i , j+1, n,m, res, path, current + 'R')
            rm(i + 1, j, n,m, res, path, current + 'D')
            rm(i, j - 1, n,m, res, path, current + 'L')
            rm(i - 1, j, n,m, res, path, current + 'U')
            path[i][j] = 0
        res=[]
        path=[[0 for i in range(n)]for j in range(n)]
        rm(0,0,n,m,res,path,"")
        res.sort()
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends