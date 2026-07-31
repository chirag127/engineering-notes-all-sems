## 22. WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them.

Here is a program that takes two arrays as input, calculates the sum of corresponding elements of these arrays, saves the result in a third array, and prints the result:

```python
# input the length of the arrays
n = int(input("Enter the length of the arrays: "))

# initialize the arrays
arr1 = [0] * n
arr2 = [0] * n
arr3 = [0] * n

# input the elements of the first array
print("Enter the elements of the first array: ")
for i in range(n):
    arr1[i] = int(input())

# input the elements of the second array
print("Enter the elements of the second array: ")
for i in range(n):
    arr2[i] = int(input())

# calculate the sum of corresponding elements and save in the third array
for i in range(n):
    arr3[i] = arr1[i] + arr2[i]

# print the result
print("The resulting array is: ")
for i in range(n):
    print(arr3[i], end=" ")
```

This program first takes the length of the arrays as input from the user. Then, it initializes three arrays of the given length with all elements set to 0. Next, it takes the elements of the first and second arrays as input from the user. After that, it calculates the sum of the corresponding elements of the first and second arrays and saves the result in the third array. Finally, it prints the resulting array.