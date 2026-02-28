class TreeNode:

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.left = left
        self.right = right
        self.parent = parent

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.value = value
        self.left = lc
        self.right = rc
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self

    def findSuccessor(self):
        succ = None
        # If there is a right subtree, it contains the successor
        if self.hasRightChild():
            succ = self.right.findMin()

        return succ

    def findMin(self):
        ''' The minimum key in the subtree rooted at self is the left most
            element in that subtree '''
        current = self
        while current.hasLeftChild():
            current = current.left
        return current

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for element in self.left:
                    yield element
            yield self
            if self.hasRightChild():
                for element in self.right:
                    yield element

    def spliceOut(self):
        assert not self.hasBothChildren()

        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None
        else:  # has only one child because of assertion
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root is None:
            self.root = TreeNode(key, val)
        else:
            self._put(key, val, self.root)
        self.size = self.size + 1

    def _put(self, key, val, curNode):
        if key < curNode.key:
            if curNode.hasLeftChild():
                self._put(key, val, curNode.left)
            else:
                curNode.left = TreeNode(key, val, parent=curNode)
        else:
            if curNode.hasRightChild():
                self._put(key, val, curNode.right)
            else:
                curNode.right = TreeNode(key, val, parent=curNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        value = None
        if self.root:
            res = self._get(key, self.root)
            if res:
                value = res.value

        return value

    def _get(self, key, curNode):
        if not curNode:
            return None
        elif curNode.key == key:
            return curNode
        elif key < curNode.key:
            return self._get(key, curNode.left)
        else:
            return self._get(key, curNode.right)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, curNode):
        if curNode.isLeaf():  # leaf
            if curNode == curNode.parent.left:
                curNode.parent.left = None
            else:
                curNode.parent.right = None

        elif curNode.hasBothChildren():  # interior
            succ = curNode.findSuccessor()
            # the successor is garantied to have only one child
            succ.spliceOut()
            curNode.key = succ.key
            curNode.value = succ.value

        else:  # this node has one child
            # DONC : même logique que le spliceOut ...
            if curNode.hasLeftChild():
                if curNode.isLeftChild():
                    curNode.left.parent = curNode.parent
                    curNode.parent.left = curNode.left
                elif curNode.isRightChild():
                    curNode.left.parent = curNode.parent
                    curNode.parent.right = curNode.left
                else:  # curNode is the root of the tree
                    curNode.replaceNodeData(curNode.left.key,
                                            curNode.left.value,
                                            curNode.left.left,
                                            curNode.left.right)

            # DONC : code symétrique  ... il faut juste changer quelques left par
            # right et vis-versa
            else:
                if curNode.isLeftChild():
                    curNode.right.parent = curNode.parent
                    curNode.parent.left = curNode.right
                elif curNode.isRightChild():
                    curNode.right.parent = curNode.parent
                    curNode.parent.right = curNode.right
                else:  # curNode is the root of the tree
                    curNode.replaceNodeData(curNode.right.key,
                                            curNode.right.value,
                                            curNode.right.left,
                                            curNode.right.right)

    def items(self):
        if self.root:
            return [x for x in self.root]
        else:
            return []

    def keys(self):
        return [x.key for x in self.items()]

    def values(self):
        return [x.value for x in self.items()]


def test():
    mytree = BinarySearchTree()
    mytree[3] = "red"
    mytree[4] = "blue"
    mytree[6] = "yellow"
    mytree[2] = "at"

    print(mytree[6])
    print(mytree[2])
