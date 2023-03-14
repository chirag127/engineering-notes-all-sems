Arrays in Java are objects that can store multiple values of the same type in a fixed-size sequential collection. Arrays can be of primitive types, such as int, float, boolean, etc., or of object types, such as String, Object, etc. Arrays can also be single-dimensional or multi-dimensional, depending on the number of indices required to access the elements.

#### Arrays in Core Java
```
+-----------------+-----------------+-----------------+-----------------+
|  anArray[0] = 1 |  anArray[1] = 2 |  anArray[2] = 3 |  anArray[3] = 4 |
+-----------------+-----------------+-----------------+-----------------+
| 0               | 1               | 2               | 3               |
+-----------------+-----------------+-----------------+-----------------+
| Index           | Index           | Index           | Index           |
+-----------------+-----------------+-----------------+-----------------+

This is a single-dimensional array of int type with four elements.

+-----------------+-----------------+-----------------+-----------------+
| anArray[0][0] = | anArray[0][1] = | anArray[0][2] = | anArray[0][3] = |
| 1               | 2               | 3               | 4               |
+-----------------+-----------------+-----------------+-----------------+
| anArray[1][0] = | anArray[1][1] = | anArray[1][2] = | anArray[1][3] = |
| 5               | 6               | 7               | 8               |
+-----------------+-----------------+-----------------+-----------------+
| anArray[2][0] = | anArray[2][1] = | anArray[2][2] = | anArray[2][3] = |
| 9               | 10              | 11              | 12              |
+-----------------+-----------------+-----------------+-----------------+
| 0,0             | 0,1             | 0,2             | 0,3             |
+-----------------+-----------------+-----------------+-----------------+
| 1,0             | 1,1             | 1,2             | 1,3             |
+-----------------+-----------------+-----------------+-----------------+
| 2,0             | 2,1             | 2,2             | 2,3             |
+-----------------+-----------------+-----------------+-----------------+
| Index           | Index           | Index           | Index           |
+-----------------+-----------------+-----------------+-----------------+

This is a two-dimensional array of int type with three rows and four columns.
```