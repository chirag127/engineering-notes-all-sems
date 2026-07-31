Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program to sort the elements of the array in ascending order using Bubble Sort technique. Here is the content in markdown format:

## 25.WAP to sort the elements of the array in ascending order using Bubble Sort technique.

- Bubble Sort is a simple sorting algorithm that compares adjacent elements of an array and swaps them if they are in the wrong order.
- The algorithm repeats this process until the array is sorted.
- The name Bubble Sort comes from the fact that the smaller elements "bubble" to the top of the array as the algorithm progresses.
- The algorithm can be implemented in any programming language that supports arrays and comparison operators.
- Here is an example of Bubble Sort algorithm in C language:

```c
// A function to swap two elements of an array
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

// A function to implement Bubble Sort algorithm
void bubbleSort(int arr[], int n)
{
    // n is the size of the array
    int i, j; // loop variables
    int swapped; // a flag to check if any swap occurred in a pass

    // Repeat n-1 passes or until the array is sorted
    for (i = 0; i < n-1; i++)
    {
        // Initialize swapped as false
        swapped = 0;

        // Compare each pair of adjacent elements and swap them if they are in the wrong order
        for (j = 0; j < n-i-1; j++)
        {
            if (arr[j] > arr[j+1])
            {
                swap(&arr[j], &arr[j+1]); // call the swap function
                swapped = 1; // set swapped as true
            }
        }

        // If no swap occurred in a pass, the array is already sorted and we can break the loop
        if (swapped == 0)
            break;
    }
}

// A function to print an array
void printArray(int arr[], int n)
{
    // n is the size of the array
    int i; // loop variable
    for (i = 0; i < n; i++)
    {
        printf("%d ", arr[i]); // print each element of the array
    }
    printf("\n"); // print a new line
}

// A main function to test the algorithm
int main()
{
    // Declare and initialize an array
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr)/sizeof(arr[0]); // calculate the size of the array

    // Print the original array
    printf("Original array: \n");
    printArray(arr, n);

    // Call the bubbleSort function to sort the array
    bubbleSort(arr, n);

    // Print the sorted array
    printf("Sorted array: \n");
    printArray(arr, n);

    return 0; // return 0 to indicate successful termination
}
```

- The output of the program is:

```
Original array: 
64 34 25 12 22 11 90 
Sorted array: 
11 12 22 25 34 64 90 
```

- The time complexity of Bubble Sort algorithm is O(n^2) in the worst case and average case, and O(n) in the best case, where n is the size of the array.
- The space complexity of Bubble Sort algorithm is O(1), as it only requires a constant amount of extra space for swapping.
- Bubble Sort is a stable sorting algorithm, which means it preserves the relative order of equal elements in the array.
- Bubble Sort is not a very efficient sorting algorithm, as it performs many unnecessary comparisons and swaps. It is only suitable for small or nearly sorted arrays.