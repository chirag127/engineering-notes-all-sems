The following is a possible ASCII diagram for 14.WAP to print sum of even and odd numbers from 1 to N numbers.

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Input: N       |------->|  Loop from 1 to |------->|  Output: Sum of |
|                 |        |  N              |        |  even and odd   |
+-----------------+        |                 |        |  numbers        |
                           +-----------------+        +-----------------+
                                  |   |
                                  |   |
                                  |   v
                                  | +-----------------+
                                  | |                 |
                                  | |  Check if i is  |
                                  +-|  even or odd    |
                                    |                 |
                                    +-----------------+
                                          |     |
                                          |     |
                                          v     v
                                +-----------------+        +-----------------+
                                |                 |        |                 |
                                |  Add i to sum   |        |  Add i to sum   |
                                |  of even        |        |  of odd         |
                                |                 |        |                 |
                                +-----------------+        +-----------------+
```