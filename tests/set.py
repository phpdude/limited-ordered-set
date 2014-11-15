from random import choice
import string
import unittest

from limited_ordered_set import LimitedOrderedSet


class Test(unittest.TestCase):
    def test_limits(self):
        limit = 10
        objcts = LimitedOrderedSet(limit)

        print 'Adding chars: ',
        for x in xrange(0, 50):
            c = choice(string.ascii_letters)
            print c,
            objcts.add(c)
        print

        print 'Resulting set items: %s' % ",".join(objcts)

        self.assertEqual(len(objcts), limit)
