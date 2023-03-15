### Output Formats for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

- OutputFormat in MapReduce job provides the RecordWriter implementation to be used to write the output files of the job. Then the output files are stored in a FileSystem.
- The framework uses FileOutputFormat.setOutputPath() method to set the output directory.
- There are several types of OutputFormat which are as follows :
  - TextOutputFormat: The default OutputFormat is TextOutputFormat. It writes (key, value) pairs on single lines of text files .
  - SequenceFileOutputFormat: This OutputFormat writes sequences files for its output. Sequence files are binary files that store serialized key-value pairs.
  - SequenceFileAsBinaryOutputFormat: It is another variant of SequenceFileInputFormat. It converts keys and values to bytes and writes them as bytes to the output file.
  - MapFileOutputFormat: It is another form of FileOutputFormat. It writes map files for its output. Map files are indexed sequence files that allow random access to the data.
  - MultipleOutputs: It allows writing data to multiple files in different formats. It can be used to write different output files for each reducer, or to write different files based on the keys or values of the output.
  - LazyOutputFormat: It is a wrapper OutputFormat that prevents the creation of empty output files. It can be used with any existing OutputFormat to avoid generating zero-sized files.
  - DBOutputFormat: It sends the reduced output to a SQL table. It can be used to write data to relational databases or to HBase .
- The output formats for relational databases and to HBase are handled by DBOutputFormat. It enables the MapReduce program to work on the data stored in the database table and uses it for writing outputs to the database table .
- The general idea of map and reduce function of Hadoop can be illustrated as follows:

  ```
  map: (K1, V1) -> list (K2, V2)
  reduce: (K2, list (V2)) -> list (K3, V3)
  ```
  - The input parameters of the key and value pair, represented by K1 and V1 respectively, are different from the output pair type: K2 and V2.
  - The output of the map function is a list of intermediate key-value pairs that are shuffled and sorted by the framework before being passed to the reduce function.
  - The reduce function takes a key and a list of values associated with that key as input, and produces a list of output key-value pairs as output.
  - The output of the reduce function is written to the output files by the OutputFormat implementation.