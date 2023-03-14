Resilient Distributed Datasets (RDDs) are the fundamental data structure of Spark. They are immutable distributed collections of objects that can be operated on in parallel. Each RDD is divided into logical partitions, which may be computed on different nodes of the cluster .

The following diagram illustrates the basic architecture of a Resilient Distributed Dataset in Spark:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Partition 1    |    |  Partition 2    |    |  Partition 3    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Partition 4    |    |  Partition 5    |    |  Partition 6    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Partition 7    |    |  Partition 8    |    |  Partition 9    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Partition 10   |    |  Partition 11   |    |  Partition 12   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Partition 13   |    |  Partition 14   |    |  Partition 15   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Partition 16   |    |  Partition 17   |    |  Partition 18   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Partition 19   |    |  Partition 20   |    |  Partition 21   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Partition 22   |    |  Partition 23   |    |  Partition 24   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Partition 25   |    |  Partition 26   |    |  Partition 27   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Partition 28   |    |  Partition 29   |    |  Partition 30   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Partition 31   |    |  Partition 32   |    |  Partition 33   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Partition 34   |    |  Partition 35   |    |  Partition 36   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Partition 37   |    |  Partition 38   |    |  Partition 39   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Partition 40   |    |  Partition 41   |    |  Partition 42   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Partition 43   |    |  Partition 44   |    |