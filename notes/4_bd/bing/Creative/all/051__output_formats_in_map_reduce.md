#### Output formats in map reduce

- Output formats are the classes that define how the output of a map reduce job is stored.
- Output formats are responsible for creating the output files, writing the key-value pairs to the files, and optionally compressing the files.
- Output formats can be specified by setting the `mapreduce.output.fileoutputformat.class` property in the job configuration.
- The default output format is `TextOutputFormat`, which writes plain text files with one line per key-value pair, separated by a tab character.
- Other common output formats are:

  - `SequenceFileOutputFormat`, which writes binary files that store sequences of key-value pairs in a compressed and serialized format. This is useful for storing intermediate data that will be consumed by another map reduce job.
  - `KeyValueTextOutputFormat`, which writes plain text files with one line per key-value pair, separated by a user-defined separator character. This is useful for customizing the output format for human readability or external tools.
  - `MultipleOutputs`, which is not an output format class, but a utility that allows writing to multiple output files from a single map reduce job. This is useful for partitioning the output data based on some criteria, such as the key or the value.

- Output formats can be customized by extending the `FileOutputFormat` abstract class and overriding the `getRecordWriter` method, which returns a `RecordWriter` object that writes the key-value pairs to the output files.
- Output formats can also be implemented by using the `OutputFormat` interface, which has two methods: `getRecordWriter` and `checkOutputSpecs`, which checks the validity of the output directory and other parameters.
- Output formats can be tested by using the `FileOutputFormatTest` class, which provides methods for creating mock output files and verifying their contents.