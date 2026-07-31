## 22.WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them.

- A WAP (write a program) is a task that requires writing code in a specific programming language to achieve a desired output or functionality.
- An array is a data structure that stores a collection of elements of the same type in a contiguous memory location.
- To input two arrays, we need to declare and initialize them with some values, or use a loop to read the values from the user or a file.
- To save the sum of corresponding elements of these arrays in a third array, we need to create a new array of the same size as the input arrays, and use another loop to iterate over the elements and add them together.
- To print the third array, we need to use a print statement or a function that displays the elements of the array on the screen or a file.

- Here is an example of a WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them in Python:

```python
# Declare and initialize two arrays of size 5
array1 = [1, 2, 3, 4, 5]
array2 = [6, 7, 8, 9, 10]

# Create a new array of size 5
array3 = [0] * 5

# Loop over the elements of the arrays and add them together
for i in range(5):
  array3[i] = array1[i] + array2[i]

# Print the third array
print(array3)
```

- The output of this program is:

```python
[7, 9, 11, 13, 15]
```