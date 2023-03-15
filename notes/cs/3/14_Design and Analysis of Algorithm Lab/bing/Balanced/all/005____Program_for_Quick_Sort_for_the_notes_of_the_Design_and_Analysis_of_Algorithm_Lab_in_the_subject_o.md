## Program for Quick Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Quick sort is a sorting algorithm that uses the divide and conquer strategy to sort a list of elements.
- The basic idea of quick sort is to choose a pivot element from the list, and partition the list into two sublists: one with elements smaller than the pivot, and one with elements larger than the pivot.
- The pivot element is then placed in its correct position in the sorted list, and the sublists are recursively sorted using the same procedure.
- The algorithm can be implemented using the following steps:

  1. Choose a pivot element from the list, usually the first or the last element.
  2. Compare each element in the list with the pivot, and swap it with another element if necessary, such that all elements smaller than the pivot are on the left of the pivot, and all elements larger than the pivot are on the right of the pivot.
  3. Place the pivot in its correct position in the sorted list, and divide the list into two sublists: one with elements on the left of the pivot, and one with elements on the right of the pivot.
  4. Recursively apply the same procedure to the sublists, until the sublists are of size one or zero.

- The following is a pseudocode for quick sort:

  ```
  function quick_sort(list, low, high)
    if low < high
      pivot_index = partition(list, low, high) // partition the list and return the pivot index
      quick_sort(list, low, pivot_index - 1) // sort the left sublist
      quick_sort(list, pivot_index + 1, high) // sort the right sublist
    end if
  end function

  function partition(list, low, high)
    pivot = list[high] // choose the last element as the pivot
    i = low - 1 // initialize the index of the smaller element
    for j = low to high - 1 // loop through the list
      if list[j] < pivot // if the current element is smaller than the pivot
        i = i + 1 // increment the index of the smaller element
        swap list[i] and list[j] // swap the current element with the smaller element
      end if
    end for
    swap list[i + 1] and list[high] // swap the pivot with the element next to the smaller element
    return i + 1 // return the pivot index
  end function
  ```

- The following is a sample program for quick sort in C language:

  ```c
  #include <stdio.h>

  // function to swap two elements in an array
  void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
  }

  // function to partition an array using the last element as the pivot
  int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // choose the last element as the pivot
    int i = low - 1; // initialize the index of the smaller element
    for (int j = low; j < high; j++) { // loop through the array
      if (arr[j] < pivot) { // if the current element is smaller than the pivot
        i++; // increment the index of the smaller element
        swap(&arr[i], &arr[j]); // swap the current element with the smaller element
      }
    }
    swap(&arr[i + 1], &arr[high]); // swap the pivot with the element next to the smaller element
    return i + 1; // return the pivot index
  }

  // function to sort an array using quick sort
  void quick_sort(int arr[], int low, int high) {
    if (low < high) {
      int pivot_index = partition(arr, low, high); // partition the array and return the pivot index
      quick_sort(arr, low, pivot_index - 1); // sort the left subarray
      quick_sort(arr, pivot_index + 1, high); // sort the right subarray
    }
  }

  // function to print an array
  void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
      printf("%d ", arr[i]);
    }
    printf("\n");
  }

  // main function
  int main() {
    int arr[] = {10, 7, 8, 9, 1, 5}; // sample array
    int size =