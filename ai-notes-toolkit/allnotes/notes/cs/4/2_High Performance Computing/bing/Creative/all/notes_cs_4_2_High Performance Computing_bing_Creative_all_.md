

## Unit 1 - Overview of Grid Computing Technology

- Grid computing is a form of distributed computing that involves coordinating and sharing computing resources across a network of computers.
- Grid computing enables the creation of a virtual supercomputer that can perform large-scale tasks, such as data analysis, scientific simulation, or weather modeling, by harnessing the power of multiple computers.
- Grid computing differs from other types of distributed computing, such as cluster computing or cloud computing, in that it does not require a centralized control or a homogeneous environment.
- Grid computing can be seen as a way of utilizing the idle or underutilized resources of computers that are connected by a network, such as the Internet or an intranet.
- Grid computing can be classified into different types, such as computational grids, data grids, service grids, or desktop grids, depending on the nature and purpose of the resources that are shared.
- Grid computing can offer various benefits, such as scalability, reliability, cost-effectiveness, and flexibility, by allowing users to access and share resources on demand, regardless of their physical location or configuration.
- Grid computing can also pose various challenges, such as security, interoperability, standardization, scheduling, or fault tolerance, that require effective solutions and protocols to ensure the efficient and reliable operation of the grid.



# History of Grid Computing

- Grid computing is a form of distributed computing that allows multiple computers to share resources and work together on a common task.
- The term grid computing originated in the early 1990s as a metaphor for making computer power as easy to access as an electric power grid .
- The idea was inspired by the success of parallel computing and supercomputers in the 1980s and 1990s, which used multiple processors to speed up computation and solve complex problems.
- However, parallel computing and supercomputers were expensive, centralized, and limited in scalability and availability.
- Grid computing aimed to overcome these limitations by using networks of heterogeneous, geographically distributed, and dynamically available computers to form a virtual supercomputer .
- The pioneers of grid computing were Steve Tuecke, Ian Foster, and Carl Kesselman, who developed the concept and the Globus Toolkit, a set of software tools for building and managing grids, in the mid-1990s .
- The Globus Toolkit became the de facto standard for grid computing and enabled many applications and projects in various domains, such as science, engineering, business, and education.
- Some examples of grid computing projects are the SETI@home project, which uses volunteers' computers to search for extraterrestrial intelligence, the LHC Computing Grid, which processes and analyzes data from the Large Hadron Collider, and the World Community Grid, which supports humanitarian research on health, energy, and environment .
- Grid computing has evolved over the years and has influenced other forms of distributed computing, such as cloud computing, edge computing, and fog computing, which offer different levels of abstraction, service models, and resource management .
- Grid computing is still an active research area and has many challenges and opportunities, such as security, interoperability, scalability, reliability, and performance .



# High Performance Computing for the notes of the Unit 1 - Overview of Grid Computing Technology

- Grid computing is the use of widely distributed computer resources to reach a common goal .
- A computing grid can be thought of as a distributed system with non-interactive workloads that involve many files.
- Grid computing is distinguished from conventional high-performance computing systems such as cluster computing in that grid computers have each node set to perform a different task/application .
- Grid computers also tend to be more heterogeneous and geographically dispersed (thus not physically coupled) than cluster computers .
- Grid computing can enable high performance computing for scientific and engineering applications that require large-scale computation and data processing .
- Grid computing can also support collaborative and cooperative work among distributed teams of researchers and professionals .
- Grid computing can leverage the cloud computing model to provide on-demand access to grid resources and services, and to scale up or down according to the workload and demand.
- Grid computing faces several challenges and opportunities, such as:
  - Developing standards and protocols for interoperability and security among heterogeneous and distributed grid resources .
  - Managing the complexity and dynamism of the grid environment, such as resource availability, reliability, performance, and fault tolerance  .
  - Optimizing the resource allocation, scheduling, and load balancing for efficient and effective grid computing  .
  - Enhancing the usability and accessibility of the grid computing for various users and applications .
  - Addressing the ethical, legal, and social issues related to the grid computing, such as data privacy, ownership, and sharing .



# Cluster Computing

- Cluster computing is a form of parallel computing that involves connecting multiple computers (called nodes) on a network and using them as a single system for high-performance applications   .
- Cluster computing provides benefits such as faster computational speed, enhanced data integrity, increased availability, load balancing and scalability .
- Cluster computing can be classified into different types based on the degree of coupling, the architecture, the communication pattern and the application domain  .
- Some common types of clusters are:
  - Beowulf cluster: A cluster of commodity hardware running Linux or other free software, designed for high-performance scientific computing .
  - Load-balancing cluster: A cluster that distributes the workload among the nodes to optimize the use of resources and improve the response time .
  - High-availability cluster: A cluster that provides redundancy and fault tolerance to ensure the continuity of service in case of node failures .
  - Grid cluster: A cluster that connects geographically distributed nodes over the internet or other networks, and allows sharing of resources and data among different organizations or domains .
- Cluster computing requires specialized software to coordinate the nodes, manage the resources, schedule the tasks, communicate the data and handle the errors   .
- Some examples of cluster computing software are:
  - MPI (Message Passing Interface): A standard for inter-process communication that supports parallel programming on clusters  .
  - SLURM (Simple Linux Utility for Resource Management): A workload manager that allocates resources, launches jobs and monitors their status on clusters.
  - Hadoop: An open-source framework that enables distributed processing of large data sets on clusters using the MapReduce programming model .
  - Kubernetes: An open-source platform that automates the deployment, scaling and management of containerized applications on clusters .



# Peer-to-Peer Computing

Peer-to-peer (P2P) computing is a distributed application architecture that partitions tasks or workloads between peers. Peers are equally privileged, equipotent participants in the network. They are said to form a peer-to-peer network of nodes.

Some characteristics of peer-to-peer computing are:

- There is no central server or authority that controls the network or the data.
- Each peer can act as both a client and a server, supplying and receiving files or services.
- The network is self-organizing, dynamic, and scalable.
- The network can utilize the resources (such as bandwidth, storage, processing) of each peer more efficiently than a traditional network.
- The network is less vulnerable to systemic failure or attacks, as there is no single point of failure or bottleneck.

Some examples of peer-to-peer computing are:

- File-sharing applications, such as BitTorrent, Napster, or Gnutella, that allow users to download and upload files from each other.
- Distributed computing projects, such as SETI@home, Folding@home, or Bitcoin, that use the idle processing power of peers to perform complex calculations or transactions.
- Peer-to-peer communication applications, such as Skype, Signal, or Tor, that enable users to communicate securely and anonymously over the network.



# Internet Computing

## Unit 1 - Overview of Grid Computing Technology

Grid computing is a form of distributed computing that allows multiple computers to work together as a single virtual supercomputer. Grid computing enables the sharing of resources, data, and services across geographically dispersed and heterogeneous networks. Grid computing can be used for high-performance computing (HPC) applications that require large-scale parallel processing, such as scientific simulations, data analysis, and machine learning.

Some of the main characteristics of grid computing are:

- **Resource coordination**: Grid computing involves the coordination of multiple resources, such as processors, memory, storage, and network bandwidth, to execute a common task. Resource coordination can be achieved by using middleware, which is software that provides services for resource discovery, allocation, scheduling, monitoring, and fault tolerance.
- **Resource heterogeneity**: Grid computing can handle different types of resources, such as clusters, supercomputers, desktops, laptops, mobile devices, and sensors, that have different architectures, operating systems, and performance levels. Resource heterogeneity requires the use of standards and protocols for interoperability and compatibility among different resources.
- **Resource dynamism**: Grid computing can adapt to the dynamic changes in the availability and demand of resources, such as failures, load fluctuations, and user preferences. Resource dynamism requires the use of mechanisms for resource discovery, negotiation, reservation, and adaptation.
- **Resource sharing**: Grid computing enables the sharing of resources among multiple users and organizations, who form a virtual organization (VO) that has a common goal or interest. Resource sharing requires the use of policies and agreements for access control, security, privacy, and accounting.

Some of the main benefits of grid computing are:

- **Performance**: Grid computing can improve the performance of applications by exploiting the parallelism and scalability of multiple resources. Grid computing can also reduce the execution time and cost of applications by using idle or underutilized resources.
- **Reliability**: Grid computing can increase the reliability of applications by providing fault tolerance and redundancy of resources. Grid computing can also handle failures and errors of resources by using mechanisms for checkpointing, replication, and migration.
- **Availability**: Grid computing can enhance the availability of applications by providing access to resources that are geographically distributed and diverse. Grid computing can also overcome the limitations of local resources by using remote resources.
- **Collaboration**: Grid computing can facilitate the collaboration of users and organizations by providing a common platform for data and service sharing. Grid computing can also support the creation of virtual communities and teams that have a common interest or goal.

Some of the main challenges of grid computing are:

- **Complexity**: Grid computing involves the management of a large number of resources that are heterogeneous, dynamic, and distributed. Grid computing also requires the coordination of multiple users and organizations that have different policies and preferences. Grid computing therefore poses significant challenges for the design, development, deployment, and maintenance of grid applications and middleware.
- **Security**: Grid computing exposes the resources, data, and services to multiple users and organizations that may have malicious or conflicting intentions. Grid computing therefore requires the provision of security mechanisms for authentication, authorization, encryption, integrity, and non-repudiation.
- **Quality of service**: Grid computing has to deal with the variability and unpredictability of the performance and availability of resources, data, and services. Grid computing therefore requires the provision of quality of service (QoS) mechanisms for resource reservation, service level agreement (SLA), and QoS monitoring and adaptation.



# Grid Computing Model and Protocols

Grid computing is a distributed architecture of multiple computers connected by networks to accomplish a joint task. These tasks are compute-intensive and difficult for a single machine to handle. Several machines on a network collaborate under a common protocol and work as a single virtual supercomputer to get complex tasks done.

Grid computing is enabled via an open set of standards and protocols such as open grid services architecture (OGSA) that allow communication across heterogeneous systems and environments that are geographically dispersed.

A grid computing model consists of the following layers :

- The Fabric Layer: This layer includes the protocols and interfaces that provide access to the resources that are being shared such as compute resources, data resources, network resources, etc.
- The Connectivity Layer: This layer defines core protocols required for grid-specific network transactions such as security, authentication, authorization, resource discovery, etc.
- The Resource Layer: This layer defines protocols for the publication, monitoring, and management of resources on the grid such as CPU, memory, disk, etc.
- The Collective Layer: This layer defines protocols for the coordination and interaction of multiple resources on the grid such as scheduling, load balancing, data replication, etc.
- The Application Layer: This layer defines protocols for the development and execution of grid applications such as workflow, grid portals, grid services, etc.

Some of the core grid protocols that are used in implementing various activities and services for global grid deployment are:

