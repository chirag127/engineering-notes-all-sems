### Analyzing Algorithms

- Analyzing algorithms is the process of finding the **computational complexity** of algorithms, which is the amount of time, storage, or other resources needed to execute them .
- The computational complexity of an algorithm is usually expressed as a **function** of the length or size of its input, such as `n` or `N`.
- The most common measures of computational complexity are **time complexity** and **space complexity**, which indicate how the running time or memory usage of an algorithm grows as the input size increases.
- Time complexity is often denoted by `T(n)` or `O(f(n))`, where `f(n)` is some function of `n` that bounds the worst-case or average-case running time of the algorithm.
- Space complexity is often denoted by `S(n)` or `O(g(n))`, where `g(n)` is some function of `n` that bounds the worst-case or average-case memory usage of the algorithm.
- The notation `O(f(n))` is called **Big O notation**, and it represents the **upper bound** or **asymptotic upper bound** of the complexity of an algorithm. It means that the algorithm's complexity is at most proportional to `f(n)` for sufficiently large `n`.
- Similarly, the notation `Ω(g(n))` is called **Big Omega notation**, and it represents the **lower bound** or **asymptotic lower bound** of the complexity of an algorithm. It means that the algorithm's complexity is at least proportional to `g(n)` for sufficiently large `n`.
- The notation `Θ(h(n))` is called **Big Theta notation**, and it represents the **tight bound** or **asymptotic tight bound** of the complexity of an algorithm. It means that the algorithm's complexity is both `O(h(n))` and `Ω(h(n))`, or equivalently, proportional to `h(n)` for sufficiently large `n`.
- Analyzing algorithms is important for several reasons :
  - To **predict** the behavior of an algorithm without implementing it on a specific computer or platform.
  - To **compare** the efficiency of different algorithms for the same problem or task.
  - To **optimize** the performance of an algorithm by choosing the best parameters or data structures.
  - To **verify** the correctness of an algorithm by reasoning formally or mathematically about it.
- Some common techniques for analyzing algorithms are:
  - **Empirical analysis**: Running the algorithm on a set of sample inputs and measuring the actual time or space used.
  - **Theoretical analysis**: Deriving a mathematical expression or formula for the complexity of the algorithm based on its logic and operations.
  - **Amortized analysis**: Averaging the complexity of a sequence of operations over the whole sequence, rather than considering the worst-case or best-case for each operation.
  - **Probabilistic analysis**: Using probability theory or statistics to model the behavior of an algorithm under random or uncertain inputs or events.