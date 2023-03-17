## 21. WAP that simply takes elements of the array from the user and finds the sum of these elements.

Here are some points to consider when writing a program to find the sum of elements in an array:

- First, initialize an empty array to store the user inputted elements.
- Ask the user for the number of elements they want to input.
- Use a loop to iterate through the number of elements and prompt the user to input each element into the array.
- Once all elements are in the array, use another loop to iterate through the array and add up all the elements.
- Store the sum of the elements in a variable.
- Finally, display the sum of the elements to the user.

Here is an example code snippet in Python that accomplishes this task:

```python
# initialize an empty array
arr = []

# ask user for number of elements
n = int(input("Enter number of elements: "))

# iterate through each element and add to array
for i in range(n):
    elem = int(input("Enter element: "))
    arr.append(elem)

# iterate through array and add up elements
sum = 0
for i in range(n):
    sum += arr[i]

# display sum of elements to user
print("The sum of the elements in the array is:", sum)
```

Remember to test your program with different input values to ensure it works correctly.