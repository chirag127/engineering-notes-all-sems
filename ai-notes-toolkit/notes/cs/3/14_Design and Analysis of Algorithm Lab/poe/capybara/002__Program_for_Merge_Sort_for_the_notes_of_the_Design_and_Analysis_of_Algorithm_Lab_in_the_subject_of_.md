## Program for Merge Sort

Merge sort is a sorting algorithm that follows the divide-and-conquer approach. It is an efficient algorithm that works well on large datasets. In this section, we will discuss the program for merge sort.

### Steps for Merge Sort

1. Divide the unsorted array into n sub-arrays, each containing one element.
2. Repeatedly merge sub-arrays to produce new sorted sub-arrays until there is only one sub-array remaining. This will be the sorted array.

### Program for Merge Sort

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

### Conclusion

In conclusion, merge sort is an efficient algorithm that follows the divide-and-conquer approach. The program for merge sort is implemented using the merge() and mergeSort() functions. The merge() function merges two sorted sub-arrays into one sorted array, and the mergeSort() function recursively divides the unsorted array into sub-arrays until each sub-array contains only one element.