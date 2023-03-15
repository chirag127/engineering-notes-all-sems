A flow chart is a graphical or symbolic representation of a process or an algorithm. It shows the steps, decisions, and data flows involved in a software design. A flow chart can help to visualize the logic, structure, and functionality of a program before coding it. It can also help to communicate the design to others or to debug it.

There are different types of flow charts, such as:

- System flow chart: shows the overall flow of data and control in a system.
- Program flow chart: shows the flow of logic and data within a program or a module.
- Data flow diagram: shows the sources, destinations, and transformations of data in a system.
- Pseudocode: shows the algorithm in a structured natural language.

To draw a flow chart, you need to use some standard symbols, such as:

- Rectangle: represents a process or an action.
- Diamond: represents a decision or a condition.
- Oval: represents the start or end of a flow chart.
- Arrow: represents the direction of the flow.
- Parallelogram: represents an input or output.

Here is an example of a flow chart for a simple calculator program:

#### Flow Charts in Software Design

```
+-----------------+
| Start           |
+-----------------+
        |
        V
+-----------------+
| Input A and B   |
+-----------------+
        |
        V
+-----------------+
| Input operator  |
+-----------------+
        |
        V
+-----------------+    Yes    +-----------------+
| Is operator +?  +---------->| C = A + B       |
+-----------------+           +-----------------+
        | No                         |
        V                            V
+-----------------+    Yes    +-----------------+
| Is operator -?  +---------->| C = A - B       |
+-----------------+           +-----------------+
        | No                         |
        V                            V
+-----------------+    Yes    +-----------------+
| Is operator *?  +---------->| C = A * B       |
+-----------------+           +-----------------+
        | No                         |
        V                            V
+-----------------+    Yes    +-----------------+
| Is operator /?  +---------->| C = A / B       |
+-----------------+           +-----------------+
        | No                         |
        V                            V
+-----------------+    Yes    +-----------------+
| Is operator %?  +---------->| C = A % B       |
+-----------------+           +-----------------+
        | No                         |
        V                            V
+-----------------+           +-----------------+
| Invalid operator|<----------+ Display C        |
+-----------------+           +-----------------+
        |                            |
        V                            V
+-----------------+           +-----------------+
| End             |<----------+ Stop            |
+-----------------+           +-----------------+
```