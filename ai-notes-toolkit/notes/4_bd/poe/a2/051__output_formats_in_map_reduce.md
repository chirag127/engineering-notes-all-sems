 Here is the content in formal tone and markdown format:

#### Output Formats in Map Reduce

1. Text Output Format
- Mapper outputs key-value pairs of text data
- Reducer outputs key-value pairs of text data
- Used for tasks like sorting, filtering, counting words etc.

2. Sequence File Output Format
- Mapper and Reducer output key-value pairs in binary sequence file format
- Efficient for storing large datasets as it is a compressed binary format
- Can store various data types like integers, floats, booleans, strings etc. for keys and values.

3. Multiple Outputs
- Mapper and Reducer can output to multiple files
- Useful in cases where we want to segregate output into multiple categories
- Mappers can output to multiple files and reducers can further aggregate those outputs into required format.

To summarize, Map Reduce provides a variety of output formats to suit various requirements. The appropriate output format can be chosen based on the nature of the task and the usage of output data. The output can be in text format for simple tasks or in efficient binary formats for storing large datasets. Multiple output files provide a convenient way to segregate outputs.