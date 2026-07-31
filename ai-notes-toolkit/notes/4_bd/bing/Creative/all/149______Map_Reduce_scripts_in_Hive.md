#### Map Reduce Scripts in Hive

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed manner.
- Hive is a data warehousing platform that supports SQL-like queries and Map Reduce operations on structured and semi-structured data.
- Users can plug in their own custom mappers and reducers in the data stream by using the TRANSFORM clause in the Hive language .
- The TRANSFORM clause allows the user to specify an executable script or program that can read the input data from the standard input and write the output data to the standard output.
- The input and output data are in the form of tab-separated text records, where each record is a single line and each field is separated by a tab character.
- The user can also specify the input and output schema of the script or program by using the AS clause.
- The user can use the MAPREDUCE keyword to indicate that the script or program is a Map Reduce job, and provide the necessary configuration parameters for the job.
- The user can also use the CLUSTER BY, DISTRIBUTE BY, and SORT BY clauses to control the partitioning and sorting of the data before and after the script or program execution.
- The user can use the GROUP BY and HAVING clauses to perform aggregations on the output data of the script or program.
- The user can use the SELECT clause to project the output data of the script or program to the desired columns.
- The user can use the INSERT clause to store the output data of the script or program to a Hive table or a file system location.
- The user can use the EXPLAIN clause to view the execution plan of the query involving the script or program.
- The user can use the SET clause to set the Hive or Map Reduce configuration properties for the query involving the script or program.
- The user can use the ADD clause to add the script or program file or other resources to the distributed cache for the query involving the script or program.