# Pig Latin

Pig Latin is a high-level programming language that is used for data analysis in Hadoop. It was developed by Yahoo! and is generally used with Hadoop to perform a lot of data administration operations. Pig Latin programs run on Hadoop cluster and make use of both Hadoop distributed file system (HDFS) and MapReduce programming layer. However, for prototyping, Pig Latin programs can also run in “local mode” without a cluster. Pig Latin has a rich set of data types and operators for performing different data operations like join, filter, sort, load, group, etc. Pig Latin programs are also called Pig scripts.

Some of the features and advantages of Pig Latin are:

- It is easy to learn and write, as it has a simple syntax and resembles SQL.
- It is extensible, as it allows users to define their own functions using Java, Python, or other languages.
- It is efficient, as it optimizes the execution plan of the Pig scripts and reduces the number of MapReduce jobs.
- It is flexible, as it can handle structured, semi-structured, and unstructured data.
- It is interoperable, as it can work with other Hadoop components like Hive, HBase, and Spark.

Some of the applications and use cases of Pig Latin are:

- Data cleansing and preprocessing: Pig Latin can be used to remove unwanted data, transform data into a desired format, and enrich data with additional information.
- Data aggregation and summarization: Pig Latin can be used to group data by certain attributes, compute aggregates like count, sum, average, etc., and generate summary reports.
- Data analysis and mining: Pig Latin can be used to perform complex data analysis tasks like sentiment analysis, recommendation systems, fraud detection, etc.

Some of the examples of Pig Latin statements are:

- To load data from a file into a relation:

```pig
A = LOAD 'data.txt' USING PigStorage(',') AS (name:chararray, age:int, salary:float);
```

- To filter data based on a condition:

```pig
B = FILTER A BY age > 30;
```

- To join two relations on a common attribute:

```pig
C = JOIN A BY name, D BY name;
```

- To group data by an attribute and compute an aggregate:

```pig
E = GROUP A BY name;
F = FOREACH E GENERATE group, COUNT(A);
```

- To store the result of a relation into a file:

```pig
STORE F INTO 'output.txt' USING PigStorage(',');
```