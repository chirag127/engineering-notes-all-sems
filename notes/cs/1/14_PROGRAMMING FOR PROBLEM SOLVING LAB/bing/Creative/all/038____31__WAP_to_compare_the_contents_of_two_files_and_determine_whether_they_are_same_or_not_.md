## 31. WAP to compare the contents of two files and determine whether they are same or not.

- To compare the contents of two files and determine whether they are same or not, we can use the following algorithm:
  - Open both files in read mode.
  - Initialize a flag variable to True.
  - Loop through the lines of both files simultaneously using a zip function.
  - Compare each line of the first file with the corresponding line of the second file using the == operator.
  - If any line does not match, set the flag to False and break the loop.
  - Close both files.
  - Return the flag value as the result of the comparison.
- Here is an example of a Python program that implements this algorithm:

```python
# Define a function to compare two files
def compare_files(file1, file2):
  # Open both files in read mode
  f1 = open(file1, "r")
  f2 = open(file2, "r")
  # Initialize a flag variable to True
  flag = True
  # Loop through the lines of both files simultaneously
  for line1, line2 in zip(f1, f2):
    # Compare each line of the first file with the corresponding line of the second file
    if line1 != line2:
      # If any line does not match, set the flag to False and break the loop
      flag = False
      break
  # Close both files
  f1.close()
  f2.close()
  # Return the flag value as the result of the comparison
  return flag

# Test the function with two sample files
file1 = "sample1.txt"
file2 = "sample2.txt"
result = compare_files(file1, file2)
if result:
  print("The files are same.")
else:
  print("The files are different.")
```