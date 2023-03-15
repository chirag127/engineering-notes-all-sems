
#### Sorting and Aggregating in Hive

* Hive supports sorting and aggregating data in two ways: sorting and bucketing. 
* Sorting is used to order the data in ascending or descending order based on a column. 
* Bucketing is used to group the data into buckets based on a column. 
* Hive supports sorting and bucketing using the ORDER BY, SORT BY and CLUSTER BY clauses in a query. 
* Hive also provides the ability to store sorted and bucketed data in a separate file format called ORC (Optimized Row Columnar). 
* ORC files are more efficient than regular text files and can be used to improve query performance. 
* Hive also provides the ability to perform aggregations on data including COUNT, SUM, AVG, MIN, MAX, etc. 
* Aggregations can be performed using the GROUP BY clause in a query. 
* Hive also provides the ability to store aggregated data in a separate file format called Parquet. 
* Parquet files are more efficient than regular text files and can be used to improve query performance. 
* Hive also provides the ability to perform window functions on data including LEAD, LAG, RANK, DENSE_RANK, etc. 
* Window functions can be performed using the WINDOW clause in a query. 
* Hive also provides the ability to store window function results in a separate file format called Avro. 
* Avro files are more efficient than regular text files and can be used to improve query performance.