#### Input Formats in Map Reduce

- Input formats are the classes that define how the input data for a MapReduce job is split, read, and processed.
- Input formats are responsible for creating input splits, which are the logical units of work that each mapper operates on.
- Input formats also provide a record reader, which is an object that reads the input split and converts it into key-value pairs that are suitable for the mapper.
- There are different types of input formats in MapReduce, each suited for different kinds of input data. Some of the common input formats are:

  - FileInputFormat: It is the base class for all file-based input formats. It handles common tasks such as splitting files into input splits, validating input paths, and filtering hidden files.
  - TextInputFormat: It is the default input format. It reads each line of a text file as a record, and splits the line by a delimiter (default is tab) into a key and a value. The key is the byte offset of the line, and the value is the line content.
  - KeyValueTextInputFormat: It is similar to TextInputFormat, but it splits the line by the first occurrence of the delimiter, instead of the last. The key is the part before the delimiter, and the value is the part after the delimiter.
  - SequenceFileInputFormat: It is an input format that reads sequence files, which are binary files that store key-value pairs in a compressed and serialized format. Sequence files are suitable for storing large amounts of data that can be efficiently processed by MapReduce.
  - SequenceFileAsTextInputFormat: It is a variant of SequenceFileInputFormat that converts the binary key-value pairs into text key-value pairs, by calling the toString() method on the keys and values. This is useful for debugging or testing purposes.
  - SequenceFileAsBinaryInputFormat: It is another variant of SequenceFileInputFormat that preserves the binary key-value pairs as byte arrays, without any conversion. This is useful for processing binary data that cannot be converted to text.
  - NLineInputFormat: It is an input format that splits the input file into input splits based on the number of lines, instead of the file size. Each input split contains N lines, where N is specified by the user. This is useful for processing files that have a logical structure based on the number of lines, such as XML documents or log files.
  - DBInputFormat: It is an input format that reads data from a relational database, using JDBC. It allows the user to specify a SQL query to select the data to be processed by MapReduce. The query results are converted into key-value pairs, where the key is the primary key of the table, and the value is a DBWritable object that contains the rest of the columns.