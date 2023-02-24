import time


def bubble_sort(list_num):
    for i in range(len(list_num)):
        swapped = False
        for j in range(len(list_num) - 1):
            if list_num[j] > list_num[j + 1]:
                list_num[j], list_num[j + 1] = list_num[j + 1], list_num[j]
                swapped = True
        if not swapped:
            break

    return list_num


def insertion_sort(list_num):
    for i in range(0, len(list_num) - 1):
        key = list_num[i + 1]
        j = i
        while j >= 0 and key < list_num[j]:
            list_num[j + 1] = list_num[j]
            j -= 1
        list_num[j + 1] = key

    return list_num


def selection_sort(list_num):
    for i in range(len(list_num)):
        min_index = i
        for j in range(i + 1, len(list_num)):
            if list_num[j] < list_num[min_index]:
                min_index = j

        list_num[i], list_num[min_index] = list_num[min_index], list_num[i]

    return list_num


def quicksort(list_num):
    if len(list_num) <= 1:
        return list_num
    else:
        pivot = list_num.pop()

    items_greater = []
    items_lower = []

    for item in list_num:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)


def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while len(result) < len(left) + len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def merge_sort(list_num):
    if len(list_num) < 2:
        return list_num

    middle = int(len(list_num) / 2)
    left = merge_sort(list_num[:middle])
    right = merge_sort(list_num[middle:])

    return merge(left, right)


def heapify(list_num, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and list_num[i] < list_num[left]:
        largest = left

    if right < n and list_num[largest] < list_num[right]:
        largest = right

    if largest != i:
        list_num[i], list_num[largest] = list_num[largest], list_num[i]
        heapify(list_num, n, largest)


def heapsort(list_num):
    size = len(list_num)

    for i in range(size // 2 - 1, -1, -1):
        heapify(list_num, size, i)

    for i in range(size - 1, 0, -1):
        list_num[i], list_num[0] = list_num[0], list_num[i]
        heapify(list_num, i, 0)

    return list_num


def test(sample_test):
    runtime = []
    start = time.time()
    bubble_sort(sample_test.copy())
    end = time.time() - start
    runtime.append({"bubble_sort": end})
    start = time.time()
    insertion_sort(sample_test.copy())
    end = time.time() - start
    runtime.append({"insertion_sort": end})
    start = time.time()
    selection_sort(sample_test.copy())
    end = time.time() - start
    runtime.append({"selection_sort": end})
    try:
        start = time.time()
        quicksort(sample_test.copy())
        end = time.time() - start
        runtime.append({"quicksort": end})
    except RecursionError:
        runtime.append({"quicksort": float("inf")})
    try:
        start = time.time()
        merge_sort(sample_test.copy())
        end = time.time() - start
        runtime.append({"merge_sort": end})
    except RecursionError:
        runtime.append({"merge_sort": float("inf")})
    try:
        start = time.time()
        heapsort(sample_test.copy())
        end = time.time() - start
        runtime.append({"heapsort": end})
    except RecursionError:
        runtime.append({"heapsort": float("inf")})
    runtime.sort(key=lambda x: list(x.values())[0])
    for i in runtime:
        print(list(i.keys())[0], ":", list(i.values())[0])


if __name__ == '__main__':
    import sys
    import random
    n = int(input("Enter n: "))
    # use this line to avoid RecursionError for quicksort, merge_sort, heapsort
    if n >= 1000:
        sys.setrecursionlimit(2*n)
    sample = [_ for _ in range(n)]
    print("Sorted case: ", sample)
    test(sample)
    sample.reverse()
    print("Reverse sorted case: ", sample)
    test(sample)
    random.shuffle(sample)
    print("Shuffle case:", sample)
    test(sample)
