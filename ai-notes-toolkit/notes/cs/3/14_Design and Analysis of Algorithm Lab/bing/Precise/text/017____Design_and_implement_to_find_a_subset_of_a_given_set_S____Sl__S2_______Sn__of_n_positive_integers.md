## Design and implement to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d.

This problem can be solved using a recursive algorithm. The basic idea is to consider all subsets of the given set S and check if the sum of elements in the subset is equal to the given positive integer d.

1. If the given set is empty, return false.
2. If the first element of the set is greater than the given positive integer d, ignore it and recur for the remaining set.
3. Else, recur for the remaining set with the given positive integer d reduced by the first element of the set.
4. If any of the above recursive calls returns true, return true.
5. Else, return false.

For example, if S ={1, 2, 5, 6, 8} and d= 9, there are two solutions {1,2,6}and {1,8}. If the given problem instance doesn't have a solution, a suitable message can be displayed.

This algorithm can be implemented using a recursive function that takes the given set S, the given positive integer d, and the current index as input arguments. The base case of the recursive function is when the current index is equal to the size of the given set S. In this case, if the given positive integer d is equal to 0, return true, else return false. The recursive function can be called twice, once by including the current element in the subset and once by excluding it. If any of the recursive calls returns true, return true, else return false.

This algorithm has an exponential time complexity as it considers all subsets of the given set S. However, it can be optimized using dynamic programming techniques. A 2D boolean array can be used to store the results of subproblems. The value of the array at index i, j represents if there is a subset of the first i elements of the given set S whose sum is equal to j. The array can be filled in a bottom-up manner using the above recursive relation. Once the array is filled, the solution can be obtained by checking the value of the array at index n, d.

This optimized algorithm has a time complexity of O(n*d) and a space complexity of O(n*d), where n is the size of the given set S and d is the given positive integer. This makes it more efficient than the recursive algorithm for large inputs. However, it still has an exponential space complexity and may not be feasible for very large inputs. In such cases, other techniques such as branch and bound or backtracking can be used to solve the problem.