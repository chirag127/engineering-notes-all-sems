### Input Formats for Map Reduce

- Input formats are classes that define how to read and split the input data for a MapReduce job.
- Input formats are responsible for creating input splits, which are logical chunks of data that are assigned to different mappers.
- Input formats also define how to convert the input data into key-value pairs, which are the input for the map function.
- There are different types of input formats in Hadoop, each suited for different kinds of data and use cases.
- Some of the common input formats are:

  - FileInputFormat: It is the base class for all file-based input formats. It handles common tasks such as splitting files, validating input paths, and creating record readers.
  - TextInputFormat: It is the default input format. It reads each line of a text file as a record, and splits the line by a delimiter (default is tab) into a key and a value. The key is the byte offset of the line, and the value is the line content.
  - KeyValueTextInputFormat: It is similar to TextInputFormat, but it splits the line by the first delimiter into a key and a value. The key and value are both text.
  - SequenceFileInputFormat: It is an input format that reads sequence files, which are binary files that store key-value pairs in a compressed and serialized format. Sequence files are suitable for storing large amounts of data that can be processed efficiently by MapReduce.
  - SequenceFileAsTextInputFormat: It is a variant of SequenceFileInputFormat that converts the binary key-value pairs into text and returns them as text key-value pairs.
  - SequenceFileAsBinaryInputFormat: It is another variant of SequenceFileInputFormat that returns the binary key-value pairs as bytes without any conversion.
  - NLineInputFormat: It is an input format that splits the input file into N-line chunks, where N is specified by the user. Each chunk is assigned to a mapper, and each line in the chunk is treated as a record. This input format is useful for processing small files or files that need to be processed as a whole by a mapper.
  - DBInputFormat: It is an input format that reads data from a relational database using JDBC. It allows users to specify a query to select the data to be processed by MapReduce. The query results are converted into key-value pairs, where the key is the primary key of the table, and the value is a DBWritable object that holds the rest of the columns.