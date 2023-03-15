# Counting Techniques for the notes of the Unit 9 - Combinatorics in the subject of Discrete Structures & Theory of Logic

- Combinatorics is the branch of mathematics that deals with the study of finite or countable discrete structures, such as sets, graphs, permutations, combinations, etc. 
- Combinatorics helps us to count the number of objects in a set quickly, to estimate the complexity of algorithms, to solve problems in discrete probability, and to analyze various combinatorial structures.  
- Counting techniques are the methods that we use to find the number of possible outcomes or arrangements of a given situation or problem. 
- Some of the basic counting techniques are:

  - The Rule of Products: If there are $n_1$ ways to do task 1, and $n_2$ ways to do task 2, and so on, then there are $n_1 \times n_2 \times \cdots \times n_k$ ways to do all the tasks in sequence. 
  - The Rule of Sums: If there are $n_1$ ways to do task 1, and $n_2$ ways to do task 2, and so on, and the tasks are mutually exclusive, then there are $n_1 + n_2 + \cdots + n_k$ ways to do any one of the tasks. 
  - The Rule of Exponents: If there are $n$ ways to do a task, and the task is repeated $k$ times, then there are $n^k$ ways to do the task $k$ times. 
  - Factorials: The number of ways to arrange $n$ distinct objects in a row is $n! = n \times (n-1) \times \cdots \times 2 \times 1$. 
  - Permutations: The number of ways to choose and arrange $k$ objects out of $n$ distinct objects is $P(n,k) = n!/(n-k)!$. 
  - Combinations: The number of ways to choose $k$ objects out of $n$ distinct objects, without regard to order, is $C(n,k) = n!/(k!(n-k)!)$. 
  - Binomial Coefficients: The number of ways to choose $k$ objects out of $n$ identical objects, without regard to order, is ${n \choose k} = (n+k-1)!/(k!(n-1)!)$. 
  - Generalized Permutations and Combinations: The number of ways to choose and arrange $k$ objects out of $n$ objects, where some of the objects are identical, is $P(n,k) = n!/(n_1!n_2!\cdots n_r!)$, where $n_1, n_2, \cdots, n_r$ are the number of identical objects of each type. The number of ways to choose $k$ objects out of $n$ objects, where some of the objects are identical, without regard to order, is $C(n,k) = (n+k-1)!/(n_1!n_2!\cdots n_r!k!)$, where $n_1, n_2, \cdots, n_r$ are the number of identical objects of each type. 
  - The Pigeonhole Principle: If $n$ objects are placed into $k$ boxes, where $n > k$, then there is at least one box that contains more than one object. 

- Some examples of counting problems are:

  - How many different license plates can be made using three letters followed by three digits? 
    - Answer: By the rule of products, there are $26 \times 26 \times 26 \times 10 \times 10 \times 10 = 17576000$ ways.
  - How many different ways can a committee of 5 people be chosen from a group of 10 people? 
    - Answer: By the formula for combinations, there are $C(10,5) = 10!/(5!5!) = 252$ ways.
  - How many different ways can 10 balls be distributed