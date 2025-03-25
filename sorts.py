def bubble_sort(lst: list) -> list:
    for i in range(1, len(lst)):
        swap = False
        for j in range(0, len(lst) - i):
            if lst[j] > lst[j+1]:
                swap = True
                lst[j], lst[j+1] = lst[j+1], lst[j]
        if not swap:
            break
    return lst


def selection_sort(lst: list) -> list:
    for i in range(len(lst) - 1):
        idx = i
        val = lst[i]
        for j in range(i + 1, len(lst)):
            if lst[j] < val:
                idx = j
                val = lst[j]
        lst[i], lst[idx] = val, lst[i]
    return lst


def insertion_sort(lst: list) -> list:
    for i in range(1, len(lst)):
        val = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > val:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = val
    return lst


def mergesort(lst: list) -> list:
    def sort(src: list, dst: list, lo: int, hi: int) -> None:
        if lo >= hi:
            return
        if lo + 1 == hi:
            if src[lo] > src[hi]:
                dst[lo], dst[hi] = src[hi], src[lo]
            return
        mid = (lo + hi) // 2
        sort(dst, src, lo, mid)
        sort(dst, src, mid + 1, hi)
        merge(src, dst, lo, mid, hi)

    def merge(src: list, dst: list, lo: int, mid: int, hi: int) -> None:
        if src[mid] <= src[mid+1]:
            for i in range(lo, hi+1):
                dst[i] = src[i]
            return
        idx = i = lo
        j = mid + 1
        while i <= mid and j <= hi:
            if src[i] <= src[j]:
                dst[idx] = src[i]
                i += 1
            else:
                dst[idx] = src[j]
                j += 1
            idx += 1
        if i > mid:
            while j <= hi:
                dst[idx] = src[j]
                j += 1
                idx += 1
        else:
            while i <= mid:
                dst[idx] = src[i]
                i += 1
                idx += 1

    sort(lst.copy(), lst, 0, len(lst) - 1)
    return lst


def quicksort(lst: list) -> list:
    def sort(lo: int, hi: int) -> None:
        if lo >= hi:
            return
        if lo == hi - 1:
            if lst[lo] > lst[hi]:
                lst[lo], lst[hi] = lst[hi], lst[lo]
            return
        mid = (lo + hi) // 2
        median_of_three(lo, mid, hi)
        mid = partition(lo, mid, hi)
        sort(lo, mid)
        sort(mid + 1, hi)

    def partition(lo: int, mid: int, hi: int) -> int:
        pivot = lst[mid]
        i = lo - 1
        j = hi + 1
        while True:
            while lst[i := i + 1] < pivot:
                pass
            while lst[j := j - 1] > pivot:
                pass
            if i >= j:
                return j
            lst[i], lst[j] = lst[j], lst[i]

    def median_of_three(lo: int, mid: int, hi: int) -> None:
        if lst[mid] < lst[lo]:
            lst[mid], lst[lo] = lst[lo], lst[mid]
        if lst[hi] > lst[mid]:
            return
        lst[hi], lst[mid] = lst[mid], lst[hi]
        if lst[mid] < lst[lo]:
            lst[hi], lst[mid] = lst[mid], lst[hi]

    sort(0, len(lst) - 1)
    return lst


def heapsort(lst: list) -> list:
    def heapify() -> None:
        # iterate over all non-leaf nodes fixing the corresponding heaps
        for root in range((len(lst) - 2) // 2, -1, -1):
            sift(root, len(lst))

    def sift(root: int, end: int) -> None:
        while (child := root * 2 + 1) < end:
            if child + 1 < end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    heapify()
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift(0, end)
    return lst
