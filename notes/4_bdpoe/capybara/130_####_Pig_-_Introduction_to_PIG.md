#### Pig - Introduction to PIG

Apache Pig is a high-level platform used for creating and executing MapReduce programs used with Apache Hadoop. It is a scripting language designed to simplify the processing of large datasets. Here are some key points to keep in mind about Pig:

- Pig Latin is the language used to write Pig scripts, and it is similar to SQL. It makes use of operators, which are similar to SQL operators, to perform operations on data.
- Pig is a data flow language, which means that the data is passed through a series of transformations before being stored or displayed.
- Pig allows for complex data types such as tuples, bags, and maps to be used in its scripts.
- Pig is designed to work with structured and semi-structured data, but it can also handle unstructured data.
- Pig can be run in two modes: local mode and MapReduce mode. In local mode, Pig runs on the local machine, while in MapReduce mode, it runs on a Hadoop cluster.
- Pig can be used for a variety of tasks such as data extraction, cleaning, transformation, and analysis.
- Pig is used in a variety of industries such as finance, healthcare, retail, and telecommunications.

Some useful tricks and mnemonics to remember while working with Pig are:

- Use the LOAD operator to load data into Pig from various sources such as HDFS, local file system, HBase, and Amazon S3.
- Use the FILTER operator to filter out unwanted data from the dataset.
- Use the GROUP operator to group data based on a specific column or set of columns.
- Use the FOREACH operator to perform operations on each row of the dataset.
- Use the STORE operator to store the output of the Pig script into various file formats such as CSV, JSON, and Avro.

Overall, Pig is a powerful tool for processing and analyzing large datasets. Its simple scripting language and ability to handle complex data types make it a popular choice for big data processing tasks.