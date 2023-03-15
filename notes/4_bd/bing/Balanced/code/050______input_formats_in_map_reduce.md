#### Input formats in map reduce

Input formats are classes that define how to read and split the input data for a map reduce job. They are responsible for creating input splits, which are logical chunks of data that are assigned to different mappers, and records, which are key-value pairs that are processed by the mappers. Input formats also validate the input specification of the job and provide information about the input data, such as the number of files, the size of the files, etc.

There are different types of input formats in map reduce, depending on the format and structure of the input data. Some of the common input formats are:

- FileInputFormat: It is the base class for all file-based input formats. It handles common tasks such as splitting files into input splits, reading files from HDFS, and filtering files based on patterns. It also supports compressed files and directories as input. FileInputFormat has several subclasses that implement specific input formats, such as:

  - TextInputFormat: It is the default input format. It reads each line of a text file as a record, and splits the line by a delimiter (default is tab) into a key and a value. The key is the byte offset of the line, and the value is the line content.

  - KeyValueTextInputFormat: It is similar to TextInputFormat, but it splits the line by the first occurrence of the delimiter into a key and a value. The key and the value are both the line content.

  - SequenceFileInputFormat: It is an input format that reads sequence files, which are binary files that store key-value pairs in a serialized format. Sequence files are efficient and compact, and can handle complex data types.

  - SequenceFileAsTextInputFormat: It is a variant of SequenceFileInputFormat that converts the binary key-value pairs into text and uses the same logic as TextInputFormat to split them into a key and a value.

  - SequenceFileAsBinaryInputFormat: It is another variant of SequenceFileInputFormat that preserves the binary key-value pairs and does not convert them into text.

- NLineInputFormat: It is an input format that splits the input file into input splits based on the number of lines specified by the user. Each input split contains N lines of the input file, and each line is treated as a record with the same logic as TextInputFormat.

- DBInputFormat: It is an input format that reads data from a relational database using JDBC. It splits the input data based on a SQL query provided by the user, and converts each row of the query result into a record with a DBWritable key and value.

- CustomInputFormat: It is possible to create a custom input format by extending the FileInputFormat or the InputFormat class and overriding the methods to define how to read and split the input data. A custom input format can handle any specific or complex data format that is not supported by the existing input formats.