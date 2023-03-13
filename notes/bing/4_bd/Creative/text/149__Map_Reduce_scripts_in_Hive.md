#### Map Reduce scripts in Hive

- Map Reduce scripts in Hive are used to plug in custom mappers and reducers in the data stream by using the TRANSFORM clause in the Hive language .
- The TRANSFORM clause allows the user to specify an executable script that can process the input records and generate the output records .
- The script can be written in any language that can read from standard input and write to standard output, such as Python, Ruby, Perl, etc .
- The syntax of the TRANSFORM clause is as follows:

```sql
SELECT TRANSFORM (input_columns)
USING 'script'
AS output_columns
FROM table
```

- The input_columns are the columns from the table that are passed to the script as tab-separated values .
- The script is the path to the executable script file that can be either local or on HDFS .
- The output_columns are the columns that are returned by the script as tab-separated values .
- The TRANSFORM clause can be used in both the map and the reduce phases of the Map Reduce job .
- For example, to run a custom mapper script - map_script - and a custom reducer script - reduce_script - the user can issue the following command:

```sql
FROM (
  FROM table
  MAP input_columns
  USING 'map_script'
  AS map_output_columns
  CLUSTER BY map_output_columns
) map_output
REDUCE map_output_columns
USING 'reduce_script'
AS reduce_output_columns;
```

- The MAP keyword indicates that the script is used as a mapper, and the REDUCE keyword indicates that the script is used as a reducer .
- The CLUSTER BY clause is used to partition the mapper output by the key columns .
- The map_output_columns and the reduce_output_columns must have the same number and type of columns .
- Map Reduce scripts in Hive can be useful for performing complex data transformations that are not supported by the built-in Hive functions or UDFs.
- Map Reduce scripts in Hive can also be used to integrate with external libraries or tools that can provide additional functionality or performance.