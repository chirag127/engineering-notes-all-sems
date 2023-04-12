

## Unit 1 - Introduction To Cloud Computing

- Cloud computing is the delivery of computing services over the internet, such as servers, storage, databases, networking, software, analytics, and intelligence.
- Cloud computing offers various benefits, such as scalability, reliability, security, cost-efficiency, and innovation.
- Cloud computing can be classified into three main service models: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS).
- IaaS provides the basic computing resources, such as servers, storage, and networks, that can be rented and managed by the user.
- PaaS provides the platform and tools for developing and deploying applications, such as operating systems, databases, and middleware, that are managed by the provider.
- SaaS provides the software applications that are hosted and run by the provider, such as email, CRM, and ERP, that can be accessed by the user via a web browser or an API.
- Cloud computing can also be classified into four main deployment models: public cloud, private cloud, hybrid cloud, and community cloud.
- Public cloud is the most common type of cloud computing, where the provider offers the services to the general public over the internet, such as AWS, Azure, and Google Cloud.
- Private cloud is a type of cloud computing where the services are dedicated to a single organization or customer, and are hosted either on-premises or off-premises by the provider or a third party, such as VMware, IBM, and Oracle.
- Hybrid cloud is a type of cloud computing where the services are a combination of public and private clouds, and are connected by a common network or technology, such as AWS Outposts, Azure Stack, and Google Anthos.
- Community cloud is a type of cloud computing where the services are shared by a group of organizations or customers that have a common interest or goal, such as security, compliance, or performance, and are hosted either on-premises or off-premises by the provider or a third party, such as OpenStack, Cloud Foundry, and G-Cloud.



### Definition of Cloud

- Cloud computing is the **delivery of computing services** over the internet, rather than using local servers or personal computers  .
- Cloud computing services include **servers, storage, databases, networking, software, analytics, and intelligence** .
- Cloud computing enables **faster innovation, flexible resources, and economies of scale** .
- Cloud computing is based on some form of **virtualized IT infrastructure** that can be **pooled and divided** irrespective of physical hardware boundaries.
- Cloud computing is **on-demand** and **managed by a cloud service provider** (or CSP) that hosts the computing resources at a remote data center .
- Cloud computing can be classified into different **service models** and **deployment models** depending on the level of abstraction, control, and sharing of resources  .



### Evolution of Cloud Computing

- Cloud computing is the delivery of computing services such as servers, storage, databases, networking, software, analytics, and intelligence over the Internet.
- The term "cloud" is derived from the symbol used to represent the Internet in network diagrams.
- The evolution of cloud computing can be divided into four stages: grid computing, utility computing, virtualization, and web services.

#### Grid Computing

- Grid computing is the use of a network of distributed computing resources to perform large-scale tasks that require high performance and parallel processing.
- Grid computing emerged in the late 1990s as a way to harness the power of geographically dispersed computers for scientific and engineering applications.
- Examples of grid computing projects include SETI@home, which searches for extraterrestrial intelligence, and Folding@home, which simulates protein folding.

#### Utility Computing

- Utility computing is the provision of computing resources as a service, similar to how electricity, water, and gas are delivered as utilities.
- Utility computing allows users to pay only for the resources they consume, rather than investing in fixed infrastructure and maintenance costs.
- Utility computing was popularized by companies such as Amazon, Google, and Salesforce, which offered scalable and on-demand computing services to customers and businesses.

#### Virtualization

- Virtualization is the creation of virtual machines that can run multiple operating systems and applications on a single physical server.
- Virtualization enables the efficient utilization of hardware resources, the isolation and security of different workloads, and the flexibility and portability of virtual machines across different platforms.
- Virtualization was pioneered by IBM in the 1970s with its VM operating system, and later by VMware, Microsoft, and others in the 2000s.

#### Web Services

- Web services are software components that can be accessed and invoked over the Internet using standard protocols such as HTTP and XML.
- Web services enable the interoperability and integration of different applications and systems across the web, regardless of their underlying platforms and languages.
- Web services are the building blocks of cloud computing, as they provide the functionality and data that can be consumed by cloud applications and users.



### Underlying Principles of Parallel and Distributed Computing

- Parallel and distributed computing are two models of computation that allow multiple tasks to be executed simultaneously, either on a single computer or across multiple computers .
- Parallel computing on a single computer uses multiple processors or cores to process tasks in parallel, whereas distributed computing uses multiple computing devices (such as computers, servers, or mobile devices) to process those tasks .
- Parallel and distributed computing build on fundamental systems concepts, such as concurrency, mutual exclusion, consistency in state/memory manipulation, message-passing, and shared-memory models .
- Concurrency is the ability of a system to execute multiple tasks at the same time, either in parallel or interleaved .
- Mutual exclusion is the property that ensures that only one task can access a shared resource at a time, preventing conflicts or inconsistencies .
- Consistency is the property that ensures that the state or memory of a system is coherent and reliable across multiple tasks or devices .
- Message-passing is a communication model in which tasks or devices exchange data or instructions through messages, such as emails, texts, or packets .
- Shared-memory is a communication model in which tasks or devices access a common memory space, such as RAM, cache, or disk .
- Parallel and distributed computing have many applications and benefits, such as speeding up computation, improving scalability, enhancing reliability, and saving time and money  .
- Parallel and distributed computing also have many challenges and limitations, such as synchronization, coordination, load balancing, fault tolerance, security, and complexity  .
- Synchronization is the process of ensuring that multiple tasks or devices operate in a coordinated and consistent manner, such as using clocks, locks, or barriers .
- Coordination is the process of managing the dependencies and interactions among multiple tasks or devices, such as using protocols, algorithms, or middleware .
- Load balancing is the process of distributing the workload evenly among multiple tasks or devices, such as using scheduling, partitioning, or replication .
- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures, such as using redundancy, recovery, or checkpointing .
- Security is the protection of a system from unauthorized or malicious access, modification, or damage, such as using encryption, authentication, or authorization .
- Complexity is the measure of the difficulty or cost of designing, implementing, testing, debugging, or maintaining a system, such as using abstraction, modularity, or decomposition .



### Cloud Characteristics

Cloud computing is a model for enabling convenient, on-demand network access to a shared pool of configurable computing resources, such as networks, servers, storage, applications, and services. Cloud computing has some essential features that distinguish it from traditional computing models. These are:

- **On-demand self-service**: Cloud users can provision and release computing resources as needed, without requiring human intervention from the service provider . This gives users more control and flexibility over their computing needs.
- **Multi-tenancy and resource pooling**: Cloud service providers use a multi-tenant architecture to accommodate more users at the same time, by sharing the same physical and virtual resources among them . This enables higher utilization and efficiency of the resources, as well as lower costs for the users.
- **Broad network access**: Cloud services are accessible over the internet, using standard protocols and devices, such as laptops, smartphones, tablets, etc . This allows users to access the cloud services from anywhere and anytime, as long as they have an internet connection.
- **Rapid elasticity and scalability**: Cloud services can be scaled up or down quickly and dynamically, depending on the demand and workload of the users . This enables users to handle peak or fluctuating demands, without worrying about the capacity or performance of the resources.
- **Measured service**: Cloud service providers monitor and measure the usage and performance of the cloud resources, and charge the users accordingly . This ensures transparency and accountability of the cloud services, as well as optimal allocation and utilization of the resources.



### Elasticity in Cloud

- Elasticity in cloud computing is the ability to adapt to workload changes by provisioning and de-provisioning resources in an autonomic manner, such that the available resources match the current demand as closely as possible.
- Elasticity is a defining characteristic that differentiates cloud computing from previous computing paradigms, such as grid computing.
- Elasticity in cloud computing allows the user to scale computer processing, memory, and storage capacity to meet changing demands.
- Elasticity in cloud computing can refer to 'cloudbursting' from on-premises infrastructure into the public cloud to meet a sudden or seasonal demand.
- Elasticity in cloud computing can also refer to the ability to grow or shrink the resources used by a cloud-based application.
- Elasticity in cloud computing is different from scalability, which is the ability to handle a growing amount of work by adding resources to the system.
- Elasticity is used to meet dynamic changes in workload, while scalability is used to meet static increases in workload.
- Elasticity is commonly used by small companies that have unpredictable or variable workloads, while scalability is used by large companies that have stable and predictable workloads.
- Elasticity is a short term planning and adopted for temporary needs, while scalability is a long term planning and adopted for permanent needs.



### On‐demand Provisioning

- On-demand provisioning is one of the features of cloud computing that enables the users to request and access cloud resources whenever they need them, without any human intervention.
- On-demand provisioning allows cloud providers to offer their services on a pay-as-you-go model, where users only pay for the resources they consume.
- On-demand provisioning also enables users to scale up or down their resources according to their changing needs, without affecting the performance or availability of the services.
- On-demand provisioning can be achieved through self-service portals, where users can select, configure, and deploy the cloud resources they require, such as virtual machines, storage, network, applications, etc.
- On-demand provisioning can also be automated through scripts, APIs, or orchestration tools, where users can specify the desired state of the cloud resources and let the system provision them accordingly.
- On-demand provisioning can benefit both the users and the providers of cloud services, as it can improve the efficiency, flexibility, scalability, and cost-effectiveness of the cloud computing model.



## Unit 2 - Cloud Enabling Technologies Service Oriented Architecture

- Service-oriented architecture (SOA) is a method of software development that uses software components called services to create business applications.
- Each service provides a business capability, and services can also communicate with each other across platforms and languages.
- SOA enables the construction of applications from loosely coupled services that can be easily integrated and reused.
- SOA is a critical technology for cloud computing as it supports the broad movement towards internet and the use of WAN and enables smooth interaction between IT service providers and consumers.
- SOA also facilitates the concept of services introduced by microservices architecture, which is a central component of modern cloud computing and virtualization.
- SOA follows an architectural pattern that uses common interface standards and protocols, such as SOAP, REST, and XML, to ensure interoperability and compatibility among services.
- SOA benefits include increased agility, reusability, scalability, and efficiency of software development and deployment.



### REST and Systems of Systems

- REST stands for REpresentational State Transfer, an architectural style for providing standards between computer systems on the web.
- REST-compliant systems, often called RESTful systems, are stateless and separate the concerns of client and server.
- RESTful systems use HTTP methods (such as GET, POST, PUT, DELETE) to perform operations on resources, which are identified by URIs.
- RESTful systems can support different formats of data representation, such as XML, JSON, HTML, etc.
- RESTful systems can be scalable, reliable, and interoperable, as they follow a uniform interface and use standard web protocols.
- Systems of systems (SoS) is a collection of task-oriented or dedicated systems that pool their resources and capabilities together to create a new, more complex system.
- SoS offers more functionality and performance than simply the sum of the constituent systems.
- SoS can be classified into four types: directed, acknowledged, collaborative, and virtual.
- Directed SoS are centrally managed and have a predefined objective, such as a missile defense system.
- Acknowledged SoS have some central management and agreed objectives, but the constituent systems retain their independent operation, such as an air traffic control system.
- Collaborative SoS have no central management and the constituent systems work together to achieve a common goal, such as a scientific research network.
- Virtual SoS have no central management and the constituent systems interact dynamically to provide a service, such as the internet.
- SoS can be challenging to design, develop, and maintain, as they involve multiple stakeholders, domains, and technologies.
- SoS can benefit from using RESTful systems as the interface for communication and integration, as they can leverage the web standards and protocols, and support heterogeneous and distributed systems.
- RESTful systems can also be considered as SoS, as they are composed of multiple web services that interact with each other to provide a higher-level functionality.



### Web Services

- A web service is a software system that supports interoperable machine-to-machine interaction over a network  .
- A web service has an interface that is described in a machine-processable format, such as WSDL (Web Services Description Language), that allows other programs to discover and invoke its functionality .
- A web service can communicate with other programs using standard web protocols, such as HTTP or HTTPS, and data formats, such as XML or JSON .
- A web service can provide data, functionality, or both, depending on the service provider and the service consumer  .
- A web service can be either:
  - A service offered by an electronic device to another electronic device, communicating with each other via the Internet, or
  - A server running on a computer device, listening for requests at a particular port over a network, serving web documents.
