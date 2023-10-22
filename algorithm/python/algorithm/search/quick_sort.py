def quicksort(arr, leftmost, rightmost):
    if leftmost < rightmost:
        pivot = partition(arr, leftmost, rightmost)
        quicksort(arr, leftmost, pivot-1)
        quicksort(arr, pivot+1, rightmost)

def partition(arr, leftmost, rightmost):
    pivot = arr[rightmost]
    i = leftmost-1
    for j in range(leftmost, rightmost):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[rightmost] = arr[rightmost], arr[i+1]
    return i+1

arr = [64, 34, 25, 12, 22, 11, 90]
quicksort(arr, 0, len(arr)-1)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" %arr[i]),