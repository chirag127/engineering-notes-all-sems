 Here is the formal content in markdown format without any emojis or external links:

## Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System.

1. Selection sort is a simple sorting algorithm. This algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.
2. The algorithm divides the input array into two parts:
- The sorted array
- The unsorted array
3. The steps to implement selection sort are:
- Find the minimum element in the unsorted array and swap it with the first element.
- Increment the sorted array size by 1.
- Repeat step#1 and step#2 until the sorted array size becomes equal to the array size.

Pseudocode:
selectionSort(array, size)
for i = 0 to size - 1
    // Find the minimum index
    minIndex = i
    for j = i+1 to size - 1
        if array[j] < array[minIndex]
            minIndex = j
    // Swap the found minimum element with the first element
    swap(array[i], array[minIndex])
end for

The time complexity of selection sort is O(n2) as there are two nested loops. Although it is a simple algorithm, it is not suitable for large data sets as its performance decreases quadratically.

The above content is written in a formal tone without any emojis or external links as per your guidelines. Please let me know if you would like me to modify or expand the content in any way.