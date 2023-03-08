 Here are the notes for ### Sorting and Order Statistics - Quick Sort:

Quicksort is a divide and conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.

Steps:

1. Pick an element as pivot.
2. Partition the array into two subarrays - left partition has all elements with values less than the pivot value and right partition has all elements with values greater than the pivot value.
3. Recur for left partition and right partition.
4. Combine the results.

Pseudocode:
quicksort(arr, low, high) {
    if (low < high) {
        pivot = partition(arr, low, high);
        quicksort(arr, low, pivot-1);
        quicksort(arr, pivot+1, high);
    }
}

partition(arr, low, high) {
    pivot = arr[high];    // pivot
    i = low - 1;  // Index of smaller element

    for (j = low; j <= high-1; j++) {
        // If current element is smaller than or equal to pivot
        if (arr[j] <= pivot) {
            i++;    // increment index of smaller element
            swap arr[i] and arr[j]
        }
    }
    swap arr[i+1] and arr[high]
    return (i+1)
}

Advantages:
- Quicksort is a very efficient general-purpose sort.
- It has an efficient implementation and is often faster in practice compared to other sorting algorithms.
- It is a stable sort as relative order of elements with equal keys is preserved.

Disadvantages:
- It has worse case O(n2) time complexity which occurs if elements are already sorted or reverse sorted.
- Extra space is used for recursion.
- Difficult to parallelize.

Applications:
- Used in Database systems for indexing data.
- Used for solving various computational geometry problems.
- Used in C/C++ standard libraries.