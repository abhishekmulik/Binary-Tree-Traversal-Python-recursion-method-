# Binary Tree Traversals
class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def print_tree(self,traversal_type):
        if traversal_type=='preorder':
            return self.preorder(bt.root,'')   # '' takes the pointer as arg below 
        elif traversal_type=='inorder':
            return self.inorder(bt.root,'')
        elif traversal_type=='postorder':
            return self.postorder(bt.root,'')
        else:
            print('The teaversal type',traversal_type,'is not supported.')
            return False
   
    def preorder(self,start,pointer):
        'Root-Lef-Right'
        if start:
            pointer += (str(start.value)+'-')
            pointer = self.preorder(start.left,pointer)
            pointer = self.preorder(start.right,pointer)
        return pointer

    def inorder(self,start,pointer):
        'Left-Root-Right'
        if start:
            pointer = self.inorder(start.left,pointer)
            pointer += (str(start.value)+'-')
            pointer = self.inorder(start.right,pointer)
        return pointer

    def postorder(self,start,pointer):
        'Left-Right-Root'
        if start:
            pointer=self.postorder(start.left,pointer)
            pointer=self.postorder(start.right,pointer)
            pointer += (str(start.value)+'-')
        return pointer


bt=BinaryTree(1)                        #                   1   ---> Root
bt.root.left=Node(2)                    #                 /   \
bt.root.right=Node(3)                   #                2      3
bt.root.left.left=Node(4)               #               / \    / \
bt.root.left.right=Node(5)              #              4   5  6   7
bt.root.right.left=Node(6)
bt.root.right.right=Node(7)

print('Preorder Traversal:',bt.print_tree('preorder'))        # 'Root-Lef-Right'
print('Inorder Traversal:',bt.print_tree('inorder'))          # 'Left-Root-Right'
print('Postorder Traversal:',bt.print_tree('postorder'))      # 'Left-Right-Root'



