def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

numbers = [1, 3, 5, 7, 9, 11, 13]
target = 10

# index = binary_search_recursive(numbers, target, 0, len(numbers) - 1)
# print(f"Index of {target}: {index}")
def find_num(arr, target):
    found = None
    start_point  = 0
    end_point = len(arr)-1
    if target in arr:
        while start_point<=end_point or arr[found]!=target:
            found = (start_point+end_point) // 2
            if arr[found] > target:
                end_point = found - 1
            else:
                start_point = found + 1

        return found
    else:
        return -1

print(find_num([1, 3, 5, 7, 9, 11, 13],1))

def found_index_faster(numbers, target):
    start_index = 0
    end_index = len(numbers)-1
    found = False
    while start_index <= end_index and not found:
        mid = (start_index + end_index) // 2
        if numbers[mid] == target:
            found = True
        else:
            if target < numbers[mid]:
                end_index = mid - 1
            else:
                start_index = mid + 1
    return found
print(found_index_faster([1, 3, 5, 7, 9, 11, 13], 10))

