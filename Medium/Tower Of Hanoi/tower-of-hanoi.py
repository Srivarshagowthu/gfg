# User function Template for python3

class Solution:
    def toh(self, N, fromm, to, aux):
        # Your code here
        def movedisk(n,src,hel,des,cnt):
            if n>0:
                movedisk(n-1,src,des,hel,cnt)
                print("move disk "+ str(n)+" from rod "+str(src)+" to rod "+str(des))
                cnt[0]+=1
                movedisk(n-1,hel,src,des,cnt)
        src,des,hel,cnt=fromm,to,aux,[0]
        movedisk(N,src,hel,des,cnt)
        return cnt[0]
            


#{ 
 # Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()


# } Driver Code Ends