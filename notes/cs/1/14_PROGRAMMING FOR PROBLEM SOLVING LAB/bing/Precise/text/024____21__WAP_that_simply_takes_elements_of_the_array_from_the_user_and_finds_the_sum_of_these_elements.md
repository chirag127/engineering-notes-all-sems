## 21. WAP that simply takes elements of the array from the user and finds the sum of these elements.

Here is an example of a program that takes elements of an array from the user and finds the sum of these elements:

```python
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

sum = 0
for i in arr:
    sum += i

print("Sum of elements in the array:", sum)
```

- The program starts by taking the number of elements in the array as input from the user.
- An empty list `arr` is initialized to store the elements of the array.
- A for loop is used to take `n` elements as input from the user and append them to the list `arr`.
- A variable `sum` is initialized to 0 to store the sum of the elements in the array.
- Another for loop is used to iterate over the elements in the list `arr` and add them to the variable `sum`.
- Finally, the sum of the elements in the array is printed.
