 Here are the notes for the topic **Greedy Methods with Examples Such as Knapsack** for the Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching in the subject Design and Analysis of Algorithms:

### Greedy Methods
- Greedy methods make locally optimal choices at each stage in hope of finding a global optimum.
- Greedy algorithms are simple and efficient but do not always yield the optimal solution.
- Examples of greedy methods:
  - Knapsack problem
  - Minimum spanning trees - Prim's and Kruskal's algorithms
  - Single source shortest paths - Dijkstra's and Bellman-Ford algorithms
  - Optimal reliability allocation

### Knapsack Problem
- Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given capacity and the total value is as large as possible.
- Applying greedy method:
  - At each stage, choose the item with the largest value-to-weight ratio.
  - If multiple items have the same ratio, choose arbitrarily among them.
- Pseudo code:
```
Item = (Value, Weight)
Items = [Item1, Item2, ..., Itemn]
Capacity = W

Sort Items in decreasing order of Value/Weight ratio

For i = 1 to n:
    If (Weight of Item[i] <= Capacity):
        Add Item[i] to Knapsack
        Capacity = Capacity - Weight of Item[i]
    Else:
        Stop
```
- Time complexity: O(nlogn) to sort + O(n) to iterate = O(nlogn)
- Advantage: Simple and efficient
- Disadvantage: Does not always yield the optimal solution

[Additional details, diagrams, examples, etc. can be added here...]