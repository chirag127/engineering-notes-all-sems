#### Schema design in HBase

- HBase is a NoSQL database that stores data in a tabular format, with rows and columns.
- HBase does not support joins, normalization, or secondary indexes, but it provides fast and scalable access to data by row key.
- HBase schema design is based on the following concepts:

  - Row key: The unique identifier for each row in a table. It is the only way to access data in HBase. Row keys are sorted lexicographically, so they should be designed carefully to optimize performance and avoid hotspots.
  - Column family: A logical grouping of columns that share the same storage and configuration properties. Each column family is stored as a separate file on disk, so they should be kept to a minimum and contain related data. Column families are defined at table creation time and cannot be changed later.
  - Column qualifier: The name of a column within a column family. Column qualifiers are dynamic and can be added or deleted at any time. They can also be used to store nested entities or complex data types, by concatenating multiple values or serializing objects.
  - Cell: The intersection of a row and a column. A cell contains a value and a timestamp. The value can be any binary data, such as a string, a number, or an image. The timestamp can be assigned by the client or the server, and it is used to keep track of multiple versions of the same cell.
  - Version: A cell can have multiple versions, each with a different timestamp and value. HBase can store and retrieve multiple versions of a cell, based on the timestamp range or the number of versions specified by the client. Versions can be used to implement features such as auditing, history, or undo.

- HBase schema design should follow these general guidelines:

  - Choose a row key that is unique, descriptive, and well distributed. Avoid using sequential or monotonically increasing values, such as timestamps or counters, as they can cause hotspots and performance degradation. Use hashing, salting, or reverse timestamp techniques to create more random and balanced row keys.
  - Choose a column family that is coherent, compact, and frequently accessed. Avoid creating too many or too few column families, as they can affect the storage efficiency and the read/write performance. Use column families to group data that is accessed together, such as user profile, user activity, or user preferences.
  - Choose a column qualifier that is meaningful, flexible, and variable. Avoid using fixed or predefined column names, as they can limit the schema evolution and the data modeling. Use column qualifiers to store dynamic or complex data, such as nested entities, arrays, maps, or JSON objects.
  - Choose a cell value that is simple, consistent, and compatible. Avoid using different data types or formats for the same column, as they can cause confusion and errors. Use cell values to store atomic or primitive data, such as strings, numbers, booleans, or bytes.
  - Choose a version policy that is appropriate, configurable, and manageable. Avoid storing too many or too few versions of a cell, as they can affect the storage space and the query performance. Use versions to store historical or temporal data, such as changes, events, or snapshots.