import unittest
import random

from bst_miller import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        '''Create new sequence and search tree.'''
        self.bst = BinarySearchTree()
        self.seq = list(range(1000))


    def testRandom(self):
        '''Inserts, finds, and deletes on a random sequence.'''

        random.shuffle(self.seq)
        for a in self.seq:
            self.bst[a] = a
            self.assertEqual(self.bst[a], a)

        # find each, delete it, and make sure they are removed
        random.shuffle(self.seq)
        for a in self.seq:
            self.assertEqual(self.bst[a], a)
            self.bst.delete(a)
            self.assertEqual(self.bst[a], None)

        random.shuffle(self.seq)
        for a in self.seq:
            self.assertEqual(self.bst[a], None)
            self.assertRaises(KeyError, lambda: self.bst.delete(a))


    def testTraversal(self):
        random.shuffle(self.seq)
        for a in self.seq:
            self.bst[a] = a

        self.seq.sort()
        self.assertListEqual(self.bst.keys(), self.seq)

if __name__ == '__main__':
    unittest.main()
