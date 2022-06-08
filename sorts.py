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

