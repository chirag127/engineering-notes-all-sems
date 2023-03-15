### Unit 3 - Map Reduce: Output Formats

1. **TextOutputFormat**: This is the default output format for MapReduce jobs. It writes data to text files, with keys and values separated by a tab character.
2. **SequenceFileOutputFormat**: This output format writes data to binary sequence files, which can be used as input for subsequent MapReduce jobs. Sequence files are efficient for storing and transferring large amounts of data between MapReduce jobs.
3. **MultipleOutputs**: This class allows writing data to multiple output files, with different output formats for each file. This can be useful when the output data needs to be partitioned into multiple files based on certain criteria.
4. **NullOutputFormat**: This output format discards all output data. It can be useful for testing purposes or when the output data is not needed.
5. **DBOutputFormat**: This output format writes data to a database table. It can be used to export data from Hadoop to a relational database management system (RDBMS).
6. **LazyOutputFormat**: This output format is similar to the default TextOutputFormat, but it does not create empty output files if no data is written to them. This can be useful when the number of output files is large and many of them are empty.
