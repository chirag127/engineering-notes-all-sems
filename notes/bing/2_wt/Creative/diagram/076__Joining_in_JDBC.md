Joining in JDBC is the process of combining data from two or more tables based on a common column or condition. JDBC provides the JoinRowSet interface to perform join operations on RowSet objects. A RowSet object is a container for a set of rows that can be manipulated and accessed in a disconnected manner.

The following diagram illustrates the basic architecture of a join operation in JDBC using the JoinRowSet interface:

```
+-----------------+     +-----------------+     +-----------------+
|     Table 1     |     |     Table 2     |     |     Table 3     |
+-----------------+     +-----------------+     +-----------------+
|  Column 1 (PK)  |     |  Column 1 (PK)  |     |  Column 1 (PK)  |
|  Column 2       |     |  Column 2       |     |  Column 2       |
|  Column 3       |     |  Column 3       |     |  Column 3       |
|  Column 4       |     |  Column 4       |     |  Column 4       |
+-----------------+     +-----------------+     +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+     +-----------------+     +-----------------+
|    RowSet 1     |     |    RowSet 2     |     |    RowSet 3     |
+-----------------+     +-----------------+     +-----------------+
|  Column 1 (PK)  |     |  Column 1 (PK)  |     |  Column 1 (PK)  |
|  Column 2       |     |  Column 2       |     |  Column 2       |
|  Column 3       |     |  Column 3       |     |  Column 3       |
|  Column 4       |     |  Column 4       |     |  Column 4       |
+-----------------+     +-----------------+     +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         V                     V                     V
+---------------------------------------------------------------+
|                        JoinRowSet                             |
+---------------------------------------------------------------+
|  Column 1 (PK)  |  Column 2  |  Column 3  |  Column 4  | ...  |
+---------------------------------------------------------------+
|  Row 1          |  Row 1     |  Row 1     |  Row 1     | ...  |
|  Row 2          |  Row 2     |  Row 2     |  Row 2     | ...  |
|  Row 3          |  Row 3     |  Row 3     |  Row 3     | ...  |
|  Row 4          |  Row 4     |  Row 4     |  Row 4     | ...  |
|  ...            |  ...       |  ...       |  ...       | ...  |
+---------------------------------------------------------------+
```

The JoinRowSet object contains the result of the join operation, which can be accessed and manipulated using the methods of the RowSet interface. The join operation can be performed using different types of joins, such as inner join, left outer join, right outer join, full outer join, or cross join. The type of join can be specified using the setJoinType method of the JoinRowSet interface. The join operation can also be performed on more than two RowSet objects, as long as they have a common match column. The match column is the column on which the join is based, and it must be a primary key or a unique column in each RowSet object. The match column can be specified using the setMatchColumn method of the RowSet interface.