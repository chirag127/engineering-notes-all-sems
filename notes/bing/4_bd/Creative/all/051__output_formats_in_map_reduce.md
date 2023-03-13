#### Output formats in map reduce

- Output formats are the classes that define how the output of a map reduce job is stored.
- Output formats are responsible for creating the output files, writing the records, and optionally compressing the data.
- Output formats can be specified by setting the `mapreduce.output.fileoutputformat.class` property in the job configuration.
- The default output format is `TextOutputFormat`, which writes plain text files with one record per line and a tab character as the separator between the key and the value.
- Some other common output formats are:

  - `SequenceFileOutputFormat`: Writes binary files that store key-value pairs in a serialized format. Sequence files are efficient and compact, and can be used as input for subsequent map reduce jobs.
  - `KeyValueTextOutputFormat`: Writes plain text files with one record per line and a configurable separator between the key and the value. The default separator is a tab character.
  - `MultipleOutputs`: A utility class that allows writing to multiple output files from a single map reduce job. Each output file can have a different output format and a different name or path. Multiple outputs can be useful for partitioning the output by some criteria, such as the key or the value.
  - `LazyOutputFormat`: A wrapper class that prevents the creation of empty output files. By default, map reduce creates one output file per reducer, even if some reducers do not produce any output. Lazy output format only creates output files when they are needed, which can save disk space and reduce the number of output files.

- A custom output format can be implemented by extending the `FileOutputFormat` abstract class and overriding the `getRecordWriter` method. The record writer is the class that writes the key-value pairs to the output file.
- A custom output format can also implement the `OutputCommitter` interface to perform any cleanup or finalization tasks after the job is completed. The output committer is responsible for committing or aborting the output, depending on the success or failure of the job.