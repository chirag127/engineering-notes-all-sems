# Counting Techniques for the notes of the Unit 9 - Combinatorics in the subject of Discrete Structures & Theory of Logic

Combinatorics is the branch of mathematics that deals with the study of finite or countable discrete structures. It includes the enumeration or counting of objects having certain properties, such as arrangements, combinations, permutations, partitions, and selections. Combinatorics methods can be used to solve various problems in computer science, cryptography, probability, graph theory, and algebra.

There are different counting techniques that can be used to count the number of objects in a set or the number of ways to perform a task. Some of the basic counting techniques are:

- **The product rule**: This rule states that if there are $n_1$ ways to do the first task, $n_2$ ways to do the second task, ..., and $n_k$ ways to do the kth task, then there are $n_1 \times n_2 \times ... \times n_k$ ways to do all the tasks in sequence. For example, if there are 10 shirts and 8 pants to choose from, then there are $10 \times 8 = 80$ ways to choose a shirt and a pant.

- **The sum rule**: This rule states that if there are $n_1$ ways to do the first task, $n_2$ ways to do the second task, ..., and $n_k$ ways to do the kth task, and these tasks are mutually exclusive (i.e. they cannot be done at the same time), then there are $n_1 + n_2 + ... + n_k$ ways to do one of the tasks. For example, if there are 5 apples, 4 oranges, and 3 bananas to choose from, then there are $5 + 4 + 3 = 12$ ways to choose one fruit.

- **The factorial**: This is a special notation that represents the product of all positive integers from 1 to a given number. It is denoted by $n!$ and defined as $n! = n \times (n-1) \times ... \times 2 \times 1$. For example, $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$. The factorial can be used to count the number of ways to arrange $n$ distinct objects in a row, which is $n!$. For example, there are $5! = 120$ ways to arrange 5 books on a shelf.

- **The permutation**: This is a way of counting the number of ways to select and arrange $r$ objects from a set of $n$ distinct objects, where the order matters. It is denoted by $P(n,r)$ or $_n P_r$ and defined as $P(n,r) = n! / (n-r)!$. For example, there are $P(5,3) = 5! / (5-3)! = 60$ ways to select and arrange 3 books from 5 books on a shelf.

- **The combination**: This is a way of counting the number of ways to select $r$ objects from a set of $n$ distinct objects, where the order does not matter. It is denoted by $C(n,r)$ or $_n C_r$ or ${n \choose r}$ and defined as $C(n,r) = n! / (r! \times (n-r)!)$. For example, there are $C(5,3) = 5! / (3! \times (5-3)!) = 10$ ways to select 3 books from 5 books on a shelf.

These are some of the basic counting techniques that can be used to solve combinatorics problems. There are also other advanced techniques, such as the inclusion-exclusion principle, the binomial theorem, the pigeonhole principle, and the principle of mathematical induction, that can be used to count more complex situations.