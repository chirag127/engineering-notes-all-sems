

#### Input Formats in Map Reduce

1. Text Input Format: The default input format in MapReduce is the TextInputFormat. It reads data line by line and provides the key-value pairs to the mapper. The key is the byte offset of the line and the value is the content of the line. 

2. Key Value Input Format: KeyValueInputFormat is used to read data in the form of (key, value) pairs. It is useful when the input data is already in the form of (key, value) pairs.

3. Sequence File Input Format: SequenceFileInputFormat is used to read data from SequenceFiles. It is a flat file format which stores binary key/value pairs.

4. NLine Input Format: NLineInputFormat is used to split the input file into ‘N’ number of splits. This is useful when we have a large number of small files as input.

5. DBInputFormat: DBInputFormat is used to read data from a relational database. It is useful when we have data stored in a relational database and need to process it using MapReduce.