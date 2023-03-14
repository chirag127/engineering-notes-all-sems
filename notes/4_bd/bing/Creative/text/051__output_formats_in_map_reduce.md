#### Output Formats in MapReduce

- OutputFormat is a class that describes the output-specification for a MapReduce job.
- The MapReduce framework relies on the OutputFormat of the job to:
  - Validate the output-specification of the job. For example, check that the output directory does not already exist, throwing an exception when it does, so that output is not overwritten.
  - Provide the RecordWriter implementation to be used to write out the output files of the job. Output files are stored in a FileSystem.
  - Get the output committer for the job. This is responsible for ensuring the output is committed correctly.
- The framework uses FileOutputFormat.setOutputPath() method to set the output directory.
- There are different types of OutputFormat in MapReduce, such as:
  - TextOutputFormat: The default OutputFormat is TextOutputFormat. It writes plain text files as output. Each key-value pair is written as a line, separated by a tab character.
  - SequenceFileOutputFormat: This OutputFormat writes sequence files for its output. Sequence files are binary files that store serialized key-value pairs.
  - SequenceFileAsBinaryOutputFormat: It is another variant of SequenceFileOutputFormat. It converts keys and values to bytes using BytesWritable and writes them as sequence files.
  - MapFileOutputFormat: It is another form of FileOutputFormat. It writes map files as output. Map files are a special type of sequence files that support random access and compression.
  - MultipleOutputs: It is a class that allows writing to multiple output files from a MapReduce job. It can be used to write different types of output from the same job, such as text, sequence, or map files.
  - LazyOutputFormat: It is a class that prevents the creation of empty output files. It delays the creation of output files until the first record is written to them.
  - DBOutputFormat: It is a class that allows writing to a relational database as output. It uses JDBC to connect to the database and insert records.