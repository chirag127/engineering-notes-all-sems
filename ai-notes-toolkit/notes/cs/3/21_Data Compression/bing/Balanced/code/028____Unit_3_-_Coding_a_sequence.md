## Unit 3 - Coding a sequence

A sequence is a set of ordered items that follow a certain pattern or rule. For example, the sequence of even numbers is 2, 4, 6, 8, and so on. The sequence of Fibonacci numbers is 1, 1, 2, 3, 5, 8, and so on.

To code a sequence, we need to:

- Define a starting value or a base case. This is the first item in the sequence.
- Define a recursive rule or a formula. This is how we get the next item in the sequence from the previous one or ones.
- Define a stopping condition or a boundary. This is when we stop generating the sequence.

For example, to code the sequence of even numbers, we can use the following pseudocode:

```
# Define the starting value
n = 2

# Define the recursive rule
n = n + 2

# Define the stopping condition
while n < 100
  print n
end
```

This code will print the even numbers from 2 to 98.

To code the sequence of Fibonacci numbers, we can use the following pseudocode:

```
# Define the starting values
a = 1
b = 1

# Define the recursive rule
c = a + b
a = b
b = c

# Define the stopping condition
while a < 100
  print a
end
```

This code will print the Fibonacci numbers from 1 to 89.