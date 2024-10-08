from random import randint


def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            if lst[smallest] > lst[j]:
                smallest = j
        lst[i], lst[smallest] = lst[smallest], lst[i]


nums = [randint(1, 100) for _ in range(10)]
print(nums)
selection_sort(nums)
print(nums)
