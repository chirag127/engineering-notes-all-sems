#### Input formats in map reduce

Input formats are the classes that define how the input data for a map reduce job is split, read and processed. Input formats are responsible for creating input splits, which are the logical chunks of data that are assigned to different mappers. Input formats also provide a record reader, which is the class that reads the key-value pairs from the input split and passes them to the mapper.

There are different types of input formats in map reduce, depending on the format and structure of the input data. Some of the common input formats are:

- FileInputFormat: It is the base class for all file-based input formats. It handles common tasks such as splitting files into input splits, validating input files, and providing a generic record reader. FileInputFormat supports compressed files and directories as input.
- TextInputFormat: It is the default input format. It reads each line of text from the input file as a record, and splits the line by a delimiter (default is tab) into a key and a value. The key is the byte offset of the line, and the value is the line content.
- KeyValueTextInputFormat: It is similar to TextInputFormat, but it splits the line by the first occurrence of the delimiter into a key and a value. The key and the value are both text.
- SequenceFileInputFormat: It is an input format that reads sequence files, which are binary files that store key-value pairs in a serialized format. Sequence files are suitable for storing large amounts of data in a compressed and efficient way.
- SequenceFileAsTextInputFormat: It is a variant of SequenceFileInputFormat that converts the binary key-value pairs into text and passes them to the mapper.
- SequenceFileAsBinaryInputFormat: It is another variant of SequenceFileInputFormat that passes the binary key-value pairs as bytes to the mapper, without any conversion.
- NLineInputFormat: It is an input format that splits the input file into input splits based on the number of lines specified by the user. Each input split contains N lines of the input file, where N is a configurable parameter. This input format is useful for cases where each line is an independent task that requires a lot of computation.
- DBInputFormat: It is an input format that reads data from a relational database using JDBC. It splits the query results into input splits based on a primary key column or a user-defined query. Each input split contains a range of rows from the database table.

The following is a possible ASCII diagram that illustrates the input formats in map reduce:

```
+-----------------+     +-----------------+     +-----------------+
|  Input File(s)  |     |  Input File(s)  |     |  Input File(s)  |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          v                     v                     v
+-----------------+     +-----------------+     +-----------------+
|  Input Format   |     |  Input Format   |     |  Input Format   |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Split the file |     |  Split the file |     |  Split the file |
|  into input     |     |  into input     |     |  into input     |
|  splits based   |     |  splits based   |     |  splits based   |
|  on the format  |     |  on the format  |     |  on the format  |
|  and size       |     |  and size       |     |  and size       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          v                     v

```
