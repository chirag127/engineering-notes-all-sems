Input formats in MapReduce are classes that define how the input data is split and read by the mapper tasks. They are responsible for creating input splits, which are logical chunks of the input data that can be processed in parallel, and record readers, which read the key-value pairs from the input splits. There are different types of input formats in MapReduce, depending on the format and structure of the input data. Some of the common input formats are:

- FileInputFormat: It is the base class for all file-based input formats. It specifies the input directory that contains the data files to be read. It divides the files into one or more input splits, based on the file size. It also provides methods to filter the files based on a pattern or a custom logic.
- TextInputFormat: It is the default input format. It treats each line of each input file as a separate record. It performs no parsing. It is useful for unformatted data or line-based records like log files. The key is the byte offset of the beginning of the line within the file, and the value is the contents of the line, excluding the line terminators.
- KeyValueTextInputFormat: It is similar to TextInputFormat, but it breaks the line into key and value by a tab character ('\t'). It is useful for formatted data where each line contains a key and a value separated by a delimiter.
- SequenceFileInputFormat: It is an input format that reads sequence files, which are binary files that store serialized key-value pairs. It is useful for reading compressed or complex data types. The key and value are the same as the ones stored in the sequence file.
- NLineInputFormat: It is an input format that splits the input files based on the number of lines specified by the user. It is useful for cases where each mapper task needs to process a fixed number of lines. The key is the byte offset of the first line in the split, and the value is the text of the lines in the split.

The following diagram illustrates the basic architecture of a file-based input format in MapReduce:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Input File   |      |   Input File   |      |   Input File   |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Input Split   |      |  Input Split   |      |  Input Split   |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
| Record Reader  |      | Record Reader  |      | Record Reader  |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Key-Value     |      |  Key-Value     |      |  Key-Value