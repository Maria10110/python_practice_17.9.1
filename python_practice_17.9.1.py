array = [int(x) for x in input("Введите числа в любом порядке от 1 до 100, через пробел: ").split()]

def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort(array))

def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle-1)
    else:
        return binary_search(array, element, right, middle+1)

element = int(input("Введите число от 1 до 100: "))
array = [i for i in range(1, 100)]

while True:
    try:
        if element < 1 or element > 100:
            raise Exception
    except ValueError:
        print("Нужно ввести число!")
    except Exception:
        print("Неправильный диапазон!")
    break

print(binary_search(array, element, 0,  len(array)))