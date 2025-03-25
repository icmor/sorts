from sorts import *
import unittest
import random

funcs = ({bubble_sort: 100,
          selection_sort: 100,
          insertion_sort: 100,
          mergesort: 10_000,
          quicksort: 10_000,
          heapsort: 10_000})

class TestSorts(unittest.TestCase):
    def test_random(self):
        l = [int(10_000 * random.random())
             for i in range(max(funcs.values()))]
        for func, size in funcs.items():
            s = l[:size] if size < len(l) else l.copy()
            with self.subTest(msg=func.__name__):
                self.assertEqual(func(s), sorted(s))

    def test_same_value(self):
        l = [42 for i in range(max(funcs.values()))]
        for func, size in funcs.items():
            s = l[:size] if size < len(l) else l.copy()
            with self.subTest(msg=func.__name__):
                func(s)

    def test_increasing(self):
        l = [i for i in range(max(funcs.values()))]
        for func, size in funcs.items():
            s = l[:size] if size < len(l) else l.copy()
            with self.subTest(msg=func.__name__):
                self.assertEqual(func(s), sorted(s))

    def test_decreasing(self):
        l = [i for i in range(max(funcs.values()) - 1, -1, -1)]
        for func, size in funcs.items():
            s = l[:size] if size < len(l) else l.copy()
            with self.subTest(msg=func.__name__):
                self.assertEqual(func(s), sorted(s))

if __name__ == "__main__":
    unittest.main()
