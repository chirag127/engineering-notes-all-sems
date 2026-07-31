Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write a program to sort the elements of the array in ascending order using Bubble Sort technique. Here is the content in markdown format:

## 25.WAP to sort the elements of the array in ascending order using Bubble Sort technique.

Bubble Sort is a simple sorting algorithm that compares adjacent elements in an array and swaps them if they are in the wrong order. The algorithm repeats this process until the array is sorted. The name comes from the fact that the smaller elements "bubble" to the top of the array.

The steps of the algorithm are as follows:

- Start from the first element of the array and compare it with the next element. If the first element is greater than the second element, swap them. Otherwise, leave them as they are.
- Move to the next pair of elements and repeat the same comparison and swapping process.
- Continue this until the end of the array. This completes one pass of the algorithm.
- Repeat the same process for the remaining passes, but each time, ignore the last sorted element of the array. This reduces the number of comparisons and swaps in each pass.
- The algorithm stops when no swaps are done in a pass, which means the array is sorted.

Here is an example of how the algorithm works on an array of 5 elements:

![Bubble Sort Example](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)

Here is the pseudocode of the algorithm:

```
procedure bubbleSort(A : list of sortable items)
    n := length(A)
    repeat
        swapped := false
        for i := 1 to n-1 inclusive do
            /* if this pair is out of order */
            if A[i-1] > A[i] then
                /* swap them and remember something changed */
                swap(A[i-1], A[i])
                swapped := true
            end if
        end for
        /* if no elements were swapped by this pass, we're done */
        n := n - 1
    until not swapped
end procedure
```

Here is the program in C language:

```c
#include <stdio.h>

void bubbleSort(int A[], int n) {
    int i, j, temp, swapped;
    do {
        swapped = 0; // initialize swapped as false
        for (i = 0; i < n - 1; i++) {
            // compare adjacent elements
            if (A[i] > A[i + 1]) {
                // swap them if they are in wrong order
                temp = A[i];
                A[i] = A[i + 1];
                A[i + 1] = temp;
                swapped = 1; // set swapped as true
            }
        }
        n--; // reduce the size of unsorted part by one
    } while (swapped); // repeat until no swaps are done
}

void printArray(int A[], int n) {
    int i;
    for (i = 0; i < n; i++) {
        printf("%d ", A[i]);
    }
    printf("\n");
}

int main() {
    int A[] = {5, 2, 7, 4, 1, 3, 6}; // sample array
    int n = sizeof(A) / sizeof(A[0]); // size of array
    printf("Original array: ");
    printArray(A, n);
    bubbleSort(A, n); // sort the array
    printf("Sorted array: ");
    printArray(A, n);
    return 0;
}
```

Here is the output of the program:

```
Original array: 5 2 7 4 1 3 6
Sorted array: 1 2 3 4 5 6 7
```