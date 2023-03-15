## 25.WAP to sort the elements of the array in ascending order using Bubble Sort technique.

- Bubble sort is a simple sorting algorithm that compares adjacent elements of an array and swaps them if they are in the wrong order.
- The algorithm repeats this process until the array is sorted.
- The name bubble sort comes from the fact that the smaller elements "bubble" to the top of the array, while the larger elements sink to the bottom.
- The algorithm can be implemented in any programming language that supports arrays and comparison operators.
- Here is an example of bubble sort in C language:

```c
// A function to sort an array using bubble sort
void bubbleSort(int arr[], int n) {
  // n is the size of the array
  int i, j, temp;
  // Loop through the array from 0 to n-1
  for (i = 0; i < n-1; i++) {
    // Loop through the array from 0 to n-i-1
    for (j = 0; j < n-i-1; j++) {
      // Compare the current element with the next element
      if (arr[j] > arr[j+1]) {
        // Swap them if they are in the wrong order
        temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
      }
    }
  }
}

// A function to print an array
void printArray(int arr[], int n) {
  // n is the size of the array
  int i;
  // Loop through the array and print each element
  for (i = 0; i < n; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

// A main function to test the bubble sort function
int main() {
  // Declare an array of 10 elements
  int arr[10] = {64, 34, 25, 12, 22, 11, 90, 45, 67, 89};
  // Print the original array
  printf("Original array: ");
  printArray(arr, 10);
  // Sort the array using bubble sort
  bubbleSort(arr, 10);
  // Print the sorted array
  printf("Sorted array: ");
  printArray(arr, 10);
  // Return 0 to indicate successful execution
  return 0;
}
```

- The output of the program is:

```
Original array: 64 34 25 12 22 11 90 45 67 89 
Sorted array: 11 12 22 25 34 45 64 67 89 90 
```

- Some important points to note about bubble sort are:

  - It is a stable sorting algorithm, meaning that it preserves the relative order of equal elements in the array.
  - It has a time complexity of O(n^2) in the worst and average case, and O(n) in the best case, where n is the size of the array.
  - It has a space complexity of O(1), meaning that it does not require any extra space to sort the array.
  - It is one of the simplest and easiest sorting algorithms to understand and implement, but it is not very efficient for large or nearly sorted arrays.