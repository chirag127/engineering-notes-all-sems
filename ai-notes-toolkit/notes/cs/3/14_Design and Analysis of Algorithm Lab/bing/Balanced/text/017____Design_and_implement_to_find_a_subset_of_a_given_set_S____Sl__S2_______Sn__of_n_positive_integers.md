## Design and implement to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d. For example, if S ={1, 2, 5, 6, 8} and d= 9, there are two solutions {1,2,6}and {1,8}. Display a suitable message, if the given problem instance doesn't have a solution. for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- This problem is an example of the **subset sum problem**, which is a special case of the **knapsack problem**. The subset sum problem is to find a subset of a given set of numbers that adds up to a given target number. The knapsack problem is to find a subset of items with given weights and values that maximizes the total value without exceeding the capacity of the knapsack.
- The subset sum problem is **NP-complete**, which means that there is no known efficient algorithm that can solve it in polynomial time for any input size. However, there are some algorithms that can solve it in **pseudo-polynomial time**, which means that they are polynomial in the input size and the target number. One such algorithm is the **dynamic programming** approach, which uses a two-dimensional array to store the possible sums that can be obtained from the subsets of the input set.
- The dynamic programming algorithm works as follows:
  - Let S = {s1, s2, ..., sn} be the input set of n positive integers, and let d be the target sum.
  - Create a boolean array T[n+1][d+1], where T[i][j] indicates whether there is a subset of {s1, s2, ..., si} that adds up to j.
  - Initialize T[0][0] to true, and T[0][j] to false for all j > 0. This means that the empty set can only add up to zero, and no other sum.
  - For each i from 1 to n, do the following:
    - For each j from 0 to d, do the following:
      - If T[i-1][j] is true, then set T[i][j] to true. This means that if there is a subset of {s1, s2, ..., si-1} that adds up to j, then there is also a subset of {s1, s2, ..., si} that adds up to j, by simply excluding si from the subset.
      - If T[i-1][j] is false, then check if j >= si. If yes, then set T[i][j] to T[i-1][j-si]. This means that if there is a subset of {s1, s2, ..., si-1} that adds up to j-si, then there is also a subset of {s1, s2, ..., si} that adds up to j, by simply including si in the subset. If no, then set T[i][j] to false. This means that there is no subset of {s1, s2, ..., si} that adds up to j, since si is larger than j.
  - After filling the array T, check the value of T[n][d]. If it is true, then there is a solution to the problem. If it is false, then there is no solution to the problem.
  - To find the actual subsets that add up to d, we can backtrack from T[n][d] and trace the choices that were made in the array. For each i from n to 1, do the following:
    - If T[i][d] is true and T[i-1][d] is false, then si is part of the solution. Add si to the subset, and update d to d-si.
    - If T[i][d] is true and T[i-1][d] is true, then si may or may not be part of the solution. We can branch into two cases: one where we include si in the subset, and one where we exclude si from the subset. In both cases, we update d accordingly and continue the backtracking.
    - If T[i][d] is false, then si is not part of the solution. We skip si and continue the backtracking.
  - The backtracking process will generate all the possible subsets that add up to d, or display a suitable message if there is no solution.
- The time complexity of the dynamic programming algorithm is O(n*d), where n is the size of the input set and d is the target