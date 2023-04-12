

## Unit 1 - Overview of Grid Computing Technology

- Grid computing is a form of distributed computing that involves coordinating and sharing computing resources across multiple administrative domains.
- Grid computing enables the virtualization of heterogeneous and geographically dispersed resources such as processors, storage, networks, data, and software, and provides mechanisms for integrating, managing, and accessing them as a unified system.
- Grid computing can support a wide range of applications, such as scientific simulations, data analysis, e-science, e-business, e-government, and e-learning, by providing high-performance, high-throughput, high-availability, and high-reliability services.
- Grid computing can be classified into different types based on the level of resource sharing, the degree of coupling, the nature of coordination, and the quality of service. Some common types are:
  - Computational grid: A grid that provides access to a large number of CPUs for executing compute-intensive tasks.
  - Data grid: A grid that provides access to a large amount of distributed data for data-intensive tasks.
  - Service grid: A grid that provides access to a variety of services, such as web services, databases, and software components, for service-oriented tasks.
  - Knowledge grid: A grid that provides access to a large amount of distributed knowledge, such as ontologies, metadata, and semantic annotations, for knowledge-intensive tasks.
- Grid computing can be implemented using different architectures, protocols, standards, and middleware. Some common components are:
  - Grid architecture: A layered model that defines the functionality and interfaces of the grid components, such as the fabric layer, the connectivity layer, the resource layer, the collective layer, and the application layer.
  - Grid protocol: A set of rules and formats that govern the communication and interaction among the grid components, such as the GridFTP, the GridRPC, the OGSA, and the WSRF.
  - Grid standard: A specification that defines the common requirements and characteristics of the grid components, such as the GGF, the OGF, the OGSI, and the OASIS.
  - Grid middleware: A software layer that provides the core services and functionalities of the grid, such as the Globus Toolkit, the UNICORE, the Condor, and the gLite.



### History of Grid Computing

- Grid computing is a form of distributed computing that allows multiple computers to share resources and work together on a common task.
- The term grid computing originated in the early 1990s as a metaphor for making computer power as easy to access as an electric power grid.
- The idea was inspired by the success of parallel computing and supercomputers in the 1980s and 1990s, which enabled high-performance computing for scientific and engineering applications.
- However, parallel computing and supercomputers were expensive, scarce, and difficult to use, and often required specialized hardware and software.
- Grid computing aimed to overcome these limitations by using the existing network infrastructure and heterogeneous resources, such as personal computers, servers, clusters, and storage devices, to create a virtual supercomputer.
- Grid computing also aimed to support a wider range of applications, such as data-intensive, collaborative, and interactive ones, that could benefit from the aggregation and sharing of resources across multiple domains and organizations.
- One of the pioneers of grid computing was the Globus project, which started in 1995 by Ian Foster, Carl Kesselman, and Steve Tuecke at Argonne National Laboratory and the University of Southern California.
- The Globus project developed the Globus Toolkit, a set of open-source software components that provided the basic services and protocols for building grid applications and infrastructures.
- The Globus Toolkit included services for resource discovery, allocation, management, security, communication, data transfer, and monitoring.
- The Globus Toolkit became the de facto standard for grid computing and was adopted by many projects and communities, such as the Earth System Grid, the TeraGrid, the Open Science Grid, and the LHC Computing Grid.
- Grid computing also received support from various initiatives and organizations, such as the Grid Forum, the Global Grid Forum, and the Open Grid Forum, which aimed to foster the development and adoption of grid standards, best practices, and interoperability.
- Grid computing also attracted the interest of industry and commercial sectors, such as IBM, HP, Oracle, and Microsoft, which developed their own grid products and solutions, such as the IBM Grid Computing, the HP Utility Data Center, the Oracle Grid Engine, and the Microsoft Azure.
- Grid computing also enabled the emergence of new paradigms and models, such as volunteer computing, peer-to-peer computing, cloud computing, and edge computing, which leveraged the concepts and technologies of grid computing to provide more scalable, flexible, and cost-effective computing services.



### High Performance Computing for the notes of the Unit 1 - Overview of Grid Computing Technology

- High performance computing (HPC) is the use of specialized hardware and software to run computationally intensive tasks at high speed and efficiency.
- HPC systems typically consist of multiple processors, memory, storage, and network devices that work together to execute parallel or distributed applications.
- HPC applications can range from scientific simulations, data analysis, machine learning, to digital media, gaming, and web services.
- Grid computing is a form of distributed computing that uses a network of heterogeneous and geographically dispersed computers to achieve a common goal.
- Grid computing differs from conventional HPC systems such as cluster computing in that grid computers have each node set to perform a different task or application, rather than the same task or application.
- Grid computing enables the sharing of resources, data, and services across multiple organizations and domains, and can support large-scale, dynamic, and collaborative workflows.
- Grid computing can be classified into different types based on the level of coordination, resource management, and security, such as computational grids, data grids, service grids, and knowledge grids.
- Grid computing can also be categorized based on the application domain, such as scientific grids, enterprise grids, desktop grids, and cloud grids.
- Grid computing faces several challenges and opportunities in terms of scalability, interoperability, reliability, security, and usability.
- Grid computing can benefit from the advances in cloud computing, edge computing, and artificial intelligence, as well as the development of standards, protocols, and middleware.



### Cluster Computing

- Cluster computing is a form of parallel computing that involves connecting multiple computers (called nodes) on a network and using them as a single system for high-performance tasks  .
- Cluster computing differs from grid computing in that the nodes in a cluster are dedicated to the same task and are controlled by a central software , while the nodes in a grid are distributed across different administrative domains and can perform different tasks.
- Cluster computing can provide benefits such as faster computational speed, enhanced data integrity, increased availability, load balancing, and scalability  .
- Cluster computing can be classified into different types based on the architecture, topology, and communication of the nodes, such as:
  - Beowulf cluster: A cluster of commodity hardware running Linux or other open-source operating systems, connected by Ethernet or other standard network protocols .
  - Symmetric multiprocessing (SMP) cluster: A cluster of nodes that share memory and processors, and can access any resource in the system .
  - Massively parallel processing (MPP) cluster: A cluster of nodes that have their own memory and processors, and communicate through a high-speed interconnect .
  - High-availability (HA) cluster: A cluster of nodes that provide redundancy and fault tolerance, and can switch over to a backup node in case of a failure .
  - Load-balancing cluster: A cluster of nodes that distribute the workload among them, and can handle fluctuations in demand and performance .
- Cluster computing can be used for various applications, such as scientific computing, data analysis, web hosting, database management, and distributed processing  .



### Peer-to-Peer Computing

- Peer-to-peer (P2P) computing is a distributed application architecture that partitions tasks or workloads between peers.
- Peers are equally privileged, equipotent participants in the network. They are said to form a peer-to-peer network of nodes.
- In a P2P network, each computer acts as both a server and a client, supplying and receiving files, with bandwidth and processing distributed among all members of the network.
- Such a decentralized network uses resources more efficiently than a traditional network and is less vulnerable to systemic failure.
- P2P computing has many applications, such as file sharing, distributed computing, collaborative work, content delivery, social networking, and blockchain.
- P2P computing also has some challenges, such as security, privacy, scalability, reliability, and legal issues .
- P2P computing is one of the technologies that enable grid computing, which is a form of distributed computing that involves coordinating and sharing computing resources across multiple administrative domains.



### Internet Computing for the notes of the Unit 1 - Overview of Grid Computing Technology in the subject of High Performance Computing

- Internet computing is the use of the internet as a platform for distributed computing, where applications and data are accessed and processed over the network, rather than on a single machine or location.
- Grid computing is a form of internet computing that involves the coordinated use of multiple machines or resources across different locations, connected by a common bus or network, to perform large-scale or complex tasks that require high performance computing (HPC).
- HPC is the use of specialized hardware and software to achieve fast and efficient processing of large amounts of data or complex calculations, often involving parallelism or concurrency.
- Grid computing can be seen as a type of HPC that leverages the power of multiple machines or resources, rather than relying on a single supercomputer or cluster.
- Grid computing can also be seen as a type of distributed computing, where a virtual supercomputer is composed of machines or resources that are geographically dispersed and heterogeneous, rather than homogeneous and centralized.
- Grid computing can provide several benefits, such as:
  - Scalability: the ability to add or remove machines or resources as needed, without affecting the performance or functionality of the grid.
  - Fault-tolerance: the ability to handle failures or errors of individual machines or resources, without affecting the overall operation of the grid.
  - Load-balancing: the ability to distribute the workload or tasks among the available machines or resources, to optimize the utilization and efficiency of the grid.
  - Cost-effectiveness: the ability to reduce the cost of acquiring, maintaining, and operating a single supercomputer or cluster, by using existing or shared machines or resources.
- Grid computing can also pose some challenges, such as:
  - Security: the need to ensure the confidentiality, integrity, and availability of the data and applications that are accessed and processed over the grid, as well as the authentication and authorization of the users and machines or resources that participate in the grid.
  - Interoperability: the need to ensure the compatibility and communication of the different machines or resources that are part of the grid, as well as the standards and protocols that are used to coordinate and manage the grid.
  - Performance: the need to ensure the quality and efficiency of the processing and communication that take place over the grid, as well as the trade-offs and overheads that may arise from the distributed and heterogeneous nature of the grid.
  - Management: the need to ensure the coordination and control of the machines or resources that are part of the grid, as well as the scheduling and allocation of the tasks and resources that are involved in the grid.



### Grid Computing Model and Protocols

Grid computing is a distributed architecture of multiple computers connected by networks to accomplish a joint task. These tasks are compute-intensive and difficult for a single machine to handle. Several machines on a network collaborate under a common protocol and work as a single virtual supercomputer to get complex tasks done.

Grid computing is enabled via an open set of standards and protocols such as open grid services architecture (OGSA) that allow communication across heterogeneous systems and environments that are geographically dispersed.

A grid computing model consists of five layers :

