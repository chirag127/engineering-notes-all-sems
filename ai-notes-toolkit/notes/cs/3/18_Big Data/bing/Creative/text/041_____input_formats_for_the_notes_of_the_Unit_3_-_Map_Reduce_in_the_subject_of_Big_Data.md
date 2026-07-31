### Input Formats for Map Reduce

- Input formats are classes that define how the input data for a MapReduce job is split, read, and processed.
- Input formats are responsible for creating input splits, which are logical chunks of the input data that are assigned to different mappers.
- Input formats are also responsible for creating records, which are key-value pairs that represent the input data for the mapper function.
- There are different types of input formats for different types of input data, such as text files, binary files, database tables, etc.
- Some of the common input formats are:

  - FileInputFormat: It is the base class for all file-based input formats. It handles common tasks such as splitting files, validating input paths, etc. It has two abstract methods: isSplitable() and createRecordReader(), which need to be implemented by subclasses.
  - TextInputFormat: It is the default input format. It reads each line of a text file as a record, with the byte offset of the line as the key and the line content as the value.
  - KeyValueTextInputFormat: It is similar to TextInputFormat, but it treats each line of a text file as a key-value pair, separated by a delimiter (default is tab).
  - SequenceFileInputFormat: It reads sequence files, which are binary files that store key-value pairs in a compressed and serialized format.
  - SequenceFileAsTextInputFormat: It is a variant of SequenceFileInputFormat, but it converts the binary key-value pairs into text before passing them to the mapper.
  - SequenceFileAsBinaryInputFormat: It is another variant of SequenceFileInputFormat, but it preserves the binary key-value pairs and passes them to the mapper as bytes.
  - NLineInputFormat: It reads N lines of a text file as a single split, where N can be specified by the user. This is useful for cases where each line is an independent input for the mapper.
  - DBInputFormat: It reads data from a relational database table using JDBC. It splits the table by a primary key column and creates records with the column values as the key-value pair.