## 22. WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them.

When working with arrays, it is often necessary to perform operations on corresponding elements of two or more arrays. One such operation is finding the sum of corresponding elements of two arrays. In this context, we can write a program in Python that takes two arrays as input, computes the sum of corresponding elements of these arrays, stores the result in a third array, and prints the output.

Here are the steps to write the program:

1. Start the program by defining the main function.
2. Within the main function, create three empty arrays using the numpy module. We'll use numpy because it provides an efficient way of performing mathematical operations on arrays.
3. Take input from the user for the length of the arrays using the input() function.
4. Use a for loop to take input for each element of the first array and store it in the first array.
5. Repeat step 4 for the second array.
6. Use another for loop to compute the sum of corresponding elements of the two arrays and store the result in the third array.
7. Print the third array using the print() function.

Here's the Python code for the program:

```python
import numpy as np

def main():
    # create empty arrays
    arr1 = np.empty(0)
    arr2 = np.empty(0)
    arr3 = np.empty(0)

    # take input for length of arrays
    n = int(input("Enter the length of the arrays: "))

    # take input for first array
    print("Enter the elements of the first array: ")
    for i in range(n):
        element = int(input())
        arr1 = np.append(arr1, element)

    # take input for second array
    print("Enter the elements of the second array: ")
    for i in range(n):
        element = int(input())
        arr2 = np.append(arr2, element)

    # compute sum of corresponding elements
    for i in range(n):
        sum = arr1[i] + arr2[i]
        arr3 = np.append(arr3, sum)

    # print the third array
    print("Sum of corresponding elements of the two arrays: ")
    print(arr3)

if __name__ == "__main__":
    main()
```

In conclusion, the above program takes two arrays as input, computes the sum of corresponding elements of these arrays, stores the result in a third array, and prints the output. It can be used as a reference to write similar programs for other array operations.