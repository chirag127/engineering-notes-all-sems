## 31. WAP to compare the contents of two files and determine whether they are same or not.

- A possible algorithm to compare the contents of two files and determine whether they are same or not is:

  - Open both files in read mode.
  - Initialize a variable `flag` to `True`.
  - Loop until the end of either file is reached:
    - Read a line from each file and store them in variables `line1` and `line2`.
    - If `line1` is not equal to `line2`, set `flag` to `False` and break the loop.
  - Close both files.
  - If `flag` is `True`, print "The files are same." Otherwise, print "The files are different."

- A possible implementation of this algorithm in Python is:

```python
# Open both files in read mode
file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

# Initialize a variable flag to True
flag = True

# Loop until the end of either file is reached
while True:
  # Read a line from each file and store them in variables line1 and line2
  line1 = file1.readline()
  line2 = file2.readline()

  # If line1 is not equal to line2, set flag to False and break the loop
  if line1 != line2:
    flag = False
    break

  # If the end of either file is reached, break the loop
  if line1 == "" or line2 == "":
    break

# Close both files
file1.close()
file2.close()

# If flag is True, print "The files are same." Otherwise, print "The files are different."
if flag:
  print("The files are same.")
else:
  print("The files are different.")
```