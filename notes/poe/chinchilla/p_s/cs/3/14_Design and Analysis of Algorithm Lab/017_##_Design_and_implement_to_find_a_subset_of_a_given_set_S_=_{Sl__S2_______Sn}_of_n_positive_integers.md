## Design and Implement to Find a Subset of a Given Set S

### Introduction
In this lab, we will learn how to design and implement an algorithm to find a subset of a given set S of n positive integers whose sum is equal to a given positive integer d. This problem is known as the Subset Sum Problem.

### Problem Statement
Given a set S = {Sl, S2,.....,Sn} of n positive integers and a positive integer d, the problem is to find a subset of S whose sum is equal to d. If there are multiple solutions, we need to find any one of them. If there is no subset whose sum is equal to d, we need to display a suitable message.

### Algorithm Design
We can solve this problem using dynamic programming. Let's define a two-dimensional array dp[i][j], where dp[i][j] is true if there exists a subset of the first i elements of S that adds up to j. Initially, all values in the array are set to false.

We can fill the array row by row, using the following recurrence relation:

- dp[0][j] = false for all j (since we cannot form a subset from an empty set)
- dp[i][0] = true for all i (since we can always form an empty subset that adds up to 0)
- dp[i][j] = true if dp[i-1][j] is true or dp[i-1][j-S[i]] is true (if we can form a subset that adds up to j without using the ith element, or if we can form a subset that adds up to j-S[i] using the ith element)

Once we have filled the array, we can find a solution by starting at dp[n][d] and tracing back which elements were used to form the sum.

### Pseudo Code
```
initialize dp[n+1][d+1] to false
for i from 0 to n:
    dp[i][0] = true
for i from 1 to n:
    for j from 1 to d:
        dp[i][j] = dp[i-1][j]
        if j >= S[i]:
            dp[i][j] = dp[i][j] or dp[i-1][j-S[i]]

if dp[n][d] is false:
    print "No subset found"
else:
    # find a solution by tracing back through dp
```

### Time Complexity
The time complexity of this algorithm is O(nd), where n is the size of the set S and d is the given sum. This is because we need to fill an n x d array, and each cell takes constant time to compute.

### Advantages
- This algorithm is guaranteed to find a solution if one exists.
- The time complexity is polynomial, which means it can handle large input sizes.

### Disadvantages
- The space complexity of this algorithm is also polynomial, which means it can use a lot of memory for large input sizes.
- If there are multiple solutions, this algorithm only finds one of them. It does not guarantee that the solution found is optimal.

### Applications
The Subset Sum Problem has many applications, including:
- Cryptography: The problem of finding a subset of integers that add up to a certain value is used in the RSA cryptosystem to encrypt and decrypt messages.
- Resource allocation: The problem of allocating resources (such as memory or bandwidth) to different tasks can be framed as a subset sum problem.
- Gene expression: The problem of determining which genes are responsible for a certain phenotype can be modeled as a subset sum problem.