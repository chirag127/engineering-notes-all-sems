### Output Formats for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

- OutputFormat in MapReduce job provides the RecordWriter implementation to be used to write the output files of the job.
- The output files are stored in a FileSystem. The framework uses FileOutputFormat.setOutputPath() method to set the output directory.
- There are several types of OutputFormat which are as follows   :

  - TextOutputFormat: The default OutputFormat is TextOutputFormat. It writes (key, value) pairs on single lines of text files. The key and value are separated by a tab character .
  - SequenceFileOutputFormat: This OutputFormat writes sequences files for its output. Sequence files are binary files that store serialized key-value pairs .
  - SequenceFileAsBinaryOutputFormat: It is another variant of SequenceFileInputFormat. It converts keys and values to bytes arrays and then writes them to sequence files.
  - MapFileOutputFormat: It is another form of FileOutputFormat. It writes map files for its output. Map files are indexed sequence files that allow random access to the data.
  - MultipleOutputs: It allows writing data to multiple files in different output formats from a single MapReduce job .
  - LazyOutputFormat: It is a wrapper OutputFormat that ensures that only those output files are created that have a record to write. It avoids creating empty files .
  - DBOutputFormat: It sends the reduced output to a SQL table. It can be used to write data to relational databases or HBase .

- The general idea of map and reduce function of Hadoop can be illustrated as follows:

  - map: (K1, V1) -> list (K2, V2)
  - reduce: (K2, list (V2)) -> list (K3, V3)

- The input parameters of the key and value pair, represented by K1 and V1 respectively, are different from the output pair type: K2 and V2.
- The output of the map function is the input for the reduce function.
- The output of the reduce function is the final output of the MapReduce job.