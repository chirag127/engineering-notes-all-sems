## 25. WAP to sort the elements of the array in ascending order using Bubble Sort technique.

The Bubble Sort technique is one of the simplest sorting algorithms. It works by repeatedly swapping adjacent elements if they are in the wrong order until the entire array is sorted. Here are the steps to sort an array in ascending order using Bubble Sort:

1. Start by defining an array with the desired elements to be sorted.
2. Define a variable to store the length of the array.
3. Use a loop to iterate through the array. The outer loop will iterate for n-1 times, where n is the length of the array.
4. The inner loop will iterate for n-i-1 times, where i is the index of the outer loop.
5. Compare the adjacent elements of the array. If the left element is greater than the right element, swap them.
6. After each iteration of the inner loop, the largest element will be moved to the end of the array.
7. Continue the outer loop until the entire array is sorted in ascending order.

Here's the pseudocode for Bubble Sort:

```
for i from 0 to n-1
    for j from 0 to n-i-1
        if arr[j] > arr[j+1]
            swap(arr[j], arr[j+1])
```

And here's the Python code to implement Bubble Sort:

```python
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubbleSort(arr)
print(sorted_arr)
```

In this example, the output will be `[11, 12, 22, 25, 34, 64, 90]`, which is the sorted array in ascending order.

Bubble Sort has a time complexity of O(n^2), which makes it inefficient for large arrays. However, it's a good sorting algorithm to learn because of its simplicity and ease of implementation.