- Grid Security Infrastructure (GSI): This protocol provides secure authentication and communication among grid entities using public key cryptography and X.509 certificates.
- Grid Resource Allocation and Management (GRAM): This protocol provides a uniform interface for requesting, accessing, monitoring, and controlling remote resources on the grid.
- Grid Resource Information Service (GRIS): This protocol provides a mechanism for publishing and discovering information about grid resources such as their attributes, capabilities, and availability.
- Grid File Transfer Protocol (GridFTP): This protocol extends the standard FTP protocol to support high-performance and reliable data transfer over the grid.
- Grid Monitoring Architecture (GMA): This protocol defines a framework for collecting, storing, and querying performance and status information about grid resources and services.
- Grid Service Specification (GSS): This protocol defines a common interface and behavior for grid services based on the web service standards such as SOAP, WSDL, and UDDI.



# Types of Grids

Grid computing is a distributed computing paradigm that involves the sharing and coordination of resources across multiple machines or organizations to achieve a common goal. Grid computing can be classified into different types based on the nature and purpose of the grid. Some of the common types of grids are:

- **Computational grid**: This is a type of grid that acts as a mediator of many computers in a given network to solve one single problem at a time. Computational grids are useful for applications that require a large amount of processing power, such as scientific simulations, weather forecasting, or cryptography. Computational grids can be further divided into two subtypes: task farming and parallel processing. Task farming involves dividing a large problem into smaller independent tasks and assigning them to different computers in the grid. Parallel processing involves splitting a problem into smaller interdependent tasks that require communication and synchronization among the computers in the grid .
- **Data grid**: The grid that deals with the sharing and managing the distributed data in a controlled manner is termed as a data grid. Data grids are useful for applications that require access to large and heterogeneous data sets, such as data mining, data analysis, or data-intensive scientific experiments. Data grids can provide features such as data replication, data caching, data security, data provenance, and data discovery. A specific type of data grid is an in-memory data grid (IMDG) which, as the name implies, runs processing in the computers’ main memory, e.g., random-access memory (RAM). The advantage is that the data is stored in memory across all the computers in the grid, so data access is extremely fast .
- **Collaborative grid**: Such types of grids help in solving collective problems that require the collaboration of multiple users or organizations. Collaborative grids are useful for applications that involve human interaction, such as online gaming, virtual reality, social networking, or e-learning. Collaborative grids can provide features such as group communication, resource sharing, coordination, and security.
- **Service grid**: The grid that provides access to various services or applications that are hosted on different machines or organizations is called a service grid. Service grids are useful for applications that require the integration of heterogeneous and distributed software components, such as web services, cloud computing, or service-oriented architecture. Service grids can provide features such as service discovery, service composition, service orchestration, and service quality .

These types of grids are not mutually exclusive and can be combined to form hybrid grids that meet the requirements of different applications. For example, a computational grid can use a data grid to access the data needed for the computation, or a service grid can use a collaborative grid to enable the interaction of the service providers and consumers. Grid computing is a dynamic and evolving field that offers many benefits and challenges for the development of high-performance computing applications.



# Desktop Grids

- Desktop grids are a type of distributed computing environment that make use of desktop computers connected via the Internet.
- Desktop grids are not used only for voluntary computing projects, but also for enterprise grids, where the desktop computers belong to a single organization and are connected via a non-dedicated network.
- Desktop grids can provide a large amount of computing power and storage capacity by harnessing the idle resources of desktop computers, which are often underutilized.
- Desktop grids can also support various types of applications, such as scientific computing, data analysis, image processing, web crawling, and peer-to-peer file sharing.
- Desktop grids can be classified into two categories: public desktop grids and private desktop grids.
  - Public desktop grids are open to anyone who wants to participate and contribute their desktop resources. Examples of public desktop grids are BOINC, SETI@home, Folding@home, and World Community Grid.
  - Private desktop grids are restricted to a specific group of users or organizations that share a common goal or interest. Examples of private desktop grids are Condor, Entropia, and OurGrid.
- Desktop grids face several challenges, such as security, reliability, scalability, heterogeneity, and incentive mechanisms.
  - Security: Desktop grids need to protect the privacy and integrity of the data and computations that are distributed among the desktop computers, as well as prevent malicious attacks from outsiders or insiders.
  - Reliability: Desktop grids need to cope with the dynamic and unpredictable behavior of the desktop computers, such as failures, disconnections, reboots, and resource fluctuations.
  - Scalability: Desktop grids need to handle the large number of desktop computers and the high volume of data and computations that are involved in the grid.
  - Heterogeneity: Desktop grids need to deal with the diversity of the desktop computers in terms of hardware, software, operating system, network, and performance.
  - Incentive mechanisms: Desktop grids need to motivate the desktop computer owners to participate and contribute their resources, as well as reward them for their contributions.



# Cluster Grids

- Cluster grids are a type of grid computing that involves a group of computers connected by a local area network (LAN) and working together as a single system .
- Cluster grids are usually homogeneous, meaning that the computers have the same hardware components and the same operating system (OS) .
- Cluster grids are tightly coupled, meaning that the computers communicate frequently and share a common memory and disk space .
- Cluster grids are often used for high-performance computing (HPC) applications that require a large amount of processing power and data transfer .
- Cluster grids can be classified into different types based on their architecture, such as Beowulf clusters, symmetric multiprocessor (SMP) clusters, massively parallel processor (MPP) clusters, and high-availability (HA) clusters.
- Cluster grids can also be integrated with other types of grid computing, such as cloud computing and volunteer computing, to form hybrid grids that leverage the advantages of each type .



# Data Grids

- A data grid is a set of structured services that gives individuals or groups of users the ability to access, modify and transfer extremely large amounts of geographically distributed data for research purposes .
- A data grid is different from a computational grid, which focuses on sharing computational resources rather than data resources.
- A data grid provides the following features:
  - Data discovery: the ability to locate and identify data sources that match certain criteria.
  - Data access: the ability to retrieve data from remote sources in a secure and efficient manner.
  - Data replication: the ability to create and manage copies of data across different locations for performance, reliability and availability reasons.
  - Data integration: the ability to combine and transform data from heterogeneous sources into a consistent and coherent view.
  - Data management: the ability to store, update, delete and query data in a distributed environment.
- A data grid can be used for various applications that require large-scale data analysis, such as scientific simulations, bioinformatics, astronomy, climate modeling, etc.
- A data grid can be implemented using various technologies, such as distributed file systems, peer-to-peer networks, web services, middleware, etc.



# High-Performance Grids

- High-performance grids are a type of distributed computing system that can harness the power of a large number of heterogeneous and geographically dispersed computing resources to meet the needs of compute-intensive applications  .
- High-performance grids are distinguished from conventional high-performance computing systems such as cluster computing or supercomputing in that grid computers have each node set to perform a different task or application, and that grid computers are not physically coupled or dedicated to a single organization or user.
- High-performance grids can provide several benefits such as scalability, fault-tolerance, resource sharing, collaboration, and cost-effectiveness .
- High-performance grids can also pose several challenges such as security, interoperability, scheduling, load balancing, data management, and performance optimization .
- High-performance grids can be used for various domains and applications such as genomics, oil and gas simulations, finance, semiconductor design, engineering, weather modeling, and more .



# Applications and Architectures of High Performance Grids

- A **grid** is a distributed system that enables the sharing and coordinated use of heterogeneous resources across multiple administrative domains .
- A **high performance grid** is a grid that can harness the power of an arbitrarily large collection of computing resources to meet the needs of compute intensive applications .
- Some examples of high performance grid applications are:
  - Scientific simulations, such as finite element models, climate models, molecular dynamics, etc.
  - Data-intensive applications, such as data mining, bioinformatics, astronomy, etc.
  - Collaborative applications, such as telemedicine, virtual reality, e-learning, etc.
- The main challenges of high performance grid computing are:
  - Resource heterogeneity, such as different hardware, software, network, security, etc.
  - Resource dynamism, such as resource availability, performance, reliability, etc.
  - Resource coordination, such as resource discovery, allocation, scheduling, monitoring, etc.
  - Resource management, such as resource access, security, accounting, etc.
- A typical high performance grid architecture consists of four layers :
  - The **fabric layer**, which provides the basic resources, such as processors, storage, networks, sensors, etc.
  - The **connectivity layer**, which provides the communication and authentication services, such as protocols, security, etc.
  - The **resource layer**, which provides the resource management and coordination services, such as discovery, allocation, scheduling, monitoring, etc.
  - The **application layer**, which provides the grid applications and development toolkits, such as libraries, frameworks, etc.
- Some examples of high performance grid architectures are:
  - The **Open Grid Services Architecture (OGSA)**, which defines a set of standard interfaces and behaviors for grid services based on web services technologies.
  - The **Globus Toolkit**, which provides a set of software components for implementing grid services based on OGSA.
  - The **MicroGrid**, which provides a simulation environment for forecasting the behavior of grid applications in new grid architectures.



# High Performance Application Development Environment

- A high performance application development environment is a set of tools, frameworks, and methodologies that enable developers to create, test, deploy, and optimize applications that run on high performance computing (HPC) systems or platforms.
- HPC systems or platforms are those that provide high levels of processing power, memory, storage, and network bandwidth to support applications that require intensive computations, large-scale data analysis, or real-time responsiveness.
- Examples of HPC systems or platforms include supercomputers, clusters, grids, clouds, and edge devices.
- Examples of applications that benefit from HPC systems or platforms include scientific simulations, machine learning, big data analytics, computer vision, natural language processing, and gaming.
- A high performance application development environment typically consists of the following components:
  - A programming model or language that defines how the application logic is expressed, parallelized, and distributed across the HPC system or platform. Examples of programming models or languages include MPI, OpenMP, CUDA, OpenCL, Python, and Java.
  - A development tool or IDE that provides features such as code editing, debugging, profiling, testing, and version control. Examples of development tools or IDEs include Visual Studio, Eclipse, PyCharm, and Jupyter Notebook.
  - A runtime system or library that manages the execution of the application on the HPC system or platform, including aspects such as scheduling, communication, synchronization, fault tolerance, and performance optimization. Examples of runtime systems or libraries include SLURM, PBS, Hadoop, Spark, TensorFlow, and PyTorch.
  - A deployment environment or platform that provides the infrastructure and services to run the application on the HPC system or platform, such as resource allocation, configuration, monitoring, scaling, and security. Examples of deployment environments or platforms include Azure, AWS, Google Cloud, IBM Cloud, and Kubernetes.
- A high performance application development environment should aim to achieve the following goals:
  - Productivity: The environment should enable developers to write, test, and deploy applications quickly and easily, with minimal overhead and complexity.
  - Portability: The environment should support multiple HPC systems or platforms, and allow developers to migrate or adapt applications to different architectures and environments without significant changes or rewrites.
  - Performance: The environment should leverage the full potential of the HPC system or platform, and provide mechanisms to measure, analyze, and improve the application performance in terms of speed, scalability, efficiency, and reliability.
  - Quality: The environment should ensure the correctness, robustness, and security of the application, and provide tools to detect, prevent, and resolve errors, bugs, and vulnerabilities.



# Unit 2 - Open Grid Services Architecture

