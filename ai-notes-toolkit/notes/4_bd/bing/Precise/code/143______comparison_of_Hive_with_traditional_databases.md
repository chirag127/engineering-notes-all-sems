#### Comparison of Hive with traditional databases

Hive and traditional databases have several differences, some of which are:

- **Schema:** Hive applies schema on read time, meaning it does not verify the data when it is loaded, but rather when it is read. Traditional databases, on the other hand, apply schema on write time, meaning the table schema is enforced when data is loaded .
- **Scalability:** Hive is easily scalable at a low cost, while traditional databases are not as scalable and can be costly to scale up .
- **Data Manipulation:** Hive is based on Hadoop notation, which means it is write once and read many times. In traditional databases, data can be read and written multiple times. Record-level updates, insertions, and deletions are not possible in Hive, while they are possible in traditional databases .
- **Interface:** Hive supports an SQL-like interface, but it is not a full database. It can be better called a data warehouse instead of a database .
