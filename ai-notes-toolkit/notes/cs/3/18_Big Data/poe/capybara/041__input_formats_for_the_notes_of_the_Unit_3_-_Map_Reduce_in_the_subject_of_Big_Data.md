### Input Formats for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

In the field of Big Data, input formats play a crucial role in the Map Reduce process. Here are some of the input formats that are commonly used:

- **TextInputFormat:** This is the default input format for Map Reduce. It reads lines of text files and provides the input to the mapper. It is useful for processing unstructured data, such as log files or web pages.

- **KeyValueTextInputFormat:** This input format is similar to TextInputFormat, but it reads key-value pairs instead of lines of text. The keys and values are separated by a delimiter, such as a tab or a comma. It is useful for processing semi-structured data, such as CSV files.

- **SequenceFileInputFormat:** This input format is used for reading binary files that contain key-value pairs. It is useful for processing large amounts of data, as it can be split across multiple nodes in a Hadoop cluster.

- **AvroKeyInputFormat:** This input format is used for reading data that is encoded in Avro format, which is a compact binary format. It is useful for processing data that has a well-defined schema, such as sensor data or financial transactions.

- **ParquetInputFormat:** This input format is used for reading data that is stored in Parquet format, which is a columnar storage format. It is useful for processing data that has a large number of columns, as it can be more efficient than row-based formats.

- **OrcInputFormat:** This input format is used for reading data that is stored in ORC format, which is another columnar storage format. It is similar to ParquetInputFormat, but is optimized for use with Hive, which is a data warehousing tool.

In conclusion, choosing the right input format is an important part of the Map Reduce process in Big Data. Each format has its strengths and weaknesses, and it is important to select the one that is best suited for your specific use case.