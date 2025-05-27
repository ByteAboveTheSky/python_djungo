def bubble_sort(arr, index=1):
    while arr[index] > arr[index-1]:
        continue
    a = arr[index-1]
    arr[index] = arr[index-1]
    arr[index-1] = a
    bubble_sort(arr, index-1)
