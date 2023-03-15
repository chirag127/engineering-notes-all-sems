#### Sorting and Aggregating in Hive

- **Sorting** in Hive refers to the process of arranging data in a specific order, either ascending or descending, based on one or more columns.
- Hive supports two types of sorting: **Order By** and **Sort By**.
- **Order By** sorts the data globally and returns the sorted data to the client. It is a costly operation as it requires shuffling of data between the nodes.
- **Sort By** sorts the data locally within each reducer. The final output may not be globally sorted, but the data within each reducer is sorted.
- **Aggregation** in Hive refers to the process of grouping data based on one or more columns and calculating aggregate functions such as sum, count, average, min, max, etc. on the grouped data.
- Hive supports several aggregate functions, including **COUNT**, **SUM**, **AVG**, **MIN**, **MAX**, etc.
- Aggregation can be performed using the **GROUP BY** clause, which groups the data based on the specified columns and calculates the aggregate functions on the grouped data.
- Hive also supports **HAVING** clause, which can be used to filter the grouped data based on the result of the aggregate functions.
