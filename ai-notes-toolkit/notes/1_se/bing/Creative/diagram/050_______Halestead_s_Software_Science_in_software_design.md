Halestead’s Software Science is a method of measuring the complexity and quality of software based on the number and types of operators and operands in the source code . It is also known as Halstead complexity measures. Halstead proposed several metrics to quantify various aspects of software, such as:

- Program length (N): the total number of operators and operands in the program.
- Program vocabulary (n): the total number of unique operators and operands in the program.
- Volume (V): the amount of information contained in the program, proportional to N and n.
- Difficulty (D): the effort required to write or understand the program, proportional to the number of unique operators and the ratio of total operands to unique operands.
- Effort (E): the amount of work or time needed to implement or maintain the program, proportional to V and D.
- Time (T): the estimated time required to write the program, proportional to E and a constant factor.
- Bugs (B): the estimated number of errors in the program, proportional to V and a constant factor.

A diagram to illustrate these metrics is shown below:

##### Halestead’s Software Science in software design

```
+-----------------+     +-----------------+
| Program length  |     | Program         |
| N = N1 + N2     |     | vocabulary      |
|                 |     | n = n1 + n2     |
+-----------------+     +-----------------+
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         +----------------------+
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |

```
