
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                  self.left = Node(data)
                else:
                    self.left.insert(data)  
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()       
            
    #-----------------Inorder Traversal----------------------------------
    
    def inorderTraversal(self,root):
        res =[]
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res  
    
    #-----------------Preorder Traversal-----------------------------------
    
    def preorderTraversal(self,root):
        res1 = []
        if root:
            res1.append(root.data)
            res1 = res1 + self.preorderTraversal(root.left)
            res1 = res1 + self.preorderTraversal(root.right)       
        return res1           
                
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)

root.PrintTree()

print('\n')

print(root.inorderTraversal(root))

print('\n')

print(root.preorderTraversal(root))