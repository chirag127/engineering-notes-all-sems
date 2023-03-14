Control flow testing is a white box testing technique that uses the control flow of the program as a model to design and execute test cases. Control flow testing aims to cover all the possible paths of execution in the program, such as nodes, edges, branches, loops, etc. Control flow testing can be performed manually or automatically, using tools that can generate a control flow graph from the source code. A control flow graph is a graphical representation of the program's structure, showing the sequence of statements and the conditions that affect the flow of control. A control flow graph consists of nodes, edges, decision nodes, and junction nodes. Nodes represent statements or blocks of code, edges represent the direction of control flow, decision nodes represent conditional statements that can branch the control flow, and junction nodes represent points where multiple paths converge. Control flow testing can help detect errors in the logic and implementation of the program, such as missing or incorrect paths, unreachable code, infinite loops, etc.

An example of a control flow graph for a simple program that checks the eligibility of a person for voting based on their age is shown below:

```
    +-------+
    | start |
    +-------+
       |
       v
    +-----+
    | age |
    +-----+
       |
       v
+--------------+
| if (age >= 18)|
+--------------+
   |       |
   |       | no
   |       v
   |    +--------+
   |    | not    |
   |    | eligible|
   |    +--------+
   |       |
   |       v
   |    +-------+
   |    | stop  |
   |    +-------+
   v
   yes
+--------+
| eligible|
+--------+
   |
   v
+-------+
| stop  |
+-------+
```