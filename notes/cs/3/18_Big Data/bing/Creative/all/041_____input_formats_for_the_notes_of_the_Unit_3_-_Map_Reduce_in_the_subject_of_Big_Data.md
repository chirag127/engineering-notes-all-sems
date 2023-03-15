# Input Formats for Map Reduce

- Input formats are classes that define how the input data for a MapReduce job is split, read, and processed.
- Input formats are responsible for creating input splits, which are logical chunks of the input data that are assigned to different mappers.
- Input formats are also responsible for creating records, which are key-value pairs that represent the input data for the mapper function.
- Input formats are specified by the `mapreduce.inputformat.class` property in the job configuration.
- There are different types of input formats available in Hadoop, each suited for different kinds of input data and use cases.

## Types of Input Formats

- FileInputFormat: It is the base class for all file-based input formats. It handles common tasks such as splitting files, validating input paths, and creating record readers. It also provides some subclasses for different file formats, such as:

  - TextInputFormat: It is the default input format. It reads each line of a text file as a record, with the byte offset as the key and the line content as the value.
  - KeyValueTextInputFormat: It is similar to TextInputFormat, but it treats each line of a text file as a key-value pair, separated by a delimiter (default is tab).
  - SequenceFileInputFormat: It reads sequence files, which are binary files that store key-value pairs in a compressed and serialized format.
  - SequenceFileAsTextInputFormat: It is a variant of SequenceFileInputFormat that converts the binary key-value pairs into text format.
  - SequenceFileAsBinaryInputFormat: It is another variant of SequenceFileInputFormat that preserves the binary key-value pairs as they are.
  - NLineInputFormat: It reads N lines of a text file as a single record, where N is specified by the user.
  - DBInputFormat: It reads data from a relational database using JDBC.

- CombineFileInputFormat: It is an abstract input format that combines multiple small files into a single split, to reduce the overhead of launching too many mappers. It also allows specifying a custom logic for grouping files based on their size, location, or other criteria.
- MultipleInputs: It is a utility class that allows using multiple input formats and paths for a MapReduce job. It can be useful when the input data is heterogeneous and requires different processing logic.
- Custom Input Format: It is possible to create a custom input format by extending the FileInputFormat class or implementing the InputFormat interface. A custom input format should provide a custom input split class and a custom record reader class. A custom input format can be useful when the input data has a complex or non-standard format that is not supported by the existing input formats.