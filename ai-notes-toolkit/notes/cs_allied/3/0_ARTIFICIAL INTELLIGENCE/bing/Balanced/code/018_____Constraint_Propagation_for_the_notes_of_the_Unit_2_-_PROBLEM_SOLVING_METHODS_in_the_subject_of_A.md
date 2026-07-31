# Constraint Propagation

- Constraint propagation is a form of reasoning, using a network of related facts, in which a value or range of possible values determined for one variable constrains the possible values of variables to which it is related.
- Constraint propagation is often used in conjunction with search to solve constraint satisfaction problems (CSPs), which are problems where the goal is to find an assignment of values to a set of variables that satisfies a set of constraints.
- Constraint propagation can be seen as a process of applying rules of combination and modification of constraints to reduce the domains of the variables and detect inconsistencies.
- Constraint propagation can be applied to both numeric and symbolic constraints. An example of symbolic constraint propagation is junction and line labelling in computer vision, where the labels of the lines and junctions in an image are constrained by geometric and photometric properties.
- The basic algorithm for constraint propagation is as follows:
  - Initialize the domains of the variables and the constraints.
  - Select a variable whose domain has been modified and a constraint that contains that variable.
  - Check if the constraint is satisfied by the current domains of the variables. If not, remove the inconsistent values from the domains and mark the affected variables as modified.
  - Repeat until no more variables or constraints can be selected, or until an empty domain is found.
  - If an empty domain is found, the problem is unsatisfiable. Otherwise, the problem is either solved or simplified.