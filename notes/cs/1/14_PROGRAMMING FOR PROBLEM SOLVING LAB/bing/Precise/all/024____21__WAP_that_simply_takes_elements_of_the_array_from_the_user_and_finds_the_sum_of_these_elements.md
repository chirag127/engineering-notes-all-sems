## 21. WAP that simply takes elements of the array from the user and finds the sum of these elements.

Here is a program that takes elements of an array from the user and finds the sum of these elements:

```python
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)
sum = 0
for i in arr:
    sum += i
print("The sum of the elements in the array is:", sum)
```

This program first takes the number of elements in the array as input from the user. Then, it takes the elements of the array one by one from the user and stores them in a list. After that, it initializes a variable `sum` to 0 and iterates over the elements of the list, adding each element to the `sum` variable. Finally, it prints the sum of the elements in the array.