#### Input Formats in MapReduce

- Input formats are the classes that define how the input data for a MapReduce job is split, read, and processed.
- Input formats are responsible for creating input splits, which are the logical units of work that are assigned to different mappers.
- Input formats also provide a record reader, which is the class that reads the input split and converts it into key-value pairs for the mapper.
- Hadoop provides several built-in input formats for different types of input data, such as text, binary, sequence, database, etc.
- Some of the common input formats are:

  - FileInputFormat: It is the base class for all file-based input formats. It handles common tasks such as splitting files, validating input paths, etc. It has two subclasses: TextInputFormat and KeyValueTextInputFormat.
  - TextInputFormat: It is the default input format. It reads each line of a text file as a record, and assigns the byte offset of the line as the key, and the line content as the value.
  - KeyValueTextInputFormat: It is similar to TextInputFormat, but it treats each line of a text file as a key-value pair, separated by a delimiter (default is tab).
  - SequenceFileInputFormat: It is an input format that reads sequence files, which are binary files that store key-value pairs in a compressed and serialized format.
  - SequenceFileAsTextInputFormat: It is a variant of SequenceFileInputFormat, that converts the binary key-value pairs into text and returns them as text key-value pairs.
  - SequenceFileAsBinaryInputFormat: It is another variant of SequenceFileInputFormat, that returns the binary key-value pairs as bytes, without any conversion.
  - NLineInputFormat: It is an input format that splits the input file based on the number of lines specified by the user. Each input split contains N lines of the input file, where N is a configurable parameter.
  - DBInputFormat: It is an input format that reads data from a relational database, using JDBC. It requires the user to specify the database connection parameters, the query to execute, and the input class to map the query results.