###### Control Flow Graphs in software design

- A control flow graph (CFG) is a graphical representation of the possible paths of execution of a program or a function.
- A CFG consists of nodes and edges, where each node represents a basic block and each edge represents a possible transfer of control between basic blocks.
- A basic block is a sequence of instructions that has a single entry point and a single exit point, and does not contain any branches or jumps.
- A CFG can be used to analyze various properties of a program or a function, such as reachability, liveness, dominance, loop detection, etc.
- A CFG can also be used to perform various optimizations, such as dead code elimination, constant propagation, common subexpression elimination, etc.
- A CFG can be constructed from the source code or the intermediate code of a program or a function, by following these steps:
  - Identify the entry and exit points of the program or the function, and create nodes for them.
  - Identify the basic blocks of the program or the function, and create nodes for them.
  - Identify the possible transfers of control between basic blocks, and create edges for them.
  - Label the nodes and edges with the corresponding instructions or conditions.
- A CFG can be represented in various ways, such as text, table, or graph. For example, consider the following pseudocode of a function:

```
function max(a, b)
  if a > b then
    return a
  else
    return b
  end if
end function
```

- A possible text representation of the CFG of this function is:

```
1: entry
2: if a > b then
3:   return a
4: else
5:   return b
6: end if
7: exit
```

- A possible table representation of the CFG of this function is:

| Node | Instruction | Successors |
|------|-------------|------------|
| 1    | entry       | 2          |
| 2    | if a > b then | 3, 5      |
| 3    | return a    | 7          |
| 4    | else        | 5          |
| 5    | return b    | 7          |
| 6    | end if      | 7          |
| 7    | exit        | -          |

- A possible graph representation of the CFG of this function is:

```
  1
  |
  2
 / \
3   4
|   |
|   5
 \ /
  6
  |
  7
```

- A possible mnemonic to remember the steps of constructing a CFG is: **E**nter the **B**asic **B**locks and **E**xit with **L**abels. (EBBEL)