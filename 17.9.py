def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


list_ = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
element = int(input("Введите число: "))
index = binary_search(bubble_sort(list_), element, 0, len(list_)-1)-1
if index == -1:
    print("Элемент не найден")
else:
    print(f"Предшествующий числу {element} индекс:", index)
