### Input Formats for Map Reduce

- Input formats are classes that define how to read and split the input data for a MapReduce job.
- Input formats are responsible for creating input splits, which are logical chunks of data that are assigned to different mappers.
- Input formats also define how to convert the input data into key-value pairs, which are the input for the map function.
- There are different types of input formats for different types of data, such as text, binary, database, etc.
- Some of the common input formats are:

  - FileInputFormat: It is the base class for all file-based input formats. It handles common tasks such as validating input paths, splitting files into input splits, and creating record readers.
  - TextInputFormat: It is the default input format. It reads each line of a text file as a record, and splits the line by a delimiter (default is tab) into a key-value pair. The key is the byte offset of the line, and the value is the line content.
  - KeyValueTextInputFormat: It is similar to TextInputFormat, but it splits the line by the first delimiter into a key-value pair. The key and value are both text.
  - SequenceFileInputFormat: It is an input format that reads sequence files, which are binary files that store key-value pairs in a compressed and serialized format. Sequence files are suitable for storing large amounts of data that can be processed efficiently by MapReduce.
  - SequenceFileAsTextInputFormat: It is a variant of SequenceFileInputFormat that converts the binary key-value pairs into text by calling toString() method on them. It is useful for debugging sequence files.
  - SequenceFileAsBinaryInputFormat: It is another variant of SequenceFileInputFormat that preserves the binary key-value pairs as bytes. It is useful for processing binary data that cannot be converted to text.
  - NLineInputFormat: It is an input format that splits the input file into input splits based on the number of lines specified by a configuration property. Each input split contains N lines of the input file, and each line is treated as a record. The key is the byte offset of the line, and the value is the line content. This input format is useful for processing files that have a fixed number of lines per record, such as log files.
  - DBInputFormat: It is an input format that reads data from a relational database using JDBC. It requires a database driver, a connection URL, a query, and a class that implements DBWritable interface to map the database columns to the key-value pair fields. This input format is useful for integrating MapReduce with existing data sources.