- Open Grid Services Architecture (OGSA) is a set of standards that extends Web services and service-oriented architecture to the grid computing environment .
- Grid computing is the use of a large number of computers, often geographically distributed and heterogeneous, to perform coordinated tasks that require a high level of parallelism or collaboration.
- OGSA defines a common, open, and extensible set of capabilities and behaviors that address key concerns in grid systems, such as security, resource management, data access, notification, and fault tolerance .
- OGSA uses most of Web service technologies, notably WSDL and SOAP, but it aims to be largely agnostic in relation to the transport-level handling of data upon the grid.
- OGSA introduces the concept of a Grid service, which is a Web service that conforms to a set of conventions and interfaces that support the creation, management, and discovery of dynamic and transient service instances.
- OGSA also defines a common resource model that describes the state and properties of Grid services and resources, and a common factory model that enables the creation and destruction of Grid service instances.
- OGSA was developed within the Open Grid Forum, which was called the Global Grid Forum (GGF) at the time, around 2002 to 2006.
- OGSA is not a complete architecture, but rather a framework that can be extended and specialized for different domains and applications.
- OGSA is intended to enable interoperability and integration among diverse and heterogeneous grid systems, and to facilitate the development and deployment of grid applications and services.



# Introduction for the notes of the Unit 2 - Open Grid Services Architecture in the subject of High Performance Computing

- Open Grid Services Architecture (OGSA) is a set of standards and specifications that define how grid computing systems should operate and interact.
- Grid computing is a form of distributed computing that enables the sharing and coordination of heterogeneous resources across multiple domains and locations.
- OGSA aims to provide a common framework for building and deploying grid applications and services that are interoperable, scalable, secure, and reliable.
- OGSA is based on the concepts and technologies of web services, which are software components that can be accessed and invoked over the internet using standard protocols and formats.
- OGSA extends the web services model to support the dynamic and complex requirements of grid environments, such as resource discovery, negotiation, provisioning, monitoring, and management.
- OGSA defines a set of core components and interfaces that constitute the basic building blocks of grid systems, such as:
  - Grid Service: a web service that conforms to the OGSA specifications and provides a set of common behaviors and capabilities, such as lifetime management, notification, and metadata access.
  - Grid Service Handle (GSH): a globally unique and persistent identifier for a grid service instance, which can be used to locate and access the service.
  - Grid Service Reference (GSR): a transient and transport-specific reference to a grid service instance, which contains the GSH and other information needed to invoke the service.
  - Service Data: a set of structured and self-describing data elements that represent the state and properties of a grid service instance, which can be queried and updated by clients and other services.
  - Factory: a grid service that can create and destroy other grid services of a specific type, according to the requests and parameters from clients and other services.
  - Registry: a grid service that can register, discover, and query other grid services and their metadata, based on various criteria and attributes.
  - Container: a software component that hosts and manages the lifecycle and execution of grid services, and provides them with access to the underlying resources and functionalities of the grid system.
- OGSA also defines a set of higher-level components and interfaces that address specific grid functionalities and domains, such as:
  - Data Access and Integration: a set of services and protocols that enable the access, integration, and manipulation of distributed and heterogeneous data sources and repositories across the grid.
  - Execution Management: a set of services and protocols that enable the submission, scheduling, execution, and control of computational tasks and workflows across the grid.
  - Resource Management: a set of services and protocols that enable the discovery, allocation, reservation, and monitoring of physical and virtual resources across the grid.
  - Security: a set of services and protocols that enable the authentication, authorization, encryption, and auditing of grid entities and interactions.
  - Information: a set of services and protocols that enable the collection, aggregation, dissemination, and analysis of information about the grid system and its components.
  - Self-Management: a set of services and protocols that enable the self-configuration, self-optimization, self-healing, and self-protection of the grid system and its components.



# Requirements for the notes of the Unit 2 - Open Grid Services Architecture in the subject of High Performance Computing

- The notes should explain the concept and purpose of Open Grid Services Architecture (OGSA) as a service-oriented architecture for grid computing.
- The notes should describe the main components and features of OGSA, such as:
  - Grid services: stateful, transient, and self-describing Web services that provide the basic building blocks for grid applications.
  - Grid service instances: individual instances of grid services that are identified by unique handles and can be created, destroyed, or migrated by clients or other services.
  - Grid service factories: grid services that can create new grid service instances on demand or according to some policy.
  - Grid service groups: collections of grid service instances that share some common characteristics or functionality and can be discovered and managed as a unit.
  - Grid service containers: software environments that host and execute grid services and provide common services such as security, logging, and monitoring.
  - Grid service interfaces: standard interfaces that define the common behaviors and capabilities of grid services, such as naming, lifetime management, notification, and metadata access.
  - Grid service bindings: specifications of how grid service interfaces are mapped to concrete protocols and formats, such as SOAP, HTTP, and XML.
- The notes should illustrate the benefits and challenges of OGSA, such as:
  - Benefits: interoperability, flexibility, scalability, reliability, and security of grid systems and applications.
  - Challenges: complexity, performance, compatibility, and standardization of grid services and technologies.
- The notes should provide some examples and use cases of OGSA, such as:
  - Data grid: a grid service that provides access to distributed and heterogeneous data sources and supports data replication, caching, and querying.
  - Compute grid: a grid service that provides access to distributed and heterogeneous computing resources and supports job submission, scheduling, and execution.
  - Workflow grid: a grid service that provides access to distributed and heterogeneous workflow engines and supports workflow composition, orchestration, and monitoring.
  - Information grid: a grid service that provides access to distributed and heterogeneous information sources and supports information discovery, integration, and analysis.



# Capabilities for the notes of the Unit 2 - Open Grid Services Architecture in the subject of High Performance Computing

- Open Grid Services Architecture (OGSA) is a set of standards that extends Web services and service-oriented architecture to the grid computing environment .
- OGSA defines a common, extensible, and flexible framework for exposing and accessing grid resources as services, using standard protocols and interfaces.
- OGSA addresses key concerns in grid systems, such as resource discovery, dynamic provisioning, monitoring, security, fault tolerance, and interoperability .
- OGSA uses most of Web service technologies, notably WSDL and SOAP, but it aims to be largely agnostic in relation to the transport-level handling of data upon the grid.
- OGSA consists of a core set of interfaces, behaviors, resource models, and bindings that define the basic functionality and semantics of grid services.
- OGSA also defines a set of optional capabilities that provide additional functionality and services for specific domains and scenarios, such as data access, execution management, information services, security, and self-management.
- OGSA enables the development of interoperable and portable grid applications and middleware that can leverage the capabilities of diverse and dynamic grid environments.



# Security Considerations for Open Grid Services Architecture

- Open Grid Services Architecture (OGSA) is a framework for building distributed systems that can share resources and services across heterogeneous and dynamic environments .
- Security is a crucial aspect of OGSA, as it involves protecting the confidentiality, integrity, availability and accountability of the resources and services, as well as the users and providers of the grid .
- OGSA security architecture aims to support, integrate and unify popular security models, mechanisms, protocols, platforms and technologies in a way that enables a variety of systems to interoperate securely .
- Some of the key security considerations for OGSA are:

  - Authentication: the process of verifying the identity of a user or a service that requests access to a resource or a service on the grid .
  - Authorization: the process of determining the permissions and privileges of a user or a service to access a resource or a service on the grid .
  - Delegation: the process of transferring the rights and obligations of a user or a service to another user or service on the grid, for a specific purpose or duration .
  - Confidentiality: the process of protecting the data and messages exchanged on the grid from unauthorized disclosure or interception .
  - Integrity: the process of ensuring the data and messages exchanged on the grid are not modified or corrupted by unauthorized parties .
  - Availability: the process of ensuring the resources and services on the grid are accessible and functional when needed by authorized parties .
  - Accountability: the process of tracking and auditing the actions and events on the grid, and enforcing the policies and agreements that govern the grid .

- OGSA security architecture relies on a number of security standards and technologies, such as:

  - Public Key Infrastructure (PKI): a system that provides the generation, distribution, management and revocation of digital certificates that bind public keys to identities .
  - X.509: a standard that defines the format and content of digital certificates and certificate revocation lists (CRLs) .
  - Secure Sockets Layer (SSL) / Transport Layer Security (TLS): protocols that provide secure communication channels between two parties over the Internet, using encryption, authentication and integrity mechanisms .
  - Simple Object Access Protocol (SOAP): a protocol that defines a standard way of exchanging structured and typed information between web services, using XML-based messages .
  - Web Services Security (WS-Security): a specification that defines how to apply security to SOAP messages, using XML-based tokens, signatures and encryption .
  - Grid Security Infrastructure (GSI): a set of extensions and enhancements to the above standards and technologies, that provide a common security framework for grid computing, based on the concept of proxy certificates .
  - Security Assertion Markup Language (SAML): a standard that defines a way of expressing and exchanging security information between different security domains, using XML-based assertions .
  - Extensible Access Control Markup Language (XACML): a standard that defines a way of expressing and enforcing access control policies, using XML-based rules and requests .

