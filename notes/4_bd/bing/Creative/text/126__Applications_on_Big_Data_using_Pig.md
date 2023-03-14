#### Applications on Big Data using Pig

- Pig is a high-level platform or tool that is used to process large datasets that are stored in HDFS  .
- Pig provides a high level of abstraction for processing over MapReduce, which is a low-level framework for distributed computing .
- Pig provides a high-level scripting language, known as Pig Latin, which is used to develop the data analysis codes  .
- Pig Latin is similar to SQL and is easy to learn, read and write, especially for SQL programmers  .
- Pig Latin provides many built-in operators for performing various operations such as filtering, joining, sorting, grouping, aggregating, etc  .
- Pig Latin also supports nested data types such as tuples, bags and maps, which are not available in MapReduce  .
- Pig Latin scripts are internally converted to MapReduce jobs by the Pig engine, which is a component of Apache Pig  .
- Pig engine can run in two modes: local mode and distributed mode. In local mode, Pig runs in a single JVM and is used for small datasets. In distributed mode, Pig runs on a Hadoop cluster and is used for large datasets .
- Pig can handle both structured and unstructured data, and can store the results in HDFS  .
- Pig is extensible and allows users to create their own user-defined functions (UDFs) in other programming languages such as Java and invoke them in Pig Latin scripts  .
- Pig reduces the development time and the lines of code compared to writing raw MapReduce programs, and provides a multi-query approach that reduces the number of scans of the data  .
- Pig was developed by Yahoo in 2006 and became an open source project under Apache Software Foundation in 2007. The latest version of Pig is 0.18, which was released in 2017.

Some of the applications of Pig in big data are:

- Pig is used by telecom companies to de-identify the customer call data information.
- Pig is used to process time-sensitive data loads.
- Pig is used by e-commerce companies to analyze customer behavior and preferences.
- Pig is used by social media platforms to process user-generated content and recommendations.
- Pig is used by healthcare organizations to analyze patient records and medical data.
- Pig is used by educational institutions to process student data and learning outcomes.