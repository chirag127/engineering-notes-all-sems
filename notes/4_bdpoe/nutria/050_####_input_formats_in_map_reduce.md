
### Input Formats in Map Reduce

- **Text Input Format**: This is the default input format in Hadoop MapReduce. It reads data line by line and provides the offset of the line as key to the mapper.
- **Key Value Input Format**: This input format is used when the input data is in the form of (key, value) pairs. It passes the key-value pair to the mapper directly.
- **Sequence File Input Format**: This is used when the input data is in the form of sequence files. It reads the sequence files and passes the key-value pairs to the mapper.
- **NLineInputFormat**: This input format is used when the input data is in the form of large text files. It splits the large text files into N-lines and then passes it to the mapper.
- **DBInputFormat**: This input format is used when the input data is in the form of a database table. It reads the table from the database and passes the records to the mapper.
- **XMLInputFormat**: This input format is used when the input data is in the form of an XML file. It reads the XML file and passes the records to the mapper.
- **MultipleInputs**: This input format is used when the input data is in the form of multiple files. It reads the multiple files and passes the records to the mapper.
- **CombineFileInputFormat**: This input format is used when the input data is in the form of multiple small files. It combines the multiple small files into one large file and then passes it to the mapper.