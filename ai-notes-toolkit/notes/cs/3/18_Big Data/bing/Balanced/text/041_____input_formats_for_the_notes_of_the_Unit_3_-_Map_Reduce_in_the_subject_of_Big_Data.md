### Input Formats for Map Reduce

- Input formats are classes that define how to read and split the input data for a map reduce job.
- Input formats are responsible for creating input splits, which are logical chunks of data that are assigned to different mappers, and records, which are key-value pairs that are processed by the mappers.
- Input formats also provide a record reader, which is an object that reads the records from the input split and converts them into key-value pairs.
- There are different types of input formats for different types of input data, such as text files, binary files, database tables, etc.
- Some of the common input formats are    :

  - FileInputFormat: It is the base class for all file-based input formats. It handles common tasks such as validating input paths, splitting files into input splits, and creating record readers.
  - TextInputFormat: It is the default input format. It reads each line of a text file as a record, and splits the line by a delimiter (default is tab) into a key-value pair. The key is the byte offset of the line, and the value is the line content.
  - KeyValueTextInputFormat: It is similar to TextInputFormat, but it splits the line by the first delimiter into a key-value pair. The key and value are both text.
  - SequenceFileInputFormat: It is an input format that reads sequence files, which are binary files that store key-value pairs in a compressed and serialized format. The key and value types are specified by the user.
  - SequenceFileAsTextInputFormat: It is a variant of SequenceFileInputFormat that converts the key-value pairs into text by calling toString() method on them.
  - SequenceFileAsBinaryInputFormat: It is another variant of SequenceFileInputFormat that preserves the binary format of the key-value pairs and does not convert them into text.
  - NLineInputFormat: It is an input format that splits the input file into input splits based on the number of lines specified by the user. Each input split contains N lines, and each line is a record. The key is the byte offset of the line, and the value is the line content.
  - DBInputFormat: It is an input format that reads data from a database table. The user specifies the database connection parameters, the query to execute, and the input class that maps the query result to a key-value pair. The key and value types are specified by the user.