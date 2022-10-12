from queue import Queue
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder(root):
    if(root==None):
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
def pre(root):
    if(root==None):
        return
    print(root.val)
    pre(root.left)
    pre(root.right)
def post(root):
    if(root==None):
        return
    post(root.left)
    post(root.right)
    print(root.val)

'''def lev(root):
    if root==None: return
    q=Queue
    q.put(root)
    while not q.empty():
        node=q.get()
        print(node)
        if node.left!=None:
            q.put(node.left)
        if node.right!=None:
            q.put(node.right)'''
def height(root):
    if root==None: return 0
    return 1+max(height(root.left),height(root.right))
def size(root):
    if root==None: return 0
    return 1+size(root.left)+size(root.right)
root = Node(1)


root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right=Node(5)
root.left.left.left=Node(6)
root.left.left.right=Node(7)
#inorder(root)
#pre(root)
#post(root)
#lev(root)
print(height(root))
print(size(root))