- The Fabric Layer: This layer includes the protocols and interfaces that provide access to the resources that are being shared such as compute resources, data resources, network resources, etc.
- The Connectivity Layer: This layer defines core protocols required for grid-specific network transactions such as security, authentication, authorization, resource discovery, etc.
- The Resource Layer: This layer defines protocols for the publication, monitoring, and management of resources on the grid such as CPU, memory, disk, etc.
- The Collective Layer: This layer defines protocols for the coordination and interaction of multiple resources on the grid such as scheduling, load balancing, data replication, etc.
- The Application Layer: This layer defines protocols for the development and execution of applications on the grid such as workflow, service composition, etc.

Some of the core grid protocols that are used in implementing various activities and services for global grid deployment are:

- Grid Security Infrastructure (GSI): This protocol provides secure authentication and communication among grid entities using public key cryptography and X.509 certificates.
- Grid Resource Allocation and Management (GRAM): This protocol provides a uniform interface for requesting, accessing, monitoring, and controlling remote resources on the grid.
- Grid Resource Information Service (GRIS): This protocol provides a directory service for publishing and querying information about grid resources and services.
- Grid File Transfer Protocol (GridFTP): This protocol provides a high-performance and reliable data transfer mechanism on the grid using parallel TCP streams and partial file transfers.
- Grid Monitoring Architecture (GMA): This protocol provides a framework for collecting, storing, and disseminating performance and status information about grid resources and services.
- Grid Service Specification (GSS): This protocol defines a common set of interfaces and behaviors for grid services based on the web service standards such as SOAP, WSDL, and UDDI.



### Types of Grids for the notes of the Unit 1 - Overview of Grid Computing Technology in the subject of High Performance Computing

- Grid computing is a distributed computing paradigm that allows multiple computers to share resources and solve complex problems in a coordinated manner.
- Grid computing networks consist of three machine types: control node/server, provider/grid node, and user/client.
- Grid computing can be classified into different types based on the purpose, architecture, and functionality of the grid. Some of the common types are:

  - Computational grid: This type of grid acts as a mediator of many computers in a given network to solve one single problem at a time. The problem is divided into smaller subtasks and distributed among the grid nodes, which perform parallel processing and return the results to the control node. Computational grids are useful for applications that require high computational power, such as scientific simulations, weather forecasting, and cryptography.
  - Data grid: The grid that deals with the sharing and managing the distributed data in a controlled manner is termed as a data grid. Data grids provide efficient data access, replication, caching, and security mechanisms to handle large volumes of data across multiple locations. Data grids are useful for applications that require data-intensive processing, such as data mining, bioinformatics, and e-commerce.
  - Collaborative grid: Such types of grids help in solving collective problems that involve human interaction and collaboration. Collaborative grids provide tools and services for communication, coordination, and knowledge sharing among the grid users. Collaborative grids are useful for applications that require social and organizational aspects, such as e-learning, e-health, and e-government.
  - Service grid: The grid that provides access to various services and resources as a utility is called a service grid. Service grids use standard protocols and interfaces to enable interoperability and integration among heterogeneous grid components. Service grids are useful for applications that require dynamic and on-demand provisioning of services, such as web services, cloud computing, and grid computing itself.
  - In-memory data grid: A specific type of data grid is an in-memory data grid (IMDG) which, as the name implies, runs processing in the computers’ main memory, e.g., random-access memory (RAM). The advantage is that the data is stored in memory across all the computers in the grid, so data access is extremely fast. IMDGs are useful for applications that require low-latency and high-performance processing, such as real-time analytics, online gaming, and financial transactions.

- Grid computing can also be classified based on the grid topology or structure, such as hierarchical, centralized, decentralized, or hybrid grids.
- Grid computing can also be classified based on the grid domain or scope, such as local, regional, national, or global grids.



### Desktop Grids

- Desktop grids are a type of distributed computing environment that make use of desktop computers connected via the Internet.
- Desktop grids are not used only for voluntary computing projects, but also for enterprise grids, where the desktop computers belong to a single organization and are connected via a non-dedicated network.
- Desktop grids can provide a large amount of computing power and storage capacity by harnessing the idle resources of desktop computers.
- Desktop grids can be classified into two categories: public desktop grids and private desktop grids.
  - Public desktop grids are open to anyone who wants to join and contribute their computing resources to a common goal, such as scientific research or social causes. Examples of public desktop grids are BOINC, SETI@home, Folding@home, etc.
  - Private desktop grids are restricted to a specific group of users or organizations that share a common interest or objective, such as business, education, or government. Examples of private desktop grids are Condor, XtremWeb, OurGrid, etc.
- Desktop grids face several challenges, such as heterogeneity, scalability, security, fault tolerance, and incentive mechanisms.
  - Heterogeneity refers to the diversity of hardware, software, and network characteristics of the desktop computers that participate in the grid.
  - Scalability refers to the ability of the grid to handle a large number of desktop computers and tasks without compromising the performance and quality of service.
  - Security refers to the protection of the grid from malicious attacks, such as data theft, sabotage, or denial of service.
  - Fault tolerance refers to the ability of the grid to cope with failures, such as network disconnections, power outages, or hardware malfunctions.
  - Incentive mechanisms refer to the strategies to motivate and reward the desktop computer owners for their participation and contribution to the grid.



### Cluster Grids

- Cluster grids are a type of grid computing that involves connecting a group of computers with similar hardware and software characteristics into a cluster.
- A cluster is a collection of computers that are connected by a local area network (LAN) and work together as a single system.
- Cluster grids are tightly coupled, meaning that the computers in the cluster have high communication and coordination among them.
- Cluster grids are usually used for high-performance computing applications that require a large amount of processing power and data sharing.
- Cluster grids can be homogeneous or heterogeneous, depending on whether the computers in the cluster have the same or different operating systems and hardware configurations.
- Cluster grids can be classified into different types based on their architecture, such as master-slave, peer-to-peer, or hybrid clusters.
- Cluster grids have some advantages over other types of grid computing, such as higher reliability, scalability, and efficiency.
- Cluster grids also have some challenges, such as load balancing, fault tolerance, security, and resource management.



### Data Grids

- A data grid is a set of structured services that gives individuals or groups of users the ability to access, modify and transfer extremely large amounts of geographically distributed data for research purposes .
- Data grids are often used in scientific domains that require collaborative analysis of large-scale data sets, such as high-energy physics, astronomy, bioinformatics, etc.
- Data grids provide various functionalities, such as:
  - Data discovery: locating and identifying data sources that match certain criteria.
  - Data access: retrieving data from remote sources using standard protocols and formats.
  - Data replication: creating and maintaining copies of data across different locations for performance, reliability or availability reasons.
  - Data caching: storing frequently accessed data in local or intermediate storage for faster access.
  - Data migration: moving data from one location to another based on policies or user requests.
  - Data synchronization: ensuring consistency and coherence of data across different replicas or caches.
  - Data security: protecting data from unauthorized access, modification or disclosure.
  - Data management: organizing, cataloging, annotating and curating data.
- Data grids rely on various components, such as:
  - Data sources: the original providers of data, such as databases, files, sensors, etc.
  - Data storage: the physical or logical devices that store data, such as disks, tapes, clouds, etc.
  - Data servers: the software entities that offer data services, such as data access, replication, caching, migration, etc.
  - Data clients: the software entities that consume data services, such as applications, portals, workflows, etc.
  - Data brokers: the software entities that mediate between data clients and data servers, such as data discovery, data security, data management, etc.
- Data grids can be classified into different types, such as:
  - Replica-based data grids: data grids that focus on creating and maintaining multiple copies of data across different locations for performance, reliability or availability reasons.
  - Computation-based data grids: data grids that focus on providing data-intensive computing capabilities, such as data analysis, data mining, data visualization, etc.
  - Knowledge-based data grids: data grids that focus on extracting and sharing knowledge from data, such as data semantics, data provenance, data quality, etc.
  - Service-based data grids: data grids that focus on exposing data as services, such as data as a service (DaaS), data federation, data integration, etc.



### High-Performance Grids

- A high-performance grid is a software component that can display and manipulate large data sets efficiently and responsively.
- A high-performance grid can have various features, such as sorting, filtering, grouping, editing, paging, scrolling, exporting, etc.
- A high-performance grid can be implemented using different technologies, such as JavaScript, Java, .NET, etc.
- A high-performance grid can be used for various applications, such as data analysis, reporting, dashboarding, business intelligence, etc.
- A high-performance grid can be evaluated based on different criteria, such as initial page load time, dynamic filtering speed, scrolling smoothness, memory usage, etc .
- A high-performance grid can benefit from various optimization techniques, such as virtualization, caching, indexing, batching, etc .
- A high-performance grid can face various challenges, such as data quality, security, scalability, compatibility, etc .
- A high-performance grid can be integrated with other components, such as charts, forms, menus, toolbars, etc .
- A high-performance grid can be customized and styled according to the user's preferences and requirements .



### Applications and Architectures of High Performance Grids

- A grid is a distributed system that enables the sharing and coordinated use of heterogeneous resources across multiple administrative domains .
- A high performance grid is a grid that can harness the power of an arbitrarily large collection of computing resources to meet the needs of compute intensive applications such as finite element model (FEM) simulations, scientific workflows, data analysis, etc .
- Some of the applications of high performance grids are:
  - Computational science and engineering: solving complex problems that require large-scale parallelism, such as climate modeling, fluid dynamics, molecular dynamics, etc.
  - Data-intensive computing: processing and analyzing massive amounts of data, such as genomics, astronomy, social networks, etc.
  - Collaborative computing: enabling distributed teams to work together on common tasks, such as telemedicine, virtual reality, e-learning, etc.
  - Service-oriented computing: providing on-demand access to various services, such as web services, databases, storage, etc.
