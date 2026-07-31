#### Scaling out with Hadoop

Here is an ASCII diagram that illustrates how scaling out with Hadoop works:

```
+------------+     +------------+
|   DataNode |     |   DataNode |
|            |     |            |
+------------+     +------------+
       |                 |
       |                 |
       v                 v
+-----------------------------+
|          NameNode          |
|                             |
+-----------------------------+
       |
       |
       v
+-----------------------------+
|          Hadoop             |
|          Cluster            |
+-----------------------------+
```
