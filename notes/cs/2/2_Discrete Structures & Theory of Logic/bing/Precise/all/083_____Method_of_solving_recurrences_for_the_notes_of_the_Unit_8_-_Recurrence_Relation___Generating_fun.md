### Method of solving recurrences

Recurrence relations are equations that describe a sequence of values in terms of their previous values. They are commonly used in the analysis of algorithms, where the running time of an algorithm is expressed as a function of its input size. There are several methods for solving recurrence relations, including:

1. **Substitution method:** This method involves guessing the form of the solution and then using mathematical induction to prove that the guess is correct. The guess is usually based on the form of the recurrence relation and the initial conditions.

2. **Recursion tree method:** This method involves drawing a tree to represent the recursive calls made by the algorithm, and then using the tree to derive a bound on the running time of the algorithm.

3. **Master theorem:** This is a powerful tool for solving recurrences of the form T(n) = aT(n/b) + f(n), where a, b, and f(n) are constants. The master theorem provides a formula for the asymptotic behavior of the solution, based on the values of a, b, and f(n).

4. **Generating functions:** This method involves representing the sequence of values as a power series, and then using techniques from calculus to manipulate the power series to derive a closed-form solution for the sequence.

These are some of the common methods for solving recurrence relations. The appropriate method to use depends on the specific form of the recurrence relation and the desired level of accuracy for the solution. It is important to have a good understanding of these methods in order to effectively analyze the running time of algorithms.