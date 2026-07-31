#### Input formats in map reduce

- Input formats are classes that define how the input data is split into input splits and how the input records are read from the input splits by the map tasks.
- Input formats are responsible for creating input splits, which are logical chunks of the input data that can be processed in parallel by different map tasks.
- Input formats also provide a record reader, which is an object that reads the input records from the input splits and converts them into key-value pairs that are passed to the map function.
- The default input format in map reduce is TextInputFormat, which splits the input data by line breaks and reads each line as a record. The key is the byte offset of the line and the value is the line content.
- Other common input formats are KeyValueTextInputFormat, which reads each line as a key-value pair separated by a tab character, and SequenceFileInputFormat, which reads binary key-value pairs from sequence files.
- Custom input formats can be implemented by extending the abstract class InputFormat and providing the logic for creating input splits and record readers.
- Input formats can be specified by setting the mapreduce.inputformat.class property in the job configuration or by using the setInputFormatClass method of the Job class.
- Input formats can affect the performance and efficiency of map reduce jobs, as they determine how the input data is distributed and processed by the map tasks. Choosing an appropriate input format can reduce the network and disk I/O, improve the load balancing, and avoid data skew and stragglers.