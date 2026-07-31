## Merge Sort

- Merge sort is a divide-and-conquer algorithm that recursively splits a given array of n elements into two halves, sorts each half, and then merges them back into a single sorted array.
- The algorithm can be described as follows:

  - Base case: If the array has zero or one element, it is already sorted. Return the array as it is.
  - Recursive case: Otherwise, divide the array into two subarrays of equal or nearly equal size. Call merge sort on each subarray and store the results in two sorted arrays. Then, merge the two sorted arrays into one sorted array by comparing the first elements of each array and taking the smaller one until both arrays are exhausted. Return the merged array as the result.

- The time complexity of merge sort is O(n log n) in the worst case, average case, and best case scenarios, where n is the number of elements in the array. This is because the algorithm always divides the array into two halves, which takes O(log n) steps, and then merges them back in O(n) time per step. Therefore, the total time is O(n log n) for any input.
- The following pseudocode illustrates the merge sort algorithm:

  ```
  function merge_sort(array)
    // Base case: array has zero or one element
    if length(array) <= 1 then
      return array
    // Recursive case: divide array into two halves
    mid = floor(length(array) / 2)
    left = array[0 ... mid-1] // first half of array
    right = array[mid ... length(array)-1] // second half of array
    // Sort each half recursively
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    // Merge the two sorted halves
    return merge(sorted_left, sorted_right)
  end function

  function merge(left, right)
    // Initialize an empty result array
    result = []
    // Initialize indices for left and right arrays
    i = 0
    j = 0
    // Loop until one of the arrays is exhausted
    while i < length(left) and j < length(right) do
      // Compare the first elements of left and right
      if left[i] <= right[j] then
        // Append the smaller element to the result
        append left[i] to result
        // Increment the index for left
        i = i + 1
      else
        // Append the smaller element to the result
        append right[j] to result
        // Increment the index for right
        j = j + 1
      end if
    end while
    // Append the remaining elements of the non-empty array to the result
    if i < length(left) then
      append left[i ... length(left)-1] to result
    else
      append right[j ... length(right)-1] to result
    end if
    // Return the result array
    return result
  end function
  ```

- To run the program for varied values of n > 5000, and record the time taken to sort, we can use a loop to generate random arrays of different sizes and measure the execution time of the merge sort function using a timer. For example, in Python, we can use the following code:

  ```
  import random
  import time

  # Define the merge sort function as above
  def merge_sort(array):
    ...

  def merge(left, right):
    ...

  # Initialize an empty list to store the time taken for different values of n
  time_list = []

  # Loop from n = 5000 to n = 10000 with a step of 500
  for n in range(5000, 10001, 500):
    # Generate a random array of size n
    array = [random.randint(0, 100) for _ in range(n)]
    # Start the timer
    start = time.time()
    # Sort the array using merge sort
    sorted_array = merge_sort(array)
    # Stop the timer
    end = time.time()
    # Calculate the time taken in seconds
    time_taken = end - start
    # Append the time taken to the time list
    time_list.append(time_taken)
    # Print the value of n and the time taken
    print(f"n = {n}, time = {time_taken} seconds")
  ```

- To plot a graph of the time taken versus n on a graph sheet, we can use a scatter plot or a line plot to show the relationship between the two variables. We can label the x-axis as "n" and the y-axis as "time (seconds)". We