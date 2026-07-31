#### Administering Hadoop in Hadoop Environment

Here is an ASCII diagram that shows the process of administering Hadoop in a Hadoop environment:

```
+-----------------+          +-----------------+
|  Hadoop Client  |          |  Hadoop Master  |
|                 |          |                 |
|  +-----------+  |          |  +-----------+  |
|  |           |  |          |  |           |  |
|  |  Submit   |  |          |  |  Monitor  |  |
|  |   Job     |  |          |  |   Job     |  |
|  |           |  |          |  |           |  |
|  +-----+-----+  |          |  +-----+-----+  |
|        |        |          |        |        |
|        |        |          |        |        |
|        v        |          |        v        |
|  +-----+-----+  |          |  +-----+-----+  |
|  |           |  |          |  |           |  |
|  |  Monitor  |  |          |  |  Manage   |  |
|  |   Job     |  |          |  |   Cluster |  |
|  |           |  |          |  |           |  |
|  +-----------+  |          |  +-----------+  |
|                 |          |                 |
+-----------------+          +-----------------+
```
