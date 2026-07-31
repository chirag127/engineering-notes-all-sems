### Method of solving recurrences

Recurrences are equations that describe the running time or complexity of an algorithm in terms of its input size and smaller subproblems. For example, the recurrence for the merge sort algorithm is:

T(n) = 2T(n/2) + n

There are different methods of solving recurrences, such as:

- **Substitution method**: This method involves guessing the form of the solution and then using mathematical induction to prove that the guess is correct or incorrect. For example, to solve the recurrence above, we can guess that T(n) = O(n log n) and then use induction to show that this is true for all n >= 1  .
- **Iteration method**: This method involves expanding the recurrence by substituting the values of the smaller subproblems until a pattern emerges. Then, we can use the pattern to find a closed-form expression for the solution. For example, to solve the recurrence above, we can expand it as follows:

T(n) = 2T(n/2) + n
     = 2(2T(n/4) + n/2) + n
     = 4T(n/4) + 2n
     = 4(2T(n/8) + n/4) + 2n
     = 8T(n/8) + 3n
     = ...
     = 2^k T(n/2^k) + kn

If we let k = log n, then we get:

T(n) = 2^(log n) T(n/2^(log n)) + n log n
     = n T(1) + n log n
     = O(n log n)

- **Master method**: This method is a shortcut for solving recurrences of the form:

T(n) = aT(n/b) + f(n)

where a, b, and f(n) are constants or functions of n. The master method provides three cases that cover different scenarios of how f(n) compares to n^(log_b a). Depending on the case, the solution will be either O(n^(log_b a)), O(f(n)), or O(f(n) log n). For example, to solve the recurrence above, we can apply the master method as follows:

T(n) = 2T(n/2) + n

Here, a = 2, b = 2, and f(n) = n. We can see that f(n) = O(n^(log_2 2)) = O(n), which falls into the second case of the master method. Therefore, the solution is T(n) = O(f(n)) = O(n).

- **Akra-Bazzi method**: This method is a generalization of the master method that can handle recurrences of the form:

T(n) = g(n) + a_1 T(n/b_1) + a_2 T(n/b_2) + ... + a_k T(n/b_k)

where g(n) is a function of n, and a_i, b_i are positive constants for i = 1, 2, ..., k. The Akra-Bazzi method involves finding a value of p such that:

a_1 (n/b_1)^p + a_2 (n/b_2)^p + ... + a_k (n/b_k)^p = n^p

and then using the formula:

T(n) = O(n^p (1 + integral of g(x)/x^(p+1) from 1 to n))

to find the solution. For example, to solve the recurrence:

T(n) = 2T(n/3) + T(n/6) + n

we can apply the Akra-Bazzi method as follows:

Here, g(n) = n, a_1 = 2, b_1 = 3, a_2 = 1, b_2 = 6. We can find p by solving:

2 (n/3)^p + 1 (n/6)^p = n^p

which gives p = 1. Then, we can use the formula:

T(n) = O(n^1 (1 + integral of n/x^2 from 1 to n))
     = O(n (1 + n/2 - 1/2))
     = O(n^2)