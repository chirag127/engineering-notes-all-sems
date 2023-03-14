Map Reduce scripts in Hive are used to plug in custom mappers and reducers in the data stream by using the TRANSFORM clause in the Hive language. The custom scripts can be written in any executable language such as Python, Ruby, Perl, etc. The scripts can process the input data from stdin and write the output data to stdout. The input and output data are delimited by tabs. The scripts can also specify the input and output schema using the AS clause.

The following diagram illustrates the basic architecture of a Map Reduce script in Hive:

#### Map Reduce scripts in Hive

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Hive Table   |      |   Map Script   |      |   Reduce Script|
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  col1 | col2   |      |  col1 | col2   |      |  col3 | col4   |
|----------------|      |----------------|      |----------------|
|  a    | 1      |----->|  a    | 1      |----->|  a    | 2      |
|  b    | 2      |----->|  b    | 2      |----->|  b    | 4      |
|  a    | 1      |----->|  a    | 1      |----->|  c    | 3      |
|  c    | 3      |----->|  c    | 3      |----->|                |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

The map script can perform some transformation or filtering on the input data, such as converting the values to uppercase or removing the duplicates. The reduce script can perform some aggregation or grouping on the output of the map script, such as counting the occurrences of each key or finding the average of each group. The output of the reduce script can be stored in another Hive table or a file.

An example of a Hive query that uses a Map Reduce script is:

```sql
FROM (
  FROM table1
  MAP table1.col1, table1.col2
  USING 'map_script'
  AS mp1, mp2
  CLUSTER BY mp1
) map_output
INSERT OVERWRITE TABLE table2
REDUCE map_output.mp1, map_output.mp2
USING 'reduce_script'
AS reducef1, reducef2;
```

This query will run the map_script on the input data from table1, and then run the reduce_script on the output of the map_script. The final output will be stored in table2. The map_script and reduce_script can be any executable files that follow the input and output format described above.