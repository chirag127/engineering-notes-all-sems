## 24. WAP to search an element in an array using Linear Search.

Linear search is a simple algorithm to search for an element in an array. It is also known as sequential search. In this algorithm, we traverse the array from the beginning to the end and check each element until we find the desired element or reach the end of the array. If the desired element is found, we return its index, otherwise, we return -1 to indicate that the element is not present in the array.

Here are the steps to implement linear search:

1. Take an array of integers as input from the user.
2. Take the element to be searched as input from the user.
3. Traverse the array from the beginning to the end.
4. Check each element of the array with the element to be searched.
5. If the element is found, return its index.
6. If the element is not found, return -1.

Here is the Python code to implement linear search:

``` python
# function to perform linear search
def linear_search(arr, x):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

# take input from user
arr = list(map(int, input("Enter the array elements: ").split()))
x = int(input("Enter the element to be searched: "))

# call the linear search function
result = linear_search(arr, x)

# check the result and print the output
if result == -1:
    print("Element not found in the array.")
else:
    print("Element found at index", result)
```

In the above code, we have defined a function named `linear_search` that takes two arguments: `arr` (the array to be searched) and `x` (the element to be searched). The function returns the index of the element if it is found, otherwise it returns -1.

We have also taken input from the user for the array and the element to be searched, and called the `linear_search` function to perform the search. Finally, we have checked the result and printed the output accordingly.

Linear search has a time complexity of O(n), where n is the size of the array. This means that the time taken to search for an element increases linearly with the size of the array. Therefore, it is not suitable for large arrays, and other algorithms like binary search should be used instead.