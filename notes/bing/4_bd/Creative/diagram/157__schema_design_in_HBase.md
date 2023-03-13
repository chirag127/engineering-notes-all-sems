Schema design in HBase is very different from relational database schema design. HBase does not support joins, but it provides single-indexing on the row key. HBase also supports denormalization with nested entities, which are columns whose names are unique identifiers for the nested entity and whose values are the entire record mashed together. HBase allows dynamic column definition, so there is no problem with adding new attributes.

The following ASCII diagram illustrates the basic architecture of a schema design in HBase:

```
+-----------------+-----------------+-----------------+-----------------+
| Row Key         | Column Family 1 | Column Family 2 | Column Family 3 |
+-----------------+-----------------+-----------------+-----------------+
| row1            | cf1:col1=val1   | cf2:col1=val2   | cf3:col1=val3   |
|                 | cf1:col2=val4   | cf2:col2=val5   | cf3:col2=val6   |
|                 | cf1:col3=val7   | cf2:col3=val8   | cf3:col3=val9   |
+-----------------+-----------------+-----------------+-----------------+
| row2            | cf1:col1=val10  | cf2:col1=val11  | cf3:col1=val12  |
|                 | cf1:col2=val13  | cf2:col2=val14  | cf3:col2=val15  |
|                 | cf1:col3=val16  | cf2:col3=val17  | cf3:col3=val18  |
+-----------------+-----------------+-----------------+-----------------+
| row3            | cf1:col1=val19  | cf2:col1=val20  | cf3:col1=val21  |
|                 | cf1:col2=val22  | cf2:col2=val23  | cf3:col2=val24  |
|                 | cf1:col3=val25  | cf2:col3=val26  | cf3:col3=val27  |
+-----------------+-----------------+-----------------+-----------------+
```

In this diagram, each row has a row key and three column families (cf1, cf2, cf3). Each column family has three columns (col1, col2, col3) and each column has a value. The values are stored as byte arrays and can be any type of data. The column names are prefixed with the column family name and a colon. The column families are defined at the table creation time, but the columns can be added dynamically. The row key is the only index for the table and the data is sorted lexicographically by the row key. HBase also supports versioning and timestamps for each cell, but they are not shown in this diagram.