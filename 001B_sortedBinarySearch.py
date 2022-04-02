import numpy as np

def sortedBinarySearch(arr, x):
    arr = np.array(arr)
    arr.sort()
    high = len(arr)-1
    low = 0
    mid = 0


    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return False


arr = [2,70,3,5,6,80,9,10,25,75]
result = sortedBinarySearch(arr, 70)

if not result:
    print("x was not in the given Array")
else:
    print(f"X is at the Index {str(result)}")