## 25.WAP to sort the elements of the array in ascending order using Bubble Sort technique.

- Bubble sort is a simple sorting algorithm that compares adjacent elements of an array and swaps them if they are in the wrong order.
- The algorithm repeats this process until the array is sorted.
- The name bubble sort comes from the fact that the smaller elements "bubble" to the top of the array, while the larger elements sink to the bottom.
- The algorithm can be implemented in any programming language, but here is an example in C:

```c
// A function to sort an array using bubble sort
void bubbleSort(int arr[], int n) {
  // n is the size of the array
  int i, j, temp; // variables for looping and swapping
  for (i = 0; i < n - 1; i++) { // loop through the array n-1 times
    for (j = 0; j < n - i - 1; j++) { // loop through the unsorted part of the array
      if (arr[j] > arr[j + 1]) { // compare adjacent elements
        // swap them if they are in the wrong order
        temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}

// A function to print an array
void printArray(int arr[], int n) {
  // n is the size of the array
  int i; // variable for looping
  for (i = 0; i < n; i++) { // loop through the array
    printf("%d ", arr[i]); // print each element
  }
  printf("\n"); // print a new line
}

// A main function to test the bubble sort function
int main() {
  int arr[] = {64, 34, 25, 12, 22, 11, 90}; // an example array
  int n = sizeof(arr) / sizeof(arr[0]); // calculate the size of the array
  printf("Unsorted array: \n");
  printArray(arr, n); // print the unsorted array
  bubbleSort(arr, n); // sort the array using bubble sort
  printf("Sorted array: \n");
  printArray(arr, n); // print the sorted array
  return 0; // end the program
}
```
- The output of the program is:

```
Unsorted array: 
64 34 25 12 22 11 90 
Sorted array: 
11 12 22 25 34 64 90 
```
- Some points to remember about bubble sort are:

  - It is a stable sorting algorithm, meaning that it preserves the relative order of equal elements in the array.
  - It has a time complexity of O(n^2) in the worst and average case, and O(n) in the best case, where n is the size of the array.
  - It has a space complexity of O(1), meaning that it does not require any extra space apart from the input array.
  - It is one of the simplest sorting algorithms to understand and implement, but it is not very efficient for large or nearly sorted arrays.