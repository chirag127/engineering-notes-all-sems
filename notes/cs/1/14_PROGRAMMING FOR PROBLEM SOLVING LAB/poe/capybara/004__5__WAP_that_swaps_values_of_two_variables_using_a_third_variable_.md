## 5. WAP that swaps values of two variables using a third variable.

Swapping values of two variables can be achieved using a third variable. Here is how it can be done:

1. Declare three variables - A, B and C.
2. Assign values to A and B.
3. Print the values of A and B before swapping.
4. Assign the value of A to C.
5. Assign the value of B to A.
6. Assign the value of C to B.
7. Print the values of A and B after swapping.

### Example

```python
# declaring variables
A = 10
B = 20
C = 0

# printing values before swapping
print("Before swapping:")
print("A =", A)
print("B =", B)

# swapping values
C = A
A = B
B = C

# printing values after swapping
print("After swapping:")
print("A =", A)
print("B =", B)
```

Output:

```
Before swapping:
A = 10
B = 20
After swapping:
A = 20
B = 10
```

Note that in the above example, we have assigned the value of A to C, then assigned the value of B to A, and then assigned the value of C to B. This way, the values of A and B are swapped using the third variable C. 

Swapping values of two variables is a common programming task and this method is used frequently. It is important to understand the logic behind it and practice it to become proficient in programming.