- A web service can be implemented using different technologies, such as SOAP (Simple Object Access Protocol), REST (Representational State Transfer), or GraphQL (Graph Query Language)  .
- A web service can be used for various purposes, such as data exchange, integration, automation, or orchestration  .
- A web service is a key component of a service-oriented architecture (SOA), which is a design paradigm that promotes loose coupling, reusability, and interoperability of software components .



### Publish, Subscribe Model

- Publish, subscribe model, or pub/sub model, is a software architecture model by which applications create and share data.
- Pub/sub model is a form of asynchronous service-to-service communication used in serverless and microservices architectures.
- In pub/sub model, any message published to a topic is immediately received by all of the subscribers to the topic.
- Pub/sub model separates the publisher that sends the message from the subscriber that receives the message. The publisher and the subscriber do not need to establish direct contact.
- Pub/sub model enables event-driven architectures and asynchronous parallel processing, while improving performance, reliability and scalability.
- Pub/sub model introduces an asynchronous messaging subsystem that includes the following components:
  - An input messaging channel used by the publisher. The publisher packages events into messages, using a known message format, and sends these messages via the input channel.
  - A messaging engine that receives the messages from the input channel and routes them to one or more output channels based on the topic of the message.
  - One or more output messaging channels used by the subscribers. The subscribers register their interest in a topic and receive the messages that match that topic from the output channel.
  - Optionally, a message store that persists the messages for later delivery or auditing purposes.
- Pub/sub model has the following benefits:
  - Decoupling: Publishers and subscribers are independent and do not need to know each other's identity, location, or implementation details.
  - Scalability: Publishers and subscribers can scale independently and handle variable workloads. Multiple subscribers can consume the same message in parallel.
  - Reliability: Publishers and subscribers can handle failures gracefully and resume communication when possible. Messages can be stored and retried until they are delivered or expired.
  - Flexibility: Publishers and subscribers can dynamically join or leave the system without affecting each other. New topics can be created or deleted as needed.



### Basics of Virtualization

- Virtualization is a process that allows for more efficient utilization of physical computer hardware by creating multiple virtual computers, called virtual machines (VMs), that run on a single physical computer or server .
- Virtualization uses software to create an abstraction layer over computer hardware that allows the hardware elements, such as processors, memory, storage, network, etc., to be divided, shared, or aggregated among the VMs  .
- Virtualization enables the VMs to run different operating systems and applications independently from each other, and to be moved, copied, or migrated across different physical computers or servers  .
- Virtualization is the foundation of cloud computing, as it allows cloud providers to offer scalable, flexible, and cost-effective services to their customers by using a large pool of virtualized resources .
- There are different types of virtualization, such as:
  - Server virtualization: The most common type of virtualization, where a physical server is divided into multiple VMs that can run different operating systems and applications  .
  - Desktop virtualization: A type of virtualization where a user's desktop environment, including the operating system, applications, and data, is stored on a remote server and accessed through a thin client or a web browser .
  - Application virtualization: A type of virtualization where an application is isolated from the underlying operating system and delivered to the user as a service or a package . There are three types of application virtualization: local application virtualization, where the application runs on the endpoint device but in a runtime environment; application streaming, where the application lives on a server and sends small components to run on the endpoint device; and remote application virtualization, where the application runs on a server and is accessed through a remote display protocol.
  - Network virtualization: A type of virtualization where the network resources, such as switches, routers, firewalls, load balancers, etc., are abstracted from the physical hardware and managed by software . Network virtualization can create multiple virtual networks that run on a single physical network, or combine multiple physical networks into a single virtual network .
  - Storage virtualization: A type of virtualization where the storage devices, such as disks, tapes, arrays, etc., are abstracted from the physical hardware and managed by software . Storage virtualization can create a single logical storage pool from multiple physical storage devices, or divide a single physical storage device into multiple logical storage units .
- There are two major kinds of virtualization technologies: virtual machines and containers. Virtual machines use a hypervisor, which is a software layer that runs on the physical hardware or on a host operating system, to create and manage the VMs . Containers use the operating system's kernel to create and manage isolated environments for applications, without the need for a hypervisor or a guest operating system. Each has its pros and cons and can be used independently or together, depending on the use case and the requirements.



### Types of Virtualization for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

Virtualization is the process of creating a virtual representation of physical resources, such as servers, storage, network, and applications, in order to optimize the utilization, performance, and scalability of the resources. Virtualization is one of the key enabling technologies for cloud computing, as it allows the creation of multiple isolated and dynamic virtual environments on a shared physical infrastructure.

There are different types of virtualization in cloud computing, depending on the level of abstraction and the resource being virtualized. Some of the common types are:

- **Server virtualization**: Server virtualization is the process of partitioning a physical server into multiple virtual servers, each with its own operating system and applications. Server virtualization allows the consolidation of multiple servers on a single physical machine, reducing the cost, space, and power consumption of the infrastructure. Server virtualization also enables the flexibility and agility of the virtual servers, as they can be created, deleted, migrated, and scaled on demand. Server virtualization can be implemented using different techniques, such as full virtualization, para-virtualization, and containerization   .

- **Storage virtualization**: Storage virtualization is the process of abstracting the physical storage devices and presenting them as a single logical storage pool. Storage virtualization allows the management of heterogeneous storage devices from a centralized console, simplifying the administration, allocation, and backup of the storage resources. Storage virtualization also enables the optimization of the storage performance, availability, and utilization, as it can perform load balancing, replication, deduplication, and compression of the data. Storage virtualization can be implemented at different levels, such as block-level, file-level, or object-level  .

- **Network virtualization**: Network virtualization is the process of creating a virtual network that is independent of the underlying physical network. Network virtualization allows the creation of multiple logical networks with different characteristics, such as topology, security, and quality of service, on a shared physical network. Network virtualization also enables the isolation and mobility of the virtual networks, as they can be assigned to different tenants, applications, or locations. Network virtualization can be implemented using different techniques, such as overlay networks, software-defined networking, and network function virtualization  .

- **Data virtualization**: Data virtualization is the process of abstracting the data sources and presenting them as a single logical data source. Data virtualization allows the integration of heterogeneous data sources, such as databases, files, web services, and cloud services, without requiring physical data movement or replication. Data virtualization also enables the access and analysis of the data in real-time, as it can perform data transformation, caching, and query optimization. Data virtualization can be implemented using different tools, such as data federation, data abstraction, and data delivery.

- **Application virtualization**: Application virtualization is the process of decoupling the application from the underlying operating system and hardware. Application virtualization allows the delivery of the application to different devices and platforms, without requiring installation or configuration. Application virtualization also enables the security and portability of the application, as it can isolate the application from the host system and run it in a sandboxed environment. Application virtualization can be implemented using different techniques, such as streaming, encapsulation, and remote display.

- **Desktop virtualization**: Desktop virtualization is the process of creating a virtual desktop that is hosted on a remote server and accessed by the user through a thin client or a web browser. Desktop virtualization allows the centralization and standardization of the desktop environment, reducing the cost, complexity, and risk of the desktop management. Desktop virtualization also enables the personalization and mobility of the desktop, as it can provide the user with a consistent and customized desktop experience across different devices and locations. Desktop virtualization can be implemented using different models, such as virtual desktop infrastructure, session-based desktop, and desktop as a service .



### Implementation Levels of Virtualization

Virtualization is the process of creating a virtual representation of physical resources, such as hardware, software, network, storage, etc. Virtualization enables multiple applications or operating systems to run on the same physical machine, sharing the available resources and improving the efficiency and flexibility of the system.

There are different levels of virtualization implementation, depending on the degree of abstraction and isolation between the virtual and physical layers. The following are the five main levels of virtualization implementation    :

- **Instruction Set Architecture Level (ISA)**: In this level, virtualization works through an ISA emulation. This means that the virtual machine (VM) can run on a different hardware architecture than the one it was designed for, by translating the instructions from one ISA to another. For example, a VM can run a Windows OS on a Linux host, or an ARM-based OS on an x86 host. This level of virtualization provides the highest compatibility and portability, but also the lowest performance and efficiency, due to the overhead of emulation.

- **Hardware Abstraction Level (HAL)**: In this level, virtualization works at the hardware level, by creating a virtual hardware layer that abstracts the physical hardware from the VMs. The VMs can run on the same hardware architecture as the host, but they are isolated from each other and from the host OS. The virtual hardware layer can also provide some features that are not available on the physical hardware, such as virtual devices, memory management, or security mechanisms. This level of virtualization provides a good balance between compatibility, performance, and security, but also requires some modifications to the guest OS and the applications to run on the virtual hardware.

- **Operating System Level**: In this level, virtualization works at the operating system level, by creating an abstract layer between the applications and the OS. The applications run on the same OS as the host, but they are isolated from each other and from the host OS by using containers, namespaces, or jails. The applications can share the same OS kernel, libraries, and binaries, but they have their own file systems, processes, network interfaces, and resources. This level of virtualization provides the highest performance and efficiency, but also the lowest compatibility and security, as the applications are limited by the OS features and vulnerabilities.

- **Library Level**: In this level, virtualization works at the library level, by creating a virtual library layer that abstracts the OS and the hardware from the applications. The applications run on the same OS as the host, but they use a different set of libraries and APIs than the ones provided by the OS. The virtual library layer can provide some features that are not available on the OS, such as cross-platform compatibility, portability, or scalability. For example, a Java application can run on any OS that supports the Java Virtual Machine (JVM), or a web application can run on any browser that supports the JavaScript engine. This level of virtualization provides a good balance between compatibility, performance, and portability, but also requires some modifications to the applications to use the virtual libraries and APIs.

- **Application Level**: In this level, virtualization works at the application level, by creating a virtual application layer that abstracts the OS, the hardware, and the libraries from the applications. The applications run on the same OS as the host, but they use a different set of applications and services than the ones provided by the OS. The virtual application layer can provide some features that are not available on the OS, such as cloud-based services, distributed computing, or parallel processing. For example, a Google Docs application can run on any OS that supports a web browser, or a Hadoop application can run on any OS that supports a Java runtime environment. This level of virtualization provides the highest compatibility and portability, but also the lowest performance and efficiency, as the applications are dependent on the network and the cloud services.



### Virtualization Structures

- Virtualization is the process of creating and delivering a virtual rather than a physical version of something, such as a desktop, operating system, network resource, or server  .
- Virtualization is a key and dominant technology in cloud computing, as it enables the creation of virtual versions of hardware and software resources that can be shared, scaled, and accessed on demand   .
- A virtualization architecture is a conceptual model of a virtual infrastructure that specifies the arrangement and interrelationships among the particular components in the virtual environment.
- A virtualization architecture runs multiple operating systems on the same machine using the same hardware and also ensures their smooth functioning.
- A virtualization architecture can be classified into two types: hardware virtualization and software virtualization.
- Hardware virtualization is the process of creating virtual machines that run on a physical machine and share its hardware resources, such as CPU, memory, disk, and network  .
- Software virtualization is the process of creating virtual environments that run on a virtual machine and provide software resources, such as operating system, applications, storage, and network .
- Hardware virtualization can be further divided into three types: full virtualization, paravirtualization, and hardware-assisted virtualization.
- Full virtualization is the process of creating virtual machines that run on a hypervisor, which is a software layer that intercepts and emulates the instructions from the guest operating systems to the hardware .
- Paravirtualization is the process of creating virtual machines that run on a modified operating system that is aware of the virtualization and communicates directly with the hypervisor, bypassing the hardware emulation .
- Hardware-assisted virtualization is the process of creating virtual machines that run on a hypervisor that is supported by the hardware features of the physical machine, such as Intel VT-x and AMD-V, which enhance the performance and security of the virtualization .
- Software virtualization can be further divided into four types: operating system virtualization, application virtualization, storage virtualization, and network virtualization .
- Operating system virtualization is the process of creating virtual environments that run on a single operating system and provide isolated and independent instances of the operating system for each application .
- Application virtualization is the process of creating virtual environments that run on a virtual machine or a host operating system and provide isolated and independent instances of the application for each user .
- Storage virtualization is the process of creating virtual environments that run on a virtual machine or a host operating system and provide a unified and abstracted view of the storage resources, such as disks, files, and volumes .
- Network virtualization is the process of creating virtual environments that run on a virtual machine or a host operating system and provide a unified and abstracted view of the network resources, such as switches, routers, and firewalls .



