### Counting Techniques for the notes of the Unit 9 - Combinatorics in the subject of Discrete Structures & Theory of Logic

Combinatorics is the branch of mathematics that deals with the study of finite or countable discrete structures. It includes the enumeration or counting of objects having certain properties, such as arrangements, combinations, permutations, partitions, etc. Combinatorics is useful for solving problems in computer science, cryptography, probability, and algebra.

Some of the basic counting techniques are:

- **The product rule**: This rule states that if there are $n_1$ ways to do one thing, and $n_2$ ways to do another thing, then there are $n_1 \times n_2$ ways to do both things. For example, if there are 10 different shirts and 8 different pants to choose from, then there are $10 \times 8 = 80$ ways to choose an outfit.

- **The sum rule**: This rule states that if there are $n_1$ ways to do one thing, and $n_2$ ways to do another thing, and these two things cannot be done at the same time, then there are $n_1 + n_2$ ways to do either one of them. For example, if there are 5 different books and 7 different magazines to read, and you can only read one at a time, then there are $5 + 7 = 12$ ways to choose something to read.

- **The factorial**: This is a notation that represents the product of all positive integers from 1 to a given number. It is denoted by $n!$, where $n$ is a positive integer. For example, $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$. The factorial is useful for counting the number of ways to arrange $n$ distinct objects in a row, which is $n!$.

- **The permutation**: This is a way of counting the number of ways to arrange $r$ out of $n$ distinct objects in a row, where the order matters. It is denoted by $P(n,r)$ or $_n P_r$, and it is equal to $\frac{n!}{(n-r)!}$. For example, the number of ways to arrange 3 out of 5 letters A, B, C, D, E in a row is $P(5,3) = \frac{5!}{(5-3)!} = \frac{120}{2} = 60$.

- **The combination**: This is a way of counting the number of ways to choose $r$ out of $n$ distinct objects, where the order does not matter. It is denoted by $C(n,r)$ or $_n C_r$ or ${n \choose r}$, and it is equal to $\frac{n!}{r!(n-r)!}$. For example, the number of ways to choose 3 out of 5 letters A, B, C, D, E is $C(5,3) = \frac{5!}{3!(5-3)!} = \frac{120}{6 \times 2} = 10$.

- **The binomial theorem**: This is a formula that gives the expansion of $(x+y)^n$, where $n$ is a non-negative integer. It states that $(x+y)^n = \sum_{r=0}^n {n \choose r} x^{n-r} y^r$, where ${n \choose r}$ are the binomial coefficients. For example, $(x+y)^3 = {3 \choose 0} x^3 y^0 + {3 \choose 1} x^2 y^1 + {3 \choose 2} x^1 y^2 + {3 \choose 3} x^0 y^3 = x^3 + 3x^2y + 3xy^2 + y^3$. The binomial theorem is useful for counting the number of ways to obtain a certain outcome in a repeated experiment, such as tossing a coin or rolling a die.

- **The inclusion-exclusion principle**: This is a way of counting the number of elements in a union of sets, by subtracting the number of elements in the intersections of the sets. It states that $|A \cup B| = |A| + |B| - |A \cap B|$, where $|A|$ denotes