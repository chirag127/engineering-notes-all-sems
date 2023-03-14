Indexing in MongoDB is a way of creating special data structures that store a small portion of the collection's data set in an easy to traverse form. Indexes support the efficient execution of queries in MongoDB by limiting the number of documents that the database engine has to scan. MongoDB supports various types of indexes, such as single field, compound, multikey, text, and geospatial indexes.

#### Indexing in MongoDB

The following diagram illustrates the basic architecture of a single field index in MongoDB:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  Collection    |    |  Index         |    |  Documents     |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  _id: 1       ----->|  _id: 1       ----->|  _id: 1        |
|  name: Alice  |    |  name: Alice  |    |  name: Alice   |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  _id: 2       ----->|  _id: 2       ----->|  _id: 2        |
|  name: Bob    |    |  name: Bob    |    |  name: Bob     |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  _id: 3       ----->|  _id: 3       ----->|  _id: 3        |
|  name: Carol  |    |  name: Carol  |    |  name: Carol   |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
```

The index stores the values of the _id and name fields of each document in the collection, ordered by the value of the name field. The index also stores a pointer to the location of the corresponding document in the database. When a query is performed on the name field, MongoDB can use the index to quickly find the matching documents without scanning the entire collection. The index also supports sorting the results by the name field.