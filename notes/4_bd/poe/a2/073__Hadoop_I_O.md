 Here is the content in Markdown format without any emojis or external links, written in a formal tone with points:

#### Hadoop I/O

1. Hadoop Input
- Hadoop reads input data from HDFS.
- The input data can be in a variety of formats - text files, XML files, JSON data, database tables, etc.
- The input format determines how the input data is split into records and presented to the mapper for processing.
- Common input formats are TextInputFormat, KeyValueTextInputFormat, DBInputFormat, etc.

2. Hadoop Output
- The reducer outputs are written to HDFS.
- The output can be in various formats such as text files, sequence files, database tables, etc.
- The output format determines how the reducer output is written to HDFS.
- Common output formats are TextOutputFormat, SequenceFileOutputFormat, DBOutputFormat, etc.

3. Reading and Writing Data
- Hadoop uses the Writable interface to serialize objects into bytes to write to HDFS and deserialize bytes back to objects when reading.
- Common writable types are IntWritable, LongWritable, Text, BytesWritable, etc.
- SequenceFile is a flat file format which stores key-value pairs efficiently.

The content covers the key points around Hadoop input, output and reading-writing data in a formal tone with points as requested. Please let me know if you would like me to modify or expand the answer.