### Method of solving recurrences for the notes of the Unit 8 - Recurrence Relation & Generating function in the subject of Discrete Structures & Theory of Logic.

Recurrences are equations that describe the relationship between the current value of a function and its previous values. They are often used to analyze the performance of algorithms and to model real-world phenomena. Solving recurrences involves finding an explicit formula for the function in terms of its initial values and any other relevant parameters. In this unit, we will learn about different methods for solving recurrences.

#### The substitution method

The substitution method involves guessing the form of the solution and then proving it by induction. This method is useful for solving linear recurrences with constant coefficients. The steps involved in this method are:

1. Guess the form of the solution.
2. Prove the correctness of the guess by induction.
3. Find the values of any constants in the solution using the initial conditions.

#### The recursion tree method

The recursion tree method is a visual way of solving recurrences. This method is useful for recurrences that can be represented as a tree. The steps involved in this method are:

1. Draw the recursion tree.
2. Calculate the cost of each level of the tree.
3. Sum the costs of all the levels to get the total cost.

#### The master theorem

The master theorem is a general method for solving recurrences of the form T(n) = aT(n/b) + f(n), where a >= 1, b > 1, and f(n) is a given function. The master theorem provides a formula for T(n) in terms of a, b, and f(n). The steps involved in this method are:

1. Determine the values of a, b, and f(n) for the given recurrence.
2. Compare f(n) to n^(log_b(a)) to determine the case of the master theorem.
3. Use the formula for the case of the master theorem to find an asymptotic bound for T(n).

#### Generating functions

Generating functions are a powerful tool for solving recurrences. They allow us to transform a sequence into a function and then manipulate the function to obtain information about the sequence. The steps involved in this method are:

1. Define the generating function for the sequence.
2. Manipulate the generating function using algebraic operations to obtain a closed form expression for the generating function.
3. Use the inverse transform to obtain a closed form expression for the sequence.

In conclusion, solving recurrences is an important part of discrete mathematics and has many applications in computer science and other fields. The methods discussed in this unit provide powerful tools for analyzing algorithms and modeling real-world phenomena. By mastering these methods, you will be well-equipped to tackle a wide range of problems in discrete structures and the theory of logic.