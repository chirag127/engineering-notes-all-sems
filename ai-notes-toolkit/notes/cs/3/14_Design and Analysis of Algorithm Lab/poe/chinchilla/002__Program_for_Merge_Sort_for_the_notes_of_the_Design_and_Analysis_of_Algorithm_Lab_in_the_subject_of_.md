## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

In this lab session, we will learn about the Merge Sort algorithm, which is a sorting algorithm used to sort elements in a list or an array. Merge Sort is an efficient algorithm with a time complexity of O(nlogn). Here is a program in Python for implementing the Merge Sort algorithm:

### Program for Merge Sort

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
```

### Explanation of the Program

In the above program, we have defined a function called `merge_sort()` that takes an array as an input. The function recursively divides the array into two halves until each sub-array has only one element. Then, the function merges the two sub-arrays in a sorted order.

The `merge()` function takes two sub-arrays, `left_half` and `right_half`, and merges them into a single array `arr`. The `i`, `j`, and `k` variables are used to keep track of the elements in the left, right, and merged arrays, respectively.

The program first checks if the length of the array is greater than 1. If it is, the program finds the middle index of the array and divides the array into two halves. The `merge_sort()` function is called recursively on the left and right halves until the length of the sub-arrays becomes 1.

Then, the `merge()` function is called to merge the two sub-arrays. The elements from the left and right sub-arrays are compared, and the smallest element is added to the `arr` array. This process continues until all the elements from both sub-arrays are added to the `arr` array.

Finally, the sorted array is returned.

### Conclusion

In this lab session, we learned about the Merge Sort algorithm and implemented it in Python. The Merge Sort algorithm is an efficient sorting algorithm with a time complexity of O(nlogn). We hope this program will help you understand the Merge Sort algorithm better and prepare you for your exams.