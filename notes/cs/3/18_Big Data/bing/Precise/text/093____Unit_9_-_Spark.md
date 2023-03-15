## Unit 9 - Spark

1. **Introduction:** Apache Spark is an open-source distributed computing system that can process large amounts of data quickly. It was developed in response to the limitations of the Hadoop MapReduce computing model, which is efficient for batch processing but not well-suited for interactive queries or iterative algorithms.

2. **Architecture:** Spark's architecture is based on the concept of a Resilient Distributed Dataset (RDD), which is an immutable distributed collection of data that can be processed in parallel. Spark also includes a driver program that coordinates the tasks across the cluster and a cluster manager that manages the allocation of resources.

3. **Programming Model:** Spark provides APIs in several programming languages, including Scala, Java, Python, and R. The programming model is based on transformations and actions applied to RDDs. Transformations create new RDDs from existing ones, while actions trigger the computation and return a result to the driver program.

4. **Libraries:** Spark includes several libraries for specific tasks, such as Spark SQL for structured data processing, MLlib for machine learning, GraphX for graph processing, and Streaming for real-time data processing.

5. **Performance:** Spark is designed to be fast, both for batch processing and interactive queries. It achieves this by keeping data in memory as much as possible and by minimizing data movement. Spark can also spill data to disk if there is not enough memory available.

6. **Deployment:** Spark can be deployed on a variety of cluster managers, including its own standalone cluster manager, Hadoop YARN, and Apache Mesos. It can also be run locally on a single machine for testing and development purposes.

7. **Conclusion:** Apache Spark is a powerful and flexible distributed computing system that has become a popular choice for big data processing. Its architecture, programming model, and libraries make it well-suited for a wide range of tasks, and its performance and ease of deployment have made it a popular choice for many organizations.