- Some of the architectures of high performance grids are:
  - Hierarchical grid: a grid that consists of multiple levels of sub-grids, each with its own resource management and scheduling policies, such as the European DataGrid (EDG) project.
  - Peer-to-peer grid: a grid that is based on the principle of decentralization and self-organization, where each node can act as both a resource provider and a resource consumer, such as the Globus Toolkit.
  - Service-oriented grid: a grid that is based on the concept of service-oriented architecture (SOA), where each resource is exposed as a service that can be discovered, invoked, and composed, such as the Open Grid Services Architecture (OGSA) and the Web Services Resource Framework (WSRF).
  - Cloud-based grid: a grid that leverages the cloud computing paradigm, where resources are dynamically provisioned and released on demand, such as the Amazon Elastic Compute Cloud (EC2) and the Google App Engine.
- Some of the challenges and issues of high performance grids are:
  - Resource heterogeneity: dealing with the diversity and variability of resources in terms of hardware, software, network, etc.
  - Resource availability: coping with the dynamic and unpredictable nature of resources, such as failures, faults, load, etc.
  - Resource discovery: finding and selecting suitable resources for a given application or task.
  - Resource allocation: distributing and scheduling resources among multiple competing applications or tasks.
  - Resource coordination: synchronizing and communicating among resources to achieve a common goal.
  - Resource security: ensuring the confidentiality, integrity, and availability of resources and data.
  - Resource performance: optimizing the efficiency and effectiveness of resources and applications.



### High Performance Application Development Environment

- A high performance application development environment is a set of tools, frameworks, and practices that enable developers to create, test, deploy, and optimize applications that run on high performance computing (HPC) systems, such as clusters, grids, supercomputers, or cloud platforms.
- A high performance application development environment typically consists of the following components  :
  - A development server, where the developers write, debug, and test the code using various programming languages, libraries, and compilers. The development server may also provide performance analysis and profiling tools to help optimize the code for HPC systems.
  - A staging server, where the developers integrate, validate, and verify the application with other components, such as data sources, middleware, or external services. The staging server may also provide tools for configuration management, version control, and continuous integration and delivery.
  - A production server, where the application is deployed and executed on the target HPC system, such as a cluster, grid, supercomputer, or cloud platform. The production server may also provide tools for monitoring, logging, troubleshooting, and scaling the application.
- A high performance application development environment may also support the following features  :
  - Resource elasticity, which allows the application to dynamically adjust the amount of computing resources (such as CPU, memory, disk, or network) it uses based on the workload and demand.
  - Software-defined networking, which allows the application to control and optimize the network configuration and performance, such as routing, load balancing, security, or quality of service.
  - Auto-provisioning, which allows the application to automatically create and destroy the required resources and environments based on the predefined policies and rules.
  - High availability, which allows the application to tolerate and recover from failures, such as hardware faults, network disruptions, or software errors.
  - Scalability, which allows the application to handle increasing or decreasing amounts of data, users, or requests without compromising the performance or quality.
- A high performance application development environment may also follow the DevOps approach, which is a set of practices that aim to improve the collaboration and communication between the development and operations teams, and to automate and streamline the application delivery process. DevOps may involve the use of tools such as GitHub, Jenkins, Docker, Kubernetes, or Azure DevTest Labs.



## Unit 2 - Open Grid Services Architecture

- Open Grid Services Architecture (OGSA) is a set of standards that extends Web services and service-oriented architecture to the grid computing environment .
- Grid computing is the use of a large number of computers, often geographically distributed and heterogeneous, to perform coordinated tasks that require a high level of processing power or data storage.
- OGSA defines a common, open, and extensible set of capabilities and behaviors that address key concerns in grid systems, such as security, resource management, data access, notification, and fault tolerance .
- OGSA uses most of Web service technologies, notably WSDL and SOAP, but it aims to be largely agnostic in relation to the transport-level handling of data upon the grid.
- OGSA introduces the concept of a Grid service, which is a Web service that conforms to a set of conventions and interfaces that provide a uniform way to interact with grid resources.
- OGSA also defines a service-oriented resource model, which describes how grid resources are represented, named, discovered, and managed by Grid services.
- OGSA was developed within the Open Grid Forum, which was called the Global Grid Forum (GGF) at the time, around 2002 to 2006.
- OGSA is not a complete architecture, but rather a framework that can be used to design and implement specific grid architectures and applications.
- OGSA is intended to be applicable and adopted for a wide range of domains and scenarios, such as business, scientific, and e-government.



### Introduction for the notes of the Unit 2 - Open Grid Services Architecture in the subject of High Performance Computing

- Open Grid Services Architecture (OGSA) is a set of standards and specifications that define how grid computing systems should be designed and implemented.
- Grid computing is a paradigm that enables the sharing and coordination of distributed resources across multiple domains and organizations, such as computing power, storage, data, software, and services.
- OGSA aims to provide a common framework for building interoperable and scalable grid systems that can support a wide range of applications and users.
- OGSA is based on the concepts and technologies of web services, which are self-describing, modular, and loosely coupled components that communicate using standard protocols and formats over the internet.
- OGSA defines a core set of grid services that provide basic functionalities for resource discovery, management, monitoring, security, and data access.
- OGSA also defines a set of higher-level services that build on the core services to provide more advanced functionalities for specific domains and scenarios, such as workflow, scheduling, brokering, and data replication.
- OGSA is not a fixed or rigid architecture, but rather an evolving and extensible one that can accommodate new requirements and technologies as they emerge.
- OGSA is developed and maintained by the Open Grid Forum (OGF), an international community of researchers, developers, vendors, and users that collaborate on defining and promoting grid standards and best practices.



### Requirements for the notes of the Unit 2 - Open Grid Services Architecture in the subject of High Performance Computing

- The notes should provide an overview of the Open Grid Services Architecture (OGSA), which is a service-oriented architecture for grid computing that extends Web services and addresses key concerns in grid systems  .
- The notes should explain the core capabilities and behaviors of OGSA, such as service creation, lifetime management, discovery, notification, security, and data access and integration.
- The notes should describe the resource models and interfaces of OGSA, such as the Grid Service, the Grid Resource, the Factory, the Handle, the Reference, and the Service Data.
- The notes should illustrate the bindings and protocols of OGSA, such as the Web Services Description Language (WSDL), the Simple Object Access Protocol (SOAP), and the Web Services Resource Framework (WSRF).
- The notes should provide examples of how OGSA can be applied to various domains and scenarios, such as scientific computing, business applications, and e-science .
- The notes should include diagrams, tables, and code snippets to demonstrate the concepts and implementations of OGSA.
- The notes should cite the sources of information and use proper formatting and referencing styles.



### Capabilities for the notes of the Unit 2 - Open Grid Services Architecture in the subject of High Performance Computing

- Open Grid Services Architecture (OGSA) is a set of standards that extends Web services and service-oriented architecture to the grid computing environment .
- OGSA defines a common, extensible, and flexible framework for exposing and accessing grid resources as services, using standard protocols and interfaces.
- OGSA addresses key concerns in grid systems, such as resource discovery, dynamic provisioning, monitoring, security, fault tolerance, and interoperability .
- OGSA uses most of Web service technologies, notably WSDL and SOAP, but it aims to be largely agnostic in relation to the transport-level handling of data upon the grid.
- OGSA consists of a core set of interfaces, behaviors, resource models, and bindings that specify how grid services are created, named, discovered, managed, and secured.
- OGSA also defines a set of common capabilities that can be used by different types of grid services, such as data access and integration, execution management, resource management, and notification.
- OGSA enables the development of interoperable and portable grid applications and middleware that can leverage the diverse and distributed resources of the grid.



### Security Considerations for Open Grid Services Architecture

- Open Grid Services Architecture (OGSA) is a framework that defines how grid services can be created, managed, and accessed in a distributed environment.
- Grid services are stateful, transient, and dynamic web services that provide access to various resources and capabilities in a grid system.
- Security is a critical aspect of OGSA, as grid services may involve sensitive data, computations, and interactions among multiple parties with different trust levels and policies.
- Some of the security challenges and requirements for OGSA are:

  - Authentication: verifying the identity and credentials of grid service providers and consumers, as well as the integrity and origin of grid service messages.
  - Authorization: enforcing access control policies and permissions for grid service operations and resources, based on the roles, attributes, and obligations of grid service participants.
  - Confidentiality: protecting the privacy and secrecy of grid service data and communications from unauthorized disclosure or interception.
  - Integrity: ensuring the correctness and completeness of grid service data and computations from unauthorized modification or corruption.
  - Non-repudiation: providing evidence and assurance of the origin and delivery of grid service messages, as well as the accountability and responsibility of grid service participants.
  - Auditing: recording and monitoring the activities and events of grid service participants, as well as the usage and performance of grid service resources and operations.
  - Availability: ensuring the reliability and accessibility of grid service resources and operations from malicious attacks or accidental failures.

- Some of the security technologies and mechanisms that are being developed or adopted for OGSA are:

  - Public key infrastructure (PKI): a system that uses public key cryptography and digital certificates to provide authentication, confidentiality, integrity, and non-repudiation for grid service messages and participants.
  - Security Assertion Markup Language (SAML): a standard that defines how security assertions and attributes can be expressed and exchanged in XML format, to support authentication and authorization for grid service participants.
  - Extensible Access Control Markup Language (XACML): a standard that defines how access control policies and decisions can be expressed and enforced in XML format, to support authorization for grid service operations and resources.
  - Web Services Security (WS-Security): a specification that defines how security tokens, signatures, and encryption can be applied to SOAP messages, to support authentication, confidentiality, integrity, and non-repudiation for grid service communications.
  - Web Services Trust (WS-Trust): a specification that defines how trust relationships and security tokens can be established and exchanged among grid service participants, to support authentication and authorization for grid service interactions.
  - Web Services Secure Conversation (WS-SecureConversation): a specification that defines how security contexts and keys can be established and maintained among grid service participants, to support confidentiality and integrity for grid service communications.
  - Web Services Federation (WS-Federation): a specification that defines how federated identity and single sign-on can be achieved among grid service participants, to support authentication and authorization for grid service interactions.
  - Web Services Policy (WS-Policy): a specification that defines how security policies and capabilities can be expressed and negotiated among grid service participants, to support security interoperability and compatibility for grid service interactions.
  - Web Services Security Policy (WS-SecurityPolicy): a specification that defines how security policies and requirements can be expressed and enforced for grid service communications, to support authentication, confidentiality, integrity, and non-repudiation for grid service messages.
  - Grid Security Infrastructure (GSI): a system that provides a set of security services and protocols for grid systems, based on PKI, X.509 certificates, proxy certificates, and SSL/TLS.
  - Grid Authorization Service (GAS): a system that provides a centralized service for managing and enforcing access control policies and permissions for grid resources and services, based on SAML and XACML.
  - Grid Resource Allocation and Management (GRAM): a system that provides a service for creating, managing, and accessing grid services and resources, based on WS-Resource Framework and WS-Notification.
  - Grid Security Audit and Trace Service (GSAT): a system that provides a service for collecting and analyzing security-related information and events from grid services and resources, based on WS-Audit and WS-Trace.

