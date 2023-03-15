# Asymptotic notations: Big Oh, Big Theta and Big Omega

- Asymptotic notations are mathematical tools that help us to analyze the efficiency of an algorithm in terms of its time and space complexity.
- They allow us to compare the performance of different algorithms for the same problem, and to ignore the constant factors and lower-order terms that are insignificant for large inputs.
- There are three common asymptotic notations: Big Oh, Big Theta and Big Omega.

## Big Oh notation

- Big Oh notation, denoted by O(f(n)), represents the upper bound of the time or space complexity of an algorithm.
- It means that the algorithm will take at most O(f(n)) time or space to execute for any input of size n.
- For example, if an algorithm has a time complexity of O(n^2 + 3n + 5), it means that the algorithm will take at most n^2 + 3n + 5 steps to complete for any input of size n.
- To simplify the notation, we can drop the lower-order terms and the constant factors, and write the time complexity as O(n^2).
- This is because as n grows large, the n^2 term will dominate the other terms, and the constant factors will not affect the order of growth.
- Big Oh notation gives us an upper bound, but it does not guarantee that the algorithm will always take O(f(n)) time or space. It only means that the algorithm will never take more than O(f(n)) time or space.

## Big Theta notation

- Big Theta notation, denoted by Θ(f(n)), represents the tight bound of the time or space complexity of an algorithm.
- It means that the algorithm will take exactly Θ(f(n)) time or space to execute for any input of size n, within a constant factor.
- For example, if an algorithm has a time complexity of Θ(n^2), it means that the algorithm will take n^2 steps to complete for any input of size n, plus or minus some constant factor.
- Big Theta notation gives us a precise estimate of the algorithm's performance, but it is harder to find than Big Oh notation.
- To prove that an algorithm has a time or space complexity of Θ(f(n)), we need to show that there exist two positive constants c1 and c2 such that c1 * f(n) <= T(n) <= c2 * f(n) for all sufficiently large n, where T(n) is the actual time or space complexity of the algorithm.

## Big Omega notation

- Big Omega notation, denoted by Ω(f(n)), represents the lower bound of the time or space complexity of an algorithm.
- It means that the algorithm will take at least Ω(f(n)) time or space to execute for any input of size n.
- For example, if an algorithm has a time complexity of Ω(n^2), it means that the algorithm will take n^2 steps or more to complete for any input of size n.
- Big Omega notation gives us a lower bound, but it does not guarantee that the algorithm will always take Ω(f(n)) time or space. It only means that the algorithm will never take less than Ω(f(n)) time or space.