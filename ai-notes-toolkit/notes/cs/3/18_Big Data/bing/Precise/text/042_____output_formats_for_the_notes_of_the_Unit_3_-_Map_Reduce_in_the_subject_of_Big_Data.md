### Output Formats for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

1. **Text Output Format**: This is the default output format for MapReduce jobs. It writes data as lines of text, with key-value pairs separated by a tab character.
2. **SequenceFile Output Format**: This format stores data in a binary format and is suitable for storing large amounts of data. It is also suitable for storing data that needs to be compressed.
3. **MapFile Output Format**: This format is similar to the SequenceFile format, but it also stores an index to allow for faster lookups of specific keys.
4. **Multiple Outputs**: This feature allows a MapReduce job to write its output to multiple files, with different output formats and compression settings for each file.
5. **Null Output Format**: This format discards all output data and is useful for testing purposes or when the output data is not needed.

These are some of the common output formats used in MapReduce jobs in the context of Big Data. It is important to choose the appropriate output format for the specific needs of the job to ensure efficient processing and storage of the data.