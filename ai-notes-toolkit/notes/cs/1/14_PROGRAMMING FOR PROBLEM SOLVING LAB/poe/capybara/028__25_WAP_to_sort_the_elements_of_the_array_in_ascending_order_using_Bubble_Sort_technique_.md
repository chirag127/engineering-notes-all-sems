## 25. WAP to sort the elements of the array in ascending order using Bubble Sort technique.

The Bubble Sort technique is a simple sorting algorithm that compares adjacent elements of an array and swaps them if they are in the wrong order. This process is repeated until the entire array is sorted in ascending order.

Here are the steps to sort an array in ascending order using Bubble Sort technique:

1. Take an array as input from the user or generate it randomly.
2. Initialize a variable 'n' to store the size of the array.
3. Start a loop that runs n-1 times.
4. Within the loop, start another loop that runs from the first element of the array to the (n-1)th element.
5. Within the second loop, compare the current element with the next element. If the current element is greater than the next element, swap them.
6. After each iteration of the second loop, the largest element of the array will be moved to the end of the array.
7. Continue the first loop until all elements have been sorted in ascending order.

Here is the code for Bubble Sort technique in C:

```c
#include <stdio.h>

void bubble_sort(int arr[], int n) {
  int i, j, temp;
  
  for(i=0; i<n-1; i++) {
    for(j=0; j<n-i-1; j++) {
      if(arr[j] > arr[j+1]) {
        temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
      }
    }
  }
}

void main() {
  int arr[100], n, i;
  
  printf("Enter the size of the array: ");
  scanf("%d", &n);
  
  printf("Enter %d elements of the array: \n", n);
  for(i=0; i<n; i++) {
    scanf("%d", &arr[i]);
  }
  
  bubble_sort(arr, n);
  
  printf("The sorted array in ascending order is: \n");
  for(i=0; i<n; i++) {
    printf("%d ", arr[i]);
  }
}
```

This code takes an array as input from the user, sorts it using Bubble Sort technique, and displays the sorted array in ascending order.

In conclusion, the Bubble Sort technique is a simple and easy-to-implement sorting algorithm that can be used to sort elements of an array in ascending order.