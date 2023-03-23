## Program for Selection Sort

Selection Sort is an algorithm for sorting a list of elements in increasing or decreasing order. It is a simple and easy-to-understand sorting algorithm, but it is not very efficient for large lists. In this lab, we will learn how to implement Selection Sort in a program.

### Steps for Selection Sort

The Selection Sort algorithm involves the following steps:

1. Set the first element of the list as the minimum value.
2. Compare the minimum value with the next element in the list.
3. If the next element is smaller than the minimum value, set the next element as the new minimum value.
4. Continue comparing the minimum value with each element in the list until the end of the list is reached.
5. Swap the minimum value with the first element of the list.
6. Repeat steps 2-5 for the remaining unsorted elements in the list.

### Implementation of Selection Sort

Here is a sample program in C++ for implementing Selection Sort:

```
#include<iostream>
using namespace std;
void selectionSort(int arr[], int n)
{
    int i, j, min_idx;
    for (i = 0; i < n-1; i++)
    {
        min_idx = i;
        for (j = i+1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;
        swap(arr[min_idx], arr[i]);
    }
}
int main()
{
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr)/sizeof(arr[0]);
    selectionSort(arr, n);
    cout << "Sorted array: \n";
    for (int i=0; i < n; i++)
        cout << arr[i] << " ";
    return 0;
}
```

The above program sorts an array of integers using Selection Sort. Here's how it works:

1. The `selectionSort` function takes an array and its size as input.
2. Two variables `i` and `j` are used for iterating over the array.
3. The `min_idx` variable is used to keep track of the index of the minimum value in the array.
4. The outer loop iterates over the unsorted elements in the array.
5. The inner loop finds the minimum value in the unsorted portion of the array.
6. The `swap` function is used to swap the minimum value with the first element of the unsorted portion of the array.
7. The sorted array is printed using a `for` loop in the `main` function.

### Time Complexity of Selection Sort

The time complexity of Selection Sort is O(n^2), where n is the number of elements in the list. This means that the algorithm takes quadratic time to sort the list. Selection Sort is not very efficient for large lists, and other sorting algorithms such as Merge Sort and Quick Sort are preferred for large datasets.

In conclusion, Selection Sort is a simple and easy-to-understand sorting algorithm that can be easily implemented in a program. However, it is not very efficient for large lists, and other sorting algorithms should be used for large datasets.