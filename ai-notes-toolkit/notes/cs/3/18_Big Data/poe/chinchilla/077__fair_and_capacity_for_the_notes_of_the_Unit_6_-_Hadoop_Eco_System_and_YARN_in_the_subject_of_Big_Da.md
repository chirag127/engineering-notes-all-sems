### Fair and Capacity for the Notes of the Unit 6 - Hadoop Eco System and YARN in the Subject of Big Data

In this unit of Big Data, we will be discussing the Hadoop Eco System and YARN. Here are some important points to keep in mind:

- Hadoop Eco System is a collection of open-source software utilities that facilitate using a network of many computers to solve problems involving massive amounts of data and computation. It is designed to scale up from single servers to thousands of machines, each offering local computation and storage.

- YARN (Yet Another Resource Negotiator) is one of the key components of Hadoop Eco System. It is responsible for managing resources and scheduling applications running on Hadoop. YARN separates the resource management and job scheduling functions, allowing them to scale independently.

- Fair scheduling is a technique used by YARN to allocate resources to applications. It ensures that each application gets a fair share of resources, regardless of the number of jobs running in the cluster.

- Capacity scheduling is another technique used by YARN to allocate resources to applications. It is based on dividing the cluster into multiple queues, each with a defined capacity. Applications are assigned to specific queues based on their resource requirements.

- Fair and capacity scheduling can be used together to provide a balance between fairness and predictability. By assigning applications to queues based on their resource requirements, capacity scheduling ensures predictability, while fair scheduling ensures fairness by allocating resources based on the needs of each application.

- YARN also provides support for containerization, which allows applications to be run in isolated environments. Containers provide a lightweight and efficient way to run applications, and they can be easily moved between machines in the cluster.

- Another important feature of YARN is its support for long-running services, such as data streaming applications. YARN allows these services to run continuously, even as individual jobs come and go.

- In summary, Hadoop Eco System and YARN provide a powerful platform for processing large amounts of data. Fair and capacity scheduling are important techniques for managing resources and ensuring that applications get the resources they need to run efficiently. Containerization and support for long-running services are also important features that make YARN a flexible and scalable resource management system.