# Overview of Commercial Real Time Databases

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases have to meet certain requirements, such as timeliness, consistency, concurrency, reliability, and availability.
- Real-time databases can be classified into two types: hard real-time and soft real-time.
  - Hard real-time databases have to guarantee strict deadlines for every transaction, and any missed deadline is considered a failure.
  - Soft real-time databases have to meet most of the deadlines, but some occasional deadline misses are acceptable.
- Some examples of commercial real-time databases are:
  - Raima Database Manager (RDM): a cross-platform, embedded, in-memory, SQL database that supports hard and soft real-time applications.
  - Oracle TimesTen: an in-memory, relational database that provides low-latency and high-throughput data access for real-time applications.
  - Google Cloud Firestore: a scalable, serverless, NoSQL database that provides real-time synchronization and offline support for web and mobile applications.
  - IBM Informix: a hybrid database that combines SQL, NoSQL, and time-series data for real-time analytics and IoT applications.
  - Microsoft SQL Server: a relational database that supports in-memory OLTP, temporal tables, and real-time operational analytics.