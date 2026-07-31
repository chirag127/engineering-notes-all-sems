## 21. WAP that simply takes elements of the array from the user and finds the sum of these elements.

Here is an example of a program that takes elements of an array from the user and finds the sum of these elements:

```python
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

sum = 0
for i in arr:
    sum += i

print("The sum of the elements in the array is:", sum)
```

- This program first takes the number of elements in the array as input from the user.
- Then, it takes the elements of the array as input from the user using a for loop.
- The elements are appended to the `arr` list.
- The program then calculates the sum of the elements in the array using another for loop.
- Finally, the sum is printed to the screen.

This is a simple program that demonstrates how to take elements of an array from the user and find the sum of these elements. You can modify this program to suit your needs.