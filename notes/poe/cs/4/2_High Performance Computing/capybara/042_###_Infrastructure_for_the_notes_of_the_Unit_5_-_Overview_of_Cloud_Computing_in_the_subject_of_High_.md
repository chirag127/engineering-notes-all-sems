### Infrastructure for the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing

Infrastructure is a crucial aspect of cloud computing that determines the reliability, scalability, and performance of cloud-based services. In this section, we will discuss the infrastructure components that make up cloud computing.

#### 1. Compute

Compute refers to the virtual machines or containers that run applications in the cloud. These virtual machines are created on demand by the cloud service provider and can be scaled up or down based on the application's resource requirements. Compute instances can be further classified into three types:

- Virtual Machines (VMs): VMs are the most common type of compute instance in the cloud. They provide a complete operating system environment and can run any application that is compatible with the OS.
- Containers: Containers provide a lightweight alternative to VMs. They share the same underlying OS kernel and are isolated from each other using namespaces and cgroups.
- Serverless Functions: Serverless functions are event-driven compute instances that execute a piece of code in response to an event.

#### 2. Storage

Cloud storage provides a scalable and durable storage solution for data. Cloud storage can be classified into two types:

- Object Storage: Object storage stores unstructured data as objects. Each object is identified by a unique key and can be accessed using a REST API. Object storage is highly scalable and durable and is best suited for storing large volumes of data.
- Block Storage: Block storage provides a raw block-level storage solution that can be attached to compute instances as a disk. Block storage is best suited for storing structured data that requires low-latency access.

#### 3. Network

The cloud network provides connectivity between compute instances, storage, and other cloud services. The cloud network can be classified into two types:

- Virtual Private Cloud (VPC): A VPC is a logically isolated network that can be customized to meet the specific requirements of an application. A VPC can be further divided into subnets for better network management.
- Load Balancers: Load balancers distribute incoming traffic across multiple compute instances to improve the availability and scalability of an application.

#### 4. Database

The cloud database provides a secure and scalable storage solution for structured data. Cloud databases can be classified into two types:

- Relational Databases: Relational databases provide a traditional SQL-based database solution. They are well-suited for applications that require complex queries and transactions.
- NoSQL Databases: NoSQL databases provide a schema-less database solution that can handle unstructured data. They are well-suited for applications that require high scalability and low-latency access to data.

#### 5. Management Tools

Cloud management tools provide a centralized way to monitor, manage, and automate cloud resources. Some common management tools include:

- Cloud Console: A web-based console that provides a graphical user interface to manage cloud resources.
- Command-line Interface (CLI): A command-line tool that provides a programmatic way to manage cloud resources.
- APIs: APIs provide a programmatic way to manage cloud resources using RESTful APIs.

Mnemonic: Remember the acronym CSNMD (Compute, Storage, Network, Management tools, and Database) to easily remember the infrastructure components of cloud computing.