The following is a detailed ASCII diagram for Impracticality of Testing AllPaths for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing.

```
Impracticality of Testing AllPaths
----------------------------------

The goal of path testing is to cover all the possible paths of execution in a program by designing test cases for each path. However, this is impractical for most programs, because the number of paths grows exponentially with the number of branches and loops in the code. For example, consider the following pseudocode:

if A then
  if B then
    statement 1
  else
    statement 2
  end if
else
  if C then
    statement 3
  else
    statement 4
  end if
end if

This program has 4 possible paths of execution:

- A and B are true, execute statement 1
- A is true and B is false, execute statement 2
- A is false and C is true, execute statement 3
- A and C are false, execute statement 4

To test all the paths, we need 4 test cases, each with a different combination of values for A, B and C. This is manageable, but if we add more branches and loops, the number of paths and test cases will increase rapidly. For example, if we add another if statement inside each branch, the number of paths will be 8, and if we add a loop that iterates n times, the number of paths will be 2^n.

The following ASCII diagram illustrates the impracticality of testing all paths for a program with 3 branches and a loop:

+-----------------+
| Start           |
+-----------------+
        |
        v
+-----------------+
| if A then       |
+-----------------+
    |         |
    v         v
+-----------------+    +-----------------+
| if B then       |    | else            |
+-----------------+    +-----------------+
    |         |             |
    v         v             v
+-----------------+    +-----------------+
| if C then       |    | if D then       |
+-----------------+    +-----------------+
    |         |             |         |
    v         v             v         v
+-----------------+    +-----------------+    +-----------------+
| statement 1     |    | statement 2     |    | statement 3     |
+-----------------+    +-----------------+    +-----------------+
    |         |             |         |             |         |
    v         v             v         v             v         v
+-----------------+    +-----------------+    +-----------------+    +-----------------+
| else            |    | else            |    | else            |    | statement 4     |
+-----------------+    +-----------------+    +-----------------+    +-----------------+
    |                   |                   |                   |
    v                   v                   v                   v
+-----------------+    +-----------------+    +-----------------+    +-----------------+
| statement 5     |    | statement 6     |    | statement 7     |    | End             |
+-----------------+    +-----------------+    +-----------------+    +-----------------+
    |                   |                   |                   |
    v                   v                   v                   v
+-----------------+    +-----------------+    +-----------------+    +-----------------+
| for i = 1 to n |    | for i = 1 to n |    | for i = 1 to n |    |                 |
+-----------------+    +-----------------+    +-----------------+    +-----------------+
    |                   |                   |                   |
    v                   v                   v                   v
+-----------------+    +-----------------+    +-----------------+    +-----------------+
| statement 8     |    | statement 9     |    | statement 10    |    |                 |
+-----------------+    +-----------------+    +-----------------+    +-----------------+
    |                   |                   |                   |
    v                   v                   v                   v
+-----------------+    +-----------------+    +-----------------+    +-----------------+
| End             |    | End             |    | End             |    |                 |
+-----------------+    +-----------------+    +-----------------+    +-----------------+
```

The number of paths in this program is 2^3