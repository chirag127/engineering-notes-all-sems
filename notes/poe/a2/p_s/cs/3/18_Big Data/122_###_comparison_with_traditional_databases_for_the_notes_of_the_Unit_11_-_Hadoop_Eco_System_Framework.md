 Here is the content in markdown format for the topic -

### Comparison with traditional databases

Traditional relational databases like Oracle, MySQL, etc. have following differences with Hadoop ecosystem frameworks like HDFS and HBase -

1. Scale - Hadoop ecosystem can scale to store and process huge volumes of data, even petabytes of data. Traditional databases have limited scale and do not work well with such huge data volumes.
2. Schema - Hadoop ecosystem has a flexible schema. The schema can be changed easily as per the data. In traditional databases, the schema is fixed and modifying it is costly.
3. Type of data - Hadoop ecosystem can store and process both structured and unstructured data like images, videos, log files, XML, JSON, etc. Traditional databases can only handle structured data well.
4. Fault tolerance - Hadoop ecosystem is highly fault tolerant as the data is replicated multiple times across data nodes. Even if some nodes fail, the data can be accessed from other replicas. Traditional databases are less fault tolerant.
5. Cost - Hadoop ecosystem is an open source, low cost solution as it uses commodity hardware. Traditional databases are expensive as they use specialized hardware and software.
6. Processing - Hadoop ecosystem uses MapReduce and distributed processing to process data in parallel across nodes for fast processing of huge data. Traditional databases do not have such distributed and parallel processing capabilities.

The key advantages of Hadoop ecosystem over traditional databases are scale, schema flexibility, capability to handle unstructured data, fault tolerance and low cost. However, Hadoop may not be suitable for some OLTP applications which require very fast query processing like traditional databases. Both have their pros and cons and are used based on the use cases.