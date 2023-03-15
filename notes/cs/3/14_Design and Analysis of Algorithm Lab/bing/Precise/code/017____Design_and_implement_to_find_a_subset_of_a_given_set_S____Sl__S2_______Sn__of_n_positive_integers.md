## Design and implement to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d.

This problem can be solved using a recursive approach. The idea is to consider two cases for every element. Either we include the current element in the subset or we do not include it. We recursively call the function for both cases. If the remaining sum becomes 0, we have found a subset with the given sum.

Here is the algorithm to solve the problem:

1. Create a function `subset_sum` that takes the set `S`, the remaining sum `d`, the current index `i`, and the current subset as input.
2. If the remaining sum is 0, print the current subset and return.
3. If the remaining sum is negative or the current index is greater than or equal to the length of the set, return.
4. Call the function `subset_sum` recursively with the current element included in the subset and the remaining sum reduced by the current element.
5. Call the function `subset_sum` recursively without including the current element in the subset.
6. In the main function, call the function `subset_sum` with the initial values of the remaining sum, current index, and current subset.

Here is an example implementation in Python:

```python
def subset_sum(S, d, i, subset):
    if d == 0:
        print(subset)
        return
    if d < 0 or i >= len(S):
        return
    subset_sum(S, d - S[i], i + 1, subset + [S[i]])
    subset_sum(S, d, i + 1, subset)

S = [1, 2, 5, 6, 8]
d = 9
subset_sum(S, d, 0, [])
```

This implementation will print the two solutions `{1, 2, 6}` and `{1, 8}` for the given example. If there are no solutions, no subsets will be printed. A suitable message can be displayed by checking if any subsets were printed or not.

This algorithm has an exponential time complexity as it generates all possible subsets of the given set. However, it can be optimized using dynamic programming techniques.