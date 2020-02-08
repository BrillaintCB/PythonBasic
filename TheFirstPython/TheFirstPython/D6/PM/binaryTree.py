# Node value(self.data) 
# left self.left
# right self.right
class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    #Init
    def __init__(self):
        self.root = None
    #Insert
    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            #print("node data", node.data, data)
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None
    #Insert end
    
    #find
    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)
    
    def find(self,key):
        return self._find_value(self.root, key)
    #find end

    #delete
    def _delete_value(self, node, key):
        if node is None:
            return node, False        
        
        deleted = False
        if node.left and node.right:
            #replace the node to the leftmost of node.right
            parent, child = node, node.right
            while child.left is not None:
                parent, child = child, child.left
            child.left = node.left
            if parent != node:
                parent.left = child.right
                child.right = node.right
            node= child
            
        elif node.left or node.right:
            node = node.left or node.right
        else:
            node = None

  #  elif key < node.data:
        node.left, deleted = self._delete_value(node.left, key)

#  7:30 ->
    #delete end

array = [1, 4, 5, 2, 3, 7, 6, 8]
bst = BinarySearchTree()
for x in array:
    bst.insert(x)
#find
print(bst.find(15))
print(bst.find(14))