### Tools and Mechanisms for Service Oriented Architecture

- Service Oriented Architecture (SOA) is an architectural style that enables the creation and integration of loosely coupled, self-contained, and interoperable services  .
- Services are software components that provide functionality through well-defined interfaces and protocols  .
- Services can be composed and orchestrated to form applications that support business processes and workflows  .
- SOA promotes the reuse, scalability, and maintainability of services, as well as the flexibility and agility of the system  .
- Some of the tools and mechanisms that support SOA are:

  - Service registry and repository: A service registry is a centralized directory that stores information about the available services, such as their names, descriptions, locations, and interfaces . A service repository is a database that stores additional metadata about the services, such as their policies, contracts, dependencies, and versions . These tools enable the discovery, governance, and management of services in SOA.
  - Service bus: A service bus is a middleware component that facilitates the communication and integration of services in SOA . It provides features such as routing, transformation, mediation, security, and monitoring of service interactions . A service bus can also support different protocols, formats, and standards for service interoperability .
  - Service composition and orchestration: Service composition is the process of combining multiple services to create a new service or application that meets a specific business requirement  . Service orchestration is the process of coordinating the execution and interaction of services in a predefined sequence or workflow  . These mechanisms enable the creation of complex and dynamic service-based solutions in SOA.
  - Service adaptation: Service adaptation is the process of modifying or evolving a service to meet changing requirements or environments in SOA. It can involve changing the functionality, interface, quality, or behavior of a service. Service adaptation can be performed manually or automatically, depending on the tools and frameworks available. Service adaptation enables the flexibility and agility of SOA.



### Virtualization of CPU

- CPU virtualization is a technique that creates multiple versions of various system resources, including your CPU, server, storage, etc. 
- CPU virtualization involves a single CPU acting as if it were multiple separate CPUs. The most common reason for doing this is to run multiple different operating systems on one machine. 
- CPU virtualization emphasizes performance and runs directly on the available CPUs whenever possible. 
- CPU virtualization can be achieved by using a software layer called a hypervisor, which creates and manages virtual machines (VMs) that run on the physical CPU. 
- CPU virtualization can be classified into two types: full virtualization and paravirtualization. 
- Full virtualization allows the guest operating system to run unmodified on the virtual CPU, as if it were running on a real CPU. The hypervisor intercepts and emulates the privileged instructions of the guest operating system. 
- Paravirtualization requires the guest operating system to be modified to run on the virtual CPU. The hypervisor exposes a set of hypercalls that the guest operating system can use to communicate with the hypervisor. Paravirtualization can improve performance and reduce overhead. 
- CPU virtualization can provide many benefits, such as:
  - Isolation: Each VM runs independently and securely from other VMs, preventing interference and improving reliability. 
  - Consolidation: Multiple VMs can run on a single CPU, reducing the need for physical hardware and saving costs. 
  - Migration: VMs can be moved from one CPU to another without downtime, enabling load balancing and fault tolerance. 
  - Compatibility: VMs can run different operating systems and applications on the same CPU, increasing flexibility and interoperability.



### Memory for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

- Service Oriented Architecture (SOA) is a design paradigm that defines how software components can interact and cooperate to provide business services .
- SOA is based on the principles of loose coupling, abstraction, reusability, composability, statelessness, discoverability, and interoperability .
- SOA enables cloud computing by facilitating the integration and orchestration of distributed and heterogeneous services across the internet  .
- REST (Representational State Transfer) is an architectural style that defines how web resources can be accessed and manipulated using a uniform and stateless interface .
- REST is based on the principles of resource identification, resource representation, resource linking, and uniform interface .
- REST enables cloud computing by providing a scalable, flexible, and efficient way of exposing and consuming web services .
- Systems of Systems (SoS) are large-scale systems that consist of multiple independent and interrelated subsystems that collaborate to achieve a common goal .
- SoS are characterized by operational and managerial independence, evolutionary development, emergent behavior, and geographical distribution .
- SoS enable cloud computing by allowing the dynamic and adaptive composition of services from different domains and providers .
- Web Services are software components that can be invoked and composed over the web using standard protocols and formats  .
- Web Services can be classified into two types: SOAP (Simple Object Access Protocol) and RESTful  .
- SOAP is a protocol that defines how to exchange structured and typed messages between web services using XML and HTTP  .
- RESTful is a style that defines how to access and manipulate web resources using HTTP methods and formats  .
- Web Services enable cloud computing by providing a platform-independent and interoperable way of exposing and consuming business functionalities  .
- Publish-Subscribe Model is a communication pattern that decouples the producers and consumers of messages by using an intermediary broker .
- Publish-Subscribe Model is based on the concepts of topics, publishers, subscribers, and brokers .
- Topics are logical channels that categorize the messages according to their content or type .
- Publishers are entities that produce and send messages to the topics .
- Subscribers are entities that register their interest in one or more topics and receive the messages that match their subscriptions .
- Brokers are entities that manage the topics, store the messages, and deliver them to the subscribers .
- Publish-Subscribe Model enables cloud computing by providing a scalable, reliable, and asynchronous way of exchanging data and events between distributed and decoupled services .



### I/O Devices

- I/O devices are hardware components that can take, output, or process data. They receive data as input and provide it to a computer, as well as send computer data to storage media as a storage output.
- Examples of I/O devices are keyboard, mouse, monitor, printer, scanner, microphone, speaker, etc.
- In cloud computing, I/O devices can be virtualized, meaning that a virtual device is substituted for its physical equivalent, such as a network interface card (NIC) or host bus adapter (HBA).
- I/O virtualization can simplify server configurations, reduce electric power consumption, and improve performance and scalability of cloud resources.
- I/O devices can also be connected to the cloud through the Internet of Things (IoT), which is a network of physical objects that can communicate and exchange data with each other and the cloud.
- IoT devices can include smart cameras, thermometers, robots, drones, vibration sensors, and other sensors and actuators.
- IoT devices can benefit from cloud computing services that can securely manage and store data from these devices, as well as provide analytics, artificial intelligence, and other applications.
- IoT devices can also leverage edge computing, which is a distributed computing paradigm that brings computation and data storage closer to the location where it is needed, to improve response times and save bandwidth.



### Virtualization Support and Disaster Recovery

- Virtualization is a process that allows a computer to share its hardware resources with multiple digitally separated environments, such as virtual machines (VMs) or containers.
- Virtualization provides flexibility and efficiency in disaster recovery, which is the process of restoring data and applications after a disruptive event, such as a natural disaster, a cyberattack, or a hardware failure.
- Virtualization helps disaster recovery in the following ways:
  - It reduces the dependency on physical hardware, as VMs can run on any compatible server, regardless of the manufacturer or model.
  - It enables faster and easier backup and recovery of data and applications, as VMs can be replicated, migrated, or restored from snapshots or images.
  - It lowers the cost and complexity of disaster recovery, as VMs can be hosted on cloud servers, which offer scalability, availability, and security .
  - It supports business continuity, as VMs can run on remote or alternate sites, minimizing the downtime and impact of a disaster .
- Virtualization also poses some challenges and risks for disaster recovery, such as:
  - It increases the workload and resource consumption of the host server, which may affect the performance and availability of the VMs.
  - It requires proper management and configuration of the virtual environment, such as network, storage, and security settings, to ensure the compatibility and functionality of the VMs.
  - It exposes the VMs to potential threats, such as malware, data breaches, or human errors, which may compromise the integrity and confidentiality of the data and applications.
- Therefore, virtualization requires careful planning and testing of the disaster recovery strategy, which should include the following steps:
  - Assess the recovery objectives and requirements of the VMs, such as the recovery point objective (RPO), the recovery time objective (RTO), and the recovery level objective (RLO).
  - Select the appropriate virtualization platform and disaster recovery solution, such as hypervisor-based, guest-based, or cloud-based.
  - Design and implement the disaster recovery architecture, such as the network, storage, and security components, and the replication, backup, and recovery methods.
  - Monitor and maintain the disaster recovery environment, such as the performance, availability, and security of the VMs, and the compliance with the policies and regulations.
  - Test and validate the disaster recovery plan, such as the functionality, reliability, and recoverability of the VMs, and the readiness and responsiveness of the staff and stakeholders.



## Unit 3 - Cloud Architecture, Services and Storage

- Cloud architecture is the way technology components combine to build a cloud, in which resources are pooled through virtualization technology and shared across a network.
- Cloud architecture consists of a front-end platform (the client or device used to access the cloud), a back-end platform (servers and storage), a cloud-based delivery (the network that connects the front-end and the back-end), and a cloud service (the software or application that runs on the cloud) .
- Cloud services are the software or applications that run on the cloud and provide various functionalities to the users. Cloud services can be classified into three main types: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS) .
- IaaS provides the basic computing resources, such as servers, storage, and networking, that users can rent and use as per their needs. Examples of IaaS providers are Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform .
- PaaS provides the development and deployment environment, such as operating systems, databases, and tools, that users can use to create and run their own applications on the cloud. Examples of PaaS providers are AWS Elastic Beanstalk, Azure App Service, and Google App Engine .
- SaaS provides the ready-made applications, such as email, office, and CRM, that users can access and use over the internet. Examples of SaaS providers are Gmail, Microsoft Office 365, and Salesforce .
- Cloud storage is a service that allows users to store and access their data on the cloud, rather than on their own devices or servers. Cloud storage can offer benefits such as scalability, durability, availability, and cost-effectiveness .
- Cloud storage can be based on different models, such as object storage, file storage, and block storage. Object storage stores data as objects, which are identified by a unique ID and can have metadata attached to them. File storage stores data as files, which are organized in a hierarchical structure of folders and directories. Block storage stores data as blocks, which are fixed-sized chunks of data that can be accessed by their address .
- Cloud storage can also be classified into different types, such as public cloud storage, private cloud storage, and hybrid cloud storage. Public cloud storage is provided by a third-party service provider, such as AWS S3 or Azure Blob Storage, and is accessible over the internet. Private cloud storage is provided by the user's own organization, and is accessible only within the organization's network. Hybrid cloud storage is a combination of public and private cloud storage, and allows users to move data between them as per their requirements .



### Layered Cloud Architecture Design

- Cloud architecture is how individual technologies are integrated to create clouds IT environments that abstract, pool, and share scalable resources across a network.
- Cloud architecture can be divided into several layers, each with its own functionality and responsibility. The common layers are:
  - Application layer: This is the top layer where the actual cloud applications are located. Cloud applications can take advantage of the automatic-scaling functionality to gain greater performance, availability, and lower operational costs.
  - Platform layer: This layer provides the tools and services for developing and deploying cloud applications, such as databases, web servers, middleware, and programming frameworks. This layer is also known as Platform as a Service (PaaS).
  - Infrastructure layer: This layer serves as the central hub of the cloud environment, where resources are constantly added using a variety of virtualization techniques. This layer provides the basic computing, storage, and network resources for the cloud, and is also known as Infrastructure as a Service (IaaS).
  - Virtualization layer: This layer enables the abstraction and isolation of the physical resources from the higher layers, allowing multiple instances of operating systems and applications to run on the same hardware. Virtualization also enables the dynamic allocation and migration of resources according to the demand.
  - Physical layer: This is the lowest layer that consists of the actual hardware devices, such as servers, switches, routers, and storage systems. This layer provides the foundation for the cloud, and is responsible for the power, cooling, and maintenance of the devices.
