### Input Formats for Map Reduce

Input formats are the classes that define how the input data is split, read, and processed by the map function in a MapReduce job. Input formats also determine the key-value pair types that are passed to the mapper. Different types of input formats are suitable for different types of input data. Some of the common input formats are:

- **FileInputFormat**: It is the base class for all file-based input formats. It handles common tasks such as splitting the input files into logical input splits, validating the input specifications, and providing the record reader implementation to read the input records. FileInputFormat supports compressed files and directories as input. Subclasses of FileInputFormat include:

  - **TextInputFormat**: It is the default input format. It reads each line of text from the input file as a record. The key is the byte offset of the line, and the value is the line content. It is suitable for plain text files, such as log files, CSV files, etc.

  - **KeyValueTextInputFormat**: It is similar to TextInputFormat, but it treats each line of text as a key-value pair. The separator character (by default, a tab) determines the boundary between the key and the value. It is suitable for text files where each line has a key and a value, such as properties files, XML files, etc.

  - **SequenceFileInputFormat**: It is an input format that reads sequence files. Sequence files are binary files that store serialized key-value pairs. They are efficient and compact, and can handle complex data types such as images, audio, video, etc.

  - **SequenceFileAsTextInputFormat**: It is a variant of SequenceFileInputFormat that converts the binary key-value pairs in the sequence file to text. The key and the value are converted to strings using their toString() methods, and separated by a tab. It is useful for debugging or testing purposes.

  - **SequenceFileAsBinaryInputFormat**: It is another variant of SequenceFileInputFormat that preserves the binary key-value pairs in the sequence file. The key and the value are wrapped in BytesWritable objects, and passed to the mapper as such. It is useful for processing binary data without any conversion.

  - **NLineInputFormat**: It is an input format that splits the input file based on the number of lines specified by the user. Each input split contains N lines of the input file, where N is a configurable parameter. It is useful for cases where each line of the input file is an independent logical unit, such as a file name, a URL, a command, etc.

  - **DBInputFormat**: It is an input format that reads data from a relational database using JDBC. It can execute a SQL query and return the results as key-value pairs. The key is a LongWritable that represents the record number, and the value is a DBWritable that holds the fields of the record. It is useful for importing data from a database to Hadoop for further processing.

- **CombineFileInputFormat**: It is an abstract input format that returns CombineFileSplit's in the getSplits() method. A CombineFileSplit is a logical input split that groups multiple smaller files into a single split. It is useful for reducing the number of map tasks and improving the data locality when dealing with a large number of small files.

- **Custom InputFormat**: It is possible to create a custom input format by extending the InputFormat abstract class and implementing its abstract methods. A custom input format can handle any type of input data that is not supported by the existing input formats, or provide a different way of splitting, reading, or processing the input data. A custom input format must also provide a custom record reader that implements the RecordReader interface and defines how to read the records from the input split.