### Input Formats for Map Reduce

- InputFormat is a class that describes the input-specification for a MapReduce job.
- InputFormat is responsible for:
  - Validating the input-specification of the job.
  - Splitting the input file(s) into logical InputSplits, each of which is then assigned to an individual mapper.
  - Providing the RecordReader implementation to be used to extract key and value pairs from the InputSplit.
- InputFormat has two generic parameters: <K, V>, which represent the types of key and value pairs that the RecordReader will generate.
- The default InputFormat is TextInputFormat, which reads plain text files line by line and returns the byte offset as the key and the line content as the value.
- There are other types of InputFormat available in Hadoop, such as:
  - KeyValueTextInputFormat: Reads plain text files where each line is a key-value pair separated by a delimiter (default is tab).
  - SequenceFileInputFormat: Reads binary files that store sequences of key-value pairs in a compressed and serialized format.
  - SequenceFileAsTextInputFormat: Reads sequence files as plain text, converting the binary key and value to Text objects.
  - SequenceFileAsBinaryInputFormat: Reads sequence files as binary, returning the raw bytes of key and value as BytesWritable objects.
  - NLineInputFormat: Reads plain text files and splits them into N lines per split, where N is specified by the user.
  - DBInputFormat: Reads data from a relational database using JDBC.
- The user can also implement custom InputFormat and RecordReader classes to support other types of input data.