- The layers are connected to each other by User Interfaces (UI), Application Programming Interfaces (API), and middleware. UI allows the users to interact with the cloud services, API allows the developers to access the cloud functionality, and middleware allows the communication and integration of different cloud components.
- A diagram of the layered cloud architecture is shown below:

Layered Cloud Architecture

: Layered Cloud Architecture | Download Scientific Diagram - ResearchGate
: Cloud Architecture Layered - theintactone
: Layered Architecture of Cloud - GeeksforGeeks



### NIST Cloud Computing Reference Architecture

- The NIST Cloud Computing Reference Architecture (NIST SP 500-292) is a document that defines a neutral and generic cloud computing architecture and taxonomy to facilitate communication and understanding of various cloud services and offerings .
- The NIST Cloud Computing Reference Architecture consists of five major components: cloud consumer, cloud provider, cloud broker, cloud auditor, and cloud carrier .
- Cloud consumer is the entity that uses cloud services from a cloud provider. Cloud consumer can be an individual, an organization, or a software system.
- Cloud provider is the entity that provides cloud services to cloud consumers. Cloud provider can offer different types of cloud service models, such as Software as a Service (SaaS), Platform as a Service (PaaS), or Infrastructure as a Service (IaaS).
- Cloud broker is an intermediary entity that manages the use, performance, and delivery of cloud services for cloud consumers. Cloud broker can provide services such as service intermediation, service aggregation, or service arbitrage.
- Cloud auditor is an independent entity that conducts audits and assessments of cloud services, such as security, privacy, performance, or compliance. Cloud auditor can provide reports or attestations to cloud consumers, cloud providers, or other stakeholders.
- Cloud carrier is the entity that transports data and information between cloud consumers and cloud providers. Cloud carrier can provide services such as network connectivity, bandwidth, or routing.
- The NIST Cloud Computing Reference Architecture also defines a set of roles and activities for each component, as well as the interactions and relationships among them. The NIST Cloud Computing Reference Architecture aims to support interoperability, portability, and security requirements for cloud computing.



### Public, Private and Hybrid Clouds

- Cloud computing is the delivery of computing services over the internet, such as servers, storage, databases, networking, software, analytics, and intelligence.
- There are three main types of cloud deployment models: public, private, and hybrid clouds. Each one has its own advantages and disadvantages, depending on the needs and preferences of the organization.
- Public cloud is cloud computing that’s delivered via the internet and shared across organizations. Anyone can subscribe to and access public cloud services, such as Amazon Web Services (AWS), Microsoft Azure, or Google Cloud Platform (GCP).
- Some of the benefits of public cloud are:
  - Lower costs, as the cloud provider manages the infrastructure and maintenance.
  - Scalability, as the cloud resources can be increased or decreased on demand.
  - Reliability, as the cloud services are distributed across multiple servers and locations.
  - Innovation, as the cloud provider offers the latest technologies and features.
- Some of the challenges of public cloud are:
  - Security, as the data and applications are exposed to the internet and shared with other users.
  - Compliance, as the cloud provider may not meet the regulatory or legal requirements of the organization.
  - Performance, as the network latency and bandwidth may affect the speed and quality of the cloud services.
  - Control, as the organization has limited visibility and customization over the cloud infrastructure and services.
- Private cloud is cloud computing that is dedicated solely to your organization. It can be hosted on-premises or by a third-party provider, but it is not accessible to the public.
- Some of the benefits of private cloud are:
  - Security, as the data and applications are isolated and protected from external threats.
  - Compliance, as the organization can ensure that the cloud meets its specific standards and regulations.
  - Performance, as the network latency and bandwidth are optimized for the organization's needs.
  - Control, as the organization has full visibility and customization over the cloud infrastructure and services.
- Some of the challenges of private cloud are:
  - Higher costs, as the organization has to invest in and maintain the cloud infrastructure and resources.
  - Limited scalability, as the cloud resources are constrained by the physical capacity and availability of the infrastructure.
  - Complexity, as the organization has to manage and integrate the cloud with its existing systems and processes.
  - Dependency, as the organization relies on a single provider or location for the cloud services.
- Hybrid cloud is any environment that uses both public and private clouds. It allows the organization to leverage the best of both worlds, depending on the workload and the situation.
- Some of the benefits of hybrid cloud are:
  - Flexibility, as the organization can choose the most suitable cloud for each application and data.
  - Cost-efficiency, as the organization can optimize the use of cloud resources and avoid unnecessary expenses.
  - Resiliency, as the organization can balance the load and backup the data across multiple clouds.
  - Innovation, as the organization can access the latest technologies and features from different cloud providers.
- Some of the challenges of hybrid cloud are:
  - Security, as the organization has to ensure that the data and applications are secure and consistent across different clouds.
  - Compliance, as the organization has to comply with the regulations and policies of different cloud providers and jurisdictions.
  - Performance, as the organization has to manage the network latency and bandwidth between different clouds.
  - Integration, as the organization has to coordinate and synchronize the cloud services and resources across different platforms and systems.



### IaaS

- IaaS stands for Infrastructure as a Service, which is a cloud service model where a cloud service provider (CSP) rents out highly scalable and automated IT infrastructure, usually over the internet, to a small and medium business (SMBs) or individual developers .
- IaaS allows users to access and manage the lowest levels of network infrastructure, such as networking, storage, servers, and virtualization, through APIs.
- IaaS is an effective cloud service model for workloads that are temporary, experimental, or that change unexpectedly, such as developing and testing new software products, hosting web applications, storing and analyzing data, and performing backup and recovery  .
- IaaS provides users with the following benefits:
  - Cost savings: Users only pay for the resources they use and do not need to invest in hardware, maintenance, or upgrades .
  - Scalability: Users can easily scale up or down their resources according to their demand and workload .
  - Flexibility: Users can choose from a variety of hardware and software options and customize their infrastructure according to their needs and preferences .
  - Control: Users have full control over their infrastructure and can configure, monitor, and manage it as they wish .
  - Security: Users can implement their own security measures and policies on their infrastructure and benefit from the CSP's security features and compliance standards .
- Some examples of IaaS providers are Amazon EC2, Rackspace, Windows Azure, Google Compute Engine, and IBM Cloud  .



### PaaS

- PaaS stands for Platform as a Service, which is a cloud computing model that provides customers a complete cloud platform for developing, running, and managing applications without the cost, complexity, and inflexibility that often comes with building and maintaining that platform on-premises  .
- PaaS solutions have three main parts:
  - Cloud infrastructure including virtual machines (VMs), operating system software, storage, networking, firewalls
  - Software for building, deploying and managing applications
  - A graphic user interface, or GUI, where development or DevOps teams can do all the tasks related to the application lifecycle
- PaaS offers several benefits for developers and businesses, such as  :
  - Faster time to market and lower development costs, as PaaS eliminates the need to buy, install, configure, and maintain hardware and software
  - Greater scalability and availability, as PaaS allows applications to automatically scale up or down according to demand and provides high availability and reliability
  - Enhanced innovation and collaboration, as PaaS enables developers to use the latest technologies and tools and to work together across different locations and devices
  - Improved security and compliance, as PaaS providers take care of the security updates and patches and adhere to the industry standards and regulations
- PaaS can be used for various types of applications, such as :
  - Web applications, such as e-commerce, social media, or content management systems
  - Mobile applications, such as games, messaging, or navigation
  - Data analytics applications, such as business intelligence, machine learning, or big data processing
  - Internet of Things (IoT) applications, such as smart home, smart city, or smart industry
- Some examples of PaaS providers are  :
  - IBM Cloud Foundry, which is an open source PaaS that supports multiple languages, frameworks, and services
  - Google App Engine, which is a PaaS that allows developers to build and run applications on Google's infrastructure
  - Microsoft Azure, which is a PaaS that offers a range of services and tools for building, deploying, and managing cloud applications



### SaaS

- SaaS stands for **Software as a Service**  .
- It is a software delivery and licensing model that allows users to access and use cloud-based applications over the Internet .
- Users do not need to install, update, or maintain the software on their own devices .
- Users pay for the software on a subscription or pay-as-you-go basis, depending on the service provider .
- SaaS provides a complete software solution that is hosted and managed by the service provider.
- SaaS offers many benefits, such as scalability, flexibility, accessibility, security, and cost-effectiveness .
- Some common examples of SaaS applications are email, calendaring, office tools, customer relationship management, enterprise resource planning, and e-commerce .



### Architectural Design Challenges

Cloud computing is the delivery of computing services such as applications, data, servers, and networks over the internet. Cloud computing architecture is the design of the components and interactions that enable cloud computing. Cloud computing architecture consists of two main parts: the front end and the back end. The front end is the interface that the users see and interact with, such as web browsers, mobile apps, or desktop applications. The back end is the collection of servers, storage, databases, and other resources that provide the computing services.

Cloud computing architecture faces several challenges, such as:

- **Scalability**: The ability to handle increasing or decreasing workloads without compromising performance, availability, or cost. Cloud computing architecture should be able to scale up or down the resources dynamically according to the demand, using techniques such as load balancing, auto-scaling, or elasticity.
- **Reliability**: The ability to ensure that the services are available and functioning correctly at all times, even in the face of failures, errors, or disruptions. Cloud computing architecture should be able to provide fault tolerance, redundancy, backup, and recovery mechanisms to ensure high availability and resilience of the services.
- **Security**: The ability to protect the data and the services from unauthorized access, modification, or disclosure. Cloud computing architecture should be able to provide encryption, authentication, authorization, access control, auditing, and monitoring features to ensure the confidentiality, integrity, and accountability of the services.
- **Performance**: The ability to deliver the services with low latency, high throughput, and high responsiveness. Cloud computing architecture should be able to optimize the network, storage, and computation resources to ensure the efficiency and quality of the services.
- **Cost**: The ability to minimize the expenses of using the cloud computing services, such as operational, maintenance, or subscription costs. Cloud computing architecture should be able to provide pay-as-you-go, metered, or subscription-based pricing models to ensure the affordability and flexibility of the services.

To address these challenges, cloud computing architecture should follow some best practices and design patterns, such as:

- **Modularity**: The practice of dividing the system into smaller, independent, and interchangeable components that can be reused, replaced, or updated easily. Modularity can improve the scalability, reliability, security, and performance of the system by reducing the complexity, coupling, and dependencies among the components.
- **Loose coupling**: The practice of minimizing the interdependence and interaction among the components of the system, such that they can operate independently and communicate only when necessary. Loose coupling can improve the scalability, reliability, security, and performance of the system by reducing the impact of changes, failures, or attacks on one component to the rest of the system.
- **Service orientation**: The practice of designing the system as a collection of self-contained, stateless, and interoperable services that can be composed, orchestrated, or consumed by other services or applications. Service orientation can improve the scalability, reliability, security, and performance of the system by enabling the reuse, integration, and distribution of the services.
- **Automation**: The practice of using software tools or scripts to perform tasks that would otherwise require human intervention, such as provisioning, configuration, deployment, monitoring, or testing. Automation can improve the scalability, reliability, security, and performance of the system by reducing the errors, delays, or inconsistencies caused by human actions.



### Cloud Storage

- Cloud storage is a mode of computer data storage in which digital data is stored on servers in off-site locations   .
- The servers are maintained by a third-party provider who is responsible for hosting, managing, and securing data stored on its infrastructure   .
- Users upload data to servers via an internet connection, where it is saved on a virtual machine on a physical server  .
- Users can access data anytime from any location and easily share it with those who are granted permission   .
- Cloud storage also offers a way to back up data to facilitate recovery off-site  .
- Cloud storage can be classified into four types: public, private, hybrid, and multi-cloud .
  - Public cloud storage: data is stored on servers owned by a cloud service provider and shared with other customers .
  - Private cloud storage: data is stored on servers dedicated to a single customer and managed by the customer or a third-party provider .
  - Hybrid cloud storage: data is stored on a combination of public and private cloud servers, depending on the security and performance requirements .
  - Multi-cloud storage: data is stored on multiple public cloud servers from different providers, to increase availability and reduce vendor lock-in .