- Some of the security architectures and models that have been proposed or implemented for OGSA are:

  - The security architecture for open grid services : a comprehensive grid security architecture that supports, integrates, and unifies popular security models, mechanisms, protocols, platforms, and technologies in a way that enables a variety of systems to interoperate securely.
  - The cybersecurity for smart grid systems



### GLOBUS Toolkit

- The GLOBUS Toolkit is an open-source toolkit for grid computing developed and provided by the Globus Alliance.
- Grid computing is a form of distributed computing that enables the sharing of resources across multiple organizations and domains.
- The GLOBUS Toolkit contains a set of libraries and programs that provides the developers of specific tools or apps with solutions for common problems that are encountered when creating a distributed system services and applications.
- Globus is a software with components and capabilities that includes:
  - Security: authentication, authorization, delegation, single sign-on, etc.
  - Data management: data transfer, replication, cataloging, etc.
  - Resource management: discovery, allocation, monitoring, etc.
  - Execution management: job submission, scheduling, fault tolerance, etc.
  - Information services: registry, directory, notification, etc.
- The GLOBUS Toolkit is based on the Open Grid Services Architecture (OGSA), which defines a set of standard interfaces and behaviors for grid services.
- Grid services are web services that follow the OGSA specifications and support the creation, management, and discovery of dynamic and transient service instances.
- The GLOBUS Toolkit is no longer available as a do-it-yourself distributed computing toolkit, but its spirit lives on in a mature, full-featured and easy to use service for research data management – Globus.org .
- Globus.org is a cloud-based platform that lets researchers efficiently, securely, and reliably transfer data directly between systems separated by an office wall or an ocean.
- Globus.org also provides features such as data sharing, data publication, data discovery, and data analysis.
- Globus.org is free for non-profit research and education purposes.



## Unit 3 - Overview of Cluster Computing

- Cluster computing is a form of distributed computing that involves a set of computers that work together as a single system  .
- Cluster computing provides solutions to solve difficult problems by providing faster computational speed, enhanced data integrity, load balancing and high availability  .
- Cluster computing can range from a simple two-node system of two personal computers to a very fast supercomputer that has a cluster architecture .
- Cluster computing typically involves two types of nodes: head node and compute nodes.
  - The head node is the central node that controls and schedules the tasks for the compute nodes.
  - The compute nodes are the nodes that perform the actual computation and data processing.
- Cluster computing can be classified into different types based on the degree of coupling, the communication network, the hardware and software configuration, and the application domain .
  - Some common types of cluster computing are:
    - Beowulf cluster: a cluster of commodity hardware that runs Linux or other free software and uses standard networking protocols .
    - High-availability cluster: a cluster that provides continuous service and fault tolerance by using redundant hardware and software components .
    - Load-balancing cluster: a cluster that distributes the workload among the nodes to optimize the performance and resource utilization .
    - High-performance computing cluster: a cluster that delivers high-speed computation and data processing for scientific and engineering applications .
    - Grid computing cluster: a cluster that connects geographically distributed resources and provides a unified platform for large-scale and heterogeneous computing .



### Cluster Computer and its Architecture

- A cluster computer is a set of connected computers that work together as a single system   .
- The connected computers are called nodes, and they can be personal computers, workstations, servers, or supercomputers  .
- A cluster computer can be used to enhance the processing power, increase the resilience, or provide high availability of a system .
- A cluster computer has a specific architecture that consists of the following components :
  - Cluster nodes: the individual computers that perform the computation, communication, and storage tasks.
  - Cluster interconnect: the network that connects the cluster nodes and provides high-speed data transfer and low latency.
  - Cluster middleware: the software that manages the cluster resources, coordinates the load sharing, detects node failures, and schedules the tasks.
  - Cluster applications: the programs that run on the cluster and exploit its parallel and distributed capabilities.
- A cluster computer can be classified into different types based on the hardware, software, or application characteristics . Some common types are:
  - High-performance computing (HPC) clusters: clusters that are designed to provide high-speed computation for scientific or engineering applications.
  - High-availability (HA) clusters: clusters that are designed to provide continuous operation and fault tolerance for critical applications.
  - Load-balancing clusters: clusters that are designed to distribute the workload among the nodes and improve the performance and scalability of the system.
  - Data-intensive clusters: clusters that are designed to handle large amounts of data and provide fast and reliable storage and analysis.



### Clusters Classifications for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

- Cluster computing is a form of parallel computing that uses a collection of interconnected computers (called nodes) to perform tasks that require high performance, availability, or scalability .
- Cluster computing can be classified into three main types based on the purpose and design of the clusters :
  - **High performance (HP) clusters**: HP clusters use computer clusters and supercomputers to solve advanced computational problems that require high speed, accuracy, and efficiency. They are used for scientific and engineering applications that need nodes to communicate frequently and synchronously as they perform their jobs. Examples of HP clusters are weather forecasting, molecular modeling, and cryptography .
  - **Load-balancing clusters**: Load-balancing clusters distribute incoming requests for resources among several nodes running similar programs or having similar content. They are used to improve the performance, reliability, and availability of web servers, databases, and other network services. Examples of load-balancing clusters are e-commerce, online gaming, and streaming media .
  - **High availability (HA) clusters**: HA clusters provide continuous operation and fault tolerance for critical applications and services. They are designed to detect and recover from node failures, network failures, or software failures without affecting the functionality or performance of the system. Examples of HA clusters are banking, healthcare, and telecommunications .
- Cluster computing can also be classified based on the architecture and components of the clusters  :
  - **CPU and accelerator**: CPU and accelerator clusters use a combination of central processing units (CPUs) and specialized hardware devices (such as field-programmable gate arrays (FPGAs) or graphics processing units (GPUs)) to accelerate the computation of certain tasks. The accelerators can be integrated into the nodes or connected via high-speed interconnects. Examples of CPU and accelerator clusters are artificial intelligence, machine learning, and image processing .
  - **Memory**: Memory clusters use different types of memory technologies (such as dynamic random-access memory (DRAM), high bandwidth memory (HBM), or non-volatile memory (NVM)) to store and access data efficiently. The memory can be distributed among the nodes or shared by the nodes via a global address space. Examples of memory clusters are big data analytics, graph processing, and in-memory databases .
  - **Storage and file system**: Storage and file system clusters use different types of storage devices (such as hard disk drives (HDDs), solid state drives (SSDs), or tape drives) and file systems (such as parallel file systems, distributed file systems, or object storage systems) to store and manage large amounts of data. The storage and file system can be local to the nodes or remote to the nodes via a network. Examples of storage and file system clusters are data warehousing, backup and recovery, and cloud computing .
  - **Networking**: Networking clusters use different types of network technologies (such as Ethernet, InfiniBand, or Omni-Path) and protocols (such as message passing interface (MPI), remote direct memory access (RDMA), or partitioned global address space (PGAS)) to connect the nodes and enable data communication and coordination. The networking can be homogeneous or heterogeneous, and can support different topologies (such as star, ring, or mesh). Examples of networking clusters are distributed computing, grid computing, and edge computing .



### Components for Clusters

- A cluster is a collection of interconnected computers that work together as a single system to perform high-performance computing tasks.
- The main components of a cluster are:

  - **Compute nodes**: These are the servers that execute the parallel applications and algorithms. They can have different configurations of CPUs, GPUs, FPGAs, memory, and other resources depending on the workload requirements. A single cluster can have hundreds or thousands of nodes.
  - **Network**: This is the communication infrastructure that connects the nodes and enables data transfer and synchronization. The network can be based on different technologies, such as Ethernet, InfiniBand, or Omni-Path, and have different topologies, such as star, ring, or mesh. The network performance is measured by its bandwidth, latency, and reliability.
  - **Storage**: This is the component that provides persistent data storage for the cluster. It can be divided into two types: general-purpose storage and high-performance storage. General-purpose storage is used to store applications and user data, and can be based on different file systems, such as NFS, CIFS, or Lustre. High-performance storage is used to store temporary data that is generated or consumed by the parallel applications, and can be based on a clustered file system, such as GPFS, BeeGFS, or OrangeFS, that provides high-speed, low-latency, and scalable access to the data.
  - **Scheduler**: This is the software component that manages the allocation of cluster resources to the submitted jobs. It maintains a queue of pending jobs, and assigns them to the available nodes based on different policies, such as priority, fairness, or load balancing. The scheduler also monitors the status of the jobs and the nodes, and handles failures and interruptions. Some examples of schedulers are Slurm, PBS, or LSF.
  - **Provisioner**: This is the software component that ensures the homogeneity and consistency of the cluster nodes. It automates the installation, configuration, and maintenance of the operating system, drivers, libraries, and applications on the nodes. It also provides tools for monitoring, troubleshooting, and updating the cluster. Some examples of provisioners are MAAS, xCAT, or Rocks.



### Cluster Middleware and SSI

