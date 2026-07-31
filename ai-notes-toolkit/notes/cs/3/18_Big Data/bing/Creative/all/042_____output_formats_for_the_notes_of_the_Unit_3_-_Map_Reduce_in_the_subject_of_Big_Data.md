# Output Formats for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

- OutputFormat is a component of MapReduce that defines how the output files of a job are written, stored and organized in a FileSystem.
- OutputFormat also provides a RecordWriter implementation that is responsible for writing the output records of the individual tasks.
- The default OutputFormat is TextOutputFormat, which writes plain text files as output.
- There are other types of OutputFormat that can be used for different purposes, such as:
  - SequenceFileOutputFormat: This OutputFormat writes sequences files for its output. Sequence files are binary files that store key-value pairs in a compressed format.
  - SequenceFileAsBinaryOutputFormat: This OutputFormat is another variant of SequenceFileOutputFormat that writes the keys and values as binary data instead of using Writable serialization.
  - MapFileOutputFormat: This OutputFormat is another form of FileOutputFormat that writes map files for its output. Map files are indexed sequence files that allow random access to the data.
  - MultipleOutputs: This OutputFormat allows writing to multiple output files with different names and formats from a single MapReduce job.
  - LazyOutputFormat: This OutputFormat prevents the creation of empty output files by wrapping around another OutputFormat and only creating output files when they are needed.
  - DBOutputFormat: This OutputFormat sends the reduced output to a SQL table. It can be used to write output to relational databases or HBase.
- The OutputFormat can be specified by using the FileOutputFormat.setOutputPath() method to set the output directory and the Job.setOutputFormatClass() method to set the OutputFormat class.
- The OutputFormat is an important part of the MapReduce programming model, which is used to process large-scale data sets in parallel on a distributed system.
- The MapReduce model consists of two phases: map and reduce. The map phase takes input pairs, processes them, and produces another set of intermediate pairs as output. The reduce phase takes the intermediate pairs, groups them by key, and performs some aggregation or transformation on the values.
- The map and reduce functions are represented as key-value pairs and are subject to parallel execution of datasets situated in a wide array of machines in a distributed architecture.
- The OutputFormat determines how the final output of the reduce phase is written and stored in the FileSystem.