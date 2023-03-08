## Unit 5 - Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi

- Iterators and recursion are two concepts that are related to loops and functions in Python.
- An iterator is an object that can be iterated over, meaning that you can traverse through all the values. For example, a list, a tuple, a string, a dictionary, a set, etc. are all iterators.
- A recursion is a technique of defining a function that calls itself within its body. For example, a function that calculates the factorial of a number by multiplying it with the factorial of its previous number is a recursive function.
- Recursion and iteration can be used to solve the same problems, but they have different advantages and disadvantages.
- Recursion is simpler and more elegant than iteration, but it is also slower and less memory-efficient. Recursion can cause stack overflow errors if the depth of recursion exceeds the limit set by the Python interpreter (default is 1000).
- Iteration is faster and more memory-efficient than recursion, but it is also more complex and less elegant. Iteration requires explicit looping statements and variables to keep track of the state.

### Recursive Fibonacci

- The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding numbers. The first two numbers are 1 and 1. For example, the first 10 numbers of the Fibonacci sequence are: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.
- The Fibonacci sequence can be implemented using recursion as follows:

```python
# Define a recursive function to calculate the nth Fibonacci number
def fibonacci(n):
  # Base case: the first and second Fibonacci numbers are 1
  if n == 1 or n == 2:
    return 1
  # Recursive case: the nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Test the function
print(fibonacci(10)) # 55
```

- The recursive function calls itself with smaller values of n until it reaches the base case, where it returns 1. Then, it adds up the returned values from the previous calls to get the final result.
- The drawback of this recursive approach is that it is very inefficient, as it repeats the same calculations many times. For example, to calculate fibonacci(5), it needs to calculate fibonacci(4) and fibonacci(3), but to calculate fibonacci(4), it also needs to calculate fibonacci(3) and fibonacci(2), and so on. This leads to an exponential growth of function calls, which consumes a lot of time and memory.

### Tower of Hanoi

- The Tower of Hanoi is a mathematical puzzle that consists of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.
- The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
  - Only one disk can be moved at a time.
  - Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
  - No disk may be placed on top of a smaller disk.
- The Tower of Hanoi puzzle can be solved using recursion as follows:

```python
# Define a recursive function to move n disks from source rod to destination rod using auxiliary rod
def tower_of_hanoi(n, source, destination, auxiliary):
  # Base case: if there is only one disk, move it from source to destination
  if n == 1:
    print(f"Move disk 1 from {source} to {destination}")
    return
  # Recursive case: move n-1 disks from source to auxiliary, then move the last disk from source to destination, then move n-1 disks from auxiliary to destination
  else:
    tower_of_hanoi(n-1, source, auxiliary, destination) # move n-1 disks from source to auxiliary
    print(f"Move disk {n} from {source} to {destination}") # move the last disk from source to destination
    tower_of_hanoi(n-1, auxiliary, destination, source) # move n-1 disks from auxiliary to destination

# Test the function
tower_of_hanoi(3, 'A

Okay, I will try to include some mnemonics and learning tricks for the topic that are easy to remember.

### Mnemonics and learning tricks for recursive Fibonacci

- One way to remember the recursive formula for the Fibonacci sequence is to use the acronym FIB: F(n) = F(n-1) + F(n-2).
- Another way to remember the recursive formula is to use the rhyme: "One and one are two, add the last and you get new".
- A visual way to remember the Fibonacci sequence is to draw a spiral using squares whose side lengths are the Fibonacci numbers. For example, start with a 1x1 square, then attach another 1x1 square to its right, then a 2x2 square below, then a 3x3 square to the left, and so on. The spiral will approximate the golden ratio, which is related to the Fibonacci sequence.

### Mnemonics and learning tricks for Tower of Hanoi

- One way to remember the recursive algorithm for the Tower of Hanoi is to use the acronym TOH: TOH(n, source, destination, auxiliary) = TOH(n-1, source, auxiliary, destination) + move disk n from source to destination + TOH(n-1, auxiliary, destination, source).
- Another way to remember the recursive algorithm is to use the phrase: "Move the top to the middle, move the bottom to the end, move the middle to the end".
- A visual way to remember the Tower of Hanoi is to use a diagram that shows the state of the rods and disks after each move. For example, for n=3, the diagram would look like this:

```
    |           |           |         |           |           |         |           |           |
   ( )          |           |        ( )          |           |        ( )         ( )          |
  (   )         |           |       (   )         |           |       (   )        (   )         |
 (     )        |           |      (     )       ( )          |      (     )       (     )       ( )
========   ========   ========   ========   ========   ========   ========   ========   ========
  A         B         C         A         B         C         A         B         C         A
```

- A logical way to remember the Tower of Hanoi is to use the following rules:
  - The number of moves required to solve the puzzle is 2^n - 1, where n is the number of disks.
  - The smallest disk always moves in the same direction, either clockwise or counterclockwise, depending on the parity of n.
  - The next disk to move is always the one that is not on the same rod as the smallest disk or its destination rod.