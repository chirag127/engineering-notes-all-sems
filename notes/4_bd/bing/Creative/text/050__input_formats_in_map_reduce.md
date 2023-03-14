#### Input Formats in Map Reduce

Input formats are classes that define how to read and process input data for a MapReduce job. Input formats are responsible for:

- Validating the input specification of the job.
- Splitting the input data into logical chunks called input splits, which are assigned to individual mappers.
- Creating record readers, which read and parse the input records from the input splits.

There are different types of input formats in MapReduce, each suited for a different kind of input data. Some of the common input formats are:

- FileInputFormat: This is the base class for all file-based input formats. It reads files from a given directory or a list of directories in HDFS, and splits them based on their size. It also provides methods to filter files based on their names or extensions.
- TextInputFormat: This is the default input format for MapReduce. It treats each line of each input file as a separate record. The key is the byte offset of the beginning of the line within the file, and the value is the content of the line excluding the line terminator.
- KeyValueTextInputFormat: This is similar to TextInputFormat, but it splits each line of input into a key and a value based on a separator character, which is a tab by default. The key and the value are both text.
- SequenceFileInputFormat: This is an input format that reads sequence files, which are binary files that store key-value pairs. Sequence files are efficient and compressible, and can handle complex data types such as arrays and maps.
- SequenceFileAsTextInputFormat: This is a variant of SequenceFileInputFormat that converts the binary key-value pairs in sequence files into text. The key and the value are both converted to hexadecimal strings.
- SequenceFileAsBinaryInputFormat: This is another variant of SequenceFileInputFormat that preserves the binary key-value pairs in sequence files. The key and the value are both byte arrays.
- NLineInputFormat: This is an input format that splits the input based on the number of lines per split, which can be specified by the user. Each split contains N lines of input, where N is a configurable parameter. This is useful for cases where each line of input requires a lot of processing and the number of mappers needs to be controlled.
- DBInputFormat: This is an input format that reads data from a relational database using JDBC. It splits the input based on a SQL query that can be specified by the user. Each split contains a range of rows from the database table. The key is the primary key of the table, and the value is a DBWritable object that contains the rest of the columns.