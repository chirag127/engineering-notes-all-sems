# 3. Running Python Programs on Raspberry Pi

One of the programs that can be run on a Raspberry Pi using Python is printing a name 'n' times, where the name and the value of 'n' are read from standard input. Here is an example of how this can be done:

```python
name = input("Enter a name: ")
n = int(input("Enter the number of times to print the name: "))

for i in range(n):
    print(name)
```

In this program, the `input()` function is used to read the name and the value of 'n' from the user. The `int()` function is used to convert the value of 'n' from a string to an integer. The `for` loop is then used to print the name 'n' times.