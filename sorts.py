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
    def sort(l: list) -> list:
        if len(l) <= 1: return l
        left = sort(l[len(l)//2:])
        right = sort(l[:len(l)//2])
        return merge(left, right)

    def merge(left: list, right: list) -> list:
        l = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                l.append(left[i])
                i += 1
            else:
                l.append(right[j])
                j += 1
        if i == len(left): l.extend(right[j:])
        else: l.extend(left[i:])
        return l

    l[:] = sort(l)
    return l


