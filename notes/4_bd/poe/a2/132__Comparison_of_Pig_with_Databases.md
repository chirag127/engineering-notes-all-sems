 Here is the content in markdown format with formal tone and without emojis:

#### Comparison of Pig with Databases.

1. Pig is a scripting language while databases like MySQL, Oracle, etc. are querying languages. Pig Latin scripts are translated into MapReduce jobs which are executed on Hadoop cluster while database queries are directly executed on the database.

2. Pig is suitable for complex data processing tasks like joining multiple datasets, filtering, grouping data, etc. while databases are suitable for simple CRUD operations. Pig can handle huge volumes of data as it works on Hadoop distributed file system. Databases have limitations on the size of data they can store and process.

3. Pig provides a higher level of abstraction over MapReduce making the programming easy while databases require learning SQL to query the data. The learning curve is easier for Pig.

4. Pig Latin scripts are executed in parallel on the Hadoop cluster making the processing faster while database queries are processed sequentially. This makes Pig a better choice for big data processing.

5. Pig supports nested data structures like tuples, bags and maps which are more complex than the tabular format supported by relational databases. This makes Pig more powerful in terms of data modeling.

In conclusion, while databases are suitable for transactional data processing and simple queries, Pig is a better choice for complex big data processing tasks on account of its programming ease, ability to handle huge volumes of data and parallel processing capabilities. The selection of Pig or databases depends on the use case and the nature of the data to be processed.