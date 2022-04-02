def binarySearch(arr, x):
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


arr = [2,3,5,6,8,9,10,25,70,75]
result = binarySearch(arr, 70)

if not result:
    print("x was not in the given Array")
else:
    print(f"X is at the Index {str(result)}")