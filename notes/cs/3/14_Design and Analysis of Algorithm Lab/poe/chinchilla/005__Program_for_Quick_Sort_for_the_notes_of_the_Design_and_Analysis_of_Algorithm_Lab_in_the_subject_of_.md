## Program for Quick Sort

Quick Sort is an efficient sorting algorithm that is widely used for sorting large sets of data. It uses the divide-and-conquer approach to sort the elements in an array. The algorithm works by partitioning the array into two sub-arrays, one containing elements smaller than a chosen pivot and the other containing elements larger than the pivot. The pivot is then placed in its correct position and the algorithm recursively applies the same process to the two sub-arrays.

Here is a program for implementing Quick Sort in C++:

### Algorithm

1. Select a pivot element from the array.
2. Partition the array into two sub-arrays, one containing elements smaller than the pivot and the other containing elements larger than the pivot.
3. Recursively apply the same process to the two sub-arrays until the entire array is sorted.

### Program

```cpp
#include<iostream>
using namespace std;

void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);

    for(int j=low; j<=high-1; j++) {
        if(arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i+1], &arr[high]);
    return (i+1);
}

void quickSort(int arr[], int low, int high) {
    if(low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi-1);
        quickSort(arr, pi+1, high);
    }
}

int main() {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr)/sizeof(arr[0]);

    quickSort(arr, 0, n-1);

    cout<<"Sorted array: ";
    for(int i=0; i<n; i++) {
        cout<<arr[i]<<" ";
    }
    return 0;
}
```

### Explanation

1. The `swap` function is used to swap two elements in the array.
2. The `partition` function takes the last element of the array as the pivot and partitions the array into two sub-arrays.
3. The `quickSort` function recursively applies the same process to the two sub-arrays until the entire array is sorted.
4. The main function initializes the array and calls the `quickSort` function to sort the array.
5. The sorted array is printed using a for loop.

### Time Complexity

The time complexity of Quick Sort is O(nlogn) in the average case and O(n^2) in the worst case. However, the worst case can be avoided by choosing the pivot element carefully, such as by selecting the median of the array as the pivot.

### Conclusion

Quick Sort is a fast and efficient sorting algorithm that is widely used in various applications. It has a time complexity of O(nlogn) in the average case and can be optimized to avoid the worst case scenario.