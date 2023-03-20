 Here is the content in markdown format without any external links or emojis:

## Unit 5 - Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi

### Recursive Fibonacci

1. Fibonacci sequence is a series of numbers where each number is the sum of the previous two numbers.
2. The first two Fibonacci numbers are 0 and 1.
3. To calculate the nth Fibonacci number, we need to recursively call the function for n-1 and n-2 positions and add the results.
4. The base cases are:
 fib(0) = 0
 fib(1) = 1
5. The recursive step is:
 fib(n) = fib(n-1) + fib(n-2)

### Tower of Hanoi

1. Tower of Hanoi is a mathematical puzzle where we have to move all disks from one rod to another rod while following certain rules.
2. There are three rods and a number of disks of different sizes.
3. The rules are:
 - Only one disk can be moved at a time.
 - A larger disk cannot be placed on top of a smaller disk.
4. To solve the puzzle, we need to make recursive function calls where in each call, the steps are:
 - Move n-1 disks from the first rod to the third rod.
 - Move the nth disk from the first rod to the second rod.
 - Move the n-1 disks from the third rod to the second rod.

The content is written in a formal tone as a study material without any emojis or external links in markdown format with points. Please let me know if you would like me to modify or add anything.