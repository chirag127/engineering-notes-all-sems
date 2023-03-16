### Constraint Propagation

- Constraint propagation is a technique for reducing the search space of a problem by applying constraints that eliminate inconsistent or impossible values from the domains of the variables.
- A constraint is a restriction on the possible values of one or more variables. For example, in a map-coloring problem, a constraint could be that two adjacent regions cannot have the same color.
- A domain is the set of possible values that a variable can take. For example, in a map-coloring problem, a domain could be the set of colors {red, green, blue}.
- Constraint propagation works by applying inference rules that exploit the structure of the constraints and the domains to eliminate values that cannot be part of a solution.
- For example, in a map-coloring problem, if a region has only one possible color left in its domain, then that color can be assigned to that region and removed from the domains of its neighbors. This is called the **singleton rule**.
- Another example of an inference rule is the **arc-consistency rule**, which checks if a value in the domain of one variable is consistent with the values in the domains of the variables that are connected to it by a constraint. If not, then that value can be eliminated from the domain of the first variable.
- Constraint propagation can be applied repeatedly until no more values can be eliminated or a contradiction is found. If a contradiction is found, then the problem is unsolvable or the initial domains are too restrictive.
- Constraint propagation can be used as a preprocessing step before applying a search algorithm, or as a filtering step during the search process. It can reduce the branching factor and the depth of the search tree, and thus improve the efficiency of the search.