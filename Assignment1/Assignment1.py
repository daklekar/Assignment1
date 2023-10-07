# %%
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.key = val
    # def display(self):  
    #     print(self.key)  
    #     return self.key


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, dummy):
        if (self.root == None):
            self.root = Node(dummy)
        else:
            self._insert_recursive(self.root, dummy)
    
    def _insert_recursive(self, node, dummy):
            if dummy > node.key:            
                if node.right == None:
                    node.right = Node(dummy)
                else:
                    self._insert_recursive(node.right, dummy)
            if dummy <= self.root.key:
                if node.left == None:
                    node.left = Node(dummy)
                else:
                    self._insert_recursive(node.left, dummy)    

    def _display_recursive(self, node):
        if node:
            self._display_recursive(node.left)
            print(node.key)
            self._display_recursive(node.right)
    
    def display(self):
        self._display_recursive(self.root)

# %%
if (__name__ == '__main__'):
    BT_1 = BinaryTree()
    BT_1.insert(5)
    BT_1.insert(4)
    BT_1.insert(3)
    BT_1.insert(8)

    BT_1.display()


