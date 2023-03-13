Control flow testing is a type of software testing that uses the program's control flow as a model. Control flow testing is a structural testing strategy that comes under white box testing. It aims to determine the execution order of statements or instructions of the program through a control structure. The control structure of a program is used to develop a test case for the program.

A control flow graph is a graphical representation of the control flow of a program. It consists of nodes and edges. Nodes represent the basic blocks of the program, which are sequences of statements that have a single entry point and a single exit point. Edges represent the possible transitions between the basic blocks. The control flow graph can be used to identify the paths that can be executed in the program, and to design test cases that cover those paths.

A possible ASCII diagram for control flow testing is shown below:

```
+-----------------+     +-----------------+     +-----------------+
| Start           |     | Input x, y      |     | If x > y        |
|                 +---->+                 +---->+                 |
+-----------------+     +-----------------+     +-----------------+
                                               /                 \
                                              /                   \
                                             /                     \
                                            /                       \
                                           /                         \
                                          /                           \
                                         /                             \
                                        /                               \
                                       /                                 \
                                      /                                   \
                                     /                                     \
                                    /                                       \
                                   /                                         \
                                  /                                           \
                                 /                                             \
                                /                                               \
                               /                                                 \
                              /                                                   \
                             /                                                     \
                            /                                                       \
                           /                                                         \
                          /                                                           \
                         /                                                             \
                        /                                                               \
                       /                                                                 \
                      /                                                                   \
                     /                                                                     \
                    /                                                                       \
                   /                                                                         \
                  /                                                                           \
                 /                                                                             \
                /                                                                               \
               /                                                                                 \
              /                                                                                   \
             /                                                                                     \
            /                                                                                       \
           /                                                                                         \
          /                                                                                           \
         /                                                                                             \
        /                                                                                               \
       /                                                                                                 \
      /                                                                                                   \
     /                                                                                                     \
    /                                                                                                       \
   /                                                                                                         \
  /                                                                                                           \
 /                                                                                                             \
/                                                                                                               \
+-----------------+     +-----------------+     +-----------------+     +-----------------+     +-----------------+
| x = x + 1       |     | y = y - 1       |     | If x == y       |     | Print "Equal"   |     | End             |
|                 +---->+                 +---->+                 +---->+                 +---->+                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+     +-----------------+
                                               /                 \
                                              /                   \
                                             /                     \
                                            /                       \
                                           /                         \
                                          /                           \
                                         /                             \
                                        /                               \
                                       /                                 \
                                      /                                   \
                                     /                                     \
                                    /                                       \
                                   /                                         \
                                  /                                           \
                                 /                                             \
                                /                                               \
                               /                                                 \
                              /                                                   \
                             /                                                     \
                            /                                                       \
                           /                                                         \
                          /                                                           \
                         /                                                             \
                        /                                                               \
                       /                                                                 \
                      /                                                                   \
                     /                                                                     \
                    /                                                                       \
                   /                                                                         \
                  /                                                                           \
                 /                                                                             \
                /                                                                               \
               /                                                                                 \
              /                                                                                   \
             /                                                                                     \
            /                                                                                       \
           /                                                                                         \
          /                                                                                           \
         /                                                                                             \
        /                                                                                               \
       /                                                                                                 \
      /                                                                                                   \
     /                                                                                                     \
    /                                                                                                       \
   /                                                                                                         \
  /                                                                                                           \
 /                                                                                                             \
/                                                                                                               \
+-----------------+     +-----------------+     +-----------------+     +-----------------+     +-----------------+
| x = x - 1       |     | y = y + 1       |     | If x < y        |     | Print "Less"    |     | End             |
|                 +---->+                 +---->+                 +---->+                 +---->+                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+     +-----------------+
```