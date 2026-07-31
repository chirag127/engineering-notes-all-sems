## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Merge sort is a divide-and-conquer algorithm that splits an array into two halves and recursively sorts each half, then merges the sorted halves into one sorted array.
- The algorithm can be implemented using the following steps:

  - Base case: If the array has zero or one element, it is already sorted and no further action is needed.
  - Recursive case: If the array has more than one element, divide it into two subarrays of equal or nearly equal size and sort each subarray recursively using merge sort.
  - Merge step: Combine the two sorted subarrays into one sorted array by comparing the first elements of each subarray and taking the smaller one into the output array, then repeating until one subarray is exhausted and appending the remaining elements of the other subarray to the output array.

- The time complexity of merge sort is O(n log n) in the average and worst cases, where n is the number of elements in the array. The space complexity is O(n) as the algorithm requires an auxiliary array of the same size as the input array.
- The following is a possible pseudocode implementation of merge sort:

  ```
  function merge_sort(array)
    // Base case
    if length(array) <= 1 then
      return array
    // Recursive case
    else
      // Divide the array into two subarrays
      mid = floor(length(array) / 2)
      left = array[0 ... mid - 1]
      right = array[mid ... length(array) - 1]
      // Sort each subarray recursively
      left = merge_sort(left)
      right = merge_sort(right)
      // Merge the sorted subarrays
      return merge(left, right)
    end if
  end function

  function merge(left, right)
    // Initialize an empty output array
    output = []
    // Initialize indices for left and right subarrays
    i = 0
    j = 0
    // Loop until one subarray is exhausted
    while i < length(left) and j < length(right) do
      // Compare the first elements of each subarray and take the smaller one into the output array
      if left[i] <= right[j] then
        output.append(left[i])
        i = i + 1
      else
        output.append(right[j])
        j = j + 1
      end if
    end while
    // Append the remaining elements of the non-exhausted subarray to the output array
    if i < length(left) then
      output.extend(left[i ... length(left) - 1])
    else
      output.extend(right[j ... length(right) - 1])
    end if
    // Return the output array
    return output
  end function
  ```