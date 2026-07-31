Cyclomatic complexity is a software metric used to measure the complexity of a program. It is calculated by developing a Control Flow Graph of the code that measures the number of linearly-independent paths through a program module. Here is an ASCII diagram that represents the Control Flow Graph of a sample code:

##### Cyclomatic Complexity Measures in software design
```
+-------+       +-------+
| Start |       |  End  |
+---+---+       +---+---+
    |               ^
    |               |
    v               |
+---+---+       +---+---+
|   A   |       |   B   |
+---+---+       +---+---+
    |               ^
    |               |
    v               |
+---+---+       +---+---+
|   C   |       |   D   |
+---+---+       +---+---+
    |               ^
    |               |
    v               |
+---+---+       +---+---+
|   E   |       |   F   |
+---+---+       +---+---+
    |               ^
    |               |
    v               |
+---+---+       +---+---+
|   G   |       |   H   |
+---+---+       +---+---+
    |               ^
    |               |
    v               |
+---+---+       +---+---+
|   I   |       |   J   |
+---+---+       +---+---+
    |               ^
    |               |
    v               |
+---+---+       +---+---+
|   K   |       |   L   |
+---+---+       +---+---+
    |               ^
    |               |
    v               |
+---+---+       +---+---+
|   M   |       |   N   |
+---+---+       +---+---+
    |               ^
    |               |
    v               |
+---+---+       +---+---+
|   O   |       |   P   |
+---+---+       +---+---+
    |               ^
    |               |
    v               |
+---+---+       +---+---+
|   Q   |       |   R   |
+---+---+       +---+---+
    |               ^
    |               |
    v               |
+---+---+       +---+---+
|   S   |       |   T   |
+---+---+       +---+---+
    |               ^
    |               |
    v               |
+---+---+       +---+---+
|   U   |       |   V   |
+---+---+       +---+---+
    |               ^
    |               |
    v               |
+---+---+       +---+---+
|   W   |       |   X   |
+---+---+       +---+---+
    |               ^
    |               |
    v               |
+---+---+       +---+---+
|   Y   |       |   Z   |
+---+---+       +---+---+
    |               ^
    |               |
    v               |
+-------+       +-------+
|  End  |       | Start |
+-------+       +-------+
```