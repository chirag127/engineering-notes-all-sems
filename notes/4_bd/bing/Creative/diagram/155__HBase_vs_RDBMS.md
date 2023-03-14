HBase and RDBMS are both types of database management systems, but they differ in several ways. Here is a detailed ASCII diagram for HBase vs RDBMS:

#### HBase vs RDBMS

```
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|    HBase         |     |    RDBMS         |     |    Features      |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Column-oriented |     |  Row-oriented    |     |  Database Type   |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Less restrictive|     |  More restrictive|     |  Schema-type     |
|  schema          |     |  schema          |     |                  |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Good with       |     |  Not optimized   |     |  Sparse Tables   |
|  sparse tables   |     |  for sparse      |     |                  |
|                  |     |  tables          |     |                  |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Scale out       |     |  Scale up        |     |  Scale up/       |
|                  |     |                  |     |  Scale out       |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Depends on      |     |  Depends on      |     |  Amount of data  |
|  number of       |     |  configuration   |     |                  |
|  machines        |     |  of the server   |     |                  |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  No built-in     |     |  ACID support    |     |  Support         |
|  support         |     |                  |     |                  |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Supports both   |     |  Suited for      |     |  Data type       |
|  structured and  |     |  structured data |     |                  |
|  non-structured  |     |                  |     |                  |
|  data            |     |                  |     |                  |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  No transaction  |     |  Guarantees      |     |  Transaction     |
|  guarantee       |     |  transaction     |     |  integrity       |
|                  |     |  integrity       |     |                  |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Supports JOINs  |     |  Does not        |     |  JOINs           |
|                  |     |  support JOINs   |     |                  |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  No in-built     |     |  Supports        |     |  Referential     |
|  support         |     |  referential     |     |  integrity       |
|                  |     |  integrity       |     |                  |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Horizontally    |     |  Vertically      |     |  Scalability     |
|  scalable        |     |  scalable        |     |                  |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Runs on top of  |     |