def recursive_merge_sort(array, left, right):
    if left < right:
        mid = (left + right) // 2
        recursive_merge_sort(array, left, mid)
        recursive_merge_sort(array, (mid + 1), right)
        merge(array, left, mid, right)


def iterative_merge_sort(array):
    current_size = 1
    n = len(array)
    for _ in range(1, n):
        left = 0
        for _ in range(n - 1):
            mid = min((left + current_size - 1), n - 1)
            right = min((left + (2 * current_size) - 1), n - 1)
            merge(array, left, mid, right)
            left += (2 * current_size)
        current_size *= 2


def merge(array, left, mid, right):
    left_array_size = mid - left + 1
    right_array_size = right - mid

    left_array = list()
    right_array = list()

    for i in range(left_array_size):
        left_array.append(array[left + i])

    for i in range(right_array_size):
        right_array.append(array[mid + 1 + i])

    left_pointer, right_pointer, main_pointer = 0, 0, left

    while left_pointer < left_array_size and right_pointer < right_array_size:
        if left_array[left_pointer] <= right_array[right_pointer]:
            array[main_pointer] = left_array[left_pointer]
            left_pointer += 1
        else:
            array[main_pointer] = right_array[right_pointer]
            right_pointer += 1
        main_pointer += 1

    while left_pointer < left_array_size:
        array[main_pointer] = left_array[left_pointer]
        left_pointer += 1
        main_pointer += 1

    while right_pointer < right_array_size:
        array[main_pointer] = right_array[right_pointer]
        right_pointer += 1
        main_pointer += 1


a = [12, 11, 13, 4, 6, 5]
#recursive_merge_sort(a, 0, (len(a) - 1))
iterative_merge_sort(a)
print(a)
