def bubble_sort(l: list) -> list:
    for i in range(1, len(l)):
        swap = False
        for j in range(0, len(l) - i):
            if l[j] > l[j+1]:
                swap = True
                l[j], l[j+1] = l[j+1], l[j]
        if not swap: break
    return l


def selection_sort(l: list) -> list:
    for i in range(len(l) - 1):
        idx = i
        val = l[i]
        for j in range(i + 1, len(l)):
            if l[j] < val:
                idx = j
                val = l[j]
        l[i], l[idx] = val, l[i]
    return l


def insertion_sort(l: list) -> list:
    for i in range(1, len(l)):
        val = l[i]
        j = i - 1
        while j >= 0 and l[j] > val:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = val
    return l


def mergesort(l: list) -> list:
    def sort(src: list, dst: list, lo: int, hi: int) -> None:
        if lo >= hi: return
        if lo + 1 == hi:
            if src[lo] > src[hi]: dst[lo], dst[hi] = src[hi], src[lo]
            return
        mid = (lo + hi) // 2
        sort(dst, src, lo, mid)
        sort(dst, src, mid + 1, hi)
        merge(src, dst, lo, mid, hi)

    def merge(src: list, dst: list, lo: int, mid: int, hi: int) -> None:
        if src[mid] <= src[mid+1]:
            for i in range(lo, hi+1): dst[i] = src[i]
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

    sort(l.copy(), l, 0, len(l) - 1)
    return l


def quicksort(l: list) -> list:
    def sort(lo: int, hi: int) -> None:
        if lo >= hi: return
        if lo == hi - 1:
            if l[lo] > l[hi]: l[lo], l[hi] = l[hi], l[lo]
            return
        mid = (lo + hi) // 2
        median_of_three(lo, mid, hi)
        mid = partition(lo, mid, hi)
        sort(lo, mid)
        sort(mid + 1, hi)

    def partition(lo: int, mid: int, hi: int) -> int:
        pivot = l[mid]
        i = lo - 1
        j = hi + 1
        while True:
            while l[i := i + 1] < pivot: pass
            while l[j := j - 1] > pivot: pass
            if i >= j: return j
            l[i], l[j] = l[j], l[i]

    def median_of_three(lo: int, mid: int, hi: int) -> None:
        if l[mid] < l[lo]:
            l[mid], l[lo] = l[lo], l[mid]
        if l[hi] > l[mid]: return
        l[hi], l[mid] = l[mid], l[hi]
        if l[mid] < l[lo]:
            l[hi], l[mid] = l[mid], l[hi]

    sort(0, len(l) - 1)
    return l
