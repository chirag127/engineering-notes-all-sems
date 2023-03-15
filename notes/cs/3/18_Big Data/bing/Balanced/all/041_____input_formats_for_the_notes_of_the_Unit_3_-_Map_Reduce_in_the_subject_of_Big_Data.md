# Input Formats for Map Reduce

- Input formats are classes that define how to read and split the input data for a map reduce job.
- Input formats are responsible for creating input splits, which are logical chunks of the input data that can be processed by a single mapper.
- Input formats are also responsible for creating record readers, which are classes that read and parse the records from the input splits and provide key-value pairs to the mapper.
- Input formats can be specified by the user using the `mapreduce.inputformat.class` property in the job configuration.
- There are different types of input formats available in Hadoop, each suited for a different kind of input data. Some of the common input formats are:

  - FileInputFormat: It is the base class for all file-based input formats. It handles common tasks such as validating input paths, splitting files into input splits, and creating record readers. It also provides methods to filter files based on patterns or modification time.
  - TextInputFormat: It is the default input format. It reads each line of a text file as a record and splits it by the tab character. The key is the byte offset of the line and the value is the line content.
  - KeyValueTextInputFormat: It is similar to TextInputFormat, but it splits each line by the first tab character. The key is the part before the tab and the value is the part after the tab.
  - SequenceFileInputFormat: It is an input format that reads sequence files, which are binary files that store key-value pairs in a compressed and serialized format. It preserves the key and value types of the sequence file as the output key and value types of the mapper.
  - SequenceFileAsTextInputFormat: It is a variant of SequenceFileInputFormat that converts the key and value of the sequence file to text by calling their `toString()` methods. The output key and value types of the mapper are `LongWritable` and `Text`, respectively.
  - SequenceFileAsBinaryInputFormat: It is another variant of SequenceFileInputFormat that reads the key and value of the sequence file as raw bytes. The output key and value types of the mapper are `BytesWritable`.
  - NLineInputFormat: It is an input format that splits the input file based on the number of lines specified by the user. Each input split contains N lines of the input file, where N is configurable by the `mapreduce.input.lineinputformat.linespermap` property. The output key and value types of the mapper are `LongWritable` and `Text`, respectively.
  - DBInputFormat: It is an input format that reads data from a relational database using JDBC. It requires the user to specify the database connection parameters, the query to execute, and the class that implements the `DBWritable` interface to map the database records to key-value pairs. The output key and value types of the mapper depend on the `DBWritable` implementation.