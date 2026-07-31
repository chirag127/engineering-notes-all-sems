### Input Formats for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

1. **Text Input Format:** This is the default input format for MapReduce. It takes text files as input and breaks them into lines. Each line is considered as a record and is processed by the mapper.

2. **KeyValueTextInputFormat:** This input format is similar to the Text Input Format, but it treats each line as a key-value pair separated by a delimiter. The default delimiter is a tab character.

3. **SequenceFileInputFormat:** This input format reads data from sequence files, which are binary files that store key-value pairs. Sequence files are commonly used in MapReduce as an intermediate data format.

4. **NLineInputFormat:** This input format splits the input data into N lines per split. This can be useful when you want to control the number of lines processed by each mapper.

5. **MultipleInputs:** This class allows you to use multiple input formats in a single MapReduce job. You can specify different input formats for different input paths.

These are some of the common input formats used in MapReduce. It is important to choose the appropriate input format for your data to ensure efficient processing by the MapReduce framework.