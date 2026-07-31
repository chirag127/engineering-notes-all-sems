### 12. Write a program to perform loop unrolling.

Loop unrolling is a technique used in computer programming to optimize the performance of loops. It involves reducing the number of iterations required to execute a loop by executing multiple loop iterations in a single iteration. This technique can improve the performance of loops by reducing the overhead associated with loop control.

Here's how you can write a program to perform loop unrolling:

1. Define a loop with a fixed number of iterations.
2. Determine the number of iterations that can be executed in a single iteration of the loop. This will depend on the number of available processor resources and the complexity of the loop body.
3. Replace the loop with a series of statements that execute the loop body for the determined number of iterations.
4. Repeat steps 2 and 3 until the loop is completely unrolled.
5. Test the program to ensure that it produces the correct results.

Here's an example of a loop that can be unrolled:

```python
for i in range(0, 10):
    print(i)
```

To unroll this loop, we can determine that it can be unrolled by two iterations per loop. Here's the unrolled version:

```python
for i in range(0, 10, 2):
    print(i)
    print(i+1)
```

In this version of the loop, we have unrolled the loop by two iterations per loop. This means that the loop body is executed twice per loop iteration, which reduces the overhead associated with loop control.

Loop unrolling can be a powerful technique for optimizing the performance of loops, but it should be used with caution. Unrolling loops too much can lead to code that is difficult to read and maintain, and can even reduce performance due to increased cache misses and instruction cache pressure. It is important to carefully analyze the loop and determine the optimal unrolling factor for each loop.