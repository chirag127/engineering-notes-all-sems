Advanced indexing in HBase is a technique to create and maintain secondary indexes on HBase tables, which can improve the performance of queries that do not use the primary row key. There are different approaches to implement advanced indexing in HBase, such as using coprocessors, Phoenix, Lily HBase Indexer, or manual indexing.

The following diagram illustrates the basic architecture of a coprocessor-based indexing solution, which uses a custom observer class to intercept the put and delete operations on the main table and update the index table accordingly .

#### Advanced indexing in HBase

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Main Table     |    |  Index Table    |    |  Observer Class |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Row Key        |    |  Row Key        |    |  prePut()       |
|  Column Family  |    |  Column Family  |    |  preDelete()    |
|  Column Qualifier|    |  Column Qualifier|    |                 |
|  Value          |    |  Value          |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Put/Delete     |    |  Put/Delete     |    |  postPut()      |
|  Operation      |    |  Operation      |    |  postDelete()   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```