### Input Formats for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

1. **Text Input Format:** This is the default input format for MapReduce. It takes text files as input and breaks the data into lines. Each line is considered as a record and is processed by the mapper.

2. **KeyValueTextInputFormat:** This input format is similar to the Text Input Format, but it treats each line as a key-value pair. The separator between the key and the value can be specified by the user.

3. **SequenceFileInputFormat:** This input format reads data from a sequence file, which is a binary file format that stores key-value pairs. It is commonly used for storing the output of a MapReduce job to be used as input for another MapReduce job.

4. **NLineInputFormat:** This input format splits the input data into N lines per split, where N is specified by the user. This can be useful for controlling the granularity of the input data for each mapper.

5. **MultipleInputs:** This class allows the user to specify multiple input formats for a MapReduce job. Each input format can be associated with a specific mapper, allowing the user to process different types of input data with different mappers.

These are some of the common input formats used in MapReduce for processing big data. It is important to choose the appropriate input format for the data being processed to ensure efficient and accurate results.