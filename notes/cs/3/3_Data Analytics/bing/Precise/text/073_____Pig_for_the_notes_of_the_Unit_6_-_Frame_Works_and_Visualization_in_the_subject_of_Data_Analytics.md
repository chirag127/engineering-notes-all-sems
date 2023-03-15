### Pig

Pig is a high-level platform for creating MapReduce programs used with Hadoop. It consists of two parts: Pig Latin, a high-level language for expressing data analysis programs, and the Pig engine, which converts these programs into MapReduce jobs that can be executed within Hadoop.

Here are some key points to remember about Pig:

1. Pig Latin is a procedural language, where the user specifies the sequence of operations to be performed on the data.
2. Pig Latin scripts can be executed in two modes: local mode, where the data and the Pig engine are on the same machine, and MapReduce mode, where the data and the Pig engine are on a Hadoop cluster.
3. Pig Latin provides many built-in functions for common data operations such as filtering, grouping, and joining, but users can also create their own custom functions using Java, Python, or other languages.
4. Pig can handle structured, semi-structured, and unstructured data, and can read data from various sources such as HDFS, HBase, and local files.
5. Pig is often used for data preprocessing, ETL (Extract, Transform, Load) tasks, and ad-hoc data analysis.
