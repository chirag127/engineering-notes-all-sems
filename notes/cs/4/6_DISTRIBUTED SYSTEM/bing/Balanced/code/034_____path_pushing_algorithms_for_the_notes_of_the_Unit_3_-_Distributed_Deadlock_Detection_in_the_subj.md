### Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The global WFG is constructed by sending the local WFG of each site to all its neighboring sites whenever a deadlock computation is performed .
- The neighboring sites then merge the received WFG with their own local WFG to update their global WFG .
- The global WFG contains all the dependency edges among the processes in the distributed system, and can be used to detect cycles that indicate deadlocks .
- Path pushing algorithms have the advantage of reducing the number of messages needed for deadlock detection, as the global WFG is only updated when a deadlock computation is initiated .
- However, path pushing algorithms also have some drawbacks, such as:
  - The global WFG may be inconsistent or outdated, as it does not reflect the current state of the distributed system .
  - The global WFG may be large and complex, as it contains all the dependency edges in the distributed system, which may increase the storage and computation overhead .
  - The global WFG may contain false dependencies, as some edges may be obsolete or irrelevant for deadlock detection, which may lead to false positives or false negatives .