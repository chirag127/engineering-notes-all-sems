### Data Format for the Notes of Unit 2 - Hadoop in the Subject of Big Data

In the world of Big Data, Hadoop has emerged as a leading technology for storing, processing, and analyzing large volumes of data. One of the key factors that sets Hadoop apart from traditional data processing systems is its ability to work with data in a variety of formats. In this note, we will discuss the different data formats that can be used in Hadoop.

1. Text Format
   - This is the most basic and commonly used data format in Hadoop.
   - Data is stored as plain text files.
   - Text files are easy to create, modify, and read using a variety of tools.
   - However, text files are not suitable for storing complex structured data.

2. SequenceFile Format
   - This is a binary file format used for storing large volumes of data.
   - SequenceFiles are optimized for sequential read and write operations.
   - They can store key-value pairs, where both the key and value can be of any data type.
   - SequenceFiles are commonly used for intermediate data storage during MapReduce jobs.

3. Avro Format
   - This is a compact and efficient data serialization format.
   - Avro supports complex data structures and schema evolution.
   - Schema evolution allows for the modification of the data structure over time without breaking compatibility with existing data.
   - Avro is commonly used in Hadoop for data exchange between different systems.

4. Parquet Format
   - This is a columnar storage format used for storing structured data.
   - Parquet is highly optimized for both read and write operations.
   - It supports schema evolution and compression, making it an ideal format for storing and processing large volumes of structured data.
   - Parquet is commonly used in Hadoop for data warehousing and analytics.

5. ORC Format
   - This is another columnar storage format used for storing structured data.
   - ORC stands for Optimized Row Columnar.
   - ORC is highly optimized for read operations and supports schema evolution and compression.
   - ORC is commonly used in Hadoop for data warehousing and analytics, especially for large-scale analytical queries.

In conclusion, Hadoop supports a variety of data formats that are optimized for different use cases. Understanding the strengths and weaknesses of each format is essential for designing efficient and scalable Big Data solutions using Hadoop.