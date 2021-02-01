class Node(object): 
    def __init__(self,value,left_child = None, right_child = None):
        self.value = value    
        self.left_child = left_child
        self.right_child = right_child

class Tree(object):
    def __init__(self):
        self.root = None # default root is None
    
    def add_root(self,value):
        return Node(value)
        
    def add_node(self, root, value):   # insert node into an existing tree
        if root == None:
            root = self.add_root(value)   # create a Node
        elif value < root.value:
            root.left_child = self.add_node(root.left_child, value)  # redefine root of the left subtree (recursive)
        else:
            root.right_child = self.add_node(root.right_child, value) # redefine root of the right subtree
        return root   # since it uses recursion, need to return root
    
    def preOrd(self,root):
        if root is not None:      # first print parent(sub-root), then left-child, then right-child
            print(root.value)
        if root.left_child is not None:
            self.preOrd(root.left_child)
        if root.right_child is not None:
            self.preOrd(root.right_child)
            
    def inOrd(self,root):
        if root.left_child is not None:
            self.inOrd(root.left_child)
        if root is not None:
            print(root.value)   # if a leaf node(see as the root of a subtree) does not have left-child, print value
        if root.right_child is not None:   
            self.inOrd(root.right_child)   # first print left-child, the sub-root(parent), then right-child 
        
    def postOrd(self,root):
        if root.left_child is not None:    
            self.postOrd(root.left_child)     
        if root.right_child is not None:
            self.postOrd(root.right_child)
        if root is not None:
            print(root.value)
            
            
mytree = Tree()
node0 = mytree.add_root(10)
mytree.add_node(node0,8)
mytree.add_node(node0,6)
mytree.add_node(node0,12)
mytree.add_node(node0,17)
mytree.add_node(node0,3)
mytree.add_node(node0,11)
mytree.add_node(node0,9)
mytree.preOrd(node0)
print('------------')
mytree.inOrd(node0)
print('------------')
mytree.postOrd(node0)
