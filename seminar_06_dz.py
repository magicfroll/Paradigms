def binary_search(arr, elem):
    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = start + (end - start) // 2
        if arr[middle] == elem:
            return middle
        elif arr[middle] < elem:
            start = middle + 1
        else:
            end = middle - 1
    return '"Элемент не найден"'


arr = [1, 3, 4, 6 ,8, 10, 14]
elem = 10
print(binary_search(arr, elem))