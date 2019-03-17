# Python Program for recursive binary search.

# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1



def bubblesort(A):

    for i in range(len(A) - 1):
        for j in range(0, len(A) - 1 - i):
            if A[j] > A[j+1]:
                A = swap(A[j], A[j+1], j, A)
    return A


def swap(a, b, i, A):
    A[i] = b
    A[i+1] = a
    return A

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)


if __name__ == "__main__":
    A = range(101)
    search_val = 60

    idx = binarySearch(A, 0, (len(A) - 1), search_val)

    print(idx)
    A = [5, 6]
    A = bubblesort(A)
    print(A)

    alist = [54,26,93,17,77,31,44,55,20]
    mergeSort(alist)
    print(alist)