- Cluster middleware is a software layer that resides between the operating system and the user-level environment of a cluster system.
- Cluster middleware provides various services and functionalities to make the cluster appear as a single parallel machine to the user, to applications, and to the network.
- Cluster middleware consists of two sub-layers of software infrastructure: availability infrastructure and single system image (SSI) infrastructure.
- Availability infrastructure provides high availability (HA) services, such as fault detection, fault recovery, and load balancing, to ensure the reliability and performance of the cluster system.
- SSI infrastructure provides a single entry point, a single file hierarchy, a single point of control, and a single view of the cluster resources, such as processes, memory, and devices, to the user and applications.
- SSI can be implemented at different levels, such as hardware, operating system, middleware, or application level, depending on the degree of transparency and scalability required.
- SSI can also support different types of communication and synchronization mechanisms, such as message passing, remote procedure call, or shared memory, to facilitate the development and execution of parallel and distributed applications on the cluster system.
- Some examples of cluster middleware and SSI systems are OpenSSI, MOSIX, Kerrighed, and OpenPBS.



### Resource Management and Scheduling

- Resource management and scheduling (RMS) are critical tasks in cluster computing, which involves coordinating and controlling the use of computing resources among multiple users and applications  .
- The main objectives of RMS are to maximize resource utilization, minimize processing time, and ensure fairness and quality of service for the users and applications .
- The RMS of clusters provides support for four main functionalities: management of resources, job queuing, job scheduling, and execution .
  - Management of resources: The RMS manages, controls, and maintains the status information of the resources, such as processors and disk storage, in the cluster system. It also monitors the availability and performance of the resources and handles failures and faults .
  - Job queuing: Jobs submitted by the users into the cluster system are initially placed into queues until there are available resources to execute the jobs. The RMS may use different policies to prioritize and order the jobs in the queues, such as first-come first-served, shortest job first, or user-defined priority .
  - Job scheduling: The cluster RMS then invokes the cluster scheduler to determine how resources are assigned to various jobs. The scheduler may use different algorithms and strategies to allocate resources to jobs, such as static or dynamic, centralized or distributed, or single or multiple criteria .
  - Execution: After that, the cluster RMS dispatches the jobs to the assigned nodes and manages the job execution processes before returning the results to the users upon job completion. The RMS may also perform load balancing, migration, or preemption of jobs to improve the performance and efficiency of the cluster system .
- Cluster resource scheduling is a challenging and complex problem, as it involves dealing with heterogeneous and dynamic resources, multiple and conflicting objectives, diverse and unpredictable workloads, and various constraints and requirements  .
- Cluster resource scheduling is also an active and evolving research area, as new technologies and applications emerge and pose new challenges and opportunities for improving the performance and functionality of cluster systems .



### Programming for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

- Cluster computing is a form of parallel computing that involves connecting multiple computers (called nodes) on a network and using them as a single system for high-performance tasks  .
- Cluster computing can provide faster computational speed, enhanced data integrity, higher availability, and better scalability than a single computer .
- Cluster computing can be classified into two types: loosely coupled and tightly coupled.
  - Loosely coupled clusters have nodes that are independent and communicate only when necessary. They are suitable for tasks that can be divided into smaller subtasks and executed in parallel with minimal coordination.
  - Tightly coupled clusters have nodes that are synchronized and communicate frequently. They are suitable for tasks that require high data exchange and coordination among the nodes.
- Cluster computing can also be categorized based on the architecture and functionality of the nodes, such as homogeneous or heterogeneous, symmetric or asymmetric, fail-over or load-balancing, etc .
- Cluster computing requires software tools to manage the nodes, distribute the workload, monitor the performance, and handle the faults  .
  - Some examples of cluster management software are Kubernetes, Apache Mesos, Hadoop, and MPI  .
  - Some examples of cluster programming models are MapReduce, Spark, OpenMP, and CUDA  .
- Cluster computing has many applications in various domains, such as scientific computing, big data analytics, web services, machine learning, and gaming  .



### Environments and Tools for Cluster Computing

