from sorts import *
from random import random
from time import time

def benchmark_sorts(funcs):
    l = [int(1_000_000 * random()) for i in range(max(funcs.values()))]
    for func, length in funcs.items():
        s = l[:length] if length < len(l) else l.copy()
        start = time()
        func(s)
        total = time() - start
        print(f"{func.__name__}: ran on {length:,} elements "
              f"in {round(total, 2)} seconds")

if __name__ == "__main__":
    benchmark_sorts({bubble_sort: 10_000,
                     selection_sort: 10_000,
                     insertion_sort: 10_000,
                     mergesort: 1_000_000,
                     quicksort: 1_000_000,
                     heapsort: 1_000_000})
