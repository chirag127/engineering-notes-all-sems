#### Input formats in map reduce

- Input formats are classes that define how the input data is split into logical units called input splits, and how to read the data from each input split.
- Input splits are the units of work that are assigned to different map tasks. Each map task processes one input split at a time.
- Input formats also provide a record reader that reads key-value pairs from the input split and feeds them to the map function.
- The default input format in map reduce is TextInputFormat, which splits the input data by line breaks and reads each line as a value, with the byte offset as the key.
- Other common input formats are:
  - KeyValueTextInputFormat: reads each line as a key-value pair, separated by a tab character.
  - SequenceFileInputFormat: reads binary key-value pairs from sequence files, which are flat files that store serialized data.
  - NLineInputFormat: reads N lines from each input split, where N is specified by the user.
  - MultipleInputs: allows using different input formats for different input paths in the same map reduce job.
- Some advantages of using input formats are:
  - They allow processing different types of data, such as text, binary, XML, JSON, etc.
  - They optimize the data splitting and reading process, by avoiding splitting records across input splits, and by using compression and serialization techniques.
  - They enable customizing the input data processing, by defining custom input formats and record readers.
- Some disadvantages of using input formats are:
  - They may introduce some overhead in creating and reading input splits, especially for small files or large numbers of files.
  - They may not be compatible with some data sources, such as databases or streaming data, that require special connectors or adapters.
  - They may not support some complex data structures, such as nested or hierarchical data, that require parsing or transformation before feeding to the map function.