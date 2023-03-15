# Asymptotic notations: Big Oh, Big Theta and Big Omega

- Asymptotic notations are mathematical tools that help us analyze the efficiency of an algorithm in terms of its running time and space usage.
- They allow us to express the growth rate of a function that represents the time or space complexity of an algorithm, as the input size approaches infinity.
- They also help us compare different algorithms and choose the best one for a given problem.
- There are three common asymptotic notations: Big Oh, Big Theta and Big Omega.

## Big Oh notation

- Big Oh notation, denoted by O(f(n)), is used to describe the upper bound of a function, or the worst-case scenario of an algorithm.
- It means that the function is at most proportional to f(n), or grows slower than or equal to f(n), as n approaches infinity.
- For example, if the time complexity of an algorithm is O(n^2), it means that the algorithm takes at most n^2 steps to complete, where n is the input size.
- To find the Big Oh of a function, we can ignore the lower-order terms and the constant factors, as they become insignificant as n grows large.
- For example, 3n^2 + 5n + 2 is O(n^2), because the n^2 term dominates the other terms as n increases.

## Big Theta notation

- Big Theta notation, denoted by Θ(f(n)), is used to describe the tight bound of a function, or the average-case scenario of an algorithm.
- It means that the function is both O(f(n)) and Ω(f(n)), or grows exactly as f(n), as n approaches infinity.
- For example, if the time complexity of an algorithm is Θ(n log n), it means that the algorithm takes exactly n log n steps to complete, where n is the input size.
- To find the Big Theta of a function, we can use the same method as Big Oh, but we have to make sure that the function is bounded both above and below by f(n).
- For example, 2n^2 + 3n is Θ(n^2), because it is both O(n^2) and Ω(n^2).

## Big Omega notation

- Big Omega notation, denoted by Ω(f(n)), is used to describe the lower bound of a function, or the best-case scenario of an algorithm.
- It means that the function is at least proportional to f(n), or grows faster than or equal to f(n), as n approaches infinity.
- For example, if the time complexity of an algorithm is Ω(n), it means that the algorithm takes at least n steps to complete, where n is the input size.
- To find the Big Omega of a function, we can ignore the higher-order terms and the constant factors, as they become insignificant as n grows large.
- For example, n^3 + 2n is Ω(n^3), because the n^3 term dominates the other terms as n increases.