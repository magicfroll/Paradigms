# сотировка в императивной парадигме
def imperativ_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# сортировка в декларативной парадигме
def declarative_sort(array):
    return sorted(array)

array = [9, 5, 7, 4, 3, 2, 1, 6 ,8 ,0]
print(imperativ_sort(array))

array = [9, 5, 7, 4, 3, 2, 1, 6 ,8 ,0]
print(declarative_sort(array))