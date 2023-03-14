MapReduce is a programming model and an associated implementation for processing and generating big datasets with a parallel, distributed algorithm on a cluster. A MapReduce program is composed of a map procedure, which performs filtering and sorting, and a reduce method, which performs a summary operation. The map and reduce functions in Hadoop MapReduce have the following general form:

map: (K1, V1) → list (K2, V2)
reduce: (K2, list (V2)) → list (K3, V3)

The input parameters of the key and value pair, represented by K1 and V1 respectively, are different from the output pair type: K2 and V2. The reduce function accepts the same format output by the map, but the type of output again of the reduce operation is different: K3 and V3.

There are different types of MapReduce based on the input and output formats of the data. The input and output formats are classes that implement the InputFormat and OutputFormat interfaces respectively. They are responsible for creating and validating the input and output specifications, such as the input and output directories, files, and record boundaries.

Some of the common input and output formats are:

- TextInputFormat: Reads plain text files and splits them by newline characters. The key is the byte offset of the line, and the value is the line content.
- KeyValueTextInputFormat: Reads plain text files and splits them by tab characters. The key is the text before the first tab, and the value is the text after the first tab.
- SequenceFileInputFormat: Reads binary files that store sequences of key-value pairs. The key and value types are specified by the file.
- SequenceFileOutputFormat: Writes binary files that store sequences of key-value pairs. The key and value types are specified by the job configuration.
- TextOutputFormat: Writes plain text files. The key and value are converted to strings and separated by a tab character.

The following diagram illustrates the basic architecture of a MapReduce job using TextInputFormat and TextOutputFormat:

```
+-----------------+     +-----------------+     +-----------------+
| Input File 1    |     | Input File 2    |     | Input File 3    |
|                 |     |                 |     |                 |
| line 1          |     | line 4          |     | line 7          |
| line 2          |     | line 5          |     | line 8          |
| line 3          |     | line 6          |     | line 9          |
+-----------------+     +-----------------+     +-----------------+
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
+-----------------+     +-----------------+     +-----------------+
| Mapper 1        |     | Mapper 2        |     | Mapper 3        |
|                 |     |                 |     |                 |
| map(line 1)     |     | map(line 4)     |     | map(line 7)     |
| map(line 2)     |     | map(line 5)     |     | map(line 8)     |
| map(line 3)     |     | map(line 6)     |     | map(line 9)     |
+-----------------+     +-----------------+     +-----------------+
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         +----------+-----------+-----------+----------+
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    |                      |
                    v                      v
+-----------------+     +-----------------+     +-----------------+
| Reducer 1       |     | Reducer 2       |     | Reducer 3       |
|                 |     |                 |     |                 |
| reduce(K2, V2)  |     | reduce(K2