import unittest
import random

from bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        '''Create new sequence and search tree.'''
        self.bst = BinarySearchTree()
        self.seq = list(range(1, 1000))


    def testFiewKeys(self):
        keys_to_insert = [4,2,5,1,3]
        random.shuffle(keys_to_insert)
        for key in keys_to_insert:
            self.bst.insert(key, key)

        for key in keys_to_insert:
            deleted_node_key = self.bst.delete(key)
            self.assertEqual(deleted_node_key, key)
            node_should_be_none = self.bst.search(key)
            self.assertEqual(node_should_be_none, None)
        self.assertEqual(self.bst.root, None)

    def testRandom(self):
        '''Inserts, finds, and deletes on a random sequence.'''

        random.shuffle(self.seq)
        for a in self.seq:
            self.bst.insert(a, a)
            self.assertEqual(self.bst.search(a).value, a)

        # find each, delete it, and make sure they are removed
        random.shuffle(self.seq)
        for a in self.seq:
            node_to_delete = self.bst.search(a)
            self.assertEqual(node_to_delete.key, a)
            deleted_node_key = self.bst.delete(a)
            self.assertEqual(deleted_node_key, a)
            node_should_be_none = self.bst.search(a)
            self.assertEqual(node_should_be_none, None)
        self.assertEqual(self.bst.root, None)

        random.shuffle(self.seq)
        for a in self.seq:
            self.assertEqual(self.bst.delete(a), None)


if __name__ == '__main__':
    unittest.main()
