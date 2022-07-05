class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

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

   #-----------Searching For a value in binary tree-------------
    def findval(self,lokval):
     if lokval < self.data:
        if self.left is None:
            return str(lokval)+"not found"
        return self.left.findval(lokval)
     elif lokval > self.data:
        if self.right is None:
            return str(lokval)+"not found"
        return self.right.findval(lokval)
     else:
        print(str(self.data)+"is found")

    #-------Priniting the tree
    def PrintTree(self):
     if self.left:
         self.left.PrintTree()
     print( self.data),
     if self.right:
         self.right.PrintTree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.findval(7))
print(root.findval(14))