- Cloud storage has many benefits, such as scalability, cost-effectiveness, reliability, security, and accessibility   .
  - Scalability: cloud storage can easily adjust to the changing needs of data storage, without requiring additional hardware or maintenance   .
  - Cost-effectiveness: cloud storage can reduce the capital and operational expenses of data storage, as users only pay for the amount of storage they use   .
  - Reliability: cloud storage can ensure data availability and durability, as data is replicated across multiple servers and locations   .
  - Security: cloud storage can protect data from unauthorized access, modification, or deletion, by using encryption, authentication, and access control mechanisms   .
  - Accessibility: cloud storage can enable data access from any device and any location, as long as there is an internet connection   .
- Cloud storage also has some challenges, such as latency, bandwidth, compatibility, and compliance   .
  - Latency: cloud storage can introduce delays in data transfer, as data has to travel over the internet or a network to reach the servers   .
  - Bandwidth: cloud storage can consume a large amount of network resources, as data has to be uploaded and downloaded from the servers   .
  - Compatibility: cloud storage can pose interoperability issues, as different cloud providers may use different standards and protocols for data storage and access   .
  - Compliance: cloud storage can raise legal and regulatory concerns, as data may be subject to different laws and policies depending on the location and jurisdiction of the servers   .



### Storage‐as‐a‐Service

- Storage-as-a-service (STaaS) is a cloud service offered by storage providers to organizations that would prefer to rent infrastructure for their data storage needs rather than purchase it and manage it on site .
- STaaS can be delivered on premises from infrastructure that is dedicated to a single customer, or it can be delivered from the public cloud as a shared service that's purchased by subscription and is billed based on usage.
- STaaS can provide the following benefits to customers  :
  - Cost savings: STaaS eliminates the need for capital expenditure (CAPEX) on storage hardware and software, as well as the operational costs of maintenance, upgrades, and staff. STaaS also enables customers to pay only for the storage they need, when they need it, and scale up or down as their requirements change.
  - Flexibility: STaaS allows customers to access a variety of storage options, such as block, file, object, and backup storage, and choose the performance, availability, and security levels that suit their applications. STaaS also enables customers to access their data from any location and device, and integrate with other cloud services and platforms.
  - Reliability: STaaS providers typically offer high levels of service level agreements (SLAs) and data protection, such as redundancy, backup, encryption, and disaster recovery. STaaS also reduces the risk of data loss or corruption due to hardware failures, human errors, or cyberattacks.
- STaaS can also pose some challenges to customers, such as :
  - Data security: STaaS customers need to trust their providers with their sensitive and confidential data, and ensure that they comply with the relevant regulations and standards. STaaS customers also need to protect their data from unauthorized access, theft, or leakage, especially when using public cloud services or shared infrastructure.
  - Data migration: STaaS customers need to transfer their data from their existing storage systems to the STaaS platform, which can be time-consuming, costly, and complex. STaaS customers also need to ensure that their data is compatible with the STaaS format and protocols, and that their applications can access the data without disruption or performance degradation.
  - Vendor lock-in: STaaS customers may become dependent on their providers for their storage needs, and face difficulties in switching to another provider or moving their data back to their own premises. STaaS customers may also have limited control over their data and storage resources, and have to abide by the provider's terms and conditions, pricing, and policies.



### Advantages of Cloud Storage

Cloud storage is a service that allows users to store and access data on remote servers over the internet. Cloud storage has many advantages over traditional storage methods, such as:

- **Usability and accessibility**: Cloud storage enables users to access their data from any device and location, as long as they have an internet connection. This improves the convenience and productivity of users, especially in the age of hybrid working .
- **Security**: Cloud storage providers offer various security features to protect the data from unauthorized access, such as encryption, authentication, backup, and disaster recovery. Cloud storage also reduces the risk of data loss due to hardware failure, theft, or natural disasters  .
- **Cost-efficiency**: Cloud storage eliminates the need for users to purchase, maintain, and upgrade their own storage devices and infrastructure. Users only pay for the amount of storage they use, and can scale up or down as needed. Cloud storage also saves energy and space costs  .
- **Convenient sharing of files**: Cloud storage allows users to easily share files with others, either by sending links or granting permissions. This facilitates collaboration and communication among users, and eliminates the need for physical media or email attachments .
- **Automation**: Cloud storage providers offer various tools and services to automate the data management and backup processes. Users can set up schedules, policies, and rules to ensure that their data is always up to date and secure .
- **Multiple users**: Cloud storage enables multiple users to access and edit the same data simultaneously, without creating conflicts or duplicates. This enhances the teamwork and efficiency of users, and allows for real-time updates and feedback .
- **Synchronization**: Cloud storage ensures that the data is always synchronized across different devices and platforms, so that users can access the latest version of their data at any time. This also prevents data inconsistency and corruption .
- **Convenient**: Cloud storage is easy to use and requires minimal technical skills. Users can access their data through web browsers or mobile apps, and can drag and drop files to upload or download them. Cloud storage also integrates with various applications and services, such as email, social media, and office software .



### Cloud Storage Providers

Cloud storage providers are companies that offer online storage services for data, files, media and other digital content. They typically use cloud computing technologies to store and access data across multiple servers and locations. Cloud storage providers can offer different features, such as file syncing, sharing, backup, versioning, encryption, security and more.

Some of the benefits of using cloud storage providers are:

- They can reduce the cost and complexity of managing local storage devices and servers.
- They can provide scalability and elasticity to meet changing storage needs and demands.
- They can enhance collaboration and productivity by allowing users to access and share data from anywhere and any device.
- They can improve data protection and recovery by using redundancy, backup and encryption mechanisms.

Some of the challenges of using cloud storage providers are:

- They can pose privacy and security risks if the data is not encrypted or if the provider is compromised or malicious.
- They can incur additional costs for bandwidth, storage space and service fees.
- They can depend on the availability and reliability of the internet connection and the provider's service level agreement (SLA).
- They can face compatibility and interoperability issues with different platforms, applications and devices.

Some of the popular cloud storage providers are:

- **Amazon Cloud Drive**: A cloud storage service from Amazon that offers unlimited photo storage and 5GB of free storage for other files. It integrates with Amazon Prime and Fire devices, and supports file syncing and sharing.
- **Apple iCloud**: A cloud storage service from Apple that offers 5GB of free storage and up to 2TB of paid storage. It integrates with iOS, macOS and Windows devices, and supports file syncing, sharing, backup and media streaming.
- **Box**: A cloud storage service that offers 10GB of free storage and up to 100GB of paid storage. It focuses on business and enterprise users, and supports file syncing, sharing, collaboration, security and integration with third-party apps.
- **Carbonite**: A cloud storage service that offers unlimited backup storage for personal and business users. It supports file syncing, sharing, versioning, encryption and recovery.
- **Dropbox**: A cloud storage service that offers 2GB of free storage and up to 3TB of paid storage. It supports file syncing, sharing, backup, versioning, encryption and integration with third-party apps.
- **Google Drive**: A cloud storage service from Google that offers 15GB of free storage and up to 30TB of paid storage. It integrates with Google Workspace and Android devices, and supports file syncing, sharing, collaboration, backup and media streaming.
- **Microsoft OneDrive**: A cloud storage service from Microsoft that offers 5GB of free storage and up to 6TB of paid storage. It integrates with Microsoft 365 and Windows devices, and supports file syncing, sharing, backup, versioning and media streaming.
- **Mozy**: A cloud storage service that offers 2GB of free backup storage and up to 1.5TB of paid storage. It supports file syncing, sharing, encryption and recovery.
- **SOS Online Backup**: A cloud storage service that offers unlimited backup storage for personal and business users. It supports file syncing, sharing, versioning, encryption and recovery.
- **SugarSync**: A cloud storage service that offers 250GB of paid storage. It supports file syncing, sharing, backup, versioning and encryption.
- **Western Digital My Cloud**: A cloud storage service that offers personal cloud storage devices that can be accessed remotely. It supports file syncing, sharing, backup and media streaming.



### S3

- S3 stands for Simple Storage Service, and it is a cloud object storage solution provided by Amazon Web Services (AWS) .
- Object storage is a way of storing and retrieving any amount of data as discrete units called objects, which consist of data and metadata .
- S3 is designed for durability, availability, scalability, and performance, and it is ideal for data lakes, mobile applications, backup and restore, archival, IoT devices, ML, AI, and analytics .
- S3 has a web services interface that allows users to create, read, update, and delete objects using HTTP requests .
- S3 also has a management console that provides a graphical user interface for performing common tasks such as creating buckets, uploading objects, and setting permissions .
- A bucket is a container for objects stored in S3, and it has a unique name and a region .
- A region is a geographical area where AWS operates a set of data centers, and it affects the latency, availability, and cost of S3 .
- An object key (or key name) is a unique identifier for an object within a bucket, and it is composed of a prefix and a suffix .
- A prefix is a logical grouping of objects within a bucket, similar to a folder or a directory .
- A suffix is the name of the object itself, similar to a file name .
- For example, in the object key `images/cat.jpg`, the prefix is `images/` and the suffix is `cat.jpg`.
- S3 offers different storage classes for different use cases, such as Standard, Standard-Infrequent Access (SIA), One Zone-Infrequent Access (ZIA), Intelligent-Tiering, Glacier, and Glacier Deep Archive .
- Each storage class has different characteristics in terms of availability, durability, performance, and cost .
- For example, Standard is the default storage class that provides high availability and performance, but also higher cost, while Glacier is a low-cost storage class that provides long-term archival, but also lower availability and performance .
- S3 also provides various features and services to enhance the functionality and security of object storage, such as encryption, versioning, lifecycle management, replication, access control, logging, tagging, and analytics .
- For example, encryption is a feature that protects the data at rest and in transit, while versioning is a feature that preserves multiple versions of an object in the same bucket .



## Unit 4 - Resource Management And Security In Cloud

- Resource management in cloud computing refers to the process of allocating, scheduling, monitoring, and optimizing the cloud resources to meet the service level objectives and the user demands.
- Resource management in cloud computing involves the following aspects:
  - Resource provisioning: The process of creating, configuring, and deploying the cloud resources such as virtual machines, storage, network, etc. according to the user requests and the available capacity.
  - Resource scheduling: The process of assigning the cloud resources to the user tasks or applications based on the performance, cost, availability, and quality of service requirements.
  - Resource monitoring: The process of collecting, analyzing, and reporting the resource utilization, performance, availability, and health status of the cloud resources and the user applications.
  - Resource optimization: The process of adjusting, scaling, migrating, and releasing the cloud resources to improve the efficiency, performance, cost, and quality of service of the cloud resources and the user applications.

- Security in cloud computing refers to the process of protecting the cloud resources, the user data, and the user applications from unauthorized access, modification, disclosure, or destruction.
- Security in cloud computing involves the following aspects:
  - Security policies: The rules and guidelines that define the security objectives, requirements, and responsibilities of the cloud providers and the cloud users.
  - Security mechanisms: The techniques and tools that implement the security policies and provide the security functions such as authentication, authorization, encryption, auditing, etc.
  - Security challenges: The issues and risks that arise due to the characteristics and features of cloud computing such as multi-tenancy, scalability, elasticity, heterogeneity, etc.
  - Security solutions: The methods and approaches that address the security challenges and provide the security guarantees such as confidentiality, integrity, availability, accountability, etc.



### Inter Cloud Resource Management

