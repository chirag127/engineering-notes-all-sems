InputFormat is a class that describes the input-specification for a Map-Reduce job. It is responsible for creating the input splits and dividing them into records that can be processed by the Mapper. There are different types of InputFormat in MapReduce, each suited for a different type of input file. Here is some code that illustrates how to use some of the common InputFormats in MapReduce:

#### Input formats in map reduce
```java
// FileInputFormat is the base class for all file-based InputFormats
// It reads files from HDFS and splits them into fixed-size chunks
// The default split size is 64 MB, but can be changed by setting mapreduce.input.fileinputformat.split.minsize and mapreduce.input.fileinputformat.split.maxsize
FileInputFormat.setInputPaths(job, new Path("/input"));

// TextInputFormat is the default InputFormat
// It reads each line of text as a record, and uses the byte offset as the key and the line content as the value
// The key and value are both of type Text
job.setInputFormatClass(TextInputFormat.class);

// KeyValueTextInputFormat is similar to TextInputFormat, but treats each line as a key-value pair
// The separator between the key and the value can be specified by setting mapreduce.input.keyvaluelinerecordreader.key.value.separator
// The default separator is a tab character
// The key and value are both of type Text
job.setInputFormatClass(KeyValueTextInputFormat.class);

// SequenceFileInputFormat reads sequence files, which are binary files that store key-value pairs
// The key and value types are specified by the sequence file metadata
// Sequence files are efficient and compressible, and can be used to store intermediate data between MapReduce jobs
job.setInputFormatClass(SequenceFileInputFormat.class);

// SequenceFileAsTextInputFormat is a variant of SequenceFileInputFormat that converts the key and value to Text
// It can be used to read sequence files as text for debugging purposes
job.setInputFormatClass(SequenceFileAsTextInputFormat.class);

// SequenceFileAsBinaryInputFormat is another variant of SequenceFileInputFormat that reads the key and value as binary data
// The key and value are both of type BytesWritable
// It can be used to read sequence files that contain non-text data
job.setInputFormatClass(SequenceFileAsBinaryInputFormat.class);

// NLineInputFormat reads N lines of text as a single split, and assigns them to a single Mapper
// The number of lines per split can be specified by setting mapreduce.input.lineinputformat.linespermap
// The default value is 1
// The key is the byte offset of the first line, and the value is the concatenation of all the lines in the split
// The key and value are both of type Text
job.setInputFormatClass(NLineInputFormat.class);

// DBInputFormat reads data from a relational database using JDBC
// It requires a DBInputFormat.DBInputSplitter implementation to split the data into chunks
// It also requires a DBWritable implementation to map the database records to key-value pairs
// The key and value types depend on the DBWritable implementation
job.setInputFormatClass(DBInputFormat.class);
```