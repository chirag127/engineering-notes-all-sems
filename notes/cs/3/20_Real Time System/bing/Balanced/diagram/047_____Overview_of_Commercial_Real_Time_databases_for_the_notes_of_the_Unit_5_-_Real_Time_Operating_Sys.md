### Overview of Commercial Real Time Databases

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases can be classified into two types: hard real-time and soft real-time.
  - Hard real-time databases have strict timing constraints and must guarantee that transactions are completed within their deadlines, otherwise the system may fail or cause severe consequences.
  - Soft real-time databases have more relaxed timing constraints and can tolerate some degree of deadline misses, but still aim to optimize the performance and quality of service.
- Some of the challenges and requirements for real-time databases are:
  - Concurrency control: ensuring that concurrent transactions do not interfere with each other and maintain the consistency and integrity of the data.
  - Scheduling: deciding the order and priority of transactions to meet their deadlines and optimize the system performance.
  - Data freshness: ensuring that the data reflects the current state of the real world and is not outdated or stale.
  - Fault tolerance: ensuring that the system can recover from failures and continue to operate normally.
  - Security: ensuring that the data is protected from unauthorized access and modification.
- Some of the examples of commercial real-time databases are :
  - Dealpath: a cloud-based platform that provides data and analytics for commercial real estate transactions and investments.
  - Altus Group: a data provider that offers historical and current information on commercial real estate markets, properties, and deals.
  - CoStar: a leading provider of commercial real estate data and analytics, covering more than 5.5 million properties and 18 million tenants.
  - Google Cloud Firestore: a highly scalable, fully managed NoSQL database service that supports real-time data synchronization and offline access for web and mobile applications.