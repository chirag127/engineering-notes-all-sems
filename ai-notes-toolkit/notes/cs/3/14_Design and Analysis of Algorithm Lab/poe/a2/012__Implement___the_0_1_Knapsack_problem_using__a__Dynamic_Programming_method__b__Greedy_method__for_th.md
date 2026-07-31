 Here is the content in markdown format without any feeling or friendliness:

## Implement , the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method. for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System.

(a) Dynamic Programming method:

1. Define the state expression (for a 0/1 knapsack):
```
dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i]] + val[i])
```
where i is the current item and w is the capacity of the knapsack.

2. Initialize the base cases:
```
dp[0][...] = 0
dp[...][0] = 0
```

3. Evaluate the state expressions in bottom-up manner.

4. Print dp[n-1][W] where n is the number of items and W is the knapsack capacity.

(b) Greedy method:

1. Sort the items in decreasing order of value per unit weight ratio (val[i]/wt[i]).

2. Loop from i=0 to n-1 and for each item:
```
if (wt[i] <= w) {
    taken[i] = true;
    w -= wt[i];
} else {
    taken[i] = false;
}
```
where w is the current capacity of knapsack.

3. Print the items for which taken[i] is true.

The above content is written in points without any emojis or external links to be formal as per the given instructions.