 Here is the content on #### Apache Hive architecture in markdown format:

#### Apache Hive architecture

Hive architecture consists of the following main components:

1. Metastore: It is the centralized repository of metadata for Hive. It stores metadata about schemas, tables, partitions, columns, etc. By default, Derby database is used as metastore but MySQL or Oracle can also be used.
2. Driver: It accepts queries from the client applications, parses it and creates an execution plan. It then executes the plan and responds back to the client with the results.
3. Execution Engine: It is responsible for executing the queries on the cluster. It converts the Hive queries into MapReduce or Tez jobs which are then executed on Hadoop.
4. SerDe: It stands for Serializer and Deserializer. It specifies the input format and output format for reading and writing data. It converts the data from Row/Delimited format to Hive format and vice versa.

Some key points about Hive architecture:

1. Hive Query Language (HQL) is translated into MapReduce or Tez jobs by the Driver.
2. Metadata about tables, schemas, etc. is stored in metastore in a database.
3. SerDe is used to specify the input/output format. Default input format is TextInputFormat and default output format is TextOutputFormat.
4. Hive can work on a wide variety of data formats like ORC, Parquet, Avro, etc.
5. Hive can access data residing in HDFS, Amazon S3, HBase, etc.

Advantages of Hive:
1. Schema on read: Hive does not require data to be structured. It can work on semi-structured and unstructured data.
2. HQL is similar to SQL which makes it easy to learn.
3. It provides a mechanism to project structure onto the data and query the data using a SQL-like language called HiveQL.
4. It can scale to large data sets and provides tools to enable easy data summarization, ad-hoc querying and analysis of large datasets.

Applications of Hive:
1. Data warehousing: Hive is commonly used for data aggregation, data summarization, generating reports, etc.
2. Ad-hoc querying and analysis on large data sets.
3. Machine Learning and Analytics.