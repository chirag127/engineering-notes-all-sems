### Unit 3 - Map Reduce: Output Formats

1. **TextOutputFormat**: This is the default output format for MapReduce jobs. It writes data as lines of text, with key-value pairs separated by a tab character.
2. **SequenceFileOutputFormat**: This output format writes data in a binary format, with key-value pairs stored as serialized objects. It is more efficient than TextOutputFormat, as it reduces the amount of data that needs to be written to disk.
3. **MapFileOutputFormat**: This output format is similar to SequenceFileOutputFormat, but it also creates an index file that allows for faster lookups of specific keys.
4. **MultipleOutputs**: This class allows for writing data to multiple output files, with different output formats for each file. This can be useful when the output data needs to be split into multiple files based on certain criteria.

These are some of the common output formats used in MapReduce jobs for handling Big Data. It is important to choose the appropriate output format based on the requirements of the job and the data being processed.