- Inter Cloud Resource Management is the process of managing the resources of multiple clouds that are interconnected and interdependent.
- Inter Cloud Resource Management aims to optimize the performance, cost, availability, and reliability of cloud services by dynamically allocating and releasing resources across different clouds.
- Inter Cloud Resource Management can be classified into four types:

  - Federation Clouds: A federation cloud is a kind of inter-cloud where several cloud service providers willingly link their cloud infrastructures together to exchange resources. Cloud service providers in the federation trade resources in an open manner.
  - Broker Clouds: A broker cloud is a kind of inter-cloud where a third-party entity acts as an intermediary between cloud service providers and cloud service consumers. The broker cloud provides value-added services such as resource discovery, negotiation, aggregation, integration, and arbitration.
  - Multi-Cloud Services: A multi-cloud service is a kind of inter-cloud where a cloud service provider offers a service that spans multiple clouds. The cloud service provider manages the resources of different clouds to provide a seamless and consistent service to the cloud service consumers.
  - Multi-Cloud Libraries: A multi-cloud library is a kind of inter-cloud where a cloud service consumer uses a uniform cloud API as a library to access multiple clouds. The cloud service consumer can leverage the features and benefits of different clouds without being aware of the underlying details.

- Inter Cloud Resource Management faces several challenges such as:

  - Resource heterogeneity: Different clouds may have different types, formats, and characteristics of resources, which makes it difficult to manage them uniformly and efficiently.
  - Resource interoperability: Different clouds may have different protocols, standards, and interfaces for resource management, which makes it difficult to communicate and coordinate among them.
  - Resource security: Different clouds may have different policies, regulations, and mechanisms for resource security, which makes it difficult to ensure the confidentiality, integrity, and availability of resources across different clouds.
  - Resource scalability: Different clouds may have different capacities, demands, and constraints for resource scalability, which makes it difficult to balance the trade-offs between resource utilization and resource provisioning.

- Inter Cloud Resource Management can benefit from several techniques and technologies such as:

  - Resource virtualization: Resource virtualization is the technique of abstracting the physical resources of different clouds into logical resources that can be managed and accessed in a uniform way.
  - Resource orchestration: Resource orchestration is the technique of coordinating and controlling the resources of different clouds to achieve a desired goal or outcome.
  - Resource optimization: Resource optimization is the technique of finding the best or most efficient allocation and utilization of resources across different clouds.
  - Resource monitoring: Resource monitoring is the technique of collecting and analyzing the data and information of resources across different clouds to measure and evaluate their performance and status.
  - Resource adaptation: Resource adaptation is the technique of adjusting and modifying the resources of different clouds to cope with the changes and uncertainties in the environment and requirements.



### Resource Provisioning

- Resource provisioning is the process of allocating and delivering cloud resources and services to a client according to their needs and demands .
- Resource provisioning can be done using one of three delivery models: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), or Software as a Service (SaaS).
- Resource provisioning can be done in different environments, such as cloud, edge, or hybrid.
- Resource provisioning can be done using different methods, such as static, dynamic, or adaptive.
- Resource provisioning can be done using different tools, such as orchestration, automation, or optimization .
- Resource provisioning can face different challenges, such as scalability, reliability, security, or cost .

: https://www.thecrazyprogrammer.com/2021/12/provisioning-in-cloud-computing.html
: https://www.geeksforgeeks.org/resource-allocation-methods-in-cloud-computing/
: https://www.opensourceforu.com/2020/11/resource-provisioning-in-a-cloud-edge-computing-environment/
: https://www.sciencedirect.com/topics/computer-science/resource-provisioning
: https://www.techtarget.com/searchitchannel/definition/cloud-provisioning
: https://learn.microsoft.com/en-us/azure/developer/python/cloud-development-provisioning



### Resource Provisioning Methods

Resource provisioning is the process of allocating and managing cloud resources to meet the requirements of cloud consumers. Resource provisioning methods are the techniques or strategies used to perform this process. Some of the common resource provisioning methods are:

- **Static provisioning or advance provisioning**: This method involves reserving a fixed amount of resources for a specific period of time, based on the expected or known demand or workload. This method can be suitable for applications that have constant or predictable resource needs, such as batch processing or data analysis. Static provisioning can reduce the risk of resource shortages or performance degradation, but it can also lead to resource wastage or underutilization if the demand or workload changes or fluctuates.
- **Dynamic provisioning or on-demand provisioning**: This method involves adding or removing resources as needed, based on the actual or current demand or workload. This method can be suitable for applications that have variable or unpredictable resource needs, such as web services or online gaming. Dynamic provisioning can improve the resource utilization and efficiency, but it can also increase the complexity and cost of resource management and monitoring.
- **Adaptive provisioning or self-adaptive provisioning**: This method involves adjusting the resource allocation automatically, based on the feedback or metrics from the system or the application. This method can be suitable for applications that have dynamic or adaptive resource needs, such as machine learning or artificial intelligence. Adaptive provisioning can enhance the resource optimization and performance, but it can also require advanced algorithms and techniques to implement and evaluate.
- **Policy-based provisioning or rule-based provisioning**: This method involves defining and enforcing a set of rules or policies that govern the resource allocation and management. These rules or policies can be based on various factors, such as service level agreements, quality of service, security, cost, or user preferences. This method can be suitable for applications that have complex or diverse resource needs, such as multi-tenant or multi-cloud environments. Policy-based provisioning can facilitate the resource control and compliance, but it can also demand high-level coordination and communication among different stakeholders.



### Global Exchange of Cloud Resources

- Global exchange of cloud resources refers to the process of sharing and accessing cloud services across different geographical regions and providers.
- It enables cloud customers to benefit from the availability, scalability, and cost-efficiency of cloud computing, as well as the diversity and redundancy of cloud resources.
- It also allows cloud providers to optimize their resource utilization, expand their market reach, and offer more value-added services to their customers.
- Some of the challenges and opportunities of global exchange of cloud resources are:

  - Data sovereignty and compliance: Cloud customers and providers need to comply with the laws and regulations of the countries where their data is stored and processed, which may vary widely and change frequently. This may limit the choice of cloud providers and locations, and increase the complexity and cost of cloud operations. On the other hand, global exchange of cloud resources may also create new opportunities for cloud providers to offer compliance solutions and services, such as data encryption, anonymization, and localization.
  - Network performance and latency: Global exchange of cloud resources may introduce network delays and congestion, which may affect the quality and reliability of cloud services, especially for latency-sensitive applications, such as real-time communication, gaming, and streaming. To overcome this challenge, cloud providers and customers may use techniques such as edge computing, content delivery networks, and network optimization to reduce network latency and improve performance.
  - Security and privacy: Global exchange of cloud resources may expose cloud data and services to more risks and threats, such as cyberattacks, data breaches, and unauthorized access. To ensure security and privacy, cloud providers and customers need to adopt appropriate measures, such as encryption, authentication, authorization, auditing, and monitoring, to protect their cloud resources and data. They also need to establish trust and cooperation among different cloud providers and stakeholders, and follow the best practices and standards of cloud security and privacy.
  - Interoperability and portability: Global exchange of cloud resources requires interoperability and portability among different cloud platforms and services, which may have different architectures, interfaces, protocols, and formats. This may pose technical and operational challenges for cloud providers and customers, such as compatibility, integration, migration, and management issues. To address this challenge, cloud providers and customers may use common standards, frameworks, and tools to enable interoperability and portability of cloud resources and data, such as the Open Cloud Computing Interface (OCCI), the Cloud Data Management Interface (CDMI), and the Cloud Migration Framework (CMF).
  - Resource management and optimization: Global exchange of cloud resources involves the coordination and allocation of cloud resources among different cloud providers and locations, which may have different capacities, demands, and prices. This may create resource management and optimization challenges for cloud providers and customers, such as resource discovery, selection, scheduling, and pricing issues. To solve this challenge, cloud providers and customers may use intelligent and automated techniques, such as cloud brokering, cloud federation, and cloud orchestration, to manage and optimize their cloud resources and services.



### Security Overview

- Cloud security is a collection of procedures and technology designed to address external and internal threats to business security.
- Cloud security encompasses three core capabilities: confidentiality, integrity, and availability.
  - Confidentiality is the ability to keep information secret from people who should not have access.
  - Integrity means that systems operate as they are intended to function and produce outputs that are not unexpected or misleading.
  - Availability means that systems are accessible and reliable when needed by authorized users.
- Cloud security involves securing the cloud infrastructure, the cloud services, and the cloud data.
  - Cloud infrastructure security refers to the protection of the physical and virtual components that make up the cloud, such as servers, storage, networks, hypervisors, etc.
  - Cloud service security refers to the protection of the applications and platforms that run on the cloud, such as software as a service (SaaS), platform as a service (PaaS), etc.
  - Cloud data security refers to the protection of the data that is stored, processed, or transmitted on the cloud, such as encryption, backup, access control, etc.
- Cloud security requires a shared responsibility model between the cloud provider and the cloud customer.
  - The cloud provider is responsible for securing the cloud infrastructure and the cloud services that they offer.
  - The cloud customer is responsible for securing the cloud data and the cloud applications that they use or develop.
  - The cloud customer should also verify the security policies and practices of the cloud provider and ensure compliance with relevant regulations and standards.



### Cloud Security Challenges

Cloud security challenges are the potential risks and threats that arise from using cloud computing services and platforms. Cloud security challenges can affect the confidentiality, integrity, and availability of the data and resources stored and processed in the cloud. Some of the common cloud security challenges are:

- **Less visibility and lack of control**: When using cloud-based technologies, the user can make the required servers function without having to manage it directly. However, this also means that the user has less visibility and control over the cloud infrastructure and operations, which can increase the risk of unauthorized access, misconfiguration, and data leakage.
- **Non-compliance with regulatory requirements**: Cloud computing involves the transfer and storage of data across different locations and jurisdictions, which can pose challenges for complying with various legal and regulatory standards. For example, some data protection laws may require the user to obtain consent from the data subjects before transferring their personal data to a third-party cloud provider or to a different country.
- **Concerns of data breach and data privacy**: One of the most important challenges of cloud security is the risk of data breaches and issues of data privacy. Before the entry of advanced technologies such as the Cloud, the IT team of every organization had control and hold over the network structure and systems. However, with cloud computing, the data is stored and processed by a third-party provider, which may not have the same level of security and encryption as the user's own network. Moreover, the data may be accessed by malicious actors who exploit the vulnerabilities in the cloud platform or the user's credentials .
- **Alerts in situations of data breaches**: Another challenge of cloud security is the timely detection and response to data breaches and incidents. Cloud computing involves a complex and dynamic environment, where the user may not have direct access to the logs and alerts generated by the cloud provider. Moreover, the user may not have the expertise or the resources to analyze and act on the alerts, which can result in delayed or ineffective remediation.
- **Access control to users**: Cloud computing enables the user to access the data and resources from anywhere and any device, which can enhance the productivity and flexibility of the user. However, this also means that the user has to ensure that only authorized and authenticated users can access the cloud services and data, and that the access rights are granted and revoked according to the principle of least privilege. Moreover, the user has to monitor and audit the user activities and behaviors, and prevent any unauthorized or malicious actions .
- **Migration to vendors**: Cloud computing involves the migration of data and applications from the user's own network to the cloud provider's platform, which can pose several challenges for the security and performance of the cloud services. For example, the user has to ensure that the data and applications are compatible and interoperable with the cloud platform, and that the migration process does not cause any data loss, corruption, or downtime. Moreover, the user has to verify that the cloud provider has the adequate security and service level agreements, and that the user can switch or exit the cloud provider without any lock-in or penalty .
- **Lack of experienced workforce**: Cloud computing requires a different set of skills and knowledge than traditional IT systems, which can create a gap in the user's workforce and capabilities. The user has to train and educate the existing staff on the cloud technologies and best practices, and hire or outsource the cloud experts and professionals who can manage and secure the cloud services and data. Moreover, the user has to ensure that the cloud workforce is updated and aware of the latest trends and developments in the cloud domain, and that they can cope with the dynamic and evolving nature of the cloud environment .
- **Vulnerable entry points**: Cloud computing exposes the user to various entry points and interfaces that can be exploited by the attackers to gain access to the cloud services and data. For example, the user may use web browsers, mobile applications, APIs, or third-party tools to interact with the cloud platform, which can introduce vulnerabilities and weaknesses in the cloud security. Moreover, the user may share the cloud services and data with other users or entities, which can increase the risk of data leakage or compromise .
- **Shared responsibility model**: Cloud computing involves a shared responsibility model, where the user and the cloud provider have to work together to ensure the security and compliance of the cloud services and data. However, this model can also create confusion and ambiguity about the roles and responsibilities of each party, and the division



