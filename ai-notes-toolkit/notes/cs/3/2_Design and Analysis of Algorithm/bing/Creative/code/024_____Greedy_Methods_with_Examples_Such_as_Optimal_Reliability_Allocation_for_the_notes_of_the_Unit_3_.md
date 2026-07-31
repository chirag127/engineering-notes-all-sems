# Greedy Methods with Examples

Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution. Greedy methods are often used to solve optimization problems, such as finding the minimum or maximum of a function, or the shortest or longest path in a graph. Greedy methods are easy to implement and fast to execute, but they do not always guarantee the optimal solution. Therefore, it is important to analyze the problem and prove that the greedy choice property and the optimal substructure property hold before applying a greedy method.

## Greedy Choice Property

The greedy choice property is the property that a globally optimal solution can be obtained by making a locally optimal (greedy) choice at each step. This means that we do not need to consider the future consequences of each choice, and we can simply pick the best option available at the moment. For example, in the fractional knapsack problem, the greedy choice is to pick the item with the highest value-to-weight ratio first, and fill the knapsack as much as possible. This choice leads to the optimal solution, as no other choice can give a higher total value.

## Optimal Substructure Property

The optimal substructure property is the property that an optimal solution to a problem contains optimal solutions to its subproblems. This means that we can solve a problem by recursively solving its smaller subproblems, and then combining the subproblem solutions to obtain the original problem solution. For example, in the minimum spanning tree problem, the optimal substructure property is that any subtree of a minimum spanning tree is also a minimum spanning tree for the subgraph induced by the subtree nodes.

## Examples of Greedy Methods

Here are some examples of problems that can be solved by greedy methods, along with their greedy algorithms and proofs of correctness.

### Optimal Reliability Allocation

The optimal reliability allocation problem is the problem of allocating a given budget to improve the reliability of a system composed of n components, such that the overall system reliability is maximized. The system reliability is the probability that all components function properly, and it is given by the product of the individual component reliabilities. The component reliability is a function of the amount of money spent on improving it, and it is assumed to be a concave increasing function.

The greedy algorithm for this problem is as follows:

- Initialize the component reliabilities to their initial values, and the remaining budget to the given budget.
- While the remaining budget is positive, do the following:
  - Find the component with the lowest marginal cost, that is, the component that gives the highest increase in reliability per unit of money spent.
  - Spend one unit of money on improving that component, and update its reliability and the remaining budget accordingly.
- Return the final component reliabilities and the system reliability.

The proof of correctness for this algorithm is based on the following lemma:

**Lemma**: Given a system with n components and a budget B, let x_i be the optimal amount of money spent on improving component i, and let y_i be the amount of money spent by the greedy algorithm. Then, for any i, x_i <= y_i.

**Proof**: Suppose, for the sake of contradiction, that there exists some i such that x_i > y_i. Let j be the component with the lowest marginal cost at the end of the greedy algorithm, and let z be the amount of money left in the budget. Then, we have:

- z > 0, since the greedy algorithm stops when the budget is exhausted.
- y_j < x_j, since otherwise the greedy algorithm would have spent more money on component j.
- The marginal cost of component i is higher than the marginal cost of component j, since the greedy algorithm always picks the component with the lowest marginal cost.

Now, consider a new allocation, where we transfer z units of money from component i to component j, and call it x'_i and x'_j, respectively. Then, we have:

- x'_i = x_i - z > y_i, since x_i > y_i and z > 0.
- x'_j = y_j + z < x_j, since y_j < x_j and z > 0.
- The system reliability with the new allocation is higher than the system reliability with the optimal allocation, since the increase in reliability due to component j is greater than the decrease in reliability due to component i, by the definition of marginal cost.

This contradicts the optimality of the original allocation, and hence the lemma is proved.

The lemma implies that the greedy algorithm spends at least as much money on each component as the optimal allocation, and therefore achieves at