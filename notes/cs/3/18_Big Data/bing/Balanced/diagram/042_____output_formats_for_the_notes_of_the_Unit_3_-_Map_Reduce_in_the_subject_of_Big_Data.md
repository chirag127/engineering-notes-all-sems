Output formats for the notes of the Unit 3 - Map Reduce in the subject of Big Data

- OutputFormat is a component of MapReduce that defines how the output files of a job are written and stored in a FileSystem.
- OutputFormat also provides a RecordWriter implementation that is used to write the output records of the map and reduce tasks.
- There are different types of OutputFormat in MapReduce, each with its own advantages and disadvantages. Some of the common types are:

  - TextOutputFormat: This is the default OutputFormat that writes plain text files as output. Each record is a line of text that consists of the key and the value separated by a tab character.
  - SequenceFileOutputFormat: This OutputFormat writes sequence files as output. Sequence files are binary files that store serialized key-value pairs. They are more efficient and compact than text files, and support compression and splitting.
  - SequenceFileAsBinaryOutputFormat: This is a variant of SequenceFileOutputFormat that writes the keys and values as binary data instead of using serialization. This can improve performance and reduce disk space, but requires the keys and values to be of fixed length.
  - MapFileOutputFormat: This is another form of FileOutputFormat that writes map files as output. Map files are a special type of sequence files that support random access and indexing. They are useful for applications that need to look up values by keys efficiently.
  - MultipleOutputs: This is a utility class that allows writing output to multiple files or directories based on the keys or values of the records. This can be helpful for partitioning or organizing the output data.
  - LazyOutputFormat: This is a wrapper class that prevents creating empty output files for the map and reduce tasks that do not produce any output. This can save disk space and avoid unnecessary overhead.
  - DBOutputFormat: This OutputFormat sends the reduced output to a SQL table in a relational database. This can be useful for integrating the output data with other applications or systems.

- The choice of OutputFormat depends on the requirements and characteristics of the output data, such as the format, size, compression, accessibility, and usability.
- The framework uses the FileOutputFormat.setOutputPath() method to set the output directory for the job. The output directory must not exist before running the job, otherwise the job will fail.
- The output files are named as part-r-00000, part-r-00001, and so on, where r stands for reduce and the numbers indicate the task ID. If the job has only map tasks and no reduce tasks, the files are named as part-m-00000, part-m-00001, and so on, where m stands for map.