Channel allocation in cellular systems is the process of assigning the available channels to the cells in a cellular network. Channels are the basic units of communication between a base station and a mobile terminal. Channels can be divided into frequency channels, time slots, or codes, depending on the type of cellular system. Channel allocation strategies aim to maximize the efficiency of channel usage, minimize the interference between cells, and satisfy the demand of users.

The following diagram illustrates the basic architecture of a cellular system:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Base         |      |    Base         |      |    Base         |
|    Station      |      |    Station      |      |    Station      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Cell         |      |    Cell         |      |    Cell         |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Mobile       |      |    Mobile       |      |    Mobile       |
|    Terminal     |      |    Terminal     |      |    Terminal     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The following diagram illustrates the frequency reuse concept in a cellular system:

```
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 1 |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| 2 | 3 | 4 | 5 | 6 | 7 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 1 | 2 |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| 3 | 4 | 5 | 6 | 7 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 1 | 2 | 3 |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| 4 | 5 | 6 | 7 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 1 | 2 | 3 | 4 |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| 5 | 6 | 7 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 1 | 2 | 3 | 4 | 5 |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| 6 | 7 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 1 | 2 | 3 | 4 | 5 | 6 |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| 7 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
```

Each cell is assigned a set of frequencies that are different from the neighboring cells. The same set of frequencies can be reused in other cells that are far enough to avoid interference. The frequency reuse factor is the ratio of the total number of available channels to the number of