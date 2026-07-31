## Sort a Given Set of n Integer Elements using Merge Sort Method and Compute its Time Complexity

Merge sort is a popular sorting algorithm that follows the "Divide and Conquer" approach. It divides the array into two halves, sorts them separately, and then merges them to obtain a sorted array. In this way, it solves the problem of sorting a large array by breaking it down into smaller sub-problems. 

### Merge Sort Algorithm

1. Divide the given array into two halves.
2. Recursively sort the left and right halves of the array.
3. Merge the two sorted halves to obtain the final sorted array.

### Pseudo Code

```
mergesort(arr, left, right)
    if left < right
        middle = (left + right) / 2
        mergesort(arr, left, middle)
        mergesort(arr, middle+1, right)
        merge(arr, left, middle, right)

merge(arr, left, middle, right)
    n1 = middle - left + 1
    n2 = right - middle
    
    L = [0] * n1
    R = [0] * n2
    
    for i in range(n1):
        L[i] = arr[left+i]
    
    for j in range(n2):
        R[j] = arr[middle+j+1]
        
    i = 0
    j = 0
    k = left
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
```

### Time Complexity Analysis

The time complexity of Merge Sort can be analyzed using the "Master Theorem." The theorem states that if a problem of size n is divided into a sub-problems of size n/b, each solved recursively in time T(n/b), and the combine step takes time O(n), then the overall time complexity can be expressed as:

T(n) = aT(n/b) + O(n)

where a is the number of sub-problems and b is the size of each sub-problem.

#### Worst Case Time Complexity

In the worst case, Merge Sort takes O(n log n) time. This occurs when the array is in reverse sorted order, and each level of recursion requires the merging of two sub-arrays of size n/2.

#### Average Case Time Complexity

The average case time complexity of Merge Sort is also O(n log n). This is because it divides the array into two halves and sorts them separately, which takes O(log n) time. The merging step takes O(n) time. Therefore, the overall time complexity is O(n log n).

#### Best Case Time Complexity

The best case time complexity of Merge Sort is also O(n log n). This occurs when the array is already sorted. In this case, the algorithm still divides the array into two halves and merges them, but each level of recursion requires only O(n) time.

### Running Time Analysis

To measure the running time of Merge Sort, we can run the algorithm on different input sizes and record the time taken to sort each list. We can use a random number generator to generate the input lists or read them from a file. We can then plot a graph of the time taken versus the input size.

### Steps to Run the Program

1. Generate or read a list of integers of size n > 5000.
2. Implement the Merge Sort algorithm as shown above.
3. Measure the time taken to sort the list using a timer function.
4. Plot a graph of the time taken versus the input size.

### Conclusion

Merge Sort is a popular sorting algorithm that uses the "Divide and Conquer" approach to sort large arrays efficiently. It has a worst-case time complexity of O(n log n) and is widely used in practice. By measuring the running time of the algorithm for different input sizes, we can analyze its performance and compare it with other sorting algorithms.