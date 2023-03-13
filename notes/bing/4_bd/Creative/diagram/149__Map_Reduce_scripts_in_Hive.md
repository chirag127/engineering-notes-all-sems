Map Reduce scripts in Hive are a way to use custom mappers and reducers in the data stream by using the TRANSFORM clause in the Hive language. The TRANSFORM clause allows the user to specify an executable script that can process the input data and output the transformed data. The script can be written in any language that can read from standard input and write to standard output, such as Python, Ruby, Perl, etc.

The basic architecture of a Map Reduce script in Hive is as follows:

#### Map Reduce scripts in Hive

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Input data   |     |   Map script   |     |   Reduce script|
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Input split  |     |   Map output   |     |   Reduce output|
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

The input data is split into multiple chunks and fed into the map script, which performs some transformation on each chunk and outputs the intermediate results. The map output is then shuffled and sorted by key and fed into the reduce script, which performs some aggregation on the values corresponding to each key and outputs the final results. The reduce output is then stored in the output location specified by the user.