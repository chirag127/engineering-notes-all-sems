## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Merge sort is a divide-and-conquer algorithm that recursively splits an array into two subarrays and then merges them in sorted order.
- The algorithm can be implemented using the following steps:

  1. If the array has only one element, return it as it is already sorted.
  2. Otherwise, divide the array into two equal or nearly equal subarrays and call merge sort on each subarray recursively.
  3. Merge the two sorted subarrays into one sorted array by comparing the first elements of each subarray and taking the smaller one into the output array. Repeat this until both subarrays are exhausted.
  4. Return the merged array as the final output.

- The time complexity of merge sort is O(n log n) in the worst, average and best cases, where n is the number of elements in the array. This is because the algorithm divides the array into log n levels and performs O(n) work at each level.
- The space complexity of merge sort is O(n) in the worst case, as the algorithm requires an auxiliary array of the same size as the input array to store the merged output.
- The following is a pseudocode for merge sort:

  ```
  function merge_sort(array)
    if length(array) <= 1 then
      return array
    end if
    mid = floor(length(array) / 2)
    left = merge_sort(array[0..mid-1])
    right = merge_sort(array[mid..length(array)-1])
    return merge(left, right)
  end function

  function merge(left, right)
    output = empty array
    i = 0
    j = 0
    while i < length(left) and j < length(right) do
      if left[i] <= right[j] then
        append left[i] to output
        i = i + 1
      else
        append right[j] to output
        j = j + 1
      end if
    end while
    append the remaining elements of left or right to output
    return output
  end function
  ```