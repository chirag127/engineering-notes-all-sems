## 22.WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them.

Here's a Python code for 22.WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them.
```
def sum_arrays(arr1, arr2):
  result = []
  for i in range(len(arr1)):
    result.append(arr1[i] + arr2[i])
  return result

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
result = sum_arrays(arr1, arr2)
print(result)
```
