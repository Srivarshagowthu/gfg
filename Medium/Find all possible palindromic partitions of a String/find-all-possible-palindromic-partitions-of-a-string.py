#User function Template for python3

class Solution:
    def allPalindromicPerms(self, s):
        def palin(ind, ds, s, res, n):
            if ind == n:
                res.append(ds.copy())
                return
            for i in range(ind, n):
                sub = s[ind:(i + 1)]
                if sub == sub[::-1]:
                    ds.append(sub)
                    palin(i + 1, ds, s, res, n)
                    ds.pop()

        n = len(s)
        res = []
        ds = []
        palin(0, ds, s, res, n)
        return res

            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        allPart = ob.allPalindromicPerms(S)
        for i in range(len(allPart)): 
            for j in range(len(allPart[i])): 
                print(allPart[i][j], end = " ") 
            print() 
# } Driver Code Ends