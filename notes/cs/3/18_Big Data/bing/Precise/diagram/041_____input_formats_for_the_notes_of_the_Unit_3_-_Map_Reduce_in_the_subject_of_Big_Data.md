### Input Formats for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

1. **Text Input Format:** This is the default input format for MapReduce. It takes text files as input and breaks the data into lines. Each line is considered as one record and is processed by the mapper.

2. **KeyValueTextInputFormat:** This input format is similar to the Text Input Format, but it treats each line as a key-value pair separated by a delimiter. The default delimiter is a tab character.

3. **SequenceFileInputFormat:** This input format reads data from a sequence file, which is a binary file format that stores key-value pairs. It is commonly used for storing the output of a MapReduce job to be used as input for another MapReduce job.

4. **NLineInputFormat:** This input format splits the input data into N lines per split. This can be useful when you want to control the number of records processed by each mapper.

5. **MultipleInputs:** This class allows you to use multiple input formats in a single MapReduce job. You can specify different input formats for different input paths.

These are some of the common input formats used in MapReduce. It is important to choose the appropriate input format for your data to ensure efficient processing by the MapReduce job.