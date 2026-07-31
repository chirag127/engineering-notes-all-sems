### Output Formats for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

- OutputFormat in MapReduce job provides the RecordWriter implementation to be used to write the output files of the job.
- The output files are stored in a FileSystem. The framework uses FileOutputFormat.setOutputPath() method to set the output directory.
- There are several types of OutputFormat which are as follows   :

  - TextOutputFormat: The default OutputFormat is TextOutputFormat. It writes (key, value) pairs on single lines of text files. The key and value are separated by a tab character .
  - SequenceFileOutputFormat: This OutputFormat writes sequences files for its output. Sequence files are binary files that store serialized key-value pairs .
  - SequenceFileAsBinaryOutputFormat: It is another variant of SequenceFileInputFormat. It converts keys and values to bytes using BytesWritable and writes them as sequence files.
  - MapFileOutputFormat: It is another form of FileOutputFormat. It writes map files for its output. Map files are indexed sequence files that allow random access to the data.
  - MultipleOutputs: It is a subclass of FileOutputFormat that allows writing data to multiple files or multiple formats from a single MapReduce job .
  - LazyOutputFormat: It is a wrapper around FileOutputFormat that prevents the creation of empty files. It creates output files only when there is a record to write .
  - DBOutputFormat: It sends the reduced output to a SQL table. It can be used to write data to relational databases or HBase .