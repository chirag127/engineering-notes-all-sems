### Method of solving recurrences

Recurrence relations are equations that describe a sequence of values in terms of their previous values. They are commonly used in computer science, mathematics, and other fields to model the behavior of systems that change over time. There are several methods for solving recurrence relations, including:

1. **Substitution method**: This method involves guessing the form of the solution and then using mathematical induction to prove that the guess is correct. This method can be effective for simple recurrence relations, but it can be difficult to guess the correct form of the solution for more complex recurrences.

2. **Recursion tree method**: This method involves drawing a tree to represent the recursive calls made by the recurrence relation. The tree can then be used to derive an upper or lower bound on the solution. This method is particularly useful for analyzing the time complexity of recursive algorithms.

3. **Master theorem**: The master theorem provides a way to solve recurrence relations of the form T(n) = aT(n/b) + f(n), where a, b, and f(n) are known functions. This method can be used to quickly determine the asymptotic behavior of the solution.

4. **Generating functions**: Generating functions can be used to represent and solve recurrence relations. This method involves defining a generating function for the sequence of values described by the recurrence relation, and then using algebraic techniques to manipulate the generating function to find a closed-form solution.

These are some of the common methods for solving recurrence relations. The appropriate method to use depends on the specific form of the recurrence relation and the desired solution. It is often helpful to try multiple methods to find the most effective approach.