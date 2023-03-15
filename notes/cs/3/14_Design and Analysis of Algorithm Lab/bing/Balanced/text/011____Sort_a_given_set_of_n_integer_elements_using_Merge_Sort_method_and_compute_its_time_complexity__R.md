## Merge Sort

- Merge sort is a divide-and-conquer algorithm that recursively splits a given array of n elements into two halves, sorts each half, and then merges them back together in sorted order.
- The algorithm can be described as follows:

  - If the array has only one element, return it as it is already sorted.
  - Otherwise, divide the array into two subarrays of equal or nearly equal size.
  - Recursively sort each subarray using merge sort.
  - Merge the two sorted subarrays into one sorted array by comparing the first elements of each subarray and taking the smaller one into the output array, until one of the subarrays is empty, then copy the remaining elements of the other subarray.
- The time complexity of merge sort is O(n log n) in the worst case, average case, and best case, where n is the number of elements in the array. This is because the algorithm always divides the array into two halves, which takes O(log n) steps, and then merges them in O(n) time at each step.
- The following pseudocode illustrates the merge sort algorithm:

  ```
  function merge_sort(array)
    if length(array) <= 1
      return array
    else
      mid = floor(length(array) / 2)
      left = merge_sort(array[0..mid-1])
      right = merge_sort(array[mid..length(array)-1])
      return merge(left, right)
  end function

  function merge(left, right)
    result = empty array
    while left and right are not empty
      if left[0] <= right[0]
        append left[0] to result
        remove left[0] from left
      else
        append right[0] to result
        remove right[0] from right
      end if
    end while
    if left is not empty
      append left to result
    else if right is not empty
      append right to result
    end if
    return result
  end function
  ```

- To run the program for varied values of n > 5000, and record the time taken to sort, one can use a loop to generate random arrays of different sizes, and measure the execution time of the merge sort function using a timer. For example, in Python, one can use the following code:

  ```
  import random
  import time

  # generate a random array of size n
  def generate_array(n):
    array = []
    for i in range(n):
      array.append(random.randint(0, 1000000))
    return array

  # run merge sort on a random array of size n and record the time taken
  def run_merge_sort(n):
    array = generate_array(n)
    start = time.time()
    sorted_array = merge_sort(array)
    end = time.time()
    return end - start

  # run the experiment for different values of n and plot the results
  n_values = [5000, 10000, 20000, 40000, 80000, 160000]
  time_values = []
  for n in n_values:
    time_values.append(run_merge_sort(n))

  # plot the graph of time taken versus n using matplotlib
  import matplotlib.pyplot as plt
  plt.plot(n_values, time_values)
  plt.xlabel('n')
  plt.ylabel('time taken (seconds)')
  plt.title('Merge Sort Time Complexity')
  plt.show()
  ```

- The graph of the time taken versus n on a non graph sheet can be drawn by hand using a ruler and a pencil, or using a software tool such as Microsoft Excel or Google Sheets. The graph should look like a curve that increases gradually as n increases, as shown below:

![Merge Sort Graph](https://i.imgur.com/0f6y1wO.png)

- To demonstrate how the divide-and-conquer method works along with its time complexity analysis, one can use an example array and show the steps of the algorithm visually, as shown below:

![Merge Sort Example](https://i.imgur.com/8Z8yG1f.png)

- The time complexity analysis can be explained as follows:

  - At each level of recursion, the array is divided into two subarrays of half the size, which takes O(1) time.
  - The number of levels of recursion is log n, where n is the size of the array, since the array is halved at each level until it reaches a single element.
  - At each level of recursion, the merge function takes O(n) time to merge the two sorted subarrays into one sorted array, where n is the size of the array at that level.
  - Therefore