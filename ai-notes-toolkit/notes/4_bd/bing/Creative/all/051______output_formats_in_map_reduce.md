#### Output Formats in Map Reduce

OutputFormat is a class that describes the output specification for a MapReduce job. It provides the RecordWriter implementation to be used to write the output files of the job to a FileSystem. The output files are stored in a directory specified by the FileOutputFormat.setOutputPath() method. The output directory must not already exist before the job execution. 

There are different types of OutputFormat in MapReduce, each with its own characteristics and use cases. Some of the common types are:

- TextOutputFormat: This is the default OutputFormat that writes plain text files as output. Each record is a line of text that consists of the key and the value separated by a tab character. 
- SequenceFileOutputFormat: This OutputFormat writes sequence files as output. Sequence files are binary files that store key-value pairs in a compressed and serialized format. They are suitable for storing large amounts of data efficiently. 
- SequenceFileAsBinaryOutputFormat: This is another variant of SequenceFileOutputFormat that writes the keys and values as binary data instead of using their toString() methods. This can be useful for preserving the original data types of the keys and values. 
- MapFileOutputFormat: This OutputFormat writes map files as output. Map files are a special type of sequence files that support random access and retrieval of records by key. They are composed of two files: a data file that stores the key-value pairs and an index file that stores the offsets of the keys in the data file. 
- MultipleOutputs: This is a utility class that allows writing to multiple output files from a MapReduce job. It can be used to write different types of output files based on the keys or values of the records, or to write to different directories or file systems. 
- LazyOutputFormat: This is a wrapper class that prevents the creation of empty output files. It delays the creation of the output files until the first record is written to them. This can be useful for reducing the number of output files and avoiding unnecessary overhead. 
- DBOutputFormat: This OutputFormat writes the output records to a relational database table using JDBC. It requires the user to specify the database connection parameters, the table name, and the column names. 

: https://techvidvan.com/tutorials/hadoop-outputformat-introduction/
: https://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapreduce/OutputFormat.html