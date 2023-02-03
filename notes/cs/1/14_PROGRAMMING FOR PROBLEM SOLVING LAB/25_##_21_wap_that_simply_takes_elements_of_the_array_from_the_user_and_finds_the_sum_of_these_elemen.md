## 21. WAP that simply takes elements of the array from the user and finds the sum of these elements.

```
# Python code to find the sum of elements in an array

def sum_array(array):
    return sum(array)

# Input array from user
arr = list(map(int, input("Enter elements of the array separated by space: ").strip().split()))

# Call function to find sum
result = sum_array(arr)

# Print result
print("Sum of elements in the array:", result)
```
