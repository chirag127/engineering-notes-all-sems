 Here is the content in Markdown format without any emojis or external links and in a formal tone:

## Program for Insertion Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System.

1. Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It iterates through the list, growing the sorted list behind it.
2. For each item it encounters, it finds the correct position within the sorted list and inserts the item there.
3. The code for insertion sort looks like this:

function insertionSort(array) {
  for (let i = 1; i < array.length; i++) {
    let temp = array[i];
    let j = i - 1;

    while (j >= 0 && array[j] > temp) {
      array[j + 1] = array[j];
      j = j - 1;
    }
    array[j + 1] = temp;
  }
  return array;
}

4. Time complexity: O(n^2) performance. The nested while loops cause the algorithm to become inefficient on large lists.
5. However, insertion sort provides several advantages:
- It is simple to implement.
- It is efficient for (quite) small data sets.
- It is a stable sort.
- It requires only O(1) additional memory.
- It is adaptive; i.e., it's efficient if the list is already substantially sorted.

6. Hence, insertion sort is often used as part of more sophisticated algorithms, for example to perform an initial sort of a list before applying a faster general-purpose sort.