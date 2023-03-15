## Design and implement to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d.

This problem can be solved using a recursive algorithm. The idea is to consider two cases for every element: (1) the element is included in the subset, (2) the element is not included in the subset. The base case of the recursion is when the remaining sum is 0, which means a subset has been found, or when there are no remaining elements, which means no subset has been found.

Here is an example implementation in Python:

```python
def subset_sum(S, n, d, subset):
    if d == 0:
        print(subset)
        return
    if n == 0:
        return
    subset_sum(S, n-1, d, subset)
    subset.append(S[n-1])
    subset_sum(S, n-1, d-S[n-1], subset)
    subset.pop()

S = [1, 2, 5, 6, 8]
d = 9
subset = []
subset_sum(S, len(S), d, subset)
```

This algorithm will print all the subsets of the given set S whose sum is equal to the given positive integer d. In the example above, the output will be [1, 8] and [1, 2, 6].

If the given problem instance doesn't have a solution, no subsets will be printed. In this case, a suitable message can be displayed by checking if any subsets were found.

For example:

```python
S = [1, 2, 5, 6, 8]
d = 9
subset = []
found = subset_sum(S, len(S), d, subset)
if not found:
    print("No solution found")
```

This algorithm has an exponential time complexity, as it considers all the possible subsets of the given set S. However, it can be optimized using dynamic programming techniques.