- Cluster computing is a form of high performance distributed computing (HPDC) that uses a network of computers (called nodes) to execute parallel and/or distributed applications that require high computational power.
- A cluster computing software stack consists of the following components:
  - Workload managers or schedulers (such as Slurm, PBS, or IBM's LSF) to orchestrate job execution on the nodes.
  - Cluster configuration tools to provision and build clusters, such as:
    - Cluster management tools (such as Managed Instance Groups or Kubernetes) to orchestrate compute nodes and scale them up or down according to the workload demand.
    - DevOps tools (such as Terraform) to automate the creation and configuration of clusters and their resources.
  - End-user applications (such as OpenFOAM, GROMACS, WRF, or Jupyter Notebooks) to execute computations and view and analyze output.
- Cluster computing environments and tools can vary depending on the type and architecture of the cluster, such as:
  - Shared-memory clusters, where all the nodes share a common memory space and communicate via memory access.
  - Distributed-memory clusters, where each node has its own memory space and communicate via message passing.
  - Hybrid clusters, where both shared-memory and distributed-memory nodes are used.
- Some examples of cluster computing environments and tools are :
  - MPI (Message Passing Interface), a standard and widely used library for message passing communication among nodes.
  - OpenMP (Open Multi-Processing), a standard and widely used API for shared-memory parallel programming.
  - PVM (Parallel Virtual Machine), a software system that enables a collection of heterogeneous computers to be used as a single parallel computer.
  - gLite, a set of middleware technologies created by the Enabling Grids for E-sciencE (EGEE) project, which provides services for job submission, data management, security, and information discovery in grid computing environments.
  - Microsoft Windows Cluster Server 2003, a platform that provides pieces for high-performance computing such as the Job Scheduler, MSMPI library and management tools.



### Cluster Applications

- Cluster computing is a popular approach to achieve high performance computing (HPC) for various scientific and engineering applications. It involves connecting multiple computers or nodes into a network to share resources and workloads.
- Cluster computing can be classified into different types based on the architecture, performance, and functionality of the clusters. Some common types are:
  - High-availability clusters: These clusters provide continuous service and fault tolerance by using redundant nodes and failover mechanisms. They are used for mission-critical applications such as databases, web servers, and email servers.
  - Load-balancing clusters: These clusters distribute the workload among multiple nodes to optimize the performance and scalability of the system. They are used for applications that have high demand and variable load, such as web services, e-commerce, and online gaming.
  - High-performance clusters: These clusters utilize supercomputers to solve complex computational problems. They are used for applications that require intensive calculations and simulations, such as climate modeling, fluid dynamics, genomics, and cryptography.
- Cluster computing has various applications in different domains and industries. Some examples are:
  - Oil and gas: Cluster computing is used to perform seismic analysis, reservoir modeling, and exploration optimization for the oil and gas industry. These applications require high computing power and parallel processing to handle large volumes of data and complex algorithms.
  - Finance: Cluster computing is used to perform risk analysis, portfolio optimization, and market simulation for the finance industry. These applications require fast and accurate computations to deal with dynamic and uncertain scenarios.
  - Semiconductor design: Cluster computing is used to perform circuit simulation, verification, and testing for the semiconductor design industry. These applications require high performance and reliability to ensure the quality and functionality of the chips.
  - Engineering: Cluster computing is used to perform finite element analysis, computational fluid dynamics, and structural optimization for the engineering industry. These applications require high resolution and accuracy to model the physical phenomena and design the optimal solutions.
  - Weather modeling: Cluster computing is used to perform atmospheric modeling, weather forecasting, and climate prediction for the weather modeling industry. These applications require high scalability and throughput to process the massive and diverse data and generate the timely and reliable results.



### Cluster Systems

- Cluster systems are a type of high performance computing (HPC) architecture that use a network of multiple servers, also called nodes, to perform parallel computations on large and complex problems  .
- Cluster systems can be classified into different types based on the nature of the problem, the communication pattern, the hardware configuration, and the software environment.
- Some common types of cluster systems are:
  - High performance (HP) clusters: These clusters are designed to solve computationally intensive problems that require high speed and low latency communication among the nodes. They often use specialized hardware such as supercomputers, GPUs, or FPGAs to accelerate the computations  .
  - High availability (HA) clusters: These clusters are designed to provide continuous and reliable service in the event of node failures or network disruptions. They often use redundant hardware and software components to ensure fault tolerance and load balancing.
  - High throughput (HT) clusters: These clusters are designed to execute a large number of independent tasks that do not require frequent communication among the nodes. They often use commodity hardware and software components to achieve cost efficiency and scalability.
- Cluster systems typically consist of the following components  :
  - Compute nodes: These are the servers that perform the actual computations. They can have different architectures, such as symmetric multiprocessors (SMP), massively parallel processors (MPP), or single instruction multiple data (SIMD).
  - Storage nodes: These are the servers that provide data storage for the compute nodes. They can use different technologies, such as hard disk drives (HDD), solid state drives (SSD), or network attached storage (NAS).
  - Network nodes: These are the servers that provide network connectivity for the compute and storage nodes. They can use different protocols, such as Ethernet, InfiniBand, or Fibre Channel.
  - Management nodes: These are the servers that provide administrative and monitoring functions for the cluster. They can use different tools, such as schedulers, resource managers, or performance analyzers.
- Cluster systems offer several advantages over traditional computing systems, such as  :
  - Higher performance: Cluster systems can achieve higher performance by distributing the workload among multiple nodes and exploiting the parallelism of the problem.
  - Higher scalability: Cluster systems can scale up or down by adding or removing nodes according to the demand and the budget.
  - Higher flexibility: Cluster systems can adapt to different types of problems and applications by using different hardware and software configurations.
  - Higher availability: Cluster systems can provide uninterrupted service by using redundant components and fault tolerance mechanisms.



## Unit 4 - Beowulf Cluster

- A Beowulf cluster is a computer cluster of what are normally identical, commodity-grade computers networked into a small local area network with libraries and programs installed which allow processing to be shared among them.
- The result is a high-performance parallel computing cluster from inexpensive personal computer hardware.
- A Beowulf cluster is scalable to a nearly unlimited number of computers, limited only by the overhead of the network.
- Provisioning of operating systems and other software for a Beowulf Cluster can be automated using software, such as Open Source Cluster Application Resources.
- Beowulf clusters are based on commodity hardware, on a private system network, with open source software (Linux) infrastructure.
- The designer can improve performance proportionally with added machines.
- Beowulf clusters are programmed such that they share processes among themselves and form parallel processing units.
- Beowulf clusters can be built using two or more computers with a Linux distribution installed in them, a network connection between them, and some configuration steps.
- Beowulf clusters make supercomputing accessible and affordable for various applications, such as modeling and simulation.
- Beowulf clusters are named after the hero of an Old English epic poem, who slayed monsters with his bare hands.



### The Beowulf Model

- A Beowulf cluster is a computer cluster of what are normally identical, commodity-grade computers networked into a small local area network with libraries and programs installed which allow processing to be shared among them.
- The result is a high-performance parallel computing cluster from inexpensive personal computer hardware.
- A Beowulf cluster is scalable to a nearly unlimited number of computers, limited only by the overhead of the network.
- Provisioning of operating systems and other software for a Beowulf Cluster can be automated using software, such as Open Source Cluster Application Resources.
- Beowulf clusters are based on commodity hardware, on a private system network, with open source software (Linux) infrastructure.
- The designer can improve performance proportionally with added machines.
- Beowulf clusters are programmed such that they share processes among themselves and form parallel processing units.
- Beowulf clusters can be built using two or more computers with a Linux distribution installed in them, a network connection between them, and some configuration steps.
- Beowulf clusters make supercomputing accessible and affordable for various applications, such as modeling and simulation.
- Beowulf clusters are named after the epic hero Beowulf, who slayed the monster Grendel using his bare hands.



### Application Domains for Beowulf Cluster

- A Beowulf cluster is a group of commodity-grade computers that are networked and programmed to perform parallel computing tasks.
- Beowulf clusters can be used for various applications that require high performance computing, such as:
  - Transport phenomena, including fluid dynamics, heat and mass transfer, multi-phase flows, aerodynamics, etc .
  - Molecular dynamics, protein folding, and bioinformatics .
  - Cellular automata to model phenomena from epidemiology to options trading.
  - Graphics: distributed raytracing and rendering.
  - Hard NP problems such as DNA sequence alignment, cryptography, and combinatorial optimization .
  - Simulation and modeling of physical systems, such as climate, astrophysics, nuclear fusion, etc .
  - Data analysis and machine learning .
- Beowulf clusters make supercomputing accessible and affordable for various domains, such as academia, industry, government, and research.



### Beowulf System Architecture

- Beowulf is a **multi-computer architecture** which can be used for **parallel computations** .
- It is a system which usually consists of **one server node**, and **one or more client nodes** connected via **Ethernet** or some other network .
- The server node is responsible for **distributing tasks** to the client nodes, **managing resources**, and **collecting results** .
- The client nodes are responsible for **executing tasks** assigned by the server node, **communicating with other nodes**, and **returning results** to the server node .
- The nodes are typically **standard PCs** or **workstations** running **Linux** or some other open-source operating system .
- The nodes are connected by a **high-speed network** such as **Gigabit Ethernet**, **InfiniBand**, or **Myrinet** .
- The network can be configured in different **topologies** such as **star**, **ring**, **mesh**, or **hypercube** depending on the **communication pattern** and **performance requirements** of the parallel applications .
- The nodes can share a **common file system** such as **NFS** or **Lustre** or have their own **local disks** .
- The nodes can also have **specialized hardware** such as **GPUs**, **FPGAs**, or **co-processors** to enhance the **computational power** and **energy efficiency** of the system .
- The system can be **scaled up** by adding more nodes or **scaled out** by connecting multiple clusters .
- The system can be **customized** according to the **needs** and **budget** of the users .
- The system can be used for a variety of **scientific** and **engineering** applications that require **high-performance computing** .



### Software Practices for the notes of the Unit 4 - Beowulf Cluster in the subject of High Performance Computing

- A Beowulf cluster is a type of high performance computing system that consists of a group of identical and commodity-grade computers that are networked together to form a parallel processing unit  .
- A Beowulf cluster is distinguished from a network of workstations by several characteristics, such as:
  - The nodes in the cluster are dedicated to the cluster and not subject to external factors.
  - The cluster uses a private system network that is separate from the public network.
  - The cluster uses open source software, such as Linux, as the operating system and the middleware .
- A Beowulf cluster is designed to be scalable, cost-effective, and flexible, as the performance can be improved by adding more machines, the hardware is inexpensive and widely available, and the software can be customized and modified.
- A Beowulf cluster can be used for various applications that require high computational power, such as scientific simulations, data analysis, image processing, machine learning, and more.
- A Beowulf cluster requires careful design and setup to ensure optimal performance and reliability, such as:
  - Choosing the appropriate hardware components, such as processors, memory, disks, network cards, switches, and cables.
  - Installing and configuring the operating system and the software packages, such as compilers, libraries, tools, and schedulers.
  - Testing and benchmarking the cluster to measure its speed, efficiency, and scalability.
  - Monitoring and maintaining the cluster to detect and resolve any issues or failures.



### Parallel Programming with MPL for Beowulf Cluster

- A Beowulf cluster is a private network of computers (usually Alpha or Intel boxes) running a stripped down version of Linux .
- A Beowulf cluster can function like a single massively parallel computer by using a parallel programming API like MPI or PVM .
- MPI (Message Passing Interface) and PVM (Parallel Virtual Machine) are libraries that permit the programmer to divide a task among a group of networked computers, and collect the results of processing.
- MPI is a standard for message-passing communication between processes in a parallel program .
- PVM is a software system that enables a collection of heterogeneous computers to be used as a coherent and flexible concurrent computational resource.
- Parallel programming with MPI or PVM involves writing programs that use the library functions to send and receive messages between processes, and to synchronize and coordinate their execution.
- Some examples of parallel programming with MPI are: Hello World, Manager/Worker, Two-Dimensional Jacobi, Collective Operations, and Parallel Monte Carlo Computation .
- Some advantages of parallel programming with MPI or PVM for Beowulf cluster are: portability, scalability, performance, and flexibility .
- Some challenges of parallel programming with MPI or PVM for Beowulf cluster are: debugging, load balancing, communication overhead, and fault tolerance .



### Parallel Virtual Machine (PVM) for the notes of the Unit 4 - Beowulf Cluster in the subject of High Performance Computing

- PVM is a software package that enables a network of heterogeneous computers (Unix and/or Windows) to be used as a single large parallel computer .
- PVM can be used to solve large computational problems more cost effectively by using the aggregate power and memory of many computers  .
- PVM provides a set of library routines that can be linked with an application program to perform various tasks such as:
  - Creating and managing a virtual machine of networked computers  .
  - Sending and receiving messages among processes in the virtual machine  .
  - Synchronizing processes and broadcasting messages  .
  - Handling errors and faults in the virtual machine  .
- PVM uses a master-slave model of parallel programming, where the master process spawns and controls the slave processes, and the slave processes perform the computation and communicate with the master and/or other slaves  .
- PVM assigns a unique identifier (TID) to each process in the virtual machine, and uses a routing mechanism to deliver messages to the correct destination  .
- PVM supports dynamic addition and deletion of hosts from the virtual machine, allowing for load balancing and fault tolerance  .
- PVM can be used as a stand-alone software or as a foundation for other heterogeneous network software.
- PVM has a console interface (pvm) that allows the user to interact with the virtual machine, such as adding or removing hosts, showing the status of processes, killing processes, etc..



## Unit 5 - Overview of Cloud Computing

- Cloud computing is a model for enabling **ubiquitous**, **convenient**, **on-demand** network access to a **shared pool** of **configurable computing resources** (e.g., networks, servers, storage, applications, and services) that can be **rapidly provisioned and released** with minimal management effort or service provider interaction.
- Cloud computing also refers to the **technology** that makes cloud work. This includes some form of **virtualized IT infrastructure**— servers, operating system software, networking, and other infrastructure that’s **abstracted**, using special software, so that it can be **pooled and divided** irrespective of physical hardware boundaries.
- Cloud computing is the **delivery** of computing services—including servers, storage, databases, networking, software, analytics, and intelligence—over the **Internet** (“the cloud”) to offer **faster innovation**, **flexible resources**, and **economies of scale**.
- Cloud computing is the **practice** of storing regularly used computer data on **multiple servers** that can be accessed through the **Internet**.



### Types of Cloud

Cloud computing is the delivery of computing services over the internet, such as servers, storage, databases, networking, software, analytics, and intelligence. Cloud computing can be classified into two main types: deployment models and service models.

#### Deployment Models

Deployment models refer to the location and management of the cloud's infrastructure. There are four common types of deployment models:

- **Public cloud**: The cloud infrastructure is owned and operated by a third-party cloud service provider, such as Amazon Web Services (AWS), Microsoft Azure, or Google Cloud Platform. The cloud services are delivered over the internet and are available to anyone who wants to use them. The customers share the same hardware, software, and network resources, and pay only for the resources they use. Public cloud is suitable for applications that have unpredictable demand, need to scale quickly, or require low cost and high availability.
- **Private cloud**: The cloud infrastructure is exclusively used by a single organization or a group of organizations that share common goals and policies. The cloud infrastructure can be owned, managed, and operated by the organization itself, a third-party service provider, or a combination of both. The cloud services are delivered over a private network or the internet, and are not accessible to the public. Private cloud is suitable for applications that have strict security, compliance, or performance requirements, or need more control and customization over the cloud environment.
- **Hybrid cloud**: The cloud infrastructure is a combination of public and private clouds, which are connected by a technology that allows data and applications to move between them. The hybrid cloud provides the benefits of both public and private clouds, such as scalability, cost-efficiency, security, and flexibility. Hybrid cloud is suitable for applications that have dynamic or changing workloads, need to integrate with legacy systems, or require a balance between innovation and stability.
- **Community cloud**: The cloud infrastructure is shared by several organizations that have similar needs, interests, or objectives, such as a specific industry, region, or mission. The cloud infrastructure can be owned, managed, and operated by one or more of the organizations, a third-party service provider, or a combination of both. The cloud services are delivered over a private network or the internet, and are accessible only to the authorized members of the community. Community cloud is suitable for applications that have specific regulatory, policy, or social requirements, or need to collaborate and share resources among the community members.

#### Service Models

Service models refer to the types and levels of cloud services that are offered to the customers. There are four common types of service models:

- **Software as a service (SaaS)**: The cloud service provider delivers software applications over the internet, which are accessed by the customers through a web browser or a mobile app. The customers do not have to install, maintain, or update the software, as the cloud service provider manages the infrastructure, platform, and software. The customers pay for the software usage, usually on a subscription or pay-per-use basis. SaaS is suitable for applications that have standard functionality, need to be accessed from anywhere, or require frequent updates.
- **Platform as a service (PaaS)**: The cloud service provider delivers a platform over the internet, which allows the customers to develop, run, and manage their own software applications without having to deal with the underlying infrastructure, operating system, or middleware. The customers have control over the configuration and deployment of the applications, but not over the platform. The customers pay for the platform usage, usually on a per-hour or per-resource basis. PaaS is suitable for applications that have custom functionality, need to be integrated with other services, or require rapid development and testing.
- **Infrastructure as a service (IaaS)**: The cloud service provider delivers infrastructure resources over the internet, such as servers, storage, network, and virtualization. The customers can provision and use the resources as they need, and have full control over the configuration and management of the resources. The customers pay for the resource usage, usually on a per-hour or per-resource basis. IaaS is suitable for applications that have variable demand, need to scale up or down quickly, or require high performance and reliability.
- **Serverless**: The cloud service provider delivers a service that allows the customers to execute code without having to provision or manage any servers. The customers only pay for the execution time of the code, which is triggered by events or requests. The cloud service provider manages the infrastructure, platform, and software. Serverless is suitable for applications that have short-lived, stateless, or event-driven functions, need to be scalable and cost-effective, or require low latency and high availability.



### Cyber infrastructure for the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing

- Cyber infrastructure is a collection of information technology systems and software, physical and information assets, processes, and people that enables an organization to efficiently and securely function on cyber space.
- Cloud computing is the delivery of computing services—including servers, storage, databases, networking, software, analytics, and intelligence—over the Internet (“the cloud”) to offer faster innovation, flexible resources, and economies of scale.
- Cloud computing is a form of cyber infrastructure that provides on-demand access, via the internet, to computing resources as services over the internet, without the need for enterprises to procure, configure, or manage resources themselves .
- Cloud computing has the following characteristics:
  - On-demand self-service: Users can provision computing resources as needed without human intervention from the service provider.
  - Broad network access: Resources are available over the network and can be accessed through standard mechanisms by various devices.
  - Resource pooling: The service provider's computing resources are pooled to serve multiple users, with different physical and virtual resources dynamically assigned and reassigned according to user demand.
  - Rapid elasticity: Resources can be quickly scaled up or down, depending on the user's needs.
  - Measured service: Resource usage is monitored, controlled, and reported, providing transparency and optimization for both the provider and the user.
- There are three primary types of cloud deployments:
  - Public cloud: The service provider offers computing resources to the general public over the internet, on a pay-as-you-go or subscription basis. Examples of public cloud providers are Microsoft Azure, IBM Cloud, Google Cloud, and Amazon Web Services.
  - Private cloud: The service provider offers computing resources exclusively to a single organization, either over the internet or on a private network. The organization can have more control and customization over the resources, but also more responsibility and cost for managing them.
  - Hybrid cloud: The service provider offers a combination of public and private cloud resources, allowing the organization to benefit from the best of both worlds. The organization can use the public cloud for scalable and cost-effective services, and the private cloud for sensitive and mission-critical applications.
- Cloud computing services can be categorized into three main types:
  - Infrastructure as a service (IaaS): The service provider offers the basic computing infrastructure, such as servers, storage, and networking, as a service over the internet. The user can rent the infrastructure and install and run any software on it, including operating systems and applications. The user is responsible for managing and maintaining the software, while the provider is responsible for managing and maintaining the hardware and the network.
  - Platform as a service (PaaS): The service provider offers a platform, such as a development environment, a database, or a web server, as a service over the internet. The user can use the platform to develop, test, deploy, and run applications, without having to worry about the underlying infrastructure. The user is responsible for managing and maintaining the applications, while the provider is responsible for managing and maintaining the platform and the infrastructure.
  - Software as a service (SaaS): The service provider offers a software application, such as an email service, a CRM system, or a video conferencing tool, as a service over the internet. The user can access the application through a web browser or a mobile app, without having to install or run anything on their own devices. The user is responsible for using the application, while the provider is responsible for managing and maintaining the application, the platform, and the infrastructure.



### Service Oriented Architecture

- Service Oriented Architecture (SOA) is an architectural style that focuses on discrete services instead of a monolithic design.
- A service is a software component that provides a business capability and can communicate with other services across platforms and languages .
- A service presents a simple interface to the requester that abstracts away the underlying complexity acting as a black box.
- SOA aims to allow users to combine large chunks of functionality to form applications that are built purely from existing services and combining them in an ad hoc manner.
- SOA has the following benefits  :
  - Reusability: Services can be reused in different contexts and applications, reducing development time and cost.
  - Interoperability: Services can communicate with each other using common standards and protocols, enabling integration and collaboration across systems and organizations.
  - Scalability: Services can be scaled up or down independently, improving performance and availability.
  - Agility: Services can be modified or replaced easily, allowing for faster and more flexible response to changing business needs.
  - Quality: Services can be tested and maintained separately, ensuring reliability and security.



### Cloud Computing Components

Cloud computing is a paradigm that delivers computing resources and services over the internet. Cloud computing architecture refers to the components and subcomponents required for cloud computing. These components typically consist of a front end platform, a back end platform, a cloud based delivery, and a network. Here are some important components of cloud computing architecture:

- **Front end platform**: This is the component that provides a graphical user interface (GUI) to the users or clients who want to access the cloud services. The front end platform can be a fat client, a thin client, or a mobile device. A fat client is a computer that has its own applications and data storage, while a thin client is a computer that relies on the cloud for applications and data storage. A mobile device is a handheld device that can access the cloud services through a wireless network.

- **Back end platform**: This is the component that provides the cloud services to the users or clients. The back end platform consists of servers, storage, and applications. Servers are the computers that run the cloud software and provide the computing resources. Storage is the component that stores the data and files of the users or clients. Applications are the software programs that run on the cloud and provide the functionality and features to the users or clients.

- **Cloud based delivery**: This is the component that delivers the cloud services to the users or clients over the internet. There are three types of cloud based delivery models: infrastructure as a service (IaaS), platform as a service (PaaS), and software as a service (SaaS). IaaS offers compute and storage services, such as virtual machines, containers, and databases. PaaS offers a develop-and-deploy environment to build cloud applications, such as web servers, frameworks, and tools. SaaS delivers applications as services, such as email, office, and social media.

- **Network**: This is the component that connects the front end platform and the back end platform. The network can be the internet, an intranet, or an intercloud. The internet is the global network that connects millions of computers and devices. An intranet is a private network that connects computers and devices within an organization. An intercloud is a network of clouds that can communicate and share resources.

- **Management**: This is the component that manages the cloud computing system and ensures its performance, availability, security, and scalability. Management includes tasks such as provisioning, monitoring, troubleshooting, backup, recovery, and auditing.

- **Security**: This is the component that protects the cloud computing system and its data from unauthorized access, modification, or damage. Security includes measures such as encryption, authentication, authorization, firewall, and antivirus.



### Infrastructure for Cloud Computing

Cloud computing is the delivery of on-demand computing services over the internet, such as applications, servers, storage, databases, networking, and analytics. Cloud computing enables users to access scalable, flexible, and cost-effective IT resources without the need for managing or owning physical infrastructure.

Cloud infrastructure is the collection of hardware and software elements that enable cloud computing. Cloud infrastructure consists of the following components   :

- **Compute**: This refers to the servers or virtual machines that provide the processing power for running applications and workloads in the cloud. Compute resources can be provisioned on-demand, scaled up or down, and billed based on usage.
- **Networking**: This refers to the connectivity and communication between the cloud components, such as routers, switches, firewalls, load balancers, and VPNs. Networking enables data transfer, security, and access control for cloud services and users.
- **Storage**: This refers to the disks, drives, or databases that store data and files in the cloud. Storage can be persistent or ephemeral, block or object, and local or distributed. Storage can also be replicated, backed up, and encrypted for reliability and security.
- **Virtualization**: This refers to the technology that creates a layer of abstraction between the physical hardware and the software that runs on it. Virtualization enables multiple virtual machines or containers to share the same physical resources, such as CPU, memory, and disk space. Virtualization also enables portability, isolation, and automation of cloud workloads.
- **User Interface**: This refers to the graphical or command-line tools that enable users to interact with and manage the cloud resources. User interface can be web-based, desktop-based, or mobile-based, and can provide features such as monitoring, reporting, billing, and troubleshooting.

Cloud infrastructure can be deployed in different models, such as public cloud, private cloud, hybrid cloud, or multi-cloud. Public cloud is when a third-party provider offers cloud services over the internet to the general public. Private cloud is when an organization builds and operates its own cloud infrastructure for its internal use. Hybrid cloud is when an organization combines public and private cloud resources for greater flexibility and efficiency. Multi-cloud is when an organization uses multiple public cloud providers for different purposes or applications.

Cloud infrastructure can also be delivered in different service models, such as infrastructure as a service (IaaS), platform as a service (PaaS), serverless, or software as a service (SaaS). IaaS is when a provider offers the basic cloud infrastructure components, such as compute, networking, and storage, to the users, who are responsible for installing and managing the software and applications on top of them. PaaS is when a provider offers a platform that includes the cloud infrastructure components as well as the operating system, middleware, and development tools, to the users, who are responsible for developing and deploying the applications on the platform. Serverless is when a provider offers a platform that abstracts away the cloud infrastructure components and automatically scales and manages the execution of the applications based on the demand. SaaS is when a provider offers a software application that runs on the cloud infrastructure and is accessible to the users over the internet.



### Storage for the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing

- Cloud storage is a model of computer data storage in which the digital data is stored in logical pools, said to be on "the cloud".
- The physical storage spans multiple servers (sometimes in multiple locations), and the physical environment is typically owned and managed by a hosting company.
- Cloud storage allows users to access and share data over the internet or other networks from different devices and locations.
- Cloud storage has several advantages over traditional data storage, such as scalability, reliability, availability, cost-effectiveness, and security. 
- Cloud storage can be classified into three main types: object storage, file storage, and block storage.
  - Object storage: The data is stored as objects, which consist of data and metadata. Each object has a unique identifier that allows it to be accessed directly through an API. Object storage is suitable for applications that require scalability and metadata.
  - File storage: The data is stored as files in a hierarchical structure, similar to a local file system. Files can be accessed and shared through a network protocol, such as NFS or SMB. File storage is suitable for applications that require a shared file system and compatibility with existing systems.
  - Block storage: The data is stored as blocks of fixed size, which are assigned to a unique address. Blocks can be combined to form a logical volume, which can be formatted with a file system. Block storage is suitable for applications that require high performance and low latency, such as databases and virtual machines.
- Some examples of cloud storage providers are Google Cloud Storage, Amazon S3, Microsoft Azure Blob Storage, Dropbox, and iCloud.



### Platform for the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing

- Cloud computing is the delivery of computing resources over the internet, without direct active management by the user .
- Cloud computing offers cost savings, scalability, high performance, economies of scale, and more.
- Cloud computing can cover a broad range of tasks, from specialized to mundane, and can be used for various industries and applications.
- High Performance Computing (HPC) is the use of a large number of CPU or GPU-based computers to solve complex mathematical tasks.
- HPC can be used for workloads such as genomics, oil and gas simulations, finance, semiconductor design, engineering, weather modeling, and more.
- HPC can be deployed on the cloud, using services such as Azure, AWS, Google Cloud, etc .
- A platform for the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing could be:

  - A website that hosts the notes in a structured and interactive way, using HTML, CSS, and JavaScript.
  - A document that contains the notes in a formatted and searchable way, using PDF, Word, or LaTeX.
  - A presentation that summarizes the notes in a concise and visual way, using PowerPoint, Keynote, or Google Slides.
  - A video that explains the notes in a clear and engaging way, using YouTube, Vimeo, or Khan Academy.
  - A quiz that tests the knowledge of the notes in a fun and challenging way, using Quizlet, Kahoot, or Socrative.



Hello, I am Sydney, your AI assistant. I can help you with your request for the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing. Here is the content in markdown format:

### Application for the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing

- Cloud computing is a paradigm that enables on-demand access to a shared pool of configurable computing resources, such as servers, storage, networks, applications, and services, that can be rapidly provisioned and released with minimal management effort or service provider interaction.
- Cloud computing offers several benefits, such as scalability, elasticity, cost-efficiency, reliability, and availability, to both users and providers of computing services.
- Cloud computing can be classified into different service models, such as Infrastructure as a Service (IaaS), Platform as a Service (PaaS), Software as a Service (SaaS), and Function as a Service (FaaS), depending on the level of abstraction and control offered to the users.
- Cloud computing can also be categorized into different deployment models, such as public cloud, private cloud, hybrid cloud, and community cloud, depending on the ownership, location, and access of the cloud resources.
- Cloud computing poses several challenges, such as security, privacy, interoperability, portability, performance, and quality of service, that need to be addressed by both users and providers of cloud services.
- Cloud computing leverages various technologies, such as virtualization, distributed systems, web services, service-oriented architecture, and parallel and distributed computing, to enable efficient and effective delivery of computing services over the internet.
- Cloud computing is an emerging and evolving field that requires continuous research and development to address the current and future needs and demands of the computing industry and society.



### Services for the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing

- Cloud computing is the delivery of different services through the Internet, such as data storage, servers, databases, networking, software, analytics, and intelligence.
- Cloud computing services offer faster innovation, flexible resources, and economies of scale.
- There are different types of cloud computing services, such as:
  - Infrastructure as a Service (IaaS): This is the most basic category of cloud computing services, which provides the users with access to IT infrastructure such as servers, storage, and networking over the Internet. The users can rent the infrastructure on demand and pay only for what they use. Examples of IaaS providers are Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform.
  - Platform as a Service (PaaS): This is a category of cloud computing services that provides the users with a platform to develop, run, and manage applications without having to deal with the underlying infrastructure. The users can focus on the application logic and code, while the platform handles the operating system, middleware, databases, and other services. Examples of PaaS providers are AWS Elastic Beanstalk, Azure App Service, and Google App Engine.
  - Software as a Service (SaaS): This is a category of cloud computing services that provides the users with access to software applications over the Internet, usually through a web browser or a mobile app. The users do not have to install, update, or maintain the software, as the service provider takes care of that. Examples of SaaS providers are Google Workspace, Microsoft 365, and Salesforce.
  - Function as a Service (FaaS): This is a category of cloud computing services that provides the users with the ability to execute code in response to events, without having to provision or manage servers. The users can write and deploy functions that are triggered by various sources, such as HTTP requests, database changes, or messages. Examples of FaaS providers are AWS Lambda, Azure Functions, and Google Cloud Functions.
- Cloud computing services can also be classified based on the deployment model, such as:
  - Public cloud: This is a type of cloud computing service that is owned and operated by a third-party provider, and is accessible to anyone over the Internet. The users share the same infrastructure and resources with other customers, and benefit from the scalability and cost-effectiveness of the service. Examples of public cloud providers are AWS, Azure, and Google Cloud.
  - Private cloud: This is a type of cloud computing service that is dedicated to a single organization, and is either hosted on the organization's own data center or a third-party provider's data center. The users have more control and security over the infrastructure and resources, but also have to bear the cost and complexity of managing and maintaining the service. Examples of private cloud providers are VMware, IBM Cloud, and Oracle Cloud.
  - Hybrid cloud: This is a type of cloud computing service that combines the features of both public and private clouds, and allows the users to move data and applications between them as needed. The users can leverage the best of both worlds, such as the scalability and cost-effectiveness of the public cloud, and the security and compliance of the private cloud. Examples of hybrid cloud providers are AWS Outposts, Azure Stack, and Google Anthos.



### Clients for the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing

- A cloud client is a hardware device or software used to access a cloud service .
- A cloud service is a type of computing service that is delivered over the internet and provides scalable and on-demand resources such as computing cycles, data storage, applications, and platforms .
- A cloud client can be classified into three types based on the level of functionality and dependency on the cloud service:
  - Thick client: A thick client is a device or software that has its own operating system, applications, and data, and can function independently of the cloud service. It can also use the cloud service for additional features or backup. Examples of thick clients are personal computers, laptops, and smartphones.
  - Thin client: A thin client is a device or software that has minimal functionality and relies heavily on the cloud service for processing, storage, and applications. It can only function when connected to the cloud service. Examples of thin clients are web browsers, Chromebooks, and some tablets.
  - Zero client: A zero client is a device or software that has no functionality and is only used as an interface to access the cloud service. It has no operating system, applications, or data, and is completely dependent on the cloud service. Examples of zero clients are some smart TVs, gaming consoles, and virtual desktops.



### Cloud Computing Architecture

Cloud computing architecture is the design and structure of the components and subcomponents required for cloud computing. Cloud computing is the delivery of computing services such as servers, storage, databases, networking, software, analytics, and intelligence over the internet. Cloud computing enables organizations to reduce or eliminate their reliance on on-premises server, storage, and networking infrastructure .

The main components of cloud computing architecture are:

- **Front end**: This is the interface that users interact with to access the cloud services. It can be a web browser, a mobile app, a desktop application, or a command-line tool. The front end communicates with the back end through a network, usually the internet.
- **Back end**: This is the collection of servers, storage, databases, and applications that provide the cloud services. The back end can be distributed across multiple locations and managed by different cloud providers. The back end is responsible for processing the requests from the front end, storing and retrieving data, running applications, and ensuring security and availability.
- **Cloud based delivery**: This is the model of how the cloud services are delivered to the users. There are four main types of cloud based delivery: infrastructure as a service (IaaS), platform as a service (PaaS), serverless, and software as a service (SaaS).
  - **IaaS**: This is the most basic type of cloud service, where the cloud provider offers virtualized computing resources such as servers, storage, and networking. The user can rent and configure these resources according to their needs, and pay only for what they use. The user is responsible for managing the operating system, applications, and data on the resources.
  - **PaaS**: This is a type of cloud service where the cloud provider offers a platform for developing, testing, and deploying applications. The platform includes the operating system, middleware, runtime, and tools. The user can focus on writing and running their code, without worrying about the underlying infrastructure. The user pays for the platform usage and the resources consumed by their applications.
  - **Serverless**: This is a type of cloud service where the cloud provider runs and manages the application code on demand, without requiring the user to provision or manage any servers. The user only pays for the execution time and the resources used by their code. The code can be triggered by events such as HTTP requests, database changes, or messages.
  - **SaaS**: This is a type of cloud service where the cloud provider offers a software application that runs on the cloud and is accessible through the internet. The user does not need to install, update, or maintain the software. The user pays for the software subscription or usage, and can access the software from any device.
- **Network**: This is the communication channel that connects the front end and the back end. It can be the internet, an intranet, or an intercloud. The network enables the data transfer and the service delivery between the user and the cloud provider. The network also affects the performance, security, and reliability of the cloud services.

Cloud computing architecture can vary depending on the type, scale, and requirements of the cloud services. However, the basic principles of cloud computing architecture are to ensure scalability, elasticity, availability, reliability, security, and cost-efficiency of the cloud services. Cloud computing architecture also aims to optimize the resource utilization and the service quality of the cloud services .

