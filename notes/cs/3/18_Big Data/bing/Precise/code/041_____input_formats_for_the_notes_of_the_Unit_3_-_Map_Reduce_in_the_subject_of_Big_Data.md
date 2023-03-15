### Input Formats for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

1. **Text Input Format:** This is the default input format for MapReduce. It takes text files as input and breaks them into lines. Each line is considered as a record and is processed by the mapper.

2. **KeyValueTextInputFormat:** This input format is similar to the Text Input Format, but it treats each line as a key-value pair. The separator between the key and the value can be specified using the `mapreduce.input.keyvaluelinerecordreader.key.value.separator` property.

3. **SequenceFileInputFormat:** This input format reads data from sequence files, which are binary files that store key-value pairs. Sequence files are commonly used as intermediate data between MapReduce jobs.

4. **NLineInputFormat:** This input format splits the input data into `N` lines per split. The number of lines per split can be specified using the `mapreduce.input.lineinputformat.linespermap` property.

5. **MultipleInputs:** This class allows the use of multiple input formats in a single MapReduce job. Each input format can be associated with a specific mapper, allowing the processing of different types of data in a single job.

These are some of the common input formats used in MapReduce. It is important to choose the appropriate input format for the data being processed to ensure efficient and accurate processing.