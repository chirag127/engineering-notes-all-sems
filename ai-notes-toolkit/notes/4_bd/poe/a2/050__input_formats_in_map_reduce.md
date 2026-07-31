 Here is the formal content on the topic "Input Formats in Map Reduce" in Markdown format:

#### Input Formats in Map Reduce

1. Text Input Format - Used for plain text input files. Splits the input into lines and passes each line to the mapper as a key-value pair where the key is the offset of the line and value is the line itself.
2. KeyValueTextInputFormat - Used for input data in the form of <key><tab><value>. The keys and values are passed to the mapper.
3. NLineInputFormat - Divides the input into N lines per split and passes it to the mapper. Useful for log files or other formats where N lines are processed together.
4. SequenceFileInputFormat - Used for sequence files which are binary encoded MapReduce data. Reads the key-value pairs from sequence files and passes it to the mapper.
5. DBInputFormat - Used to read data from databases and pass it to the mapper. Queries the database and fetches results which are then processed by the mapper.

The input format is defined by the InputFormat class used. The framework then splits the input into chunks, assigns them to individual map tasks which then process the key-value pairs provided by the input format. The choice of input format depends on the structure and format of the input data.