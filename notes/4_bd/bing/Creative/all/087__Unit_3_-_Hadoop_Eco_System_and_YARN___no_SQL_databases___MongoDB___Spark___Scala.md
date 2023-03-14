## Unit 3 - Hadoop Eco System and YARN , no SQL databases , MongoDB , Spark , Scala

- Hadoop is an open-source framework that allows users to store and process large-scale data sets across a network of computers.
- Hadoop consists of four main modules: Hadoop Distributed File System (HDFS), Yet Another Resource Negotiator (YARN), Hadoop MapReduce and Hadoop Common.
- HDFS is the primary data storage system that manages large data sets running on commodity hardware. It provides high-throughput data access and high fault tolerance.
- YARN is the cluster resource manager that schedules tasks and allocates resources (e.g., CPU and memory) to applications. It also supports multiple processing frameworks such as Spark, Hive and Pig.
- Hadoop MapReduce is the programming model that splits big data processing tasks into smaller ones, distributes the small tasks across different nodes, then runs each task in parallel.
- Hadoop Common is the set of utilities and libraries that support the other Hadoop modules.
- Hadoop also has an extensive ecosystem of open-source technologies that prepare, process, manage and analyze big data sets. Some of the most popular ones are:
  - Hive: A data warehouse system that provides a SQL-like interface to query and analyze structured and semi-structured data stored in HDFS.
  - Pig: A scripting language that allows users to write complex data transformations and analysis using a high-level syntax.
  - Spark: A data processing engine that can handle batch, streaming, interactive and machine learning workloads. It can run on top of Hadoop, standalone or in the cloud. It is faster than Hadoop MapReduce as it uses in-memory caching and optimized execution plans.
  - Scala: A general-purpose programming language that supports both object-oriented and functional paradigms. It is the main language used to write Spark applications, as it offers concise syntax, interoperability with Java and powerful features.
  - MongoDB: A NoSQL database that stores data as documents (i.e., JSON-like objects) in collections. It supports dynamic schemas, horizontal scaling, high availability and flexible querying.
  - NoSQL: A term that refers to a variety of non-relational databases that are designed to handle large-scale, unstructured or semi-structured data. They offer advantages such as schema flexibility, scalability, performance and availability over traditional relational databases.

Some mnemonics and learning tricks for this unit are:

- Hadoop: **H**uge **A**mounts of **D**ata **O**n **O**odles of **P**rocessors
- YARN: **Y**et **A**nother **R**esource **N**egotiator
- Spark: **S**peedy **P**rocessing and **A**nalysis of **R**eal-time and **K**omplex data
- Scala: **S**calable **L**anguage
- MongoDB: **M**assive **O**nline **N**oSQL **D**ata**B**ase
- NoSQL: **N**ot **O**nly **SQL**