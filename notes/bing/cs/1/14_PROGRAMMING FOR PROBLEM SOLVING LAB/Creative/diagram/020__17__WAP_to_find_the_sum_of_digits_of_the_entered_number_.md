## 17. WAP to find the sum of digits of the entered number.

The following diagram illustrates the basic algorithm of the program:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Input a number | ----> |  Initialize sum | ----> |  Repeat until   |
|                 |       |  to zero        |       |  number is zero |
+-----------------+       +-----------------+       +-----------------+
                                         |                 |
                                         |                 |
                                         |                 v
                                         |       +-----------------+
                                         |       |                 |
                                         |       |  Add last digit |
                                         |       |  of number to   |
                                         |       |  sum            |
                                         |       |                 |
                                         |       +-----------------+
                                         |                 |
                                         |                 |
                                         |                 v
                                         |       +-----------------+
                                         |       |                 |
                                         |       |  Remove last    |
                                         |       |  digit of       |
                                         |       |  number         |
                                         |       |                 |
                                         |       +-----------------+
                                         |                 |
                                         |                 |
                                         +-----------------+
                                                       |
                                                       |
                                                       v
                                             +-----------------+
                                             |                 |
                                             |  Output sum     |
                                             |                 |
                                             +-----------------+
```