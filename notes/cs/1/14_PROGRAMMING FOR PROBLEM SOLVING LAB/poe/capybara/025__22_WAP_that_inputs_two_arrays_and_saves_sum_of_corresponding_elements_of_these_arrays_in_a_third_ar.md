## 22. WAP that inputs two arrays and saves the sum of corresponding elements of these arrays in a third array and prints them.

In this program, we will be taking two arrays as input and then adding the corresponding elements of these arrays to create a third array. Finally, we will print the elements of the third array.

Here are the steps to create the program:

1. First, we will declare three arrays - `arr1`, `arr2`, and `sum`.

2. Next, we will take input from the user for the values of the first two arrays `arr1` and `arr2`. We will use a loop to take input for each element of the array.

3. Once we have the two input arrays, we will use another loop to add the corresponding elements of these arrays and store the result in the `sum` array.

4. Finally, we will use a loop to print the elements of the `sum` array.

Here is the code for the program:

```python
# Declare the arrays
arr1 = []
arr2 = []
sum = []

# Take input for arr1
n = int(input("Enter the size of the array: "))
print("Enter the elements of array 1:")
for i in range(n):
    arr1.append(int(input()))

# Take input for arr2
print("Enter the elements of array 2:")
for i in range(n):
    arr2.append(int(input()))

# Add the corresponding elements and store in sum array
for i in range(n):
    sum.append(arr1[i] + arr2[i])

# Print the sum array
print("The sum of corresponding elements of the arrays is:")
for i in range(n):
    print(sum[i])
```

By following these steps, we can create a program that takes two arrays as input, adds the corresponding elements, and prints the sum of the corresponding elements in a third array. This program can be used to solve problems that require adding two arrays.