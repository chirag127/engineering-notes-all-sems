## Design and implement to find a subset of a given set S = {Sl, S2,.....,Sn} of n positive integers whose SUM is equal to a given positive integer d.

Given a set of positive integers S and a target positive integer d, the problem is to find a subset of S whose sum is equal to d. If such a subset exists, the algorithm should return the subset. Otherwise, it should display a message indicating that the problem instance doesn't have a solution.

### Algorithm

The algorithm for solving this problem can be implemented using dynamic programming. The steps involved are:

1. Create a 2-D array of size (n+1) x (d+1), where n is the number of elements in the set S and d is the target sum.
2. Initialize the first column of the array to True and the first row to False.
3. For each element in the set S, iterate through the columns of the array from d to the value of the element.
4. If the previous row at the current column minus the value of the current element is True, set the current cell to True. Otherwise, set it to False.
5. If the cell at the bottom right of the array is True, backtrack through the array to find the subset that adds up to d.

### Pseudo Code

```
function find_subset(S, d):
    n = len(S)
    table = [[False] * (d+1) for _ in range(n+1)]
    
    for i in range(n+1):
        table[i][0] = True
    
    for i in range(1, n+1):
        for j in range(1, d+1):
            if j < S[i-1]:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j] or table[i-1][j-S[i-1]]
    
    if not table[n][d]:
        print("No solution exists")
        return None
    
    subset = []
    i = n
    j = d
    while j > 0:
        if table[i-1][j]:
            i -= 1
        else:
            subset.append(S[i-1])
            j -= S[i-1]
            i -= 1
    
    print("Subset that adds up to d:", subset)
    return subset
```

### Time Complexity

The time complexity of this algorithm is O(nd), where n is the number of elements in the set S and d is the target sum. This is because we iterate through all the elements of the set S and for each element, we iterate through all the possible sums from 1 to d.

### Space Complexity

The space complexity of this algorithm is O(nd), as we need to create a 2-D array of size (n+1) x (d+1) to store the intermediate results.