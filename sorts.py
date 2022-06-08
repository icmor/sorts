def bubble_sort(l: list) -> list:
    for i in range(1, len(l)):
        swap = False
        for j in range(0, len(l) - i):
            if l[j] > l[j+1]:
                swap = True
                l[j], l[j+1] = l[j+1], l[j]
        if not swap: break
    return l