- OGSA security architecture also addresses some of the specific challenges and requirements of grid computing, such as:

  - Scalability: the ability to handle a large number of users, services and resources on the grid, without compromising the performance or security of the grid .
  - Interoperability: the ability to support different security models, mechanisms, protocols, platforms and technologies on the grid, and enable them to work together securely .
  - Dynamism: the ability to adapt to the changing and unpredictable nature of the grid, such as the creation, discovery, invocation and termination of services and resources, and the mobility and heterogeneity of users and devices .
  - Trust: the ability to establish and maintain the confidence and reliability of the users, services and resources on the grid, and to deal with the risks and uncertainties of the grid [^2^



# GLOBUS Toolkit

- The GLOBUS Toolkit is an open-source toolkit for grid computing developed and provided by the Globus Alliance.
- Grid computing is a form of distributed computing that enables the sharing of resources across multiple organizations or domains.
- The GLOBUS Toolkit contains a set of libraries and programs that provides the developers of specific tools or apps with solutions for common problems that are encountered when creating a distributed system services and applications.
- Globus is a software with components and capabilities that includes:
  - Security: authentication, authorization, delegation, single sign-on, etc.
  - Data management: data transfer, replication, cataloging, etc.
  - Resource management: job submission, monitoring, scheduling, etc.
  - Information services: discovery, monitoring, notification, etc.
  - Common runtime: logging, configuration, fault handling, etc.
- The GLOBUS Toolkit is based on the Open Grid Services Architecture (OGSA), which defines a set of standard interfaces and behaviors for grid services.
- Grid services are web services that follow certain conventions to support dynamic and transient interactions in a distributed environment.
- The GLOBUS Toolkit is no longer available as a do-it-yourself distributed computing toolkit, but its spirit lives on in a mature, full-featured and easy to use service for research data management – Globus.org!
- Globus.org is a cloud-based platform that allows researchers to easily and securely move, share, and discover data across any location or storage system.
- Globus.org also provides advanced features such as automation, auditing, data publication, and identity management.



# Unit 3 - Overview of Cluster Computing

- Cluster computing is a form of parallel computing that involves connecting multiple computers (called nodes) on a network and using them as a single system for high-performance tasks  .
- Cluster computing can provide faster computational speed, enhanced data integrity, higher availability, and better scalability than a single computer .
- Cluster computing can be classified into different types based on the degree of coupling, the architecture, the communication pattern, and the application domain  .
- Some common types of clusters are:
  - Beowulf cluster: A cluster of commodity hardware running Linux or other free software, designed for scientific or engineering applications.
  - Load-balancing cluster: A cluster that distributes the workload among the nodes to optimize the performance and availability of web servers or other network services.
  - High-availability cluster: A cluster that provides redundancy and fault tolerance by switching to a backup node in case of a failure of the primary node.
  - Grid cluster: A cluster that connects geographically distributed nodes over the internet or other networks, and allows sharing of resources and data among different organizations or domains .
- Cluster computing requires special software to coordinate the nodes, schedule the tasks, manage the data, and handle the communication and synchronization among the nodes  .
- Some examples of cluster computing software are:
  - MPI (Message Passing Interface): A standard for inter-process communication that supports parallel programming on clusters and other platforms  .
  - Hadoop: An open-source framework for distributed storage and processing of large-scale data sets on clusters of commodity hardware .
  - Kubernetes: An open-source system for automating the deployment, scaling, and management of containerized applications on clusters of nodes.
- Cluster computing has many applications in various fields, such as scientific computing, data analysis, machine learning, web hosting, gaming, and cloud computing   .



# Cluster Computer and its Architecture

- A cluster computer is a set of connected computers that work together as a single system   .
- The connected computers are called nodes, and they can be personal computers, workstations, servers, or supercomputers  .
- A cluster computer can be used to enhance the processing power, increase the resilience, or provide high availability of a system .
- A cluster computer has a specific architecture that consists of the following components :
  - Cluster nodes: the individual computers that perform the computation, communication, and storage tasks.
  - Cluster interconnect: the network that connects the cluster nodes and enables data transfer and synchronization.
  - Cluster middleware: the software that manages the cluster resources, coordinates the load sharing, detects node failures, and schedules node replacements.
  - Cluster applications: the programs that run on the cluster and exploit its parallel and distributed capabilities.
- A cluster computer can be classified into different types based on the hardware, software, and application characteristics . Some common types are:
  - High-performance computing (HPC) clusters: clusters that are designed to provide high-speed computation for scientific and engineering applications.
  - High-availability (HA) clusters: clusters that are designed to provide continuous operation and fault tolerance for critical applications.
  - Load-balancing clusters: clusters that are designed to distribute the workload among multiple nodes and improve the performance and scalability of applications.
  - Data-intensive clusters: clusters that are designed to handle large amounts of data and provide fast and reliable data access and analysis.



# Clusters Classifications for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

- Cluster computing is a form of parallel computing that uses a collection of interconnected computers, called nodes, to perform tasks that require high performance, availability, or scalability .
- Cluster computing can be classified into three main types, based on the purpose and design of the clusters :
  - **High performance (HP) clusters**: HP clusters use computer clusters and supercomputers to solve advanced computational problems that require high speed, accuracy, and efficiency. HP clusters are used for scientific computing, engineering simulations, data analysis, artificial intelligence, and other demanding applications. HP clusters typically have high-performance processors, memory, storage, and networking components, as well as specialized software and hardware to optimize the performance and parallelism of the cluster  .
  - **Load-balancing clusters**: Load-balancing clusters distribute incoming requests or workloads among several nodes running similar programs or having similar content. Load-balancing clusters are used to improve the availability, reliability, and scalability of web servers, databases, applications, and other services. Load-balancing clusters can also provide fault tolerance and redundancy by detecting and replacing failed nodes or rerouting requests to other nodes .
  - **High availability (HA) clusters**: HA clusters ensure that a critical service or application remains operational and accessible at all times, even in the event of a node failure, network outage, or other disruption. HA clusters use techniques such as heartbeat monitoring, failover, replication, and backup to detect and recover from failures and maintain the continuity and consistency of the service or application. HA clusters are used for mission-critical systems, such as banking, healthcare, e-commerce, and telecommunications .



# Components for Clusters

- A cluster is a collection of interconnected computers that work together as a single system to perform high-performance computing tasks.
- A cluster typically consists of the following components    :
  - A cluster provisioner that ensures node homogeneity and manages the installation and configuration of the cluster software and hardware.
  - Servers, often referred to as nodes, that provide the computing power and run the applications. Nodes can be homogeneous or heterogeneous in terms of their hardware and software specifications. Nodes can be divided into different types, such as head nodes, compute nodes, login nodes, and service nodes, depending on their roles and functions in the cluster.
  - A scheduler that queues up workloads against the cluster resources and allocates nodes to the jobs submitted by the users. A scheduler also monitors the status and performance of the cluster and handles failures and errors.
  - A network for communication between nodes and external devices. The network can be composed of different types of interconnects, such as Ethernet, InfiniBand, or Omni-Path, that vary in their bandwidth, latency, and cost. The network topology and routing can also affect the performance and scalability of the cluster.
  - A general-purpose storage solution used to store applications and user data. This can be a local storage attached to each node, a shared storage accessible by all nodes, or a cloud storage service. The storage solution should provide sufficient capacity, performance, reliability, and security for the cluster needs.
  - A high-speed, low-latency clustered file system generally used for computational storage. This is a special type of file system that allows multiple nodes to access the same files concurrently and consistently. A clustered file system can improve the data throughput and availability of the cluster and reduce the data movement and duplication. Examples of clustered file systems are Lustre, GPFS, and BeeGFS.



# Cluster Middleware and SSI

- Cluster middleware is a software layer that provides a unified view of the cluster resources and services to the users and applications.
- Cluster middleware consists of two sub-layers: SSI infrastructure and SAI infrastructure.
- SSI stands for Single System Image, which is the property of a system that hides the heterogeneous and distributed nature of the available resources and presents them to users and applications as a single unified computing resource .
- SSI infrastructure provides features such as process migration, load balancing, distributed shared memory, global process management, global file system, global I/O, global IPC, and global device namespace  .
- SAI stands for System Availability Infrastructure, which is the software layer that provides fault tolerance and high availability to the cluster services and applications.
- SAI infrastructure provides features such as check pointing, automatic failover, recovery from failure, and fault-tolerant communication  .
- Cluster middleware and SSI enable cluster computing to achieve high performance, scalability, and reliability.



# Resource Management and Scheduling for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

- Resource management and scheduling (RMS) are critical tasks in cluster computing, as they determine how the cluster resources are allocated and utilized by the applications.
- The RMS of clusters provides support of four main functionalities:
  - Management of resources: The RMS manages, controls and maintains the status information of the resources such as processors and disk storage in the cluster system.
  - Job queuing: Jobs submitted by the users into the cluster system are initially placed into queues until there are available resources to execute the jobs.
  - Job scheduling: The cluster RMS then invokes the cluster scheduler to determine how resources are assigned to various jobs based on some criteria such as fairness, priority, performance, etc.
  - Job execution: After that, the cluster RMS dispatches the jobs to the assigned nodes and manages the job execution processes before returning the results to the users upon job completion.
- Cluster resource scheduling includes two main functions:
  - Resource allocation: The process of assigning a certain quantity of computing resources to each user or application at runtime, guided by a global policy to share cluster resources among multiple users based on fairness and/or predefined priority.
  - Job scheduling: The process of mapping the tasks of an application to the allocated resources, taking into account the dependencies, communication, load balancing, and optimization objectives.
- There are different types of cluster schedulers, such as:
  - Batch schedulers: They execute jobs in batches, without any user interaction. They are suitable for long-running, compute-intensive, and parallel applications. Examples are Slurm, PBS, and LSF.
  - Interactive schedulers: They execute jobs on demand, with user interaction. They are suitable for short-running, interactive, and sequential applications. Examples are SSH and RSH.
  - Hybrid schedulers: They combine the features of batch and interactive schedulers, and can execute both types of jobs. Examples are Condor and SGE.
- There are different challenges and trade-offs involved in cluster resource scheduling, such as:
  - Heterogeneity: The cluster resources may have different capabilities, availability, and performance, which makes the scheduling more complex and dynamic.
  - Scalability: The cluster may have a large number of resources and jobs, which requires efficient and distributed algorithms and data structures to handle the scheduling problem.
  - Fault tolerance: The cluster may experience failures of resources or jobs, which requires mechanisms to detect, recover, and reschedule the affected tasks.
  - Quality of service: The cluster may have different service level agreements (SLAs) with the users or applications, which requires mechanisms to ensure the satisfaction of the SLAs in terms of performance, availability, reliability, etc.
  - Energy efficiency: The cluster may consume a large amount of energy, which requires mechanisms to reduce the energy consumption and carbon footprint of the cluster, such as dynamic voltage and frequency scaling (DVFS), power capping, and resource consolidation.



# Programming for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

## Cluster Computing

- Cluster computing is a form of parallel computing that involves connecting multiple computers (called nodes) together in a network to perform a common task.
- Cluster computing can provide faster computational speed, enhanced data integrity, higher availability, and better scalability than a single computer.
- Cluster computing can be classified into two types: loosely coupled and tightly coupled.
  - Loosely coupled clusters have each node running its own operating system and software, and communicate with each other through a network interface.
  - Tightly coupled clusters have each node running the same operating system and software, and communicate with each other through a high-speed interconnect.
- Cluster computing can be used for various applications, such as scientific computing, data analysis, web hosting, load balancing, and fault tolerance.

## Cluster Architecture

- A typical cluster architecture consists of the following components:
  - Head node: The head node is the central node that controls and coordinates the activities of the cluster. It is responsible for scheduling jobs, managing resources, and providing access to the cluster for users and applications.
  - Compute nodes: The compute nodes are the nodes that perform the actual computation and processing of the cluster. They receive tasks from the head node and execute them in parallel.
  - Storage nodes: The storage nodes are the nodes that provide storage space for the cluster. They can be either local or distributed, depending on the cluster configuration and the data requirements.
  - Network: The network is the medium that connects the nodes together and enables data transfer and communication among them. The network can be either a local area network (LAN) or a wide area network (WAN), depending on the cluster size and location.

## Cluster Programming

- Cluster programming is the process of developing and running applications that can utilize the cluster resources and achieve high performance and efficiency.
- Cluster programming can be done using various tools and frameworks, such as:
  - Message Passing Interface (MPI): MPI is a standard for writing parallel programs that communicate through messages. MPI provides a set of functions and libraries that allow programmers to create, send, receive, and synchronize messages among processes in a cluster.
  - OpenMP: OpenMP is a standard for writing parallel programs that use shared memory. OpenMP provides a set of directives and functions that allow programmers to specify parallel regions, loops, and tasks in a cluster.
  - MapReduce: MapReduce is a framework for writing parallel programs that process large-scale data sets. MapReduce provides a simple programming model that consists of two functions: map and reduce. The map function applies a transformation to each input data element and produces intermediate key-value pairs. The reduce function aggregates the intermediate values associated with the same key and produces the final output.



# Environments and Tools for Cluster Computing

- Cluster computing is a form of high performance distributed computing (HPDC) that uses a network of computers (called nodes) to execute parallel or distributed applications.
- Cluster computing requires a software stack that consists of the following components:
  - Workload managers or schedulers: These are software tools that manage the allocation and execution of jobs on the cluster nodes. Examples are Slurm, PBS, or IBM's LSF.
  - Cluster configuration tools: These are software tools that automate the creation and management of cluster nodes. Examples are Managed Instance Groups or Kubernetes for cloud-based clusters, or Terraform for provisioning and building clusters.
  - End-user applications: These are software tools that perform the actual computations and analysis on the cluster nodes. Examples are OpenFOAM, GROMACS, WRF, or Jupyter Notebooks for scientific and engineering applications.
- Cluster computing environments and tools vary depending on the type, size, and purpose of the cluster. Some common types of clusters are:
  - Beowulf clusters: These are clusters of commodity hardware that run Linux and use open source software for workload management and cluster configuration. Examples are Rocks Cluster Distribution or OSCAR.
  - Cloud clusters: These are clusters of virtual machines that run on cloud platforms and use cloud services for workload management and cluster configuration. Examples are Google Cloud Platform or Amazon Web Services.
  - Container clusters: These are clusters of containers that run on any platform and use containerization and cluster management tools for workload management and cluster configuration. Examples are Docker Swarm, Kubernetes, or Rancher.
  - Grid clusters: These are clusters of heterogeneous and geographically distributed nodes that run on different platforms and use grid middleware for workload management and cluster configuration. Examples are gLite or Globus Toolkit.
- Cluster computing environments and tools are constantly evolving and improving to meet the challenges and demands of HPDC applications. Some of the current trends and issues are:
  - Scalability: Cluster computing environments and tools need to support large-scale clusters with thousands or millions of nodes and handle dynamic and heterogeneous workloads.
  - Fault tolerance: Cluster computing environments and tools need to ensure the reliability and availability of the cluster nodes and the applications running on them, and handle failures gracefully.
  - Security: Cluster computing environments and tools need to protect the cluster nodes and the applications running on them from unauthorized access and malicious attacks.
  - Energy efficiency: Cluster computing environments and tools need to optimize the energy consumption and performance of the cluster nodes and the applications running on them, and reduce the environmental impact of cluster computing.
  - Usability: Cluster computing environments and tools need to provide user-friendly interfaces and tools for cluster creation, management, and monitoring, and support various programming models and languages for cluster applications.



# Cluster Applications

Cluster computing is a popular approach to achieve high performance computing (HPC) for various scientific and engineering applications. It involves connecting multiple computers or nodes into a network to share resources and workloads. Cluster computing can be used to solve complex computational problems that require high-speed, high-throughput and low-latency components. Some of the applications of cluster computing are:

- **Genomics**: Cluster computing can be used to analyze large-scale genomic data, such as sequencing, alignment, annotation, and comparison of DNA and RNA. Cluster computing can help accelerate the discovery of new genes, variants, and biomarkers, as well as the understanding of the molecular mechanisms of diseases and treatments.
- **Oil and gas simulations**: Cluster computing can be used to model the exploration, extraction, and processing of oil and gas resources. Cluster computing can help optimize the design and operation of wells, pipelines, refineries, and other facilities, as well as the prediction and management of risks and environmental impacts.
- **Finance**: Cluster computing can be used to perform complex financial calculations, such as portfolio optimization, risk analysis, pricing, and trading. Cluster computing can help improve the accuracy and efficiency of financial decisions, as well as the security and compliance of financial transactions.
- **Semiconductor design**: Cluster computing can be used to design and test new semiconductor devices, such as microprocessors, memory chips, and sensors. Cluster computing can help reduce the time and cost of development, as well as the power consumption and heat dissipation of the devices.
- **Engineering**: Cluster computing can be used to simulate and optimize various engineering problems, such as structural analysis, fluid dynamics, heat transfer, and electromagnetics. Cluster computing can help improve the performance and reliability of engineering products, such as aircraft, vehicles, bridges, and buildings.
- **Weather modeling**: Cluster computing can be used to forecast and analyze the weather and climate conditions, such as temperature, precipitation, wind, and pressure. Cluster computing can help improve the accuracy and resolution of weather predictions, as well as the understanding and mitigation of weather-related hazards and disasters.

These are some of the examples of cluster applications for high performance computing. Cluster computing can also be used for other domains, such as web services, data mining, artificial intelligence, and bioinformatics. Cluster computing can offer many benefits, such as scalability, reliability, availability, and cost-effectiveness, for various HPC applications.



# Cluster Systems

- A cluster system is a set of computers that work together as a single system to provide high performance, availability, and scalability.
- A cluster system consists of two or more individual computer systems, called nodes, that are connected by a network and share common storage .
- A cluster system can be classified into two types: hardware clusters and software clusters.
  - Hardware clusters are based on the physical configuration of the nodes and the storage devices. They can be further divided into shared-nothing clusters, shared-disk clusters, and shared-memory clusters.
  - Software clusters are based on the logical organization of the nodes and the applications running on them. They can be further divided into high-availability clusters, load-balancing clusters, and high-performance clusters.
- A cluster system can provide several benefits, such as:
  - Fault tolerance: If one or more nodes fail, the cluster can continue to provide service by transferring the workload to the surviving nodes (a process known as failover).
  - Load balancing: The cluster can distribute the workload among the nodes to optimize the resource utilization and performance.
  - Scalability: The cluster can be easily expanded by adding more nodes or storage devices without disrupting the service.
- A cluster system can also face some challenges, such as:
  - Complexity: The cluster requires additional hardware and software components to coordinate the nodes and the storage devices. It also requires careful planning and configuration to ensure the compatibility and consistency of the cluster.
  - Overhead: The cluster introduces some overhead for communication, synchronization, and management of the nodes and the storage devices. This can affect the performance and efficiency of the cluster.
  - Security: The cluster exposes more attack surfaces and vulnerabilities than a single system. It also requires additional security measures to protect the data and the applications on the cluster.



# Unit 4 - Beowulf Cluster

- A Beowulf cluster is a computer cluster of what are normally identical, commodity-grade computers networked into a small local area network with libraries and programs installed which allow processing to be shared among them.
- The result is a high-performance parallel computing cluster from inexpensive personal computer hardware.
- A Beowulf cluster is scalable to a nearly unlimited number of computers, limited only by the overhead of the network.
- Provisioning of operating systems and other software for a Beowulf Cluster can be automated using software, such as Open Source Cluster Application Resources.
- Beowulf clusters are based on commodity hardware, on a private system network, with open source software (Linux) infrastructure.
- The designer can improve performance proportionally with added machines.
- Beowulf clusters are programmed such that they share processes among themselves and form parallel processing units.
- Beowulf clusters can be used for applications that require high computational power, such as scientific computing, data analysis, image processing, etc.
- Beowulf clusters can be built using simple steps, such as installing a Linux distribution on the computers, connecting them with a network, configuring the network settings, installing the necessary software packages, and testing the cluster performance.
- Beowulf clusters make supercomputing accessible and affordable for various domains, such as engineering, education, research, etc.
- Beowulf clusters are an example of how open source software and hardware can enable innovation and collaboration in the field of computing.



# The Beowulf Model

- A Beowulf cluster is a computer cluster of what are normally identical, commodity-grade computers networked into a small local area network with libraries and programs installed which allow processing to be shared among them.
- The result is a high-performance parallel computing cluster from inexpensive personal computer hardware.
- A Beowulf cluster is scalable to a nearly unlimited number of computers, limited only by the overhead of the network.
- Provisioning of operating systems and other software for a Beowulf Cluster can be automated using software, such as Open Source Cluster Application Resources.
- Beowulf clusters are based on commodity hardware, on a private system network, with open source software (Linux) infrastructure.
- The designer can improve performance proportionally with added machines.
- Beowulf clusters are programmed such that they share processes among themselves and form parallel processing units.
- Beowulf clusters can be built using simple steps, such as installing Linux on the computers, configuring the network, setting up password-less SSH, installing MPI, compiling and running parallel programs.
- Beowulf clusters make supercomputing accessible and affordable for various applications, such as modeling and simulation, data analysis, machine learning, etc.



# Application Domains for Beowulf Cluster

- A Beowulf cluster is a group of commodity-grade computers that are networked and programmed to perform parallel computing tasks.
- Beowulf clusters can be used for various applications that require high performance computing, such as:
  - Transport phenomena, including fluid dynamics, heat and mass transfer, multi-phase flows, aerodynamics, etc .
  - Molecular dynamics, protein folding, and bioinformatics .
  - Cellular automata to model phenomena from epidemiology to options trading.
  - Graphics: distributed raytracing and rendering.
  - Hard NP problems such as DNA sequence alignment, cryptography, and combinatorial optimization .
  - Modeling and simulation of physical systems, such as climate, earthquakes, nuclear reactors, etc.
  - Data analysis and machine learning.
- Beowulf clusters can provide supercomputing capabilities at a low cost and with high scalability.



# Beowulf System Architecture

- Beowulf is a multi-computer architecture which can be used for parallel computations .
- It is a system which usually consists of one server node, and one or more client nodes connected via Ethernet or some other network .
- The server node acts as the master node that controls and coordinates the tasks of the client nodes, which are also called slave or worker nodes .
- The client nodes are typically commodity hardware, such as personal computers or workstations, that run Linux or some other open source operating system .
- The client nodes communicate with the server node and each other using standard protocols, such as TCP/IP, MPI, or PVM .
- The client nodes can also share data and files using a distributed file system, such as NFS or PVFS .
- The Beowulf system architecture is scalable, flexible, and cost-effective, as it can be built from readily available and inexpensive components .
- The Beowulf system architecture can be used for various applications that require high performance computing, such as scientific simulations, data analysis, image processing, and machine learning .
- The Beowulf system architecture is an example of a cluster computing system, which is a type of parallel computing system that consists of a collection of interconnected computers that work together as a single system .
- The Beowulf system architecture was invented by Thomas Sterling and Donald Becker at NASA's Goddard Space Flight Center in the mid-1990s. They named it after the epic poem Beowulf, which tells the story of a hero who slays a monster .



# Software Practices for Beowulf Cluster

A Beowulf cluster is a type of high-performance computing (HPC) system that consists of a group of identical, commodity-grade computers networked into a small local area network (LAN) with libraries and programs installed which allow processing to be shared among them . The result is a parallel computing cluster that can perform complex tasks faster and cheaper than a single supercomputer.

Some of the software practices for Beowulf cluster are:

- **Operating system**: The most common operating system used for Beowulf cluster is Linux, as it is open source, customizable, and compatible with various hardware and software components. Linux also supports various parallel programming models, such as MPI (Message Passing Interface), OpenMP (Open Multi-Processing), and Pthreads (POSIX Threads)  .
- **Network**: The network is a crucial component of a Beowulf cluster, as it connects the nodes and enables data transfer and communication among them. The network should be fast, reliable, and secure, and should match the bandwidth and latency requirements of the applications. Some of the common network technologies used for Beowulf cluster are Ethernet, InfiniBand, and Myrinet  .
- **File system**: The file system is the software that manages the storage and access of data on the cluster. The file system should be scalable, distributed, and fault-tolerant, and should support concurrent and parallel access from multiple nodes. Some of the common file systems used for Beowulf cluster are NFS (Network File System), PVFS (Parallel Virtual File System), and Lustre  .
- **Scheduling and resource management**: The scheduling and resource management software is responsible for allocating and managing the resources (such as CPU, memory, disk, and network) on the cluster, and for executing and monitoring the jobs submitted by the users. The software should be efficient, fair, and flexible, and should support various policies and priorities. Some of the common scheduling and resource management software used for Beowulf cluster are PBS (Portable Batch System), SLURM (Simple Linux Utility for Resource Management), and LSF (Load Sharing Facility)  .
- **Application software**: The application software is the software that performs the actual computation and analysis on the cluster. The application software should be parallelized, optimized, and scalable, and should exploit the features and capabilities of the cluster. Some of the common application software used for Beowulf cluster are COMSOL Multiphysics, MATLAB, and BLAST (Basic Local Alignment Search Tool)   .



# Parallel Programming with MPL

MPL is a compiler for parallel programming on shared-memory multicore machines. The MPL language is essentially Standard ML (SML) with extensions for parallelism. MPL generates executables with excellent multicore performance, utilizing a novel approach to memory management based on the theory of disentanglement    .

## Features of MPL

- MPL supports nested (fork-join) parallelism, which allows the programmer to express parallel computations as a tree of tasks that can be executed concurrently by different cores.
- MPL provides a parallel version of the SML library, which includes parallel data structures, parallel algorithms, and parallel I/O operations.
- MPL implements a space-efficient garbage collector that avoids copying or moving data between cores, and ensures that each core only accesses its own local memory regions.
- MPL uses a type-and-effect system to statically check the parallelism and locality properties of the program, and to optimize the code generation and runtime system accordingly.
- MPL supports interoperability with C, allowing the programmer to call C functions from MPL and vice versa.

## Example of MPL

The following code snippet shows a parallel implementation of the quicksort algorithm in MPL:

```sml
fun quicksort [] = []
  | quicksort (x::xs) =
    let
      val (lesser, greater) = List.partition (fn y => y < x) xs
      val (sorted_lesser, sorted_greater) =
        par (quicksort lesser, quicksort greater)
    in
      sorted_lesser @ [x] @ sorted_greater
    end
```

The `par` construct creates two parallel tasks, one for sorting the `lesser` list and one for sorting the `greater` list, and waits for both tasks to finish before concatenating the results. The `List.partition` function is also parallelized by MPL, using a divide-and-conquer strategy.

## References

: Disentanglement: A New Approach to Space-Efficient Parallel Functional Programming. Umut A. Acar, Arthur Charguéraud, Mike Rainey, and Filip Sieczkowski. In Proceedings of the 2020 ACM SIGPLAN International Conference on Functional Programming (ICFP 2020), pages 1–29, 2020.

: Disentanglement: A New Approach to Space-Efficient Parallel Functional Programming (Extended Version). Umut A. Acar, Arthur Charguéraud, Mike Rainey, and Filip Sieczkowski. Technical Report, 2020.

: Disentanglement: A New Approach to Space-Efficient Parallel Functional Programming (Slides). Umut A. Acar, Arthur Charguéraud, Mike Rainey, and Filip Sieczkowski. Presented at ICFP 2020, 2020.

: Disentanglement: A New Approach to Space-Efficient Parallel Functional Programming (Video). Umut A. Acar, Arthur Charguéraud, Mike Rainey, and Filip Sieczkowski. Presented at ICFP 2020, 2020.

: Disentanglement: A New Approach to Space-Efficient Parallel Functional Programming (Website). Umut A. Acar, Arthur Charguéraud, Mike Rainey, and Filip Sieczkowski. https://mpl.cis.upenn.edu/, 2020.



# Parallel Virtual Machine (PVM) for the notes of the Unit 4 - Beowulf Cluster in the subject of High Performance Computing

- Parallel Virtual Machine (PVM) is a software tool for parallel networking of computers.
- It allows a network of heterogeneous Unix and/or Windows machines to be used as a single distributed parallel processor  .
- It can solve large computational problems more cost effectively by using the aggregate power and memory of many computers  .
- It can also handle the dynamic addition or deletion of machines during the execution of parallel programs.
- It provides a library of functions that can be used by C, C++, Fortran, and Java programs to send and receive messages, start and stop processes, and manage the configuration of the virtual machine .
- It supports various features such as load balancing, fault tolerance, debugging, and performance monitoring .
- It is designed to be portable, easy to use, and flexible .
- It can be used as a stand-alone software or as a foundation for other heterogeneous network software.
- It is an example of a message-passing system, where the communication between processes is explicit and under the control of the programmer .
- It is also an example of a master-slave system, where one process (the master) coordinates the work of other processes (the slaves) .
- It is one of the software tools that can be used to build and run a Beowulf cluster, which is a type of high-performance computing system that consists of a collection of commodity hardware connected by a local area network .



# Unit 5 - Overview of Cloud Computing

- Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction.
- Cloud computing also refers to the technology that makes cloud work. This includes some form of virtualized IT infrastructure— servers, operating system software, networking, and other infrastructure that’s abstracted, using special software, so that it can be pooled and divided irrespective of physical hardware boundaries.
- Cloud computing is the delivery of computing services—including servers, storage, databases, networking, software, analytics, and intelligence—over the Internet (“the cloud”) to offer faster innovation, flexible resources, and economies of scale.
- Cloud computing has several benefits for users and businesses, such as:
  - Cost savings: Cloud computing eliminates the need for upfront capital investment in hardware and software, as well as the ongoing costs of maintenance and upgrades. Users only pay for the resources they use, and can scale up or down as needed.
  - Scalability: Cloud computing allows users to access more or less computing resources on demand, without worrying about the capacity or availability of physical servers. Cloud services can handle peak loads and sudden spikes in traffic or demand, as well as support growth and expansion.
  - Performance: Cloud computing offers high-speed and reliable access to computing resources, as well as improved security and backup. Cloud services are hosted on geographically distributed data centers that are constantly updated and optimized for efficiency and performance.
  - Innovation: Cloud computing enables users to access the latest technologies and tools, such as artificial intelligence, machine learning, big data analytics, and Internet of Things. Cloud services also facilitate collaboration and experimentation, as users can easily share and test new ideas and solutions.
  - Flexibility: Cloud computing supports different types of applications and workloads, as well as different deployment models and service levels. Users can choose from various cloud service providers and cloud service models, such as public, private, hybrid, or multi-cloud, and software as a service (SaaS), platform as a service (PaaS), or infrastructure as a service (IaaS).



# Types of Cloud

Cloud computing is the delivery of computing services over the internet, such as servers, storage, databases, networking, software, analytics, and intelligence. Cloud computing can be classified into two main categories: deployment models and service models.

## Deployment Models

Deployment models refer to the location and management of the cloud's infrastructure. There are four main types of deployment models:

- **Public cloud**: The cloud infrastructure is owned and operated by a third-party cloud service provider, such as Amazon Web Services (AWS), Microsoft Azure, or Google Cloud Platform (GCP). The cloud services are delivered over the internet and are available to anyone who wants to use them. The customers share the same infrastructure and resources, which are dynamically allocated and released according to demand. Public cloud offers scalability, cost-effectiveness, and reliability, but may have less control and security than other models.
- **Private cloud**: The cloud infrastructure is exclusively used by a single organization or a group of organizations that share common goals and interests. The cloud infrastructure can be owned, managed, and operated by the organization itself, a third-party service provider, or a combination of both. The cloud services are delivered over a private network or the internet, and are not accessible to the public. Private cloud offers more control, security, and customization than public cloud, but may have higher costs and complexity.
- **Hybrid cloud**: The cloud infrastructure is a combination of public and private clouds, which are connected by a technology that allows data and applications to move between them. The hybrid cloud model enables the organization to leverage the benefits of both public and private clouds, such as scalability, cost-efficiency, security, and flexibility, depending on the needs and preferences of the organization. However, hybrid cloud also poses some challenges, such as compatibility, integration, and governance issues.
- **Community cloud**: The cloud infrastructure is shared by several organizations that have similar requirements and objectives, such as a specific industry, region, or community. The cloud infrastructure can be owned, managed, and operated by one or more of the organizations, a third-party service provider, or a combination of both. The cloud services are delivered over a private network or the internet, and are accessible only to the members of the community. Community cloud offers a balance between public and private clouds, as it provides some level of control, security, and cost-effectiveness, but may have less scalability and availability than public cloud.

## Service Models

Service models refer to the types and levels of services that are provided by the cloud to the customers. There are three main types of service models:

- **Software-as-a-Service (SaaS)**: The cloud service provider delivers software applications over the internet, which are accessible by the customers through a web browser or a mobile app. The customers do not have to install, maintain, or update the software, as the cloud service provider takes care of all the infrastructure and platform aspects. The customers only pay for the software usage, usually on a subscription or pay-per-use basis. SaaS offers convenience, accessibility, and compatibility, but may have less customization and integration than other models. Examples of SaaS are Gmail, Netflix, and Salesforce.
- **Platform-as-a-Service (PaaS)**: The cloud service provider delivers a platform over the internet, which enables the customers to develop, run, and manage their own software applications without having to worry about the underlying infrastructure. The customers have control over the software configuration and deployment, but not over the platform maintenance and security. The customers only pay for the platform resources, such as computing, storage, and networking, that they use. PaaS offers flexibility, scalability, and productivity, but may have less portability and interoperability than other models. Examples of PaaS are AWS Elastic Beanstalk, Microsoft Azure App Service, and Google App Engine.
- **Infrastructure-as-a-Service (IaaS)**: The cloud service provider delivers the basic computing infrastructure over the internet, such as servers, storage, networks, and virtualization. The customers have full control over the infrastructure configuration and management, as well as the software installation and operation. The customers only pay for the infrastructure resources, such as CPU, RAM, disk space, and bandwidth, that they consume. IaaS offers the most control, customization, and flexibility, but also the most responsibility and complexity. Examples of IaaS are AWS EC2, Microsoft Azure Virtual Machines, and Google Compute Engine.



# Cyber infrastructure for the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing

- Cyber infrastructure is a collection of information technology systems and software, physical and information assets, processes, and people that enables an organization to efficiently and securely function on cyber space.
- Cloud computing is the delivery of computing services—including servers, storage, databases, networking, software, analytics, and intelligence—over the Internet (“the cloud”) to offer faster innovation, flexible resources, and economies of scale.
- Cloud computing is a form of cyber infrastructure that provides on-demand access, via the internet, to computing resources hosted at a remote data center managed by a cloud service provider (or CSP).
- Cloud computing eliminates the need for enterprises to procure, configure, or manage resources themselves, and they only pay for what they use.
- Cloud computing has the following characteristics:
  - Self-service provisioning: Users can request and access resources without human intervention from the CSP.
  - Broad network access: Resources are available over the internet and can be accessed from any device and location.
  - Resource pooling: Resources are shared among multiple users and dynamically allocated according to demand.
  - Rapid elasticity: Resources can be scaled up or down quickly and automatically to meet changing needs.
  - Measured service: Resources are monitored and measured by the CSP and users are charged accordingly.
- There are three primary types of cloud deployments:
  - Public cloud: Resources are owned and operated by a third-party CSP and shared among multiple users over the internet. Examples: Microsoft Azure, Google Cloud, Amazon Web Services.
  - Private cloud: Resources are owned and operated by a single organization and used exclusively by its members over a private network. Examples: On-premise data centers, private cloud providers.
  - Hybrid cloud: Resources are distributed across public and private clouds and connected by a common platform or technology. Examples: Hybrid cloud providers, cloud brokers, cloud integrators.
- There are three main categories of cloud computing services:
  - Infrastructure as a service (IaaS): The CSP provides the basic computing resources, such as servers, storage, and networks, and the user can install and run any software on them. Examples: Microsoft Azure, Google Compute Engine, Amazon Elastic Compute Cloud.
  - Platform as a service (PaaS): The CSP provides the computing resources as well as the software platform, such as operating system, database, and development tools, and the user can create and deploy applications on them. Examples: Microsoft Azure App Service, Google App Engine, Amazon Elastic Beanstalk.
  - Software as a service (SaaS): The CSP provides the computing resources as well as the software application, such as email, office suite, or CRM, and the user can access them via a web browser or a mobile app. Examples: Microsoft Office 365, Google Workspace, Salesforce.



# Service Oriented Architecture

Service Oriented Architecture (SOA) is an architectural style that focuses on discrete services instead of a monolithic design. A service is a self-contained unit of functionality that provides a specific business capability or value. Services can communicate with each other using a common language and protocol over a network .

Some of the benefits of SOA are:

- Reusability: Services can be reused in different applications and contexts, reducing development time and cost .
- Interoperability: Services can interact with each other across platforms and languages, enabling integration and collaboration .
- Scalability: Services can be scaled up or down independently, improving performance and reliability .
- Agility: Services can be modified or replaced easily, allowing for faster and more flexible changes .

Some of the challenges of SOA are:

- Complexity: Services can introduce additional layers of abstraction and coordination, increasing the difficulty of design and management .
- Security: Services can expose sensitive data and functionality to external parties, requiring proper authentication and encryption .
- Governance: Services can have different owners and stakeholders, requiring clear policies and standards for quality and compliance .

SOA is related to the concept of cloud computing, which is the delivery of computing resources and services over the internet. Cloud computing can leverage SOA to provide scalable, interoperable, and reusable services to users and applications. Some of the common types of cloud services are:

- Infrastructure as a Service (IaaS): Provides access to low-level computing resources such as servers, storage, and networks.
- Platform as a Service (PaaS): Provides access to high-level computing resources such as databases, frameworks, and tools.
- Software as a Service (SaaS): Provides access to ready-made software applications such as email, CRM, and ERP.

SOA is not a specific technology or standard, but rather a design philosophy and a set of best practices . Some of the common technologies and standards that support SOA are:

- Web services: A type of service that uses web protocols and formats such as HTTP, XML, SOAP, and WSDL .
- RESTful services: A type of service that uses web protocols and formats such as HTTP, JSON, and URIs .
- Service bus: A software component that mediates and routes messages between services .
- Service registry: A software component that stores and publishes information about services .
- Service orchestration: A software component that coordinates and controls the execution of services .
- Service choreography: A software component that defines the interactions and dependencies between services .



# Cloud Computing Components

Cloud computing is the delivery of computing services over the internet, such as servers, storage, databases, networking, software, analytics, and intelligence. Cloud computing architecture refers to the components and subcomponents required for cloud computing. These components typically consist of a front end platform, a back end platform, a cloud based delivery, and a network. Here are some important components of cloud computing architecture:

- **Client Infrastructure**: Client infrastructure is a front-end component that provides a graphical user interface (GUI) to the users. It can be any device that can access the cloud services, such as a desktop, laptop, tablet, smartphone, or thin client. The client infrastructure communicates with the cloud service provider through a web browser or a dedicated application.

- **Application**: The application can be any software or platform that a client wants to access. It can be a web application, a mobile application, a cloud-native application, or a cloud-based service. The application runs on the cloud servers and is delivered to the client infrastructure through the internet.

- **Service**: The service component manages which type of service the client can access according to their requirements. There are three types of cloud computing service models: infrastructure as a service (IaaS), platform as a service (PaaS), and software as a service (SaaS). IaaS offers compute and storage services, PaaS offers a develop-and-deploy environment to build cloud applications, and SaaS delivers applications as services.

- **Runtime Cloud**: Runtime cloud is the component that executes the application code and provides the runtime environment for the application. It can be a virtual machine, a container, a serverless function, or a microservice. The runtime cloud is managed by the cloud service provider and scales up or down according to the demand.

- **Storage**: Storage is the component that provides persistent and scalable data storage for the application. It can be a file system, a database, a data warehouse, a data lake, or a blob storage. The storage component is also managed by the cloud service provider and offers various options for data security, backup, and recovery.

- **Infrastructure**: Infrastructure is the component that provides the physical and virtual resources for the cloud computing system. It includes the servers, the network, the power supply, the cooling system, and the security devices. The infrastructure component is usually located in a data center or a server farm and is shared by multiple cloud service providers and clients.

- **Management**: Management is the component that monitors and controls the cloud computing system. It includes the tools and processes for provisioning, configuration, orchestration, automation, performance, availability, security, and billing of the cloud services. The management component can be accessed by the cloud service provider and the client through a web portal or an application programming interface (API).

- **Security**: Security is the component that protects the cloud computing system from unauthorized access, data breaches, cyberattacks, and other threats. It includes the policies, protocols, encryption, authentication, authorization, firewalls, and antivirus software. The security component is implemented by both the cloud service provider and the client to ensure the confidentiality, integrity, and availability of the cloud services.

- **Internet**: Internet is the component that connects the client infrastructure, the application, the service, the runtime cloud, the storage, the infrastructure, the management, and the security components. It is the medium through which the cloud computing system delivers the cloud services to the users. The internet component can be a public network, a private network, or a hybrid network.



# Infrastructure for Cloud Computing

Cloud computing is the delivery of on-demand computing services over the internet, such as applications, storage, servers, databases, networking, and analytics. Cloud computing enables users to access scalable, flexible, and cost-effective IT resources without investing in physical infrastructure or hardware.

To provide cloud computing services, cloud providers need to have a set of hardware and software elements that constitute the cloud infrastructure. Cloud infrastructure is the collection of the components and elements required to enable cloud computing. Cloud infrastructure consists of the following main components :

- **Compute**: This refers to the servers or virtual machines that provide the processing power for running applications and workloads in the cloud. Compute resources can be provisioned on-demand, scaled up or down, and billed based on usage.
- **Networking**: This refers to the connectivity and communication between the cloud resources, such as routers, switches, firewalls, load balancers, and VPNs. Networking enables data transfer, security, and access control for cloud services.
- **Storage**: This refers to the disks, drives, or databases that store data and files in the cloud. Storage can be persistent or ephemeral, block or object, and local or distributed. Storage can also be replicated, backed up, and encrypted for reliability and security.
- **Virtualization**: This refers to the technology that creates a layer of abstraction between the physical hardware and the software that runs on it. Virtualization enables multiple virtual machines or containers to share the same physical resources, such as CPU, memory, and disk. Virtualization also enables portability, isolation, and automation of cloud resources.

Cloud infrastructure can be deployed in different models, such as public, private, hybrid, or multi-cloud. Public cloud infrastructure is owned and operated by a third-party cloud provider and shared by multiple users over the internet. Private cloud infrastructure is owned and operated by a single organization and used exclusively by its members. Hybrid cloud infrastructure is a combination of public and private cloud infrastructure, connected by a common network. Multi-cloud infrastructure is a use of multiple public cloud providers for different purposes or applications.

Cloud infrastructure can also be delivered in different service models, such as infrastructure as a service (IaaS), platform as a service (PaaS), serverless, or software as a service (SaaS). IaaS is the most basic level of cloud service, where users can rent compute, storage, and networking resources and manage them themselves. PaaS is a level above IaaS, where users can also access development tools, middleware, and operating systems to create and deploy applications. Serverless is a level above PaaS, where users can run code without worrying about the underlying infrastructure, as it is managed by the cloud provider. SaaS is the highest level of cloud service, where users can access ready-made applications that run on the cloud provider's infrastructure.

Cloud infrastructure management is the process of overseeing, monitoring, and optimizing the cloud infrastructure components and services. Cloud infrastructure management involves tasks such as provisioning, configuration, scaling, security, backup, recovery, and performance tuning. Cloud infrastructure management can be done by the cloud provider, the cloud user, or a third-party service provider, depending on the cloud deployment and service model. Cloud infrastructure management can also be automated using tools, scripts, or APIs. Cloud infrastructure management aims to ensure the availability, reliability, and efficiency of cloud computing services.



# Storage for Cloud Computing

Storage for cloud computing is a mode of computer data storage in which digital data is stored on servers in off-site locations. The servers are maintained by a third-party provider who is responsible for hosting, managing, and securing data stored on its infrastructure.

There are three main types of storage for cloud computing:

- **Object storage**: This type of storage is suitable for applications that are developed inside the cloud and require scalability and metadata. Object storage stores data as objects, which consist of data and associated metadata. Each object has a unique identifier that allows it to be accessed through a RESTful API. Object storage is ideal for storing unstructured data, such as images, videos, documents, etc.
- **File storage**: This type of storage is suitable for applications that need to access a shared file system. File storage stores data as files, which are organized in a hierarchical structure of folders and subfolders. File storage supports common file operations, such as create, read, update, and delete. File storage is ideal for storing structured or semi-structured data, such as spreadsheets, databases, etc.
- **Block storage**: This type of storage is suitable for applications that need to access data at a low level. Block storage stores data as blocks, which are fixed-sized chunks of data. Each block has a unique address that allows it to be accessed through a block-level protocol, such as SCSI or iSCSI. Block storage is ideal for storing high-performance data, such as operating systems, applications, etc.

Some of the benefits of storage for cloud computing are :

- **Scalability**: Storage for cloud computing can scale up or down according to the demand of the applications. Users can provision or deprovision storage resources as needed, without worrying about the physical limitations of the storage devices.
- **Cost-effectiveness**: Storage for cloud computing can reduce the cost of data storage by eliminating the need for purchasing, maintaining, and upgrading storage hardware and software. Users only pay for the amount of storage they use, and can benefit from the economies of scale of the cloud provider.
- **Availability**: Storage for cloud computing can ensure the availability of data by replicating it across multiple servers and locations. This can prevent data loss or corruption due to hardware failures, natural disasters, or human errors. Users can also access their data from anywhere and anytime, as long as they have an internet connection.
- **Security**: Storage for cloud computing can protect the data from unauthorized access or modification by encrypting it at rest and in transit. The cloud provider also implements various security measures, such as firewalls, access control, authentication, and auditing, to safeguard the data stored on its infrastructure. Users can also choose the level of security they want for their data, depending on their compliance and regulatory requirements.



# Platform for the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing

- Cloud computing is the on-demand availability of computer system resources, especially data storage and computing power, without direct active management by the user.
- Cloud computing can cover a broad range of tasks, from high powered computing to more mundane ones. It can be used for specialized tasks, as well as those that can be carried out on a standard home computer.
- The benefits of cloud computing include convenience, scalability, flexibility, cost-efficiency, and reliability .
- High-performance computing (HPC), also called "big compute", uses a large number of CPU or GPU-based computers to solve complex mathematical tasks.
- HPC is used by many industries to solve some of their most difficult problems, such as genomics, oil and gas simulations, finance, semiconductor design, engineering, and weather modeling.
- HPC requires high-speed networks, large-scale storage systems, specialized software, and powerful hardware to achieve high performance and efficiency.
- Cloud computing and HPC can be integrated to provide a flexible and powerful HPC foundation. Cloud HPC solutions offer advantages such as easy deployment, on-demand scalability, pay-per-use pricing, and access to the latest technology .
- Some of the cloud HPC platforms available are Azure HPC, Google Cloud HPC, AWS HPC, and IBM Cloud HPC .
- Cloud HPC platforms provide various features and services to support HPC applications, such as virtual machines, containers, clusters, orchestration, storage, networking, security, and analytics .
- Cloud HPC platforms also offer optimized application services for specific domains, such as genomics, artificial intelligence, machine learning, and quantum computing .



# Application for the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing

- To: Professor John Smith
- From: Student A
- Date: 16 March 2023
- Subject: Request for the notes of the Unit 5 - Overview of Cloud Computing

Dear Professor Smith,

I am writing to request the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing. I am a student enrolled in your course HPC101 this semester.

I was unable to attend the lecture on 15 March 2023 due to a medical emergency. I have attached a copy of my doctor's certificate as proof of my absence. I apologize for any inconvenience this may have caused.

I am very interested in learning about the concepts and applications of cloud computing, as I believe they are essential for my future career in the field of high performance computing. I have been following the course materials and assignments diligently, and I have achieved good grades so far.

I would appreciate it if you could kindly share the notes of the Unit 5 - Overview of Cloud Computing with me, either by email or by uploading them on the course website. This would help me to catch up with the missed lecture and prepare for the upcoming quiz and project.

Thank you for your consideration and understanding. I look forward to hearing from you soon.

Sincerely,
Student A



# Services for Cloud Computing

Cloud computing is the delivery of different services through the Internet, such as data storage, servers, databases, networking, software, analytics, and intelligence. Cloud computing services provide users with a series of functions, including:

- Email
- Storage, backup, and data retrieval
- Creating and testing apps
- Analyzing data
- Streaming audio and video
- Delivering software on demand
- Embedding intelligence

There are different types of cloud computing services, depending on the level of abstraction and the service model. The main types are:

- **Infrastructure as a Service (IaaS)**: This is the most basic and flexible type of cloud service, where users rent IT infrastructure, such as servers, virtual machines, storage, networks, and operating systems, from a cloud provider on a pay-as-you-go basis. Examples of IaaS providers are Microsoft Azure, Amazon Web Services, Google Cloud, and IBM Cloud.
- **Platform as a Service (PaaS)**: This type of cloud service provides users with a platform to develop, run, and manage applications without having to deal with the underlying infrastructure. PaaS offers tools and services for coding, testing, deploying, managing, and updating applications. Examples of PaaS providers are Google App Engine, Microsoft Azure App Service, AWS Elastic Beanstalk, and Oracle Cloud Platform.
- **Software as a Service (SaaS)**: This type of cloud service delivers software applications over the Internet, usually on a subscription or pay-per-use basis. Users can access the software from any device, without having to install or maintain it. SaaS providers manage the infrastructure, security, updates, and backups of the software. Examples of SaaS providers are Google Workspace, Microsoft 365, Salesforce, and Dropbox.
- **Function as a Service (FaaS)**: This type of cloud service allows users to run individual functions or pieces of code in response to events, without having to provision or manage servers. FaaS is a form of serverless computing, where the cloud provider manages the scaling and availability of the functions. Examples of FaaS providers are AWS Lambda, Azure Functions, Google Cloud Functions, and IBM Cloud Functions.

Some of the benefits of using cloud computing services are:

- Cost savings: Users can avoid the upfront cost and complexity of owning and maintaining their own IT infrastructure, and only pay for what they use.
- Scalability: Users can easily scale up or down their cloud resources according to their needs, without having to worry about capacity planning or hardware limitations.
- Performance: Users can access high-performance computing resources from anywhere in the world, and benefit from the constant upgrades and innovations of the cloud providers.
- Reliability: Users can rely on the cloud providers to ensure the availability and redundancy of their data and applications, and to provide backup and disaster recovery solutions.
- Security: Users can benefit from the expertise and best practices of the cloud providers to protect their data and applications from cyberattacks, and to comply with the relevant regulations and standards.

Some of the challenges of using cloud computing services are:

- Privacy and compliance: Users may have to entrust their sensitive data and applications to a third-party provider, and may face legal and regulatory issues depending on the location and jurisdiction of the cloud provider and the user.
- Vendor lock-in: Users may face difficulties in migrating their data and applications from one cloud provider to another, or back to their own infrastructure, due to the differences in the features, standards, and formats of the cloud services.
- Security and control: Users may have to share the responsibility of securing their data and applications with the cloud provider, and may have less visibility and control over the underlying infrastructure and processes of the cloud services.
- Technical issues and downtime: Users may experience performance issues, service disruptions, or data loss due to the technical failures, human errors, or malicious attacks on the cloud provider or the Internet connection.



# Clients for the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing

- A cloud client is a hardware device or software used to access a cloud service .
- A cloud service is a type of computing service that is delivered over the internet and provides scalable and on-demand resources such as computing cycles, data storage, applications, and platforms .
- A cloud client can be classified into three types based on the level of functionality and dependency on the cloud service:
  - Thick client: A thick client is a device or software that has its own operating system, applications, and data, and can function independently of the cloud service. A thick client can use the cloud service for additional features or backup, but does not rely on it for core functionality. Examples of thick clients are personal computers, laptops, and smartphones.
  - Thin client: A thin client is a device or software that has minimal functionality and relies on the cloud service for most of its operations. A thin client usually has a basic operating system, a web browser, and a network connection, and uses the cloud service to access applications and data. Examples of thin clients are Chromebooks, tablets, and smart TVs.
  - Zero client: A zero client is a device or software that has no functionality and relies entirely on the cloud service for all its operations. A zero client has no operating system, no local storage, and no applications, and uses the cloud service to access a virtual desktop environment. Examples of zero clients are dumb terminals, thin clients with no operating system, and virtual machines.
- The advantages of using cloud clients are:
  - Reduced cost: Cloud clients can reduce the cost of hardware, software, maintenance, and energy consumption, as they rely on the cloud service for most of their functionality and resources.
  - Increased security: Cloud clients can reduce the risk of data loss, theft, or corruption, as they store and process data on the cloud service, which can provide better encryption, backup, and recovery options.
  - Improved performance: Cloud clients can improve the performance and scalability of applications and data, as they leverage the cloud service's computing power, storage capacity, and network bandwidth.
  - Enhanced mobility: Cloud clients can enable users to access applications and data from anywhere and any device, as they use the cloud service's internet connection and web interface.



# Cloud Computing Architecture

Cloud computing architecture is the design and structure of the components and subcomponents required for cloud computing. Cloud computing is the delivery of computing services over the internet, such as servers, storage, databases, networking, software, analytics, and intelligence.

## Components of Cloud Computing Architecture

Cloud computing architecture consists of two main components: the front end and the back end.

- The front end is the part of the cloud that users interact with, such as applications, web browsers, or mobile devices. The front end communicates with the back end through a network, usually the internet.
- The back end is the part of the cloud that provides the computing resources and services, such as servers, storage, databases, and software. The back end is managed by a cloud provider, who is responsible for the security, scalability, and availability of the cloud.

## Types of Cloud Computing Services

Cloud computing services can be classified into four broad categories, based on the level of abstraction and control they offer to the users. These categories are:

- Infrastructure as a service (IaaS): This is the most basic and flexible type of cloud service, where the user can rent and manage the infrastructure components, such as servers, storage, and networking, from the cloud provider. The user is responsible for installing and maintaining the operating system, applications, and middleware on the rented infrastructure.
- Platform as a service (PaaS): This is a type of cloud service where the user can develop and deploy applications using the tools and frameworks provided by the cloud provider. The user does not have to manage the underlying infrastructure, but only the application code and configuration. The cloud provider handles the scalability, security, and availability of the platform and the applications.
- Serverless: This is a type of cloud service where the user can run code without provisioning or managing any servers. The code is executed by the cloud provider in response to events or triggers, such as HTTP requests, database changes, or messages. The user only pays for the execution time and resources used by the code, not for the idle servers. The cloud provider handles the scalability, security, and availability of the code and the servers.
- Software as a service (SaaS): This is the most common and user-friendly type of cloud service, where the user can access and use software applications that are hosted and managed by the cloud provider. The user does not have to install, update, or maintain the software, but only pays for the subscription or usage of the service. The cloud provider handles the scalability, security, and availability of the software and the data.

## Benefits of Cloud Computing Architecture

Cloud computing architecture offers several benefits to the users and the cloud providers, such as:

- Cost efficiency: Cloud computing reduces the capital and operational costs of owning and maintaining IT infrastructure and software. Users only pay for the resources and services they use, and cloud providers can achieve economies of scale by sharing the infrastructure and software among multiple users.
- Scalability: Cloud computing enables users to scale up or down the computing resources and services according to their needs and demands. Cloud providers can dynamically allocate and deallocate the resources and services based on the usage and load of the cloud.
- Availability: Cloud computing ensures that the computing resources and services are always available and accessible to the users, regardless of their location and device. Cloud providers can use redundancy and backup mechanisms to prevent or recover from failures and disasters that may affect the cloud.
- Security: Cloud computing provides various levels of security and privacy to the users and the cloud providers, such as encryption, authentication, authorization, and auditing. Cloud providers can use firewalls, antivirus, and intrusion detection systems to protect the cloud from external threats and attacks. Users can also use their own security measures to protect their data and applications in the cloud.

