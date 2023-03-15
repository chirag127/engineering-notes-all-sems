## 25. WAP to sort the elements of the array in ascending order using Bubble Sort technique.

Bubble sort is a simple sorting algorithm that compares adjacent elements in an array and swaps them if they are in the wrong order. The algorithm continues to do this until the entire array is sorted in ascending order. Here is an example of how to implement bubble sort in C++ to sort an array of integers in ascending order:

```c++
#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n)
{
    for (int i = 0; i < n-1; i++)
    {
        for (int j = 0; j < n-i-1; j++)
        {
            if (arr[j] > arr[j+1])
            {
                swap(arr[j], arr[j+1]);
            }
        }
    }
}

int main()
{
    int arr[] = {5, 2, 42, 6, 1, 3, 2};
    int n = sizeof(arr)/sizeof(arr[0]);
    bubbleSort(arr, n);
    cout << "Sorted array: \n";
    for (int i=0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
    return 0;
}
```

- The function `bubbleSort` takes as input an array of integers and its size.
- The outer loop runs from 0 to `n-1`, where `n` is the size of the array.
- The inner loop runs from 0 to `n-i-1`.
- In each iteration of the inner loop, the algorithm compares the current element `arr[j]` with the next element `arr[j+1]`.
- If the current element is greater than the next element, the algorithm swaps them using the `swap` function.
- The algorithm continues to do this until the entire array is sorted in ascending order.

This is how bubble sort can be used to sort the elements of an array in ascending order. It is important to note that bubble sort is not the most efficient sorting algorithm and is not suitable for large datasets. However, it is simple to understand and implement, making it a good starting point for learning about sorting algorithms.