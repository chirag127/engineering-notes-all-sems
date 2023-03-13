I assume you want me to draw a detailed ASCII diagram for a program that prints 'D' if the input is below 60%. Here is one possible diagram:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Get input (x)  |------->|  Check if x<60  |------->|  Print 'D'      |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
                             |               ^
                             |               |
                             v               |
                           +-----------------+
                           |                 |
                           |  Do nothing     |
                           |                 |
                           +-----------------+
```