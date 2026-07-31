## Unit 3 - Cloud Architecture, Services And Storage

This unit covers the following topics:

- Cloud architecture: the design principles and components of a cloud computing system, such as virtualization, scalability, elasticity, availability, fault tolerance, and security.
- Cloud services: the types and characteristics of cloud services, such as Software as a Service (SaaS), Platform as a Service (PaaS), Infrastructure as a Service (IaaS), and Function as a Service (FaaS).
- Cloud storage: the methods and technologies for storing and accessing data in the cloud, such as object storage, block storage, file storage, and database storage.

### Cloud architecture

Cloud architecture is the design of a cloud computing system that consists of various components and layers that work together to deliver cloud services. Some of the key components and layers of cloud architecture are:

- Virtualization: the process of creating virtual instances of physical resources, such as servers, storage, and networks, that can be dynamically allocated and managed by the cloud provider. Virtualization enables cloud computing to achieve scalability, elasticity, and resource optimization.
- Scalability: the ability of a cloud system to handle increasing or decreasing demand for cloud services by adding or removing virtual resources. Scalability can be horizontal (adding more instances of the same resource) or vertical (increasing the capacity of an existing resource).
- Elasticity: the ability of a cloud system to automatically adjust the amount of virtual resources according to the current workload and performance requirements. Elasticity enables cloud computing to provide on-demand and pay-as-you-go services.
- Availability: the degree to which a cloud system is accessible and operational at any given time. Availability is measured by the percentage of time that a cloud service is up and running, and is affected by factors such as redundancy, backup, recovery, and failover mechanisms.
- Fault tolerance: the ability of a cloud system to continue functioning correctly in the event of failures or errors in its components or layers. Fault tolerance is achieved by implementing techniques such as replication, load balancing, and fault detection and isolation.
- Security: the protection of cloud data and services from unauthorized access, modification, or destruction. Security is a major concern in cloud computing, and involves aspects such as encryption, authentication, authorization, auditing, and compliance.

### Cloud services

Cloud services are the different types of offerings that cloud providers deliver to cloud users over the internet. Cloud services can be classified into four main categories, based on the level of abstraction and control that the user has over the cloud resources:

- Software as a Service (SaaS): the delivery of software applications that are hosted and managed by the cloud provider, and accessed by the user through a web browser or a mobile app. The user does not have to install, update, or maintain the software, and only pays for the usage or subscription of the service. Examples of SaaS are Gmail, Netflix, and Salesforce.
- Platform as a Service (PaaS): the delivery of a development and deployment environment that allows the user to create, test, and run software applications using the cloud provider's tools and infrastructure. The user does not have to manage the underlying servers, storage, or networks, and only pays for the resources and services that are used. Examples of PaaS are Google App Engine, Microsoft Azure, and Heroku.
- Infrastructure as a Service (IaaS): the delivery of computing resources, such as servers, storage, and networks, that are virtualized and provisioned by the cloud provider, and accessed by the user through a web interface or an API. The user has full control and responsibility over the configuration, operation, and maintenance of the resources, and only pays for the amount and duration of the resources that are used. Examples of IaaS are Amazon Web Services, IBM Cloud, and DigitalOcean.
- Function as a Service (FaaS): the delivery of a serverless computing model that allows the user to execute small pieces of code, called functions, in response to events or triggers, without having to manage any servers or infrastructure. The user only pays for the execution time and resources of the functions, and benefits from the scalability and elasticity of the cloud provider. Examples of FaaS are AWS Lambda, Google Cloud Functions, and Azure Functions.

### Cloud storage

Cloud storage is the method of storing and accessing data in the cloud, using the cloud provider's infrastructure and services. Cloud storage can be categorized into four main types, based on the data model and access method:

- Object storage: the storage of data as discrete units, called objects, that have a unique identifier, metadata, and data. Object storage is suitable for storing unstructured or semi-structured data, such as images, videos, documents, and backups. Object storage is accessed through a RESTful API, using HTTP methods such as GET, PUT, and DELETE