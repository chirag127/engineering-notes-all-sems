## 25. WAP to sort the elements of the array in ascending order using Bubble Sort technique.

Bubble sort is a simple sorting algorithm that compares adjacent elements in an array and swaps them if they are in the wrong order. The algorithm continues to do this until the entire array is sorted in ascending order.

Here is an example of how to implement bubble sort in C++:

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
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr)/sizeof(arr[0]);
    bubbleSort(arr, n);
    cout << "Sorted array: \n";
    for (int i=0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
    return 0;
}
```

This code defines a function `bubbleSort` that takes an array of integers and its size as arguments. The function uses two nested loops to iterate over the array. In the inner loop, adjacent elements are compared and swapped if they are in the wrong order. The outer loop runs until the entire array is sorted.

In the `main` function, we create an array of integers and call the `bubbleSort` function to sort it. Finally, we print the sorted array.

Bubble sort has a time complexity of O(n^2) in the worst case, where n is the number of elements in the array. This makes it inefficient for large datasets. However, it is easy to understand and implement, making it a good choice for small datasets or for educational purposes.