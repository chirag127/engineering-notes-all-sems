#### Input Formats in Map Reduce

- Input formats are classes that define how the input data is split into input splits and how the input records are read from the input splits.
- Input splits are logical chunks of the input data that are assigned to different map tasks for parallel processing.
- Input records are key-value pairs that are passed to the map function as input.
- The default input format in Map Reduce is TextInputFormat, which splits the input data by line and assigns the byte offset of the line as the key and the line content as the value.
- Other common input formats are KeyValueInputFormat, which splits the input data by line and assigns the first token as the key and the rest of the line as the value, and SequenceFileInputFormat, which reads binary key-value pairs from sequence files.
- Custom input formats can be implemented by extending the abstract class InputFormat and overriding the methods getSplits and createRecordReader.