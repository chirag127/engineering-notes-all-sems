#### Input Formats in MapReduce

1. InputFormat is responsible for defining the input data for a MapReduce job.
2. It splits the input data into logical chunks called InputSplits and assigns them to individual map tasks for processing.
3. The two most commonly used InputFormats are TextInputFormat and KeyValueTextInputFormat.
4. TextInputFormat reads data line by line and sends each line as a value to the mapper with the key being the byte offset of the line.
5. KeyValueTextInputFormat reads data line by line, but splits each line on a separator character and sends the first part as the key and the second part as the value to the mapper.
6. Other InputFormats include SequenceFileInputFormat, NLineInputFormat, and DBInputFormat.
7. Custom InputFormats can also be created to handle specific data formats.
8. The InputFormat can be specified using the setInputFormatClass method of the Job class.