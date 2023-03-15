#### Output Formats in Map Reduce

- Output formats are the classes that define how the output of a map reduce job is stored.
- The output format is specified by setting the `mapreduce.output.fileoutputformat.class` property in the job configuration.
- The default output format is `TextOutputFormat`, which writes plain text files with one record per line and a tab character as the separator between the key and the value.
- Other output formats provided by Hadoop are:

  - `SequenceFileOutputFormat`: Writes binary files that store sequences of key-value pairs. Sequence files are efficient and compressible, and can be used as input for other map reduce jobs.
  - `KeyValueTextOutputFormat`: Writes plain text files with one record per line and a user-defined separator between the key and the value. The separator can be specified by setting the `mapreduce.output.keyvaluetextoutputformat.separator` property in the job configuration.
  - `LazyOutputFormat`: A wrapper output format that only creates output files for the reducers that actually produce output. This can be useful to avoid creating empty files when the number of reducers is larger than the number of output keys.
  - `MultipleOutputs`: A utility class that allows writing to multiple output files from a single reducer. The output files can have different output formats and different names based on the keys or values.

- To implement a custom output format, one needs to extend the `FileOutputFormat` abstract class and override the `getRecordWriter()` method, which returns a `RecordWriter` object that writes the output records to a file.
- A custom output format can also implement the `checkOutputSpecs()` method, which checks the validity of the output directory and other output parameters before the job is submitted.