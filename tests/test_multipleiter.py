# coding=utf8
from unittest import TestCase


class TestMultipleiter(TestCase):
    def test_multipleiter (self):
        from multipleiterator import multipleiter
        list1 = [1, 2, 3, 4, 5]
        list2 = [int.__add__, int.__sub__]
        list3 = [7, 6, 5]
        rs = []
        for n1, op, n2 in multipleiter(list1, list2, list3):
            rs.append(op(n1, n2))
        print rs
        self.assertEqual(len(rs), 30)

        
