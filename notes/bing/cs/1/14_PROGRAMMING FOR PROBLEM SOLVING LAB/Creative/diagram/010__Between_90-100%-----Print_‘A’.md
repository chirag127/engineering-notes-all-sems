I will draw a detailed ASCII diagram for Between 90-100%-----Print ‘A’. I assume you want a flowchart diagram that shows the logic of the program.

The following diagram illustrates the basic architecture of a program that prints 'A' if the input is between 90 and 100, otherwise prints 'Invalid input':

```
+-----------------+
| Start           |
+-----------------+
        |
        v
+-----------------+
| Input x         |
+-----------------+
        |
        v
+-----------------+    Yes    +-----------------+
| Is x >= 90?     |---------->| Is x <= 100?    |
+-----------------+           +-----------------+
        | No                        | Yes
        v                          v
+-----------------+    +-----------------+
| Print "Invalid" |    | Print "A"       |
+-----------------+    +-----------------+
        |                          |
        +--------------------------+
        v
+-----------------+
| End             |
+-----------------+
```