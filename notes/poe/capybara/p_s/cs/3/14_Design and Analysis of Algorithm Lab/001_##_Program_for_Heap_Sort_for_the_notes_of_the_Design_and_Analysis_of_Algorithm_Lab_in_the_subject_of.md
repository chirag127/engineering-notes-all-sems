## Program for Merge Sort

Merge Sort is a popular sorting algorithm that follows the divide-and-conquer approach. It divides the array into smaller sub-arrays, sorts them individually, and then merges them to obtain the sorted array. In this section, we will discuss the program for Merge Sort and its implementation in the Design and Analysis of Algorithm Lab in the subject of Real-Time Systems.

### Steps in Merge Sort

The following steps are involved in the Merge Sort algorithm:

1. Divide the array into two halves
2. Sort the left half
3. Sort the right half
4. Merge the two halves

### Program for Merge Sort

Here is the program for Merge Sort in C++:

```
void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
 
    int L[n1], R[n2];
 
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
 
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
 
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}
 
void mergeSort(int arr[], int l, int r)
{
    if (l < r) {
        int m = l + (r - l) / 2;
 
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
 
        merge(arr, l, m, r);
    }
}
```

### Implementation in the Design and Analysis of Algorithm Lab

In the Design and Analysis of Algorithm Lab, Merge Sort can be implemented in the following steps:

1. Define the Merge function: The Merge function takes the array, the starting index l, the middle index m, and the ending index r as inputs. It first creates two sub-arrays, L and R, and copies the elements from the original array to the sub-arrays. It then compares the elements of the sub-arrays and merges them in a sorted order.

2. Define the Merge Sort function: The Merge Sort function takes the array, the starting index l, and the ending index r as inputs. It first calculates the middle index m, and then recursively calls itself for the left and right sub-arrays. Finally, it calls the Merge function to merge the two sorted sub-arrays.

3. Call the Merge Sort function: In the main function, we can call the Merge Sort function with the array, the starting index 0, and the ending index n-1, where n is the size of the array.

### Advantages of Merge Sort

1. Merge Sort has a time complexity of O(nlogn), which is the best time complexity for comparison-based sorting algorithms.
2. Merge Sort is a stable sort, which means that it maintains the relative order of equal elements in the sorted array.
3. Merge Sort is a parallelizable algorithm, which means that it can be easily implemented in parallel processing systems.

### Disadvantages of Merge Sort

1. Merge Sort requires extra space for the sub-arrays, which can be a problem for large arrays.
2. Merge Sort has a higher constant factor in its time complexity, which makes it slower than other sorting algorithms for small arrays.

### Applications of Merge Sort

1. Merge Sort is used in the implementation of external sorting algorithms, where the data is too large to fit into the main memory.
2. Merge Sort is used in the implementation of merge join algorithms in databases, where two sorted tables are merged to obtain the join result.

In conclusion, Merge Sort is a popular sorting algorithm that is widely used in various applications. Its time complexity, stability, and parallelizability make it a preferred choice for many sorting problems. Understanding the program for Merge Sort and its implementation in the Design and Analysis of Algorithm Lab can be helpful in learning and mastering the algorithm.