## 22. WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them.

Here is an example of a program that inputs two arrays and saves the sum of corresponding elements of these arrays in a third array and prints them:

```python
# Input the length of the arrays
n = int(input("Enter the length of the arrays: "))

# Initialize the arrays
arr1 = [0] * n
arr2 = [0] * n
arr3 = [0] * n

# Input the elements of the first array
print("Enter the elements of the first array: ")
for i in range(n):
    arr1[i] = int(input())

# Input the elements of the second array
print("Enter the elements of the second array: ")
for i in range(n):
    arr2[i] = int(input())

# Calculate the sum of corresponding elements and store in the third array
for i in range(n):
    arr3[i] = arr1[i] + arr2[i]

# Print the third array
print("The third array is: ")
for i in range(n):
    print(arr3[i])
```

This program first inputs the length of the arrays and initializes them. Then, it inputs the elements of the first and second arrays. After that, it calculates the sum of corresponding elements of the first and second arrays and stores the result in the third array. Finally, it prints the third array.