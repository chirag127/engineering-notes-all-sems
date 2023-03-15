# Pig - Introduction to PIG

- Pig is a high-level programming language that allows users to write complex data analysis tasks using a simple syntax.
- Pig is an open-source project that is part of the Apache Hadoop ecosystem, a framework for distributed processing of large-scale data sets.
- Pig scripts are translated into a series of MapReduce jobs that run on a Hadoop cluster.
- Pig can handle structured, semi-structured, and unstructured data, and supports various data formats, such as text, JSON, XML, and binary.
- Pig provides a rich set of built-in operators and functions for data manipulation, such as filtering, grouping, joining, sorting, aggregating, and transforming.
- Pig also allows users to define their own custom functions using Java, Python, or other languages.
- Pig can be run in two modes: local mode and MapReduce mode.
  - Local mode: Pig runs on a single machine, using the local file system as the data source and destination. This mode is useful for testing and debugging Pig scripts.
  - MapReduce mode: Pig runs on a Hadoop cluster, using the Hadoop Distributed File System (HDFS) as the data source and destination. This mode is suitable for processing large-scale data sets in parallel.
- Pig has two components: Pig Latin and Pig Engine.
  - Pig Latin: Pig Latin is the scripting language that users write to express their data analysis tasks. Pig Latin is a declarative language that focuses on the logic of the data flow, rather than the implementation details.
  - Pig Engine: Pig Engine is the component that compiles Pig Latin scripts into MapReduce jobs, optimizes the execution plan, and executes the jobs on a Hadoop cluster. Pig Engine also provides an interactive shell, called Grunt, that allows users to run Pig Latin commands interactively.