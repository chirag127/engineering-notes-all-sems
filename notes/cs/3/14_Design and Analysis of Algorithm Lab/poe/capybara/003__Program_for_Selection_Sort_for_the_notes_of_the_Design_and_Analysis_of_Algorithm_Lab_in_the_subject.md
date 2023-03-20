## Program for Selection Sort

In this section, we will discuss the program for selection sort. Selection sort is an algorithm that sorts an array by repeatedly finding the minimum element from the unsorted part of the array and placing it at the beginning of the sorted part.

The steps to implement selection sort in C++ are as follows:

1. Create a function `selectionSort()` that takes an array of integers and its size as parameters.
2. In the function, create two variables `minIndex` and `temp`.
3. Use a nested loop to traverse the array. The outer loop will traverse the array from the first element to the second last element. The inner loop will traverse the array from the next element of the outer loop to the last element.
4. Inside the inner loop, check if the current element is less than the minimum element found so far. If it is, update the `minIndex` variable to the index of the current element.
5. After the inner loop completes, swap the minimum element found with the first element of the unsorted part of the array.
6. Repeat steps 3-5 until the entire array is sorted.

The complete program for selection sort in C++ is as follows:

```C++
#include <iostream>
using namespace std;

void selectionSort(int arr[], int n) {
    int minIndex, temp;
    for (int i = 0; i < n - 1; i++) {
        minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}

int main() {
    int arr[] = {5, 2, 7, 3, 9, 1, 4, 6, 8};
    int n = sizeof(arr) / sizeof(arr[0]);
    selectionSort(arr, n);
    cout << "Sorted array:";
    for (int i = 0; i < n; i++) {
        cout << " " << arr[i];
    }
    cout << endl;
    return 0;
}
```

This program takes an array of integers, sorts it using selection sort, and then prints the sorted array.

In conclusion, selection sort is a simple yet effective sorting algorithm. The program for selection sort is easy to understand and implement in C++. By using this program, we can sort arrays of integers in real-time systems efficiently.