 Here is the content in markdown format without any emotions or friendliness:

## Write programs to

**(a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm.**

1. Accept the adjacency matrix as input.
2. Take 3 nested loops:
- outer loop: To pick each vertex as an intermediate vertex.
- middle loop: To pick source vertex.
- inner loop: To pick destination vertex.
3. Update the distance matrix[i][j] if it is smaller than the previous value and the path exists through the intermediate vertex k.
4. Print the distance matrix.

**(b) Implement Travelling Sales Person problem using Dynamic programming.**

1. Accept the number of cities and the cost matrix as input.
2. Create a table dp[n][1<<n] and initialize all values as infinity. Here, 1<<n gives all subsets of cities.
3. Fill the base cases:
- dp[i][1<<i] = cost[0][i]   //tour starts and ends at city 0
4. Use the recursive formula:
dp[i][subset] = min(dp[i][subset], dp[j][subset^(1<<j)] + cost[j][i])
Here, subset^(1<<j) toggles the bit jth bit.
5. Print the minimum cost tour from dp[0][(1<<n)-1].

The content is written in a formal way with points and without any emojis or external links as per the given instructions. The topic is explained like study material to learn and read from for exams.