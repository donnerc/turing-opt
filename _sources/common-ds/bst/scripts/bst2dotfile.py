from io import StringIO
import sys


class DuplicateKey(Exception):
    pass


class BSTNode(object):
    """
    Implementation for the node of Binary Search Tree
    """

    nil_count = 0

    def __init__(self, key, value, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def _set_left(self, node):
        self.left = node
        return self.left

    def _set_right(self, node):
        self.right = node
        return self.right

    def _insert(self, node):
        if node.key == self.key:
            raise DuplicateKey
        elif node.key < self.key:
            return self.left and self.left._insert(node) or self._set_left(node)
        else:
            return self.right and self.right._insert(node) or self._set_right(node)

    def print_edges(self):
        if self.left:
            print(f'"{self.key}" -> "{self.left.key}"')
            self.left.print_edges()
        else:
            BSTNode.nil_count += 1
            print(f'nil{BSTNode.nil_count} [shape=point, color=red];')
            print(f'"{self.key}" -> "nil{BSTNode.nil_count}"')
        
        if self.right:
            print(f'"{self.key}" -> "{self.right.key}"')
            self.right.print_edges()
        else:
            BSTNode.nil_count += 1
            print(f'nil{BSTNode.nil_count} [shape=point, color=red];')
            print(f'"{self.key}" -> "nil{BSTNode.nil_count}"')
        

    def __repr__(self):
        return f"BSTNode(key={self.key}, value={self.value}, left={self.left}, right={self.right})"

    def __str__(self):
        return repr(self)


class BinarySearchTree:
    """
    Implementation for Binary Search Trees
    """

    def __init__(self):
        self.root = None
        self.size = 0

    def insert_rec(self, key, value):
        node = BSTNode(key, value)
        if self.root is None:
            self.root = node
        else:
            self.root._insert(node)
        self.size += 1

    def insert(self, key, value):
        """
        Insert the (key, value) to the BST

        @param key: the key to insert
        @param value: the value to insert
        @return: True if insert successfully; otherwise return False
        """
        if None == self.root:
            self.root = BSTNode(key, value)
            return True

        current_node = self.root
        while current_node:
            if key == current_node.key:
                raise DuplicateKey
            elif key < current_node.key:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BSTNode(key, value)
                    self.size += 1
                    return True
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BSTNode(key, value)
                    self.size += 1
                    return True

    def show(self, options=None):
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()

        print("digraph BST {")
        self.root.print_edges()
        print("}")
        # blah blah lots of code ...

        sys.stdout = old_stdout

        return mystdout

    def __repr__(self):
        return f"BinarySearchTree(root={self.root}, size={self.size})"


from random import shuffle

bst = BinarySearchTree()
keys = list(range(25))
shuffle(keys)
for k in keys:
    # print("inserting", k)
    bst.insert_rec(k, None)
dotfile = bst.show().getvalue()
# print(repr(dotfile))
print(dotfile)


# print(bst)

# bst.show()
