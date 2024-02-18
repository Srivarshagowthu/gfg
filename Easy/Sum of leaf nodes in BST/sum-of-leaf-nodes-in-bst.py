#User function Template for python3

##Structure of node
'''
class Node:
    def __init__(self, data=0):
        self.data=0
        self.left=None
        self.right=None
'''

class Solution:
    def sumOfLeafNodes(self, root):
        res=[]
        def inorder(node):
            if not node:
                return
            if node.left==None and node.right==None:
                res.append(node.data)
            inorder(node.left)
            inorder(node.right)
        inorder(root)
        return sum(res)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data=0):
        self.data=data
        self.left=None
        self.right=None


def createNewNode(value):
    temp=Node()
    temp.data=value
    temp.left=None
    temp.right=None
    return temp
    

def newNode(root,data):
    if(root is None):
        root=createNewNode(data)
    elif(data<root.data):
        root.left=newNode(root.left,data);
    else:
        root.right=newNode(root.right,data)
        
    return root

for _ in range(int(input())):
    root=None
    sizeOfArray=int(input())
    arr=[int(x) for x in input().strip().split()]
    for i in arr:
        root=newNode(root,i)
    ob = Solution()
    print(ob.sumOfLeafNodes(root))
# } Driver Code Ends