### Software‐as‐a‐Service Security

- Software-as-a-service (SaaS) is a licensing model in which access to software is provided on a subscription basis, where the software is located on external servers rather than on servers located in-house.
- SaaS security refers to the practices and policies implemented by the providers of SaaS to ensure the privacy and security of customer data in cloud-based applications and other information assets.
- SaaS security involves the following aspects:
  - Secure development life cycle: SaaS providers should follow a systematic process to design, develop, test, and deploy secure software, and to monitor and update it regularly.
  - Secure hosting stack: SaaS providers should use a secure platform for hosting their application in production, including the infrastructure, network, operating system, database, and application layers.
  - Security-related customer inquiries: SaaS providers should adopt a multilevel model for addressing security-related customer inquiries, such as providing self-service resources, dedicated security contacts, and third-party audits.
  - Security integrations: SaaS providers should facilitate integrations with customers' existing security tools and systems, such as identity and access management, data loss prevention, encryption, and logging.
  - Data privacy: SaaS providers should help customers address data privacy issues, such as complying with relevant regulations, obtaining consent, and managing data retention and deletion.
- SaaS security challenges include the following:
  - Shared responsibility: SaaS security is a shared responsibility between the provider and the customer, and both parties should clearly define their roles and obligations.
  - Data breaches: SaaS security can be compromised by data breaches, which can result from malicious attacks, human errors, or system failures.
  - Data sovereignty: SaaS security can be affected by data sovereignty, which refers to the legal jurisdiction of the data based on its location.
  - Security as a service: SaaS security can be enhanced by security as a service (SECaaS), which is a cloud delivered model for outsourcing cybersecurity services.



### Security Governance for the notes of the Unit 4 - Resource Management And Security In Cloud in the subject of Cloud Computing

- Security governance in cloud computing is a framework of policies designed to dictate what cloud resources can be used, how they should be used, and who can use them.
- Security governance also enforces rules governing how individual resources should be secured to prevent their misuse by malicious actors.
- Security governance bridges the business priorities with technical implementation like architecture, standards, and policy.
- Security governance teams provide oversight and monitoring to sustain and improve security posture over time.
- Security governance teams also report compliance as required by regulating bodies.
- Security governance in the cloud environment supports the business objectives by defining policies and controls to manage risk.
- Security governance in the cloud also enables faster and more agile delivery of features and services by empowering the people closest to the business.
- Security governance in the cloud requires the following five disciplines:
  - Cost Management: Develop policies for cost control for all cloud platforms.
  - Security Baseline: Establish security requirements and apply them across network, data, and asset configurations.
  - Resource Consistency: Define and enforce standards for resource naming, tagging, and provisioning.
  - Identity Baseline: Define and enforce policies for identity and access management, including roles, permissions, and authentication methods.
  - Deployment Acceleration: Define and enforce policies for continuous integration and continuous delivery, including testing, validation, and approval processes.



### Virtual Machine Security for the notes of the Unit 4 - Resource Management And Security In Cloud in the subject of Cloud Computing

- Virtual machine (VM) security is the protection of the data and applications hosted on virtualized servers or cloud platforms from unauthorized access, attacks, or breaches.
- VM security is a subdomain of cloud security, which covers the broader aspects of securing cloud computing systems, services, data, and infrastructure.
- VM security is important because VMs are often exposed to the same threats as physical servers, such as malware, denial-of-service attacks, data theft, or unauthorized access. However, VMs also face some unique challenges, such as:
  - VM sprawl: the proliferation of VMs that are created, used, and forgotten, leading to unmanaged and unpatched VMs that pose security risks.
  - VM isolation: the separation of VMs from each other and from the underlying host, which can be compromised by malicious VMs or hypervisor attacks.
  - VM mobility: the ability to migrate or clone VMs across different hosts or cloud providers, which can create inconsistent security policies or configurations.
- To ensure VM security in cloud computing, some best practices include:
  - Isolating VMs from each other and from the host, using techniques such as network segmentation, firewall rules, encryption, or virtual private networks (VPNs).
  - Applying security patches and updates to VMs and the host regularly, and using antimalware software to protect VMs from viruses and malware.
  - Implementing security policies and controls for VM creation, access, and management, and enforcing them through tools such as identity and access management (IAM), role-based access control (RBAC), or security groups.
  - Monitoring and auditing VM activity and performance, and detecting and responding to any anomalies or threats, using tools such as security information and event management (SIEM), intrusion detection and prevention systems (IDS/IPS), or log analysis.
  - Complying with the security standards and regulations that apply to the cloud environment and the data hosted on VMs, such as the Payment Card Industry Data Security Standard (PCI DSS), the Health Insurance Portability and Accountability Act (HIPAA), or the General Data Protection Regulation (GDPR).



### IAM

Identity and access management (IAM) is a process of defining and managing the roles and access privileges of individual network entities (users and devices) to a variety of cloud and on-premises applications. IAM ensures that only authorized entities can access the right resources at the right times and for the right reasons.

Some of the benefits of IAM are:

- Enhanced security: IAM reduces the risk of unauthorized access, data breaches, and identity theft by enforcing strong authentication and authorization policies.
- Improved user experience: IAM simplifies the user login process by providing single sign-on (SSO) and federated identity capabilities, which allow users to access multiple applications with one set of credentials.
- Increased efficiency: IAM automates the identity lifecycle management, such as provisioning, deprovisioning, and updating user accounts, which reduces the administrative overhead and human errors.
- Compliance: IAM helps organizations comply with various regulations and standards, such as GDPR, HIPAA, PCI DSS, and ISO 27001, by providing audit trails, reports, and alerts on user activities and access events.

Some of the challenges of IAM are:

- Complexity: IAM involves multiple components, such as identity providers, service providers, directories, protocols, and policies, which need to be integrated and coordinated across different systems and platforms.
- Scalability: IAM needs to support a large and dynamic number of users and devices, as well as a variety of applications and services, which may have different requirements and standards for identity and access management.
- Cost: IAM requires significant investment in hardware, software, and personnel, as well as ongoing maintenance and updates, which may affect the return on investment and the total cost of ownership.

Some of the common IAM concepts and terms are:

- Identity: An identity is a unique representation of an entity, such as a user or a device, in a system or a network. An identity can have multiple attributes, such as name, email, role, and group membership, which can be used to identify and authenticate the entity.
- Authentication: Authentication is a process of verifying the identity of an entity, usually by asking for some credentials, such as a username and a password, a token, or a biometric factor.
- Authorization: Authorization is a process of granting or denying access to a resource, such as an application or a file, based on the identity and the permissions of an entity.
- Role: A role is a collection of permissions that can be assigned to an identity or a group of identities, which defines what actions they can perform on a resource.
- Policy: A policy is a set of rules that governs how identities and roles are managed and how access is granted or denied to resources.
- Single sign-on (SSO): SSO is a feature that allows users to access multiple applications or services with one login session, without having to enter their credentials multiple times.
- Federated identity: Federated identity is a feature that allows users to use their existing identity from one system or domain to access another system or domain, without having to create a new identity or account.
- Multi-factor authentication (MFA): MFA is a feature that requires users to provide more than one factor of authentication, such as something they know (e.g., password), something they have (e.g., token), or something they are (e.g., fingerprint), to enhance the security of their login process.



### Security Standards for Cloud Computing

Security standards are sets of guidelines and best practices that help organizations ensure the security of their cloud-based data and systems. Security standards can address various aspects of cloud security, such as:

- **Security controls**: These are the technical and organizational measures that cloud service providers (CSPs) and cloud service customers (CSCs) implement to protect the confidentiality, integrity, and availability of cloud data and resources. Security controls can include encryption, authentication, authorization, logging, monitoring, auditing, backup, recovery, etc.
- **Security compliance**: This is the process of verifying that the cloud services and operations meet the relevant legal and regulatory requirements, as well as the contractual obligations and industry standards. Security compliance can involve audits, assessments, certifications, attestations, etc.
- **Security governance**: This is the framework that defines the roles, responsibilities, policies, procedures, and processes for managing and overseeing cloud security. Security governance can include risk management, incident response, change management, security awareness, etc.

Some of the security standards that are applicable to cloud computing are:

- **ISO/IEC 27017**: This is an international standard that provides guidance and recommendations for security controls specific to cloud services. It is based on the ISO/IEC 27002 standard, which is a general code of practice for information security management. ISO/IEC 27017 covers topics such as roles and responsibilities, asset management, access control, cryptography, operations security, communications security, etc.
- **NIST SP 800-53**: This is a US federal standard that defines a catalog of security and privacy controls for federal information systems and organizations. It is based on the NIST Framework for Improving Critical Infrastructure Cybersecurity, which is a voluntary framework for managing cybersecurity risks. NIST SP 800-53 covers topics such as identification and authentication, contingency planning, system and information integrity, system and communications protection, etc.
- **CSA CCM**: This is a cloud security standard developed by the Cloud Security Alliance (CSA), which is a non-profit organization that promotes best practices and education for cloud security. The CSA Cloud Controls Matrix (CCM) is a comprehensive set of security controls that are aligned with various industry standards, such as ISO/IEC 27001, PCI DSS, COBIT, HIPAA, etc. The CSA CCM covers topics such as data governance, human resources security, business continuity management, encryption and key management, etc.
- **CIS Benchmarks**: This is a cloud security standard developed by the Center for Internet Security (CIS), which is a non-profit organization that provides cybersecurity resources and tools. The CIS Benchmarks are a set of configuration guidelines and best practices for securing various cloud platforms and services, such as AWS, Azure, Google Cloud, etc. The CIS Benchmarks cover topics such as identity and access management, network security, logging and monitoring, storage security, etc.
- **SOC 2**: This is a cloud security standard developed by the American Institute of Certified Public Accountants (AICPA), which is a professional organization that sets standards and rules for the accounting profession. The Service Organization Control (SOC) 2 report is an attestation report that evaluates the security, availability, processing integrity, confidentiality, and privacy of a cloud service provider's system and operations. The SOC 2 report covers topics such as security policies, procedures, and practices, security monitoring and testing, security incident management, security training and awareness, etc.



## Unit 5 - Cloud Technologies And Advancements Hadoop

- Hadoop is an open source framework that allows for the distributed storage and processing of large datasets across clusters of computers using simple programming models  .
- Hadoop is credited with being the foundation for the modern cloud data lake, as it democratized computing power and made it possible for companies to analyze and query big data sets in a scalable manner using free, open source software and inexpensive, off-the-shelf hardware.
- Hadoop is designed to scale up from a single computer to thousands of clustered computers, with each machine offering local computation and storage . In this way, Hadoop can efficiently store and process petabytes of data without relying on expensive or proprietary hardware or software.
- Hadoop consists of four main modules: Hadoop Distributed File System (HDFS), MapReduce, YARN, and Hadoop Common.
  - HDFS is a distributed file system that runs on standard or low-end hardware. HDFS provides better data throughput than traditional file systems, in addition to high fault tolerance and native support of large datasets.
  - MapReduce is a programming model and a software framework for writing applications that process large amounts of data in parallel on clusters of nodes. MapReduce divides the input data into smaller chunks, assigns them to mapper tasks that transform them into intermediate key-value pairs, and then assigns them to reducer tasks that aggregate the values for each key and produce the final output.
  - YARN is a resource management layer that allocates and schedules resources (such as CPU, memory, disk, and network) for applications running on Hadoop clusters. YARN also provides a platform for developing and running distributed applications that are not based on MapReduce, such as Spark, Hive, HBase, and Kafka.
  - Hadoop Common is a set of common utilities and libraries that support the other Hadoop modules. It includes configuration, logging, security, and serialization components.
- Hadoop can run on public, private, or hybrid cloud resources versus on-premises hardware to gain flexibility, availability, and cost control. Many cloud solution providers offer fully managed services for Hadoop, such as Dataproc from Google Cloud, EMR from Amazon Web Services, and HDInsight from Microsoft Azure . These services allow users to create and configure Hadoop clusters on demand, and to access a variety of tools and applications that integrate with Hadoop, such as Spark, Hive, HBase, Kafka, and many others.



### MapReduce

- MapReduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
- MapReduce consists of two phases: map and reduce.
- The map phase takes an input pair and produces a set of intermediate key/value pairs. The map function is applied in parallel to every input pair on the cluster.
- The reduce phase takes all the intermediate values associated with the same intermediate key and combines them to form a smaller set of values. The reduce function is applied in parallel to each distinct key on the cluster.
- MapReduce allows for the specification of a partition function that determines how the intermediate keys are distributed among the reducers.
- MapReduce also allows for the specification of a combiner function that can perform local aggregation of the intermediate results to reduce the amount of data sent between the mappers and the reducers.
- MapReduce is fault-tolerant, as it can handle failures of individual nodes in the cluster by re-executing the failed tasks on other nodes.
- MapReduce is scalable, as it can process large amounts of data on thousands of nodes in a cluster.
- MapReduce is widely used for various applications such as web indexing, data mining, machine learning, natural language processing, image processing, etc.



### Virtual Box for Hadoop

- Virtual Box is a software that allows you to create and run virtual machines on your computer.
- Hadoop is a framework that enables distributed storage and processing of large-scale data using clusters of computers.
- You can use Virtual Box to install and configure Hadoop on one or more virtual machines for learning and experimentation purposes.
- Some of the advantages of using Virtual Box for Hadoop are:
  - You can create multiple virtual machines with different configurations and operating systems to simulate a Hadoop cluster.
  - You can isolate your Hadoop environment from your host system and avoid any conflicts or dependencies.
  - You can easily start, stop, pause, resume, clone, or delete your virtual machines as needed.
  - You can use pre-built images or distributions of Hadoop, such as Cloudera or Hortonworks, to simplify the installation and setup process.
- Some of the steps to install and run Hadoop on Virtual Box are:
  - Download and install Virtual Box on your host system (Windows, Linux, or Mac OS).
  - Download a Linux virtual machine image, such as Ubuntu, and import it into Virtual Box.
  - Configure the network settings of your virtual machine to enable communication between the host and the guest systems, and among the guest systems if you have more than one.
  - Install Java and Hadoop on your virtual machine, either manually or using a pre-built distribution.
  - Configure the Hadoop files, such as core-site.xml, hdfs-site.xml, mapred-site.xml, and yarn-site.xml, to specify the parameters and properties of your Hadoop cluster.
  - Start the Hadoop services, such as NameNode, DataNode, ResourceManager, and NodeManager, on your virtual machine(s).
  - Verify the status and functionality of your Hadoop cluster using the web interface or the command line tools.
  - Run some Hadoop commands or applications to test your cluster and perform some data operations.



### Google App Engine

- Google App Engine (GAE) is a platform-as-a-service (PaaS) product that provides web app developers and enterprises with access to Google's scalable hosting and tier 1 internet service.
- GAE requires that applications be written in Java or Python, store data in Google Bigtable and use the Google query language.
- GAE is a fully managed cloud computing platform that uses in-built services to run your apps .
- GAE supports popular development languages such as Node.js, Go, PHP, Ruby, and .NET.
- GAE offers two environments: standard and flexible.
  - The standard environment runs your app in a sandboxed environment with preconfigured runtime environments and automatic scaling.
  - The flexible environment runs your app in a Docker container on Google Compute Engine virtual machines with custom runtime environments and manual or automatic scaling.
- GAE provides various features and benefits such as:
  - No server management: GAE handles the infrastructure, security, and maintenance for you.
  - High availability: GAE leverages Google's global network of data centers and load balancers to ensure your app is always available and responsive.
  - Integrated services: GAE offers a range of services such as Cloud Firestore, Cloud Storage, Cloud SQL, Cloud Pub/Sub, Cloud Functions, Cloud Vision API, and more to enhance your app's functionality and performance .
  - Developer tools: GAE provides tools such as Cloud SDK, Cloud Shell, Cloud Build, Cloud Debugger, Cloud Trace, Cloud Logging, and Cloud Monitoring to help you develop, test, deploy, and debug your app .
  - Pricing: GAE offers a free tier and a pay-as-you-go model based on the resources you use. You can also set a daily spending limit to control your costs.
- To get started with GAE, you need to create a Google Cloud project, install the Cloud SDK, and deploy your app using the gcloud command-line tool or the Cloud Console.



### Programming Environment for Google App Engine

- Google App Engine is a cloud computing platform that allows developers to build and run web applications on Google's infrastructure.
- Google App Engine provides four possible runtime environments for applications, one for each of four programming languages: Java, Python, PHP, and Go.
- The environment you choose depends on the language and related technologies you want to use for developing the application.
- Google App Engine also offers two types of environments: standard and flexible.
- The standard environment is based on container instances running on Google's infrastructure. Containers are preconfigured with one of several available runtimes. The standard environment makes it easy to build and deploy an application that runs reliably even under heavy load and with large amounts of data.
- The flexible environment is based on Google Compute Engine VM instances that can be customized with any runtime, framework, or library. The flexible environment gives you more control over the configuration and scaling of your application.
- To create an application for an app engine, you can use the SDKs and tools provided by Google for each language and environment. You can develop and test an app locally using the SDK's deployment toolkit. Each language's SDK and runtime are unique .
- You can also use other Google Cloud services and APIs to enhance your app's functionality, such as Cloud Storage, Cloud Datastore, Cloud SQL, Cloud Pub/Sub, Cloud Vision, and Cloud Natural Language.



### Open Stack

- Open Stack is a free, open source cloud computing platform that provides infrastructure-as-a-service (IaaS) for both public and private clouds.
- Open Stack consists of interrelated components that control diverse, multi-vendor hardware pools of processing, storage, and networking resources throughout a data center.
- Open Stack can be managed either through a web-based dashboard, through command-line tools, or through RESTful web services.
- Open Stack is developed by the community and is trusted to manage millions of cores around the world, across dozens of industries.
- Open Stack aims to provide a common platform for cloud infrastructure, with interoperability, scalability, and flexibility as key features.



### Federation in the Cloud

- Federation means associating small divisions to a single group for performing a common task.
- Federated cloud is a seamless environment formed by connecting the cloud environment of two or more cloud service providers using a common standard .
- Federated cloud integrates heterogeneous cloud environments such as community cloud, public cloud, and private cloud in order to scale up the resources and services for the users.
- Federation with Azure AD or O365 enables users to authenticate using on-premises credentials and access all resources in cloud .
- Federation also helps to improve availability, reliability, and security of cloud services.




### Four Levels of Federation for the notes of the Unit 5 - Cloud Technologies And Advancements Hadoop in the subject of Cloud Computing

- Federation in the cloud is the concept of integrating different cloud services and applications across multiple cloud providers and platforms.
- Federation can enhance the scalability, availability, interoperability, and security of cloud computing.
- Federation can be achieved at four levels: infrastructure, platform, application, and data.
- Infrastructure level federation involves sharing and pooling of physical and virtual resources, such as compute, storage, and network, among different cloud providers.
- Platform level federation involves sharing and integrating of cloud platforms, such as Hadoop, Google App Engine, and OpenStack, among different cloud providers.
- Application level federation involves sharing and composing of cloud applications, such as web services, workflows, and mashups, among different cloud providers.
- Data level federation involves sharing and synchronizing of data, such as files, databases, and streams, among different cloud providers.
- Hadoop is an open source platform for distributed processing of large-scale data using a cluster of commodity hardware.
- Hadoop consists of two main components: Hadoop Distributed File System (HDFS) and MapReduce.
- HDFS is a distributed file system that stores data in blocks across multiple data nodes in the cluster.
- MapReduce is a programming model that allows parallel processing of data using two functions: map and reduce.
- HDFS federation is a feature of Hadoop that allows multiple independent name nodes to coexist in the same cluster, each managing a separate namespace and a subset of data nodes.
- HDFS federation improves the scalability, availability, and performance of HDFS by allowing horizontal scaling of name nodes, reducing the load on a single name node, and increasing the throughput of data access.
- HDFS federation can be configured using the following steps:
  - Define the name nodes and their namespaces in the configuration file `hdfs-site.xml`.
  - Define the data nodes and their name node mappings in the configuration file `dfs.datanode.data.dir`.
  - Start the name nodes and the data nodes using the scripts `hdfs namenode` and `hdfs datanode`.
  - Use the command `hdfs dfsadmin -report` to check the status of the name nodes and the data nodes.



### Federated Services and Applications for Hadoop

- Hadoop is an open source distributed processing framework that manages data processing and storage for big data applications.
- Hadoop Distributed File System (HDFS) is a key component of Hadoop that provides a reliable and scalable way of storing and accessing large volumes of data across multiple nodes.
- HDFS Federation is a feature introduced in Hadoop 2.x that allows multiple independent NameNodes/namespaces to coexist in the same cluster  .
- A NameNode is the master node that manages the metadata and namespace of a HDFS cluster.
- A namespace is a logical grouping of files and directories that share a common root directory.
- HDFS Federation improves the scalability, performance, and isolation of HDFS by allowing multiple NameNodes to serve different namespaces without any coordination or synchronization  .
- HDFS Federation also enables the use of different storage types and policies for different namespaces, such as SSD, HDD, or archival storage.
- The DataNodes are the worker nodes that store the actual data blocks and serve read/write requests from the clients.
- The DataNodes are shared by all the NameNodes and can belong to multiple namespaces at the same time  .
- The DataNodes report the block locations and other information to all the NameNodes that they belong to  .
- The clients can access any namespace by contacting the corresponding NameNode and obtaining the block locations from it  .
- The clients can also use a federated URI scheme to specify the namespace and the path of the file or directory they want to access .
- HDFS Federation configuration is backward compatible and allows existing single NameNode configurations to work without any change.
- HDFS Federation configuration is also designed such that all the nodes in the cluster have the same configuration without the need for deploying different configurations based on the type of the node in the cluster.
- HDFS Federation is an example of balancing centralized and federated IT in a DevOps transformation, where the trade-off between operational speed and simplicity, and developer flexibility and choice, is optimized.



### Future of Federation for the notes of the Unit 5 - Cloud Technologies And Advancements Hadoop in the subject of Cloud Computing

- Federation is a feature of Hadoop 2.x that allows multiple NameNodes to manage different namespaces in a single cluster. This improves the scalability, performance, and isolation of HDFS.
- Federation separates the namespace and the storage layers of HDFS. Each NameNode manages a namespace volume, which consists of a namespace, a block pool, and a set of DataNodes. The DataNodes can belong to multiple block pools and serve read and write requests from multiple NameNodes.
- Federation does not require any changes to the existing single NameNode configuration. It is backward compatible and supports the same HDFS commands and APIs. Federation also does not affect the replication and fault tolerance mechanisms of HDFS.
- Federation enables future innovations in HDFS, such as supporting multiple file systems, dynamic block placement policies, and heterogeneous storage types. Federation also facilitates the integration of HDFS with other cloud-based technologies, such as Apache Spark, Apache Hive, and Apache HBase.
- Federation is an ongoing project in the Apache Hadoop community. The current challenges and future directions of federation include improving the load balancing, high availability, and security of multiple NameNodes, as well as enhancing the federation management and monitoring tools.

