#Function should return a list/array containing the required words

''' The function returns a  list of strings 
present in the dictionary which matches
the string pattern.
You are required to complete this method '''
from collections import Counter

def findSpecificPattern(Dict, pattern):
    #Code here
    k=Counter(pattern)
    q=list(k.values())
    l=[]
    for i in Dict:
        w=Counter(i)
        if list(w.values())==q:
            l.append(i)
    return l




#{ 
 # Driver Code Starts
#function goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        string = input().strip()
        res = findSpecificPattern(arr, string)
        for i in res:
            print(i, end=" ")
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends