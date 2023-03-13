#### Input formats in map reduce

- Input formats are classes that define how the input data is split into input splits and how to read the records from the input splits.
- Input splits are logical chunks of the input data that are assigned to different mappers for parallel processing.
- Input formats also provide a `RecordReader` implementation that is responsible for extracting key-value pairs from the input split.
- There are two types of input formats: `FileInputFormat` and `InputFormat`.
- `FileInputFormat` is an abstract class that extends `InputFormat` and provides common functionality for reading files as input.
- `FileInputFormat` has several subclasses that can handle different types of files, such as `TextInputFormat`, `KeyValueTextInputFormat`, `SequenceFileInputFormat`, `NLineInputFormat`, etc.
- `InputFormat` is an interface that defines the methods for creating input splits and record readers. It can be implemented by custom classes that need to read data from sources other than files, such as databases, web services, etc.
- The default input format is `TextInputFormat`, which reads each line of a text file as a record and splits the line by a tab character into a key-value pair.
- The key is the byte offset of the line from the beginning of the file and the value is the line itself.
- The input format can be specified by setting the `mapreduce.inputformat.class` property in the job configuration or by using the `setInputFormatClass()` method of the `Job` class.
- The input format can also be specified by using the `@InputFormat` annotation on the mapper class.
- A custom input format can be created by implementing the `InputFormat` interface and overriding the `getSplits()` and `createRecordReader()` methods.
- The `getSplits()` method should return a list of `InputSplit` objects that represent the logical partitions of the input data.
- The `createRecordReader()` method should return a `RecordReader` object that can read the key-value pairs from the input split.
- A custom record reader can be created by implementing the `RecordReader` interface and overriding the `initialize()`, `nextKeyValue()`, `getCurrentKey()`, `getCurrentValue()`, and `close()` methods.
- The `initialize()` method should initialize the record reader with the input split and the task context.
- The `nextKeyValue()` method should advance to the next key-value pair and return true if one exists or false if the end of the input split is reached.
- The `getCurrentKey()` and `getCurrentValue()` methods should return the current key and value respectively.
- The `close()` method should close the record reader and release any resources.

Some mnemonics and learning tricks for the input formats in map reduce are:

- Remember that input formats are responsible for splitting and reading the input data.
- Remember that input splits are logical chunks of the input data and record readers are the ones that extract key-value pairs from them.
- Remember that `FileInputFormat` is a common base class for reading files and `InputFormat` is an interface for reading other sources of data.
- Remember that the default input format is `TextInputFormat` and it splits the lines by tabs into key-value pairs.
- Remember that the input format can be specified by setting a property, using a method, or using an annotation.
- Remember that a custom input format can be created by implementing the `InputFormat` interface and a custom record reader can be created by implementing the `RecordReader` interface.