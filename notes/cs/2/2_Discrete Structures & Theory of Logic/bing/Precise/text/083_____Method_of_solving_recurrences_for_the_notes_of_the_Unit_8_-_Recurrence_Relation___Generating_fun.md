### Method of solving recurrences for the notes of the Unit 8 - Recurrence Relation & Generating function in the subject of Discrete Structures & Theory of Logic

1. **Substitution Method:** In this method, we make a guess for the solution and then use mathematical induction to prove the guess is correct or incorrect.
2. **Recursion Tree Method:** This method is useful for solving recurrences of the form T(n) = aT(n/b) + f(n) where a >= 1 and b > 1. We draw a recursion tree to represent the cost of each level of the recursion and then sum the costs of all levels to determine the total cost of the algorithm.
3. **Master Theorem:** This theorem provides a way to solve recurrences of the form T(n) = aT(n/b) + f(n) where a >= 1 and b > 1. It provides asymptotic upper and lower bounds for the recurrence.
4. **Generating Functions:** This method involves representing the sequence defined by the recurrence relation as a power series and then manipulating the series to find a closed-form solution for the sequence.
