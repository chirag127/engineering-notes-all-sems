### Asymptotic notations: Big Oh, Big Theta and Big Omega

- Asymptotic notations are mathematical tools that help us to analyze the efficiency of an algorithm in terms of its time and space complexity.
- They allow us to compare the performance of different algorithms for the same problem, and to ignore the constant factors and lower-order terms that are insignificant for large inputs.
- There are three main asymptotic notations: Big Oh, Big Theta and Big Omega. They are defined as follows:

#### Big Oh notation
- Big Oh notation, denoted by O(f(n)), represents the upper bound of the time or space complexity of an algorithm. It means that the algorithm will take at most O(f(n)) time or space to execute for any input of size n.
- For example, if an algorithm has a time complexity of O(n^2 + n), it means that the algorithm will take at most n^2 + n steps to complete for any input of size n. We can ignore the lower-order term n and the constant factor 1, and say that the algorithm is O(n^2) in the worst case.
- To prove that an algorithm is O(f(n)), we need to find a constant c and a value n0 such that for all n >= n0, the algorithm takes at most c * f(n) steps to complete.

#### Big Theta notation
- Big Theta notation, denoted by Θ(f(n)), represents the tight bound of the time or space complexity of an algorithm. It means that the algorithm will take exactly Θ(f(n)) time or space to execute for any input of size n, up to a constant factor.
- For example, if an algorithm has a time complexity of Θ(n^2), it means that the algorithm will take exactly n^2 steps to complete for any input of size n, up to a constant factor. We cannot ignore the lower-order terms or the constant factors, and say that the algorithm is Θ(n^2) in the best, average and worst case.
- To prove that an algorithm is Θ(f(n)), we need to find two constants c1 and c2 and a value n0 such that for all n >= n0, the algorithm takes at least c1 * f(n) and at most c2 * f(n) steps to complete.

#### Big Omega notation
- Big Omega notation, denoted by Ω(f(n)), represents the lower bound of the time or space complexity of an algorithm. It means that the algorithm will take at least Ω(f(n)) time or space to execute for any input of size n.
- For example, if an algorithm has a time complexity of Ω(n^2), it means that the algorithm will take at least n^2 steps to complete for any input of size n. We can ignore the lower-order terms and the constant factors, and say that the algorithm is Ω(n^2) in the best case.
- To prove that an algorithm is Ω(f(n)), we need to find a constant c and a value n0 such that for all n >= n0, the algorithm takes at least c * f(n) steps to complete.