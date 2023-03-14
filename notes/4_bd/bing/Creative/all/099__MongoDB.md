### MongoDB

MongoDB is an open source, nonrelational database management system (DBMS) that uses flexible documents instead of tables and rows to process and store various forms of data. MongoDB is a document-oriented database, which means that data is stored as documents, and documents are grouped in collections. The document model is a lot more natural for developers to work with because documents are self-contained and can be treated as objects. MongoDB is also a distributed database at its core, so high availability, horizontal scaling, and geographic distribution are built in and easy to use.

Some of the features and key characteristics of MongoDB are:

- MongoDB supports a rich and expressive query language that allows you to filter and sort by any field, no matter how nested it may be within a document. You can also perform complex aggregations and joins across multiple collections, and use full-text search, geospatial queries, and graph traversals.
- MongoDB allows you to store data in a flexible and dynamic schema, which means that you can change the structure and content of your documents without affecting the existing data. You can also use schema validation to enforce data integrity and consistency.
- MongoDB provides ACID transactions that span multiple documents, multiple collections, multiple shards, and multiple replica sets. This ensures that your data is consistent and reliable across complex and distributed systems.
- MongoDB offers various options for data storage, such as in-memory, encrypted, or compressed. You can also use GridFS to store and stream large files, such as images, videos, or audio.
- MongoDB can scale horizontally by using sharding, which is the process of distributing data across multiple machines. Sharding allows you to handle large volumes of data and high throughput operations, while maintaining high performance and availability.
- MongoDB can run on any platform, from your laptop to your data center. You can also use MongoDB Atlas, which is a fully-managed cloud service that provides security, backup, monitoring, and automation features. You can deploy MongoDB Atlas on AWS, Google Cloud, or Azure, and access advanced functionality such as auto-scaling, serverless instances, full-text search, and data distribution across regions and clouds.
- MongoDB has a vibrant and active community of developers and users, who contribute to the development and improvement of the database. You can also access various resources and tools, such as MongoDB University, MongoDB Shell, MongoDB Compass, MongoDB Connector for BI, and more.

Some of the advantages of using MongoDB are:

- MongoDB is easy to use and learn, as it supports many programming languages and frameworks, and has a simple and intuitive syntax. You can also use MongoDB Shell, which is an interactive JavaScript interface that allows you to interact with your data and perform various operations.
- MongoDB is flexible and adaptable, as it allows you to store and process data in various formats and structures, and change them as your needs evolve. You can also use MongoDB for various use cases, such as transactional, analytical, search, time series, and more.
- MongoDB is fast and scalable, as it uses an efficient and compact binary data format (BSON), and supports various indexing and caching techniques. You can also use sharding and replication to distribute your data and workload across multiple machines, and ensure high performance and availability.
- MongoDB is reliable and secure, as it provides ACID transactions, data encryption, authentication, authorization, auditing, and backup features. You can also use MongoDB Atlas, which is a fully-managed cloud service that provides security, backup, monitoring, and automation features .

Some of the disadvantages of using MongoDB are:

- MongoDB does not support joins, which means that you have to denormalize your data and store it in a single document, or use multiple queries to fetch data from different collections. This can lead to data duplication, inconsistency, and increased storage space.
- MongoDB does not support SQL, which means that you have to learn a new query language and syntax, and use different tools and drivers to access and analyze your data. You can also use MongoDB Connector for BI, which allows you to use SQL-based tools and applications with MongoDB, but it has some limitations and performance overhead.
- MongoDB does not enforce a schema, which means that you have to ensure data quality and consistency at the application level, or use schema validation to enforce some rules and constraints. However, schema validation can also affect performance and flexibility.

Some of the mnemonics and learning tricks