#!/usr/bin/env python

class DuplicateKey(KeyError): pass

class _BSTNode:
    '''A node in a binary search tree. Has left and right subtrees.'''
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


class BinarySearchTree:
    '''Representes a (possibly unbalenced) binary search tree.'''

    def __init__(self):
        '''Create a new search tree.'''
        self.root = None


    def insert(self, x):
        '''Put x into the search tree, raise DuplicateKey if already there.'''
        # if tree is empty
        if self.root is None:
            self.root = _BSTNode(x)
            return

        # search for x and its would-be parent
        p, q = self.__find_and_parent(x)
        if p is not None: raise DuplicateKey

        # make x a child of q
        if x < q.data:
            assert q.left is None
            q.left = _BSTNode(x)
        else:
            assert q.right is None
            q.right = _BSTNode(x)


    def delete(self, x):
        '''Remove item x from the tree.'''
        node_to_delete, parent = self.__find_and_parent(x)
        p = node_to_delete
        if node_to_del is None: raise KeyError      # x not found

        # has two children
        if None not in (node_to_del.left, node_to_del.right):
            r, parent = self.__find_min(node_to_del.right, node_to_del)
            node_to_del.data = r.data
            node_to_del = r    # Note: below we delete this new node_to_del

        # is leaf
        if (node_to_del.left, node_to_del.right) == (None,None):
            # if parent is None
            if parent is None: self.root = None
            elif node_to_del.data < parent.data: parent.left = None
            else: parent.right = None

        # has only one child
        elif None in (p.left, p.right):
            # c is the non-None child
            c = p.left
            if c is None: c = p.right

            if parent is None: self.root = c
            elif p.data < parent.data: parent.left = c
            else: parent.right = c


    def find(self, x):
        '''Find x, return None if x is not present.'''
        p, _ = self.__find_and_parent(x)
        if p is None: return None
        else: return p.data


    def inorder_traversal(self):
        '''Return a list of the items in sorted order.'''
        L = []
        self.__inorder_traversal(self.root, L)
        return L


    def __inorder_traversal(self, p, L):
        '''Recursively build the inorder list.'''
        if p is not None:
            self.__inorder_traversal(p.left, L)
            L.append(p.data)
            self.__inorder_traversal(p.right, L)


    def __find_min(self, p, q):
        '''Return the smallest element under node p, and its parent.
        q should be the parent of p'''
        if p is None: return None
        while p.left is not None:
            q = p
            p = p.left
        return p, q


    def __find_and_parent(self, key):
        '''Search for key, returning the node with key and its parent.
        If key doesn't exist, returns None and key's would-be parent.'''
        q = None           # parent
        p = self.root      # current node
        while p is not None and p.key != key:
            q = p
            if key < p.key:
                p = p.left
            else:
                p = p.right
        return p, q


#================================================================================
# Unit Test
#================================================================================

import unittest
import random

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        '''Create new sequence and search tree.'''
        self.BST = BinarySearchTree()
        self.seq = range(1000)


    def testRandom(self):
        '''Inserts, finds, and deletes on a random sequence.'''

        random.shuffle(self.seq)
        for a in self.seq:
            self.BST.insert(a)
            self.assertEqual(self.BST.find(a), a)

        for a in self.seq:
            self.assertEqual(self.BST.find(a), a)

        # try to insert twice, and make sure error raised
        random.shuffle(self.seq)
        for a in self.seq:
            self.assertRaises(DuplicateKey, lambda: self.BST.insert(a))

        # find each, delete it, and make sure they are removed
        random.shuffle(self.seq)
        for a in self.seq:
            self.assertEqual(self.BST.find(a), a)
            self.BST.delete(a)
            self.assertEqual(self.BST.find(a), None)

        random.shuffle(self.seq)
        for a in self.seq:
            self.assertEqual(self.BST.find(a), None)
            self.assertRaises(KeyError, lambda: self.BST.delete(a))


    def testTraversal(self):
        random.shuffle(self.seq)
        for a in self.seq:
            self.BST.insert(a)

        self.seq.sort()
        self.assertEqual(self.BST.inorder_traversal(), self.seq)

if __name__ == '__main__': unittest.main()
