

## Unit 1 - Introduction To Cloud Computing

1. **Definition**: Cloud computing is the delivery of computing services, including servers, storage, databases, networking, software, analytics, and intelligence, over the internet to offer faster innovation, flexible resources, and economies of scale.

2. **Characteristics**: Cloud computing has several characteristics that distinguish it from traditional hosting, including on-demand self-service, broad network access, resource pooling, rapid elasticity, and measured service.

3. **Service Models**: There are three main service models of cloud computing: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS).

4. **Deployment Models**: There are four main deployment models of cloud computing: Public Cloud, Private Cloud, Community Cloud, and Hybrid Cloud.

5. **Advantages**: Cloud computing offers several advantages, including cost savings, scalability, flexibility, and security.

6. **Challenges**: Despite its many advantages, cloud computing also presents several challenges, including data privacy, data security, and vendor lock-in.

7. **Trends**: Cloud computing is a rapidly evolving field, with new trends and developments emerging regularly. Some current trends include the rise of multi-cloud and hybrid cloud strategies, the increasing use of artificial intelligence and machine learning in the cloud, and the growing importance of edge computing.




### Definition of Cloud

Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction .

In simpler terms, cloud computing is the delivery of computing services—including servers, storage, databases, networking, software, analytics, and intelligence—over the Internet (“the cloud”) to offer faster innovation, flexible resources, and economies of scale .

Cloud computing is the on-demand availability of computing resources as services over the internet. It eliminates the need for enterprises to procure, configure, or manage resources themselves, and they only pay for what they use .

Cloud computing is on-demand access, via the internet, to computing resources—applications, servers (physical servers and virtual servers), data storage, development tools, networking capabilities, and more—hosted at a remote data center managed by a cloud services provider (or CSP) .



### Evolution of Cloud Computing

1. The evolution of cloud computing can be divided into three basic phases: The Idea Phase, The Pre-Internet Bubble Era, and The Recent Development Phase .
2. The Idea Phase began in the early 1960s with the emergence of utility and grid computing. Joseph Carl Robnett Licklider was the founder of cloud computing .
3. The most recent development of cloud computing has evolved from Web2.0 technology, which caters to web applications that facilitate participatory information sharing, interoperability, and user-centered design. Examples of Web 2.0 include wikis, blogs, social networking, and video sharing .
4. New technologies have emerged recently as a result of the growth of cloud computing. The delivery of many, dynamically scalable, virtualized resources as a service through the Internet is known as cloud computing .
5. Virtualization has played a significant role in the evolution of cloud computing. IBM released an operating system called VM in the 1970s that allowed multiple virtual systems to be run on a single physical system .
6. Virtualization for PC-based systems started in earnest, and as the Internet grew, the idea of delivering computing resources through a global network became more and more feasible .
7. The cloud was born, and since then, it has continued to evolve with new trends such as containers, serverless computing, and improved cloud security .



### Underlying Principles of Parallel and Distributed Computing

- The terms parallel computing and distributed computing are used interchangeably.
- Parallel computing implies a tightly coupled system.
- Distributed systems refers to a wider class of system, including those that are tightly coupled.
- Parallel computing is characterised by homogeneity of components (Uniform Structure).
- Multiple Processors share the same physical memory.
- In systems implementing parallel computing, all the processors share the same memory. They also share the same communication medium and network. The processors communicate with each other with the help of shared memory.
- Distributed systems, on the other hand, have their own memory and processors.
- Distributed computing is often used in tandem with parallel computing. Parallel computing on a single computer uses multiple processors to process tasks in parallel, whereas distributed parallel computing uses multiple computing devices to process those tasks.
- Parallel and distributed computing occurs across many different topic areas in computer science, including algorithms, computer architecture, networks, operating systems, and software engineering.
- During the early 21st century there was explosive growth in multiprocessor design and other strategies for complex applications to run faster.
- The sequential model assumes that only one operation can be executed at a time, and that is true of a single computer with a single processor. However, most modern computers have multi-core processors, where each core can independently execute an operation.



### Cloud Characteristics

Cloud computing is a technology that uses computing resources, including hardware and software, offering services over a network. Here are some of the major characteristics of cloud computing:

1. **Automation**: Automation is an essential characteristic of cloud computing. It is the ability of cloud computing to automatically install, configure, and maintain a cloud service, making the most of technology and reducing manual effort.

2. **Multi-Tenancy**: One of the best characteristics of Cloud Computing is its Multi-Tenancy. Multi-Tenancy is a software architecture that allows a single program instance to serve several user groups. It signifies that numerous cloud provider customers are sharing the same computing resources.

3. **On-demand self-service**: Cloud computing services do not require any human administrators, users themselves are able to provision computing capabilities, such as server time and network storage, as needed automatically without requiring human interaction with each service provider.

4. **Broad network access**: The Computing services are generally provided over standard networks and are accessible through standard mechanisms that promote use by heterogeneous thin or thick client platforms (e.g., mobile phones, tablets, laptops, and workstations).

5. **Resource pooling**: Public cloud providers rely on multi-tenant architectures to accommodate more users at the same time.

6. **Scalability**: Cloud computing allows for easy scalability of resources, allowing users to quickly increase or decrease the amount of resources they are using based on their needs.




### Elasticity in Cloud Computing

Elasticity is a defining characteristic that differentiates cloud computing from previously proposed computing paradigms, such as grid computing. In cloud computing, elasticity is defined as "the degree to which a system is able to adapt to workload changes by provisioning and de-provisioning resources in an autonomic manner, such that at each point in time the available resources match the current demand as closely as possible".

Elasticity in cloud computing is the ability for the organization to adjust its storage requirements in terms of capacity and processing with respect to operational requirements. This has the following benefits:

- Elasticity allows you to scale computer processing, memory, and storage capacity to meet changing demands.
- Elasticity can refer to ‘cloudbursting’ from on-premises infrastructure into the public cloud for example to meet a sudden or seasonal demand.
- Elasticity can also refer to the ability to grow or shrink the resources used by a cloud-based application.
- Scalability will prevent you from having to worry about capacity planning and peak engineering.



### On‐demand Provisioning

On-demand provisioning, also referred to as “on-demand cloud provisioning,” is a delivery model in which cloud resources are deployed to match customers’ fluctuating demands . Customers are provided with resources on runtime, meaning that the resources are made available as and when they are needed . This is one of the biggest advantages of cloud computing as it eliminates the need for creating buffer resources .

On-demand resource provision is also used to reduce the cost of the edge cloud . The load estimation is used to estimate the load of the next cycle in advance and to ensure that the resources available in the edge cloud can meet the load requirements .

In summary, on-demand provisioning in cloud computing allows for the efficient and cost-effective allocation of resources to meet the changing demands of customers. This is achieved through the use of load estimation and the provision of resources on runtime.



## Unit 2 - Cloud Enabling Technologies Service Oriented Architecture

Service Oriented Architecture (SOA) is an architectural style that supports service orientation. It is a way of designing, developing, deploying, and managing enterprise systems where services are the main construct for achieving the desired functionality.

Some key characteristics of SOA include:

1. **Loose coupling:** Services are designed to be loosely coupled, meaning that they can be used and reused without being tightly bound to other services or systems.
2. **Reusability:** Services are designed to be reusable, meaning that they can be used in multiple contexts and by multiple applications.
3. **Interoperability:** Services are designed to be interoperable, meaning that they can work with other services and systems, regardless of the underlying technology or platform.
4. **Abstraction:** Services abstract the underlying implementation details, meaning that the service consumer does not need to know how the service is implemented.
5. **Discoverability:** Services are designed to be discoverable, meaning that they can be easily found and used by service consumers.

SOA is an important enabling technology for cloud computing, as it provides a way to build and deploy scalable, flexible, and reusable services that can be consumed by cloud-based applications. By using SOA, organizations can take advantage of the benefits of cloud computing, such as increased agility, reduced costs, and improved scalability, while still maintaining control over their services and data.



### REST and Systems of Systems

- REST stands for Representational State Transfer. It is an architectural style for designing networked applications.
- REST is a set of constraints applied to the architecture of systems that use the HTTP protocol for communication.
- Systems of Systems (SoS) refers to a collection of systems that are integrated to create a larger, more complex system.
- SoS is used to solve problems that cannot be addressed by a single system.
- In the context of cloud computing, REST and SoS are used in Service Oriented Architecture (SOA).
- SOA is an architectural style that supports the creation of services that can be reused and combined to create composite applications.
- Web services are a common implementation of SOA, using standards such as SOAP and REST to enable communication between services.
- The Publish-Subscribe model is a messaging pattern used in SOA, where messages are sent to subscribers based on their interests rather than a specific destination.
- Virtualization is a key enabling technology for cloud computing, allowing multiple virtual machines to run on a single physical host.
- There are different types of virtualization, including full and para-virtualization, and different levels of implementation, including virtualization of CPU, memory, and I/O devices.
- Virtualization tools and mechanisms are used to manage and support virtualized environments, including disaster recovery.




### Web Services

Web services are a key component of Service Oriented Architecture (SOA) and Cloud Computing. They provide a standardized way for applications to communicate with each other over the internet.

1. **Definition:** A web service is a software system designed to support interoperable machine-to-machine interaction over a network. It has an interface described in a machine-processable format, such as WSDL (Web Services Description Language).

2. **Communication:** Web services use XML (eXtensible Markup Language) to encode data and SOAP (Simple Object Access Protocol) to transport it.

3. **Types of Web Services:** There are two main types of web services: SOAP and REST (Representational State Transfer). SOAP is a protocol for exchanging structured information, while REST is an architectural style for building web services.

4. **Advantages:** Web services provide several advantages, including platform independence, language independence, and loose coupling. This means that applications written in different languages and running on different platforms can communicate with each other using web services.

5. **Usage:** Web services are widely used in cloud computing, where they enable applications to access cloud-based resources and services. They are also used in enterprise applications, where they provide a way to integrate disparate systems.

6. **Standards:** There are several standards related to web services, including WSDL, SOAP, and UDDI (Universal Description, Discovery, and Integration). These standards provide a common framework for building and using web services.

7. **Security:** Security is an important consideration when using web services. There are several mechanisms for securing web services, including SSL (Secure Sockets Layer), WS-Security, and SAML (Security Assertion Markup Language).

In summary, web services are a key technology for building distributed systems and enabling interoperability between applications. They provide a standardized way to communicate over the internet and are widely used in cloud computing and enterprise applications.



### Publish, Subscribe Model

The publish-subscribe model is a messaging pattern used in distributed systems. It is a part of the Service Oriented Architecture (SOA) in Cloud Computing. In this model, messages are sent from publishers to subscribers through a message broker. The message broker is responsible for routing the messages to the appropriate subscribers.

1. **Publishers** are the entities that produce messages and send them to the message broker. They do not have any knowledge about the subscribers or the routing of the messages.
2. **Subscribers** are the entities that receive messages from the message broker. They express their interest in receiving certain types of messages by subscribing to a specific topic or pattern.
3. **Message Broker** is the intermediary between the publishers and subscribers. It is responsible for routing the messages from the publishers to the appropriate subscribers based on their subscriptions.

The publish-subscribe model has several advantages, including:

- **Decoupling**: Publishers and subscribers are decoupled, meaning that they do not need to have any knowledge about each other. This allows for greater flexibility and scalability in the system.
- **Scalability**: The message broker can handle a large number of publishers and subscribers, allowing the system to scale easily.
- **Flexibility**: Subscribers can dynamically subscribe and unsubscribe to topics, allowing them to receive only the messages they are interested in.

This model is commonly used in event-driven systems, where events are generated by publishers and consumed by subscribers. It is also used in systems where data needs to be disseminated to multiple subscribers in real-time, such as stock market data or news feeds.

In summary, the publish-subscribe model is a messaging pattern that allows for decoupling, scalability, and flexibility in distributed systems. It is commonly used in event-driven systems and real-time data dissemination. It is an important concept in the Service Oriented Architecture (SOA) in Cloud Computing.



### Basics of Virtualization

Virtualization is the creation of a virtual version of something, such as an operating system, a server, a storage device, or network resources. It allows multiple operating systems to run on a single physical machine, sharing the underlying hardware resources.

1. **Types of Virtualization**: There are several types of virtualization, including server virtualization, storage virtualization, network virtualization, and desktop virtualization.
2. **Hypervisor**: A hypervisor is a software layer that enables virtualization by allowing multiple operating systems to share a single hardware host. It manages the virtual machines and allocates the physical resources, such as CPU, memory, and storage, to the virtual machines.
3. **Benefits of Virtualization**: Virtualization can provide several benefits, including cost savings, improved resource utilization, increased flexibility, and simplified management.
4. **Virtual Machine**: A virtual machine is a software-based representation of a physical computer. It runs its own operating system and applications, and is isolated from other virtual machines on the same physical host.
5. **Virtualization in Cloud Computing**: Virtualization is a key enabling technology for cloud computing. It allows cloud providers to create and manage virtual machines, providing customers with scalable and flexible computing resources on demand.




### Types of Virtualization

Virtualization is the creation of a virtual version of something, such as an operating system, a server, a storage device, or network resources. There are several types of virtualization, including:

1. **Hardware Virtualization**: This type of virtualization involves creating virtual machines that act like real computers with their own operating systems. The virtual machines are created and managed by a hypervisor, which is a software layer that sits between the hardware and the virtual machines.

2. **Operating System Virtualization**: This type of virtualization involves running multiple operating systems on a single physical server. Each operating system runs in its own virtual environment and is isolated from the others.

3. **Storage Virtualization**: This type of virtualization involves creating virtual storage devices that can be used by multiple servers. The virtual storage devices are created and managed by a storage virtualization software layer.

4. **Network Virtualization**: This type of virtualization involves creating virtual networks that can be used by multiple servers. The virtual networks are created and managed by a network virtualization software layer.

5. **Application Virtualization**: This type of virtualization involves running applications in a virtual environment that is isolated from the underlying operating system and hardware. This allows multiple applications to run on a single server without interfering with each other.

These are some of the main types of virtualization used in cloud computing. Each type of virtualization has its own benefits and use cases, and they can be used in combination to create powerful and flexible cloud environments.



### Implementation Levels of Virtualization

Virtualization is a technology that enables the creation of multiple virtual environments on a single physical system. There are several levels at which virtualization can be implemented, including:

1. **Hardware-level virtualization:** This involves virtualizing the physical hardware resources of a system, such as the CPU, memory, and storage, to create multiple virtual machines that can run different operating systems and applications.

2. **Operating system-level virtualization:** This involves virtualizing the operating system itself, allowing multiple isolated user-space instances to run on a single physical system. Each instance appears to have its own operating system, but in reality, they all share the same underlying kernel.

3. **Application-level virtualization:** This involves virtualizing individual applications, allowing them to run in isolated environments on the same physical system. This can be useful for running multiple versions of the same application, or for running applications that may conflict with each other if installed on the same system.

These different levels of virtualization provide varying degrees of isolation and resource utilization, and can be used in different scenarios depending on the specific needs of the user. They are all important components of cloud computing, enabling the efficient use of resources and the ability to scale services on demand.



### Virtualization Structures

Virtualization is a technology that allows multiple operating systems and applications to run on a single physical server. It is a key enabling technology for cloud computing, as it allows for the efficient sharing of resources and the creation of flexible, scalable, and cost-effective cloud environments.

There are several types of virtualization structures, including:

1. **Hardware virtualization:** This involves the creation of virtual machines that run on top of a hypervisor, which is a layer of software that sits between the hardware and the operating systems. The hypervisor manages the allocation of resources to the virtual machines and ensures that they are isolated from each other.

2. **Operating system virtualization:** This involves the creation of multiple isolated user-space instances, known as containers, on a single operating system kernel. Each container has its own file system, networking, and resource allocation, but shares the underlying kernel with other containers.

3. **Application virtualization:** This involves the encapsulation of an application and its dependencies into a self-contained package that can be run on any compatible operating system. This allows for the easy deployment and management of applications, as well as the ability to run multiple versions of the same application on the same system.

4. **Storage virtualization:** This involves the abstraction of physical storage resources into a single, logical storage pool that can be managed and allocated as needed. This allows for the efficient utilization of storage resources and the ability to easily scale storage capacity as needed.

5. **Network virtualization:** This involves the creation of virtual networks that can be managed and configured independently of the underlying physical network infrastructure. This allows for the creation of flexible, scalable, and secure network environments.

Virtualization structures are a key component of cloud computing, as they allow for the efficient sharing of resources and the creation of flexible, scalable, and cost-effective cloud environments. By understanding the different types of virtualization structures, it is possible to design and implement effective cloud solutions.



### Tools and Mechanisms for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

1. **Service Oriented Architecture (SOA)**: SOA is an architectural style that supports service orientation. It is a way of designing, developing, deploying, and managing enterprise systems where services are the main construct for achieving the desired functionality.

2. **Enterprise Service Bus (ESB)**: An ESB is a middleware tool used to distribute work among connected components of an application. It is used to integrate different systems by providing a communication channel between them.

3. **Web Services**: Web services are a standardized way of integrating web-based applications using XML, SOAP, WSDL, and UDDI open standards over an internet protocol backbone.

4. **Representational State Transfer (REST)**: REST is an architectural style for building web services. It is based on the idea that resources are identified by URIs and can be manipulated using standard HTTP methods.

5. **Simple Object Access Protocol (SOAP)**: SOAP is a messaging protocol used for exchanging structured information between applications over a network.

6. **Web Services Description Language (WSDL)**: WSDL is an XML-based language used to describe the functionality offered by a web service.

7. **Universal Description, Discovery, and Integration (UDDI)**: UDDI is a platform-independent, XML-based registry for businesses to list their web services.




### Virtualization of CPU

Virtualization of CPU refers to the process of creating a virtual version of a physical CPU. This allows multiple operating systems to share a single physical CPU, as each operating system is provided with its own virtual CPU. This is achieved through the use of a hypervisor, which is a software layer that sits between the physical hardware and the virtual machines.

Some key points to note about CPU virtualization are:

1. CPU virtualization allows multiple operating systems to run on a single physical CPU.
2. A hypervisor is used to manage the virtual CPUs and allocate resources to the virtual machines.
3. CPU virtualization can improve the efficiency of resource utilization, as multiple virtual machines can share the same physical resources.
4. CPU virtualization can also improve security, as each virtual machine is isolated from the others, reducing the risk of a security breach affecting multiple systems.

Overall, CPU virtualization is an important technology in cloud computing, as it enables the efficient and secure sharing of physical resources among multiple virtual machines. This is a key enabler of the scalability and flexibility of cloud computing services.



### Memory

Memory is a crucial component in cloud computing, as it enables the storage and retrieval of data and instructions. In the context of cloud enabling technologies and service-oriented architecture, memory plays a vital role in the efficient functioning of the system.

Here are some key points to consider when studying memory in Unit 2 - Cloud Enabling Technologies Service Oriented Architecture:

1. Memory is used to store data and instructions that are required for the execution of programs and services.
2. Memory can be classified into two types: volatile and non-volatile. Volatile memory, such as RAM, loses its contents when the power is turned off, while non-volatile memory, such as a hard drive, retains its contents even when the power is turned off.
3. Memory management is an important aspect of cloud computing, as it ensures that memory is allocated and deallocated efficiently to prevent wastage of resources.
4. Memory virtualization is a technique used in cloud computing to provide a virtual memory space to applications, allowing them to access more memory than is physically available on the system.
5. Memory caching is another technique used in cloud computing to improve performance by storing frequently accessed data in a cache, reducing the need to access slower storage devices.

These are some of the key points to consider when studying memory in the context of cloud enabling technologies and service-oriented architecture. It is important to have a thorough understanding of these concepts to fully grasp the subject of cloud computing.



### I/O Devices

I/O devices, or input/output devices, are hardware components that allow a computer to interact with its environment. These devices can be classified into two categories: input devices and output devices.

Input devices are used to provide data and control signals to the computer. Some common input devices include:

1. Keyboard: A device used to input text and commands into the computer.
2. Mouse: A pointing device used to control the movement of a cursor on the screen.
3. Microphone: A device used to input audio into the computer.
4. Scanner: A device used to input images or documents into the computer.
5. Camera: A device used to input video or still images into the computer.

Output devices, on the other hand, are used to display or output data from the computer. Some common output devices include:

1. Monitor: A device used to display visual output from the computer.
2. Printer: A device used to produce a hard copy of the computer's output.
3. Speakers: A device used to output audio from the computer.
4. Projector: A device used to display the computer's output on a large screen.

I/O devices are essential components of a computer system, as they allow the computer to interact with its environment and perform tasks such as data input, data output, and user interaction. These devices are typically connected to the computer via ports, such as USB or HDMI, and can be either internal or external to the computer. In the context of cloud computing, I/O devices can be used to interact with cloud services and applications, allowing users to access and manipulate data stored in the cloud.



### Virtualization Support and Disaster Recovery

Virtualization is a technology that allows multiple operating systems to run on a single physical server. This technology is used to increase the efficiency of the server and reduce the cost of hardware. Virtualization support is an important aspect of cloud computing, as it allows for the creation of virtual machines that can be used to run different applications and services.

Disaster recovery is the process of restoring data and systems in the event of a disaster. In the context of cloud computing, disaster recovery involves the use of virtualization technology to create backups of data and systems that can be quickly restored in the event of a disaster. This allows for a faster recovery time and reduces the risk of data loss.

Some key points to consider when discussing virtualization support and disaster recovery in cloud computing include:

1. Virtualization technology allows for the creation of virtual machines that can run different operating systems and applications.
2. Virtualization support is important for cloud computing, as it increases the efficiency of the server and reduces the cost of hardware.
3. Disaster recovery involves the use of virtualization technology to create backups of data and systems that can be quickly restored in the event of a disaster.
4. Disaster recovery in cloud computing allows for a faster recovery time and reduces the risk of data loss.



## Unit 3 - Cloud Architecture, Services And Storage

Cloud computing is a model for enabling convenient, on-demand network access to a shared pool of configurable computing resources. These resources can include networks, servers, storage, applications, and services. Cloud computing allows users to access these resources with minimal management effort or service provider interaction.

Cloud architecture refers to the various components and subcomponents required for cloud computing. These components typically consist of a front-end platform, back-end platforms, a cloud-based delivery, and a network.

Cloud services refer to the wide range of services delivered on demand to companies and customers over the internet. These services are designed to provide easy, affordable access to applications and resources, without the need for internal infrastructure or hardware.

Cloud storage is a model of computer data storage in which the digital data is stored in logical pools. The physical storage spans multiple servers, and the physical environment is typically owned and managed by a hosting company.

Some key points to remember about cloud architecture, services, and storage are:

1. Cloud computing allows for convenient, on-demand access to a shared pool of computing resources.
2. Cloud architecture refers to the various components and subcomponents required for cloud computing.
3. Cloud services are designed to provide easy, affordable access to applications and resources.
4. Cloud storage is a model of computer data storage in which the digital data is stored in logical pools.
5. The physical storage of cloud storage spans multiple servers and is typically owned and managed by a hosting company.



### Layered Cloud Architecture Design

1. Layered cloud architecture design is a common approach to organizing and managing cloud computing resources.
2. This design involves dividing the cloud infrastructure into layers, with each layer responsible for a specific function or service.
3. The layers are typically arranged in a hierarchical manner, with the lower layers providing the foundation for the higher layers.
4. The most common layers in a layered cloud architecture design are the infrastructure layer, the platform layer, and the application layer.
5. The infrastructure layer is responsible for providing the physical and virtual resources required to support the cloud environment, such as servers, storage, and networking.
6. The platform layer provides a runtime environment for cloud applications, including operating systems, middleware, and runtime libraries.
7. The application layer is where cloud applications are deployed and run, providing the end-user with the desired functionality and services.
8. By separating the cloud infrastructure into layers, it is possible to achieve greater flexibility, scalability, and manageability in the cloud environment.
9. Each layer can be independently managed and scaled, allowing for more efficient use of resources and improved performance.
10. Layered cloud architecture design is widely used in both public and private cloud environments, and is a key concept in the field of cloud computing.



### NIST Cloud Computing Reference Architecture

The National Institute for Standard and Technology (NIST) created Special Publication (SP) 500-292, “NIST Cloud Computing Reference Architecture,” in September 2011 to establish a baseline cloud computing architecture . The NIST Cloud Computing Reference Architecture defines services and relationships between cloud service providers, consumers, and other stakeholders .

The most critical stakeholders in the NIST Cloud Computing Reference Architecture are consumers and providers. The entire architecture, comprising five “Architectural Components,” can be understood as a way of defining the relationships between them .

NIST aims to foster cloud computing systems and practices that support interoperability, portability, and security requirements that are appropriate and achievable for important usage scenarios .



### Public, Private and Hybrid Clouds

Unit 3 - Cloud Architecture, Services And Storage in the subject of Cloud Computing

- **Public Cloud**: A public cloud is a type of cloud computing in which a service provider makes resources, such as virtual machines (VMs), applications or storage, available to the general public over the internet. Public cloud services may be free or offered on a pay-per-usage model.

- **Private Cloud**: A private cloud is a model of cloud computing where IT services are provisioned over private IT infrastructure for the dedicated use of a single organization. A private cloud is usually managed via internal resources.

- **Hybrid Cloud**: A hybrid cloud is a cloud computing environment that uses a mix of on-premises, private cloud and third-party, public cloud services with orchestration between the two platforms. By allowing workloads to move between private and public clouds as computing needs and costs change, hybrid cloud gives businesses greater flexibility and more data deployment options.



### IaaS (Infrastructure as a Service)
IaaS is one of the three main categories of cloud computing services, alongside Software as a Service (SaaS) and Platform as a Service (PaaS). IaaS provides virtualized computing resources over the internet. It is a form of cloud computing that provides virtualized computing resources over the internet.

- IaaS is a self-service model for accessing, monitoring, and managing remote data center infrastructures.
- IaaS allows businesses to purchase resources on-demand and as-needed instead of having to buy hardware outright.
- IaaS resources are scalable and elastic, meaning they can be adjusted as needed.
- IaaS provides a high level of flexibility and control over IT resources.
- IaaS is typically billed on a pay-as-you-go basis, meaning businesses only pay for the resources they use.
- IaaS is commonly used for web hosting, virtual data centers, and development and testing environments.




### PaaS

Platform as a Service (PaaS) is a cloud infrastructure layer that provides resources to build user-level tools and applications. It includes the underlying infrastructure including compute, network, and storage resources, as well as development tools, database management systems, and middleware .

PaaS is a primary tier of modern cloud infrastructures. The base stack is Infrastructure as a Service (IaaS), which provides compute, network, and storage resources. PaaS is at the middle of the stack between IaaS and Software as a Service (SaaS). PaaS is dependent on IaaS but also enables SaaS.

PaaS is a complete development and deployment environment in the cloud, with resources that enable you to deliver everything from simple cloud-based apps to sophisticated, cloud-enabled enterprise applications.



### SaaS

- SaaS stands for Software as a Service. It is a cloud service model where vendor applications run on a cloud infrastructure.
- SaaS offers a variety of services such as file storage, backup data system, web-based email, and project management tools.
- SaaS architecture refers to a method of software delivery, in which a vendor hosts an application on a remote server for an organization before delivering the app’s capabilities to that organization’s end users over the Internet.
- This model allows multiple companies or organizations to share a single model and a single configuration.
- SaaS differs from both Infrastructure-as-a-Service (IaaS) and Platform-as-a-service (PaaS). In IaaS, a cloud computing service provides an organization access to computing resources such as servers, storage, and networking in the cloud.
- SaaS eliminates the maintenance work that comes with locally installed software, such as purchasing, installing, and maintaining it.
- Common examples of SaaS are email, calendaring, and office tools (such as Microsoft Office 365).
- SaaS provides a complete software solution that you purchase on a pay-as-you-go basis from a cloud service provider.



### Architectural Design Challenges

When designing a cloud architecture, there are several challenges that must be considered:

1. **Scalability:** The architecture must be able to handle an increasing amount of work and data, and be able to scale up or down as needed.
2. **Availability:** The architecture must be designed to ensure that the system is always available and accessible to users, even in the event of failures or outages.
3. **Security:** The architecture must be designed to protect against unauthorized access and data breaches, and to ensure the confidentiality, integrity, and availability of data.
4. **Performance:** The architecture must be designed to provide fast and efficient access to data and services, and to minimize latency and response times.
5. **Cost:** The architecture must be designed to minimize costs, while still providing the necessary level of performance, availability, and security.
6. **Interoperability:** The architecture must be designed to allow for integration with other systems and services, and to support data exchange and communication between different systems.
7. **Manageability:** The architecture must be designed to allow for easy management and monitoring of the system, and to provide tools and interfaces for managing and configuring the system.
8. **Portability:** The architecture must be designed to allow for easy migration of data and services between different cloud providers or platforms.

These challenges must be carefully considered and addressed when designing a cloud architecture, in order to ensure that the system is able to meet the needs of users and provide the necessary level of performance, availability, security, and cost-effectiveness.



### Cloud Storage

Cloud storage is a model of computer data storage in which the digital data is stored in logical pools. The physical storage spans multiple servers, and the physical environment is typically owned and managed by a hosting company. These cloud storage providers are responsible for keeping the data available and accessible, and the physical environment protected and running. People and organizations buy or lease storage capacity from the providers to store user, organization, or application data.

Cloud storage services may be accessed through a co-located cloud computing service, a web service application programming interface (API) or by applications that utilize the API, such as cloud desktop storage, a cloud storage gateway, or Web-based content management systems.

Some key points to remember about cloud storage are:
- Cloud storage is a model of storing data on remote servers.
- Data is stored in logical pools across multiple servers.
- The physical environment is owned and managed by a hosting company.
- Cloud storage providers are responsible for keeping the data available and accessible.
- Storage capacity can be bought or leased from the providers.
- Cloud storage can be accessed through various means, including APIs and web-based systems.



### Storage‐as‐a‐Service
- Storage‐as‐a‐Service (STaaS) is a cloud storage service that you rent from a Cloud Service Provider (CSP) and that provides basic ways to access that storage.
- Enterprises, small and medium businesses, home offices, and individuals can use the cloud for multimedia storage, data repositories, data backup and recovery, and disaster recovery.
- STaaS is more cost-efficient than building private storage infrastructure, especially when you can match data types to cloud storage offerings.
- STaaS is a subscription service model where a storage provider supplies access to storage and compute resources both on-premises and/or over the cloud.
- STaaS saves you money through operating expenditure (OPEX) agility—you only pay for the storage you need, when you need it.
- STaaS is a subscription model where a client rents cloud space from a third-party provider and uses the space to store their digital information.



### Advantages of Cloud Storage

1. **Scalability**: Cloud storage allows for easy scalability of storage capacity, meaning that users can increase or decrease their storage needs as required without having to worry about purchasing and maintaining additional hardware.

2. **Accessibility**: Cloud storage can be accessed from anywhere with an internet connection, making it easy for users to access their data from any location.

3. **Cost-effective**: Cloud storage can be more cost-effective than traditional storage methods, as users only pay for the storage they use and do not have to invest in expensive hardware.

4. **Disaster recovery**: Cloud storage can provide an effective solution for disaster recovery, as data is stored off-site and can be easily retrieved in the event of a disaster.

5. **Collaboration**: Cloud storage makes it easy for users to collaborate on documents and projects, as multiple users can access and work on the same files simultaneously.

6. **Automatic backups**: Many cloud storage providers offer automatic backups, ensuring that data is always backed up and protected.

7. **Security**: Cloud storage providers often have robust security measures in place to protect user data, including encryption and access controls.




### Cloud Storage Providers

Cloud storage providers offer online storage and backup services for personal and business use. These services allow users to store, access, and share data from anywhere with an internet connection. Some of the most popular cloud storage providers include:

1. **Sync.com** - A cloud storage service with excellent file sharing, versioning, and security features .
2. **pCloud** - A cloud storage provider that offers excellent lifetime plans .
3. **Livedrive** - A cloud storage provider .
4. **Icedrive** - A cloud storage provider that offers excellent lifetime plans .
5. **Polarbackup** - A cloud storage provider .
6. **Zoolz BigMIND** - A cloud storage provider .
7. **IBackup** - A cloud storage provider .
8. **IDrive** - A cloud storage provider that tops the charts with its easy-to-use desktop and mobile apps, excellent backup features, strong security, and great value .
9. **Amazon Cloud Drive** - A cloud storage provider .
10. **Dropbox** - A cloud storage provider that is a big corporate player .
11. **Google Drive** - A cloud storage provider that is a big corporate player .
12. **Microsoft OneDrive** - A cloud storage provider that is a big corporate player .
13. **Box** - A cloud storage provider .
14. **iCloud** - A cloud storage provider for Mac .
15. **OpenDrive** - A cloud storage provider .
16. **Tresorit** - A cloud storage provider .
17. **Amazon S3** - A cloud storage provider .

When selecting a cloud storage provider, it is important to consider the platform for use, such as Windows, Mac, iPhone, Android, or BlackBerry phones . Some cloud storage services, such as Apple iCloud, Google Drive, and Microsoft OneDrive, are generalists, offering not only folder and file syncing but also media-playing and device syncing .



### S3 - Cloud Architecture, Services And Storage

- Amazon Simple Storage Service (Amazon S3) is a scalable, high-speed, web-based cloud storage service designed for online backup and archiving of data and applications on Amazon Web Services (AWS) .
- S3 is an object storage service, which differs from other types of cloud computing storage types, such as block and file storage. Each object is stored as a file with its metadata included and is also given an ID number .
- The S3 object storage cloud service gives a subscriber access to the same systems that Amazon uses to run its own websites. S3 enables customers to upload, store and download practically any file or object that is up to 5 terabytes (TB) in size -- with the largest single upload capped at 5 gigabytes (GB) .
- Amazon S3 has storage management features that you can use to manage costs, meet regulatory requirements, reduce latency, and save multiple distinct copies of your data for compliance requirements. S3 Lifecycle – Configure a lifecycle configuration to manage your objects and store them cost effectively throughout their lifecycle .
- Amazon S3 is cloud object storage with industry-leading scalability, data availability, security, and performance. S3 is ideal for data lakes, mobile applications, backup and restore, archival, IoT devices, ML, AI, and analytics .
- Use Amazon S3 to store and retrieve any amount of data using highly scalable, reliable, fast, and inexpensive data storage. User Guide Provides detailed information and instructions for getting started, developing, and working with Amazon S3 using the AWS Management Console, AWS CLI, AWS SDKs, and REST API .



## Unit 4 - Resource Management And Security In Cloud

1. **Resource Management in Cloud Computing:** Cloud computing allows for the efficient allocation and management of resources, including storage, processing power, and bandwidth. This is achieved through the use of virtualization technologies, which allow multiple virtual machines to share the same physical resources.

2. **Scalability and Elasticity:** One of the key benefits of cloud computing is the ability to scale resources up or down as needed. This is known as elasticity. Cloud providers offer a range of tools and services to help customers manage their resource usage and scale their infrastructure as needed.

3. **Security in Cloud Computing:** Security is a critical concern in cloud computing. Cloud providers implement a range of security measures to protect customer data and applications, including encryption, firewalls, and access controls. Customers are also responsible for implementing their own security measures, such as strong passwords and regular backups.

4. **Data Protection and Privacy:** Cloud providers are subject to data protection and privacy regulations, and must comply with these regulations to protect customer data. Customers are also responsible for ensuring that their data is stored and processed in compliance with relevant regulations.

5. **Disaster Recovery and Business Continuity:** Cloud computing can help organizations to improve their disaster recovery and business continuity capabilities. Cloud providers offer a range of tools and services to help customers to backup their data and applications, and to quickly recover from disasters.

6. **Compliance and Auditing:** Cloud providers are subject to a range of compliance and auditing requirements, and must demonstrate that they are meeting these requirements. Customers are also responsible for ensuring that their use of cloud services is compliant with relevant regulations and standards.

7. **Identity and Access Management:** Identity and access management is a critical component of cloud security. Cloud providers offer a range of tools and services to help customers to manage user identities and access to cloud resources. Customers are responsible for implementing strong access controls and for regularly reviewing user access to ensure that it is appropriate.

8. **Threat and Vulnerability Management:** Cloud providers implement a range of measures to protect their infrastructure from threats and vulnerabilities. Customers are also responsible for implementing their own threat and vulnerability management measures, such as regular vulnerability scanning and patch management.

9. **Monitoring and Logging:** Monitoring and logging are important for maintaining the security and availability of cloud resources. Cloud providers offer a range of tools and services to help customers to monitor their resource usage and to log events. Customers are responsible for regularly reviewing their logs to identify and respond to security incidents.

10. **Incident Response and Forensics:** Cloud providers have incident response and forensics capabilities to help customers to respond to security incidents. Customers are responsible for implementing their own incident response plans and for working with their cloud provider to investigate and respond to security incidents.



### Inter Cloud Resource Management

- Inter-Cloud Resource Management is the process of combining numerous various separate clouds into a single fluid mass for on-demand operations when a cloud’s infrastructure’s processing and storage capacity could be exhausted.

- One of the types of Inter-Cloud Resource Management is Federation Clouds, where several cloud service providers willingly link their cloud infrastructures together to exchange resources. Cloud service providers in the federation trade resources in an open manner.

- The inter-cloud initiatives OPTIMUS, contrail, MOSAIC, STRATOS, and commercial cloud management solutions leverage multi-cloud services.

- Multi-Cloud Libraries is another type of Inter-Cloud Resource Management where clients use a uniform cloud API as a library to create their own brokers. Inter clouds that employ libraries make it easier to use clouds consistently.

- Intercloud computing or cloud federation is a scenario where clouds have to communicate with other clouds and share their resources for scalability and better service provisioning. Resource management is one of the key concerns to be addressed in Intercloud computing.



### Resource Provisioning

Resource provisioning is the process of allocating, deploying, and managing computing resources in a cloud computing environment. This includes the allocation of virtual machines, storage, and network resources to meet the demands of cloud users. The goal of resource provisioning is to ensure that the cloud infrastructure is used efficiently and that users have access to the resources they need when they need them.

Some key points to consider when discussing resource provisioning in cloud computing include:

1. **Elasticity**: One of the main benefits of cloud computing is the ability to scale resources up or down as needed. Resource provisioning plays a key role in enabling this elasticity by allowing cloud providers to quickly allocate and de-allocate resources in response to changing demand.

2. **Automation**: Resource provisioning is often automated, with cloud providers using algorithms and tools to manage the allocation of resources. This can help to reduce the time and effort required to provision resources, and can also help to ensure that resources are used efficiently.

3. **Monitoring**: In order to effectively provision resources, cloud providers need to monitor the usage of their infrastructure. This can help them to identify trends and patterns in resource usage, and to make informed decisions about when and how to allocate resources.

4. **Service Level Agreements (SLAs)**: Cloud providers often offer SLAs to their customers, which specify the level of service that the customer can expect. Resource provisioning plays a key role in enabling cloud providers to meet these SLAs by ensuring that the necessary resources are available to meet the demands of their customers.

Overall, resource provisioning is a critical component of cloud computing, and is essential for ensuring that cloud users have access to the resources they need in a timely and efficient manner. It involves a combination of automation, monitoring, and management to ensure that resources are used effectively and that cloud providers are able to meet the demands of their customers.



### Resource Provisioning Methods

Resource provisioning is the process of allocating resources to applications and services in a cloud computing environment. There are several methods for resource provisioning in cloud computing, including:

1. **Static Provisioning or Advance Provisioning**: Static provisioning can be used successfully for applications with known and typically constant demands or workloads. In this method, resources are allocated in advance based on the expected demand.

2. **Dynamic Provisioning or On-demand Provisioning**: With dynamic provisioning, the provider adds resources as needed and subtracts them as they are no longer required. This method is more flexible and can better handle changes in demand.

3. **Virtualization**: Virtualization techniques and commodity infrastructures are used in cloud computing to efficiently partition resources and gain a higher utilization rate.

4. **Monitoring Agent with Fuzzy Logic**: A monitoring agent with fuzzy logic is used for resource provisioning in cloud computation. This method is better in terms of performance and security levels compared with other methods.

There are also several tools available for cloud provisioning, including Google Cloud Deployment Manager, IBM Cloud Orchestrator, AWS CloudFormation, and Microsoft Azure Resource Manager.



### Global Exchange of Cloud Resources

- In cloud computing, large numbers of customers use cloud services from all over the world. To ensure reliability in the cloud server, the service provider establishes various data centers in different locations worldwide.
- For example, the famous e-commerce website A-m-a-z-o-n has data centers in different geographical areas across the world.
- Global Cloud Xchange (GCX) is a company that provides network services for enterprises, new media providers, and telecoms carriers. In September 2022, it was acquired by 3i Infrastructure for $512 million.
- The principal elements of the Global Cloud Xchange Global Network include five subsea cable systems operating on major global data traffic routes: the Trans-Atlantic route, the Europe-Asia route, the Europe-Middle East and Egypt route, and the Intra-Asia route.
- The five largest hyperscale public cloud providers that disclose segmented revenues saw their combined revenues grow by 31% in 2019 to US$94 billion.
- Despite widespread tech spending weakness in calendar Q1 2020, revenues grew by 31% over the same period in the previous year.
- Some of the top cloud infrastructure and data solutions IPOs include Asana, an enterprise productivity SaaS solution, IPO’d at $19 billion in September 2020, and Snowflake, a data warehousing company IPO’d at $33.2 billion and is recently valued at $96 billion.



### Security Overview

1. **Cloud security** refers to the technologies, policies, and procedures that are put in place to protect cloud-based systems, data, and infrastructure.
2. **Threats** to cloud security can come from both external and internal sources, and can include unauthorized access, data breaches, and malicious attacks.
3. **Cloud service providers** typically implement a range of security measures to protect their customers' data, including encryption, firewalls, and access controls.
4. **Customers** also have a responsibility to ensure the security of their data in the cloud, by using strong passwords, regularly updating software, and being vigilant against phishing attacks.
5. **Compliance** with industry standards and regulations, such as the General Data Protection Regulation (GDPR), is also an important aspect of cloud security.
6. **Risk management** involves identifying, assessing, and mitigating risks to cloud security, and is an ongoing process that requires regular review and updating.
7. **Incident response** plans should be in place to quickly and effectively respond to security breaches or other incidents that may compromise cloud security.
8. **Security audits** and assessments can help to identify vulnerabilities and areas for improvement in cloud security, and should be carried out regularly.



### Cloud Security Challenges

Cloud security is a major concern for organizations that are moving their data and applications to the cloud. Here are some of the key challenges that organizations face when it comes to cloud security:

1. **Data breaches**: One of the most important challenges of cloud security is the risk of data breaches and issues of data privacy.
2. **Data loss**: Among the many cloud security challenges in cloud computing and cloud storage, the common challenge is the risk of data loss.
3. **Delayed software updates and patch management**: Delayed software updates and patch management is another challenge that organizations face when it comes to cloud security.
4. **Malware Injection**: Malware injection is another challenge that organizations face when it comes to cloud security.
5. **Insufficient identity, credential, access, and key management**: Insufficient identity, credential, access, and key management is another challenge that organizations face when it comes to cloud security.
6. **DoS and DDoS attacks**: DoS and DDoS attacks are another challenge that organizations face when it comes to cloud security.

These are some of the key challenges that organizations face when it comes to cloud security. It is important for organizations to have a strong cloud security strategy in place to mitigate these risks and protect their data and applications in the cloud.



### Software‐as‐a‐Service Security

Software‐as‐a‐Service (SaaS) Security refers to the practices and policies implemented by the providers of SaaS to ensure the privacy and security of customer data in cloud-based applications and other information assets. These security policies make SaaS apps safe and trustworthy.

- SaaS Security refers to securing user privacy and corporate data in subscription-based cloud applications.
- SaaS applications carry a large amount of sensitive data and can be accessed from almost any device by a mass of users, thus posing a risk to privacy and sensitive information.
- Security-as-a-service providers usually function the same way as SaaS providers: they charge a monthly subscription fee to reduce cost burden for outsourced services. But instead of providing access to a tool or platform, they provide protection for your apps, data, and operations that run in the cloud.
- For all the value that SaaS promises, security concerns limit enterprise customers seeking to make the transition from on-premises solutions to SaaS-based ones.
- SaaS is a business model that provides access to applications over the internet or cloud. It’s an alternative to buying and installing software locally. SaaS implies a subscription-based and centrally-hosted model of software licensing and deployment.



### Security Governance

Security governance in cloud computing is a framework of policies designed to dictate what cloud resources can be used, how they should be used, and who can use them. They can also enforce rules governing how individual resources should be secured to prevent their misuse by malicious actors.

- Cloud security governance is a management model that facilitates effective and efficient security management and operations in a cloud computing environment.
- This security governance model also incorporates executive mandates, operational practices, structures, and metrics.
- Cloud governance is a set of policies and rules used by companies who build or work in the cloud.
- This framework is designed to ensure data security, system integration and the deployment of cloud computing are properly managed.
- Security governance bridges your business priorities with technical implementation like architecture, standards, and policy.
- Governance teams provide oversight and monitoring to sustain and improve security posture over time.
- These teams also report compliance as required by regulating bodies.
- Security governance in particular is used to support business objectives by defining policies and controls to manage risk.
- Moving to the cloud provides you with an opportunity to deliver features faster, react to the changing world in a more agile way, and return some decision making to the hands of the people closest to the business.
- Once security requirements are established, cloud governance policies and enforcement apply those requirements across network, data, and asset configurations.



### Virtual Machine Security

Virtual Machine Security is an important aspect of Resource Management and Security in Cloud Computing. Here are some key points to consider when studying this topic:

1. Virtual machines (VMs) are software-based representations of physical machines that can run their own operating systems and applications. They are commonly used in cloud computing environments to provide scalable and flexible computing resources.

2. Security is a critical concern when using virtual machines, as vulnerabilities in the virtualization layer can potentially compromise the security of all virtual machines running on the same physical host.

3. Some common security risks associated with virtual machines include: 
    - VM escape: where an attacker gains access to the host system from within a virtual machine.
    - Inter-VM attacks: where an attacker gains access to one virtual machine and uses it to attack other virtual machines on the same host.
    - VM sprawl: where the proliferation of virtual machines leads to a lack of oversight and control, increasing the attack surface.

4. To mitigate these risks, it is important to implement security best practices such as:
    - Regularly patching and updating the virtualization software and guest operating systems.
    - Implementing strict access controls and monitoring user activity.
    - Segregating virtual machines with different security requirements on separate physical hosts.
    - Using encryption to protect sensitive data stored on virtual machines.

5. In addition to these technical measures, it is also important to have a comprehensive security policy in place that covers the use of virtual machines, including regular security assessments and incident response procedures.

These are some key points to consider when studying Virtual Machine Security as part of the Resource Management and Security in Cloud unit of the Cloud Computing subject. It is important to have a thorough understanding of these concepts in order to effectively manage and secure virtual machines in a cloud computing environment.



### IAM (Identity and Access Management)

IAM is a framework of policies and technologies for ensuring that the proper people in an enterprise have the appropriate access to technology resources. It is a crucial component of resource management and security in cloud computing.

Here are some key points to consider when studying IAM in the context of cloud computing:

1. IAM allows administrators to control who can access specific resources and what actions they can perform.
2. IAM policies can be used to grant or deny access to resources based on user attributes, such as job function or location.
3. IAM can help organizations meet compliance requirements by providing audit trails and reports on user activity.
4. IAM can also help prevent data breaches by enforcing strong authentication methods and monitoring for suspicious activity.
5. Many cloud providers offer built-in IAM tools and services to help customers manage access to their resources.

In summary, IAM is an essential component of cloud security and resource management, and it is important to understand its role and capabilities when working with cloud computing.



### Security Standards for Resource Management And Security In Cloud

Cloud security standards are essential for ensuring the safety and security of data and resources in the cloud. Here are some of the most important security standards for resource management and security in the cloud:

1. **ISO-27001 / ISO-27002**: ISO-27001 is a cloud security compliance standard that an organization must follow to get certified. ISO-27002 is an additional standard that helps comply with the security standard by describing measures that can be implemented .

2. **ISO-27017**: ISO-27017 is a security standard established for cloud service providers and consumers with the goal of reducing the risk of a security incident in the cloud.

3. **General Data Protection Regulation (GDPR)**: GDPR is a regulation that requires businesses to protect the personal data and privacy of EU citizens for transactions that occur within EU member states.

4. **System and Organisation Controls (SOC) Reporting**: SOC reports are internal control reports on the services provided by a service organization, providing valuable information that users need to assess and address the risks associated with an outsourced service.

5. **Payment Card Industry Data Security Standard (PCI DSS)**: PCI DSS is a set of security standards designed to ensure that all companies that accept, process, store or transmit credit card information maintain a secure environment.

6. **Health Insurance Portability and Accountability Act (HIPAA)**: HIPAA is a US law designed to provide privacy standards to protect patients' medical records and other health information provided to health plans, doctors, hospitals and other health care providers.

7. **CIS AWS Foundations v1.2**: CIS AWS Foundations v1.2 is a set of security configuration best practices for hardening AWS accounts, providing prescriptive guidance for establishing a secure baseline configuration for AWS.

8. **OASIS**: OASIS is a nonprofit that develops open standards for security, cloud technology, IoT, content technologies and emergency management. Its cloud technical committees include the OASIS Cloud Application Management for Platforms, OASIS Identity in the Cloud, and OASIS Topology and Orchestration Specification for Cloud Applications.

These are some of the most important security standards for resource management and security in the cloud. It is important for organizations to comply with these standards to ensure the safety and security of their data and resources in the cloud.



## Unit 5 - Cloud Technologies And Advancements Hadoop

Hadoop is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. It is designed to scale up from a single computer to thousands of clustered computers, with each machine offering local computation and storage.

Hadoop ecosystems also play a key role in supporting the development of artificial intelligence and machine learning applications. Companies often choose to run Hadoop clusters on public, private, or hybrid cloud resources versus on-premises hardware to gain flexibility, availability, and cost control.

Recent advancements introduced in the Hadoop ecosystem include real-time data streams, MPP data analytics, in-memory analytics, and data virtualization, all of which extend and challenge the strengths of a variety of established enterprise solutions .

Hadoop is also leading to phenomenal technical advancements. For instance, HBase will soon become a vital Platform for Blob Stores (Binary Large Objects) and for Lightweight OLTP (Online Transaction Processing).

Hadoop consists of four main modules: Hadoop Distributed File System (HDFS) – A distributed file system that runs on standard or low-end hardware. HDFS provides better data throughput than traditional file systems, in addition to high fault tolerance and native support of large datasets.



### MapReduce

MapReduce is a programming model and an associated implementation for processing and generating large data sets. It is a key component of the Apache Hadoop software framework, which is used for distributed processing of large data sets across clusters of computers.

The MapReduce model consists of two main phases: the Map phase and the Reduce phase. In the Map phase, the input data is divided into chunks and processed in parallel by multiple map tasks. Each map task applies a user-defined function to the input data and generates a set of intermediate key-value pairs.

In the Reduce phase, the intermediate key-value pairs are grouped by key and processed by multiple reduce tasks. Each reduce task applies a user-defined function to the values associated with the same key and generates a set of output values.

The MapReduce model is designed to be scalable and fault-tolerant, allowing for the processing of large data sets on clusters of commodity hardware. It is widely used in big data and cloud computing applications.

Some key features of MapReduce include:

- **Scalability:** The MapReduce model is designed to scale to large data sets and clusters of computers.
- **Fault-tolerance:** The MapReduce implementation in Hadoop is designed to be fault-tolerant, automatically re-executing failed tasks.
- **Data locality:** The MapReduce implementation in Hadoop attempts to schedule map tasks on nodes where the input data is stored, reducing data transfer and improving performance.
- **Flexibility:** The MapReduce model is flexible, allowing for the processing of structured and unstructured data, and supporting a wide range of data formats and processing algorithms.

MapReduce is a powerful tool for processing large data sets, and is widely used in big data and cloud computing applications. It is an important component of the Hadoop software framework, and is a key technology in the field of cloud computing.



### Virtual Box

VirtualBox is a cross-platform virtualization software that allows users to run multiple operating systems on a single physical computer. It is a type 2 hypervisor, meaning it is installed on top of an existing operating system. Some of the key features of VirtualBox include:

1. **Portability**: VirtualBox runs on multiple host operating systems, including Windows, Linux, macOS, and Solaris.
2. **Guest Additions**: VirtualBox provides a set of drivers and system applications that optimize the performance of guest operating systems.
3. **Snapshots**: VirtualBox allows users to take snapshots of the virtual machine's state, allowing them to revert to a previous state if needed.
4. **Seamless Mode**: VirtualBox can display the windows of a guest operating system directly on the host operating system's desktop, allowing for a seamless integration of the two systems.
5. **Shared Folders**: VirtualBox allows users to share folders between the host and guest operating systems, making it easy to transfer files between the two systems.

VirtualBox is commonly used for testing and development purposes, as it allows developers to test their applications on multiple operating systems without the need for multiple physical computers. It is also used for running legacy applications that may not be compatible with newer operating systems. VirtualBox is a powerful tool for anyone looking to run multiple operating systems on a single computer.



### Google App Engine

- Google App Engine (GAE) is a platform-as-a-service product that provides web app developers and enterprises with access to Google's scalable hosting and tier 1 internet service.
- GAE requires that applications be written in Java or Python, store data in Google Bigtable and use the Google query language.
- The development and hosting platform Google App Engine, which powers anything from web programming for huge enterprises to mobile apps, uses the same infrastructure as Google’s large-scale internet services.
- It is a fully managed PaaS (platform as a service) cloud computing platform that uses in-built services to run your apps.
- You can define Google App Engine as a hosting and development platform empowering business web applications and mobile games with a framework similar to the one powering Google’s global web apps.
- It also packs the qualities of a PaaS cloud platform, which is entirely manageable and utilizes built-services for running the apps.
- App Engine supports popular development languages with a range of developer tools.
- New customers get $300 in free credits to spend on App Engine.
- App Engine is a fully managed, serverless platform for developing and hosting web applications at scale.
- You can choose from several popular languages, libraries, and frameworks to develop your app.
- The App Engine application is a top-level container that includes the service, version, and instance resources that make up your app.
- When you create your App Engine app, all your resources are contained within this top-level container.



### Programming Environment for Google App Engine

Google App Engine provides four possible runtime environments for applications, one for each of four programming languages: Java, Python, PHP, and Go. The environment you choose depends on the language and related technologies you want to use for developing the application.

Google Cloud provides 2 environments to use App Engine, one is a standard environment with constrained environments and support for languages such as Python, Go, node.js.

The App Engine standard environment is based on container instances running on Google's infrastructure. Containers are preconfigured with one of several available runtimes. The standard environment makes it easy to build and deploy an application that runs reliably even under heavy load and with large amounts of data.

To create an application for an app engine, you can use Go, Java, PHP, or Python. You can develop and test an app locally using the SDK’s deployment toolkit. Each language’s SDK and runtime are unique. Your program is run in a: Java Run Time Environment version 7, Python Run Time environment version 2.7, PHP runtime’s PHP 5.4 environment.



### OpenStack

OpenStack is a free and open-source cloud computing platform that provides infrastructure as a service (IaaS) for public and private clouds. It is managed by the OpenStack Foundation, a non-profit organization that oversees the development and community building efforts of the project.

Some key features of OpenStack include:

1. **Compute**: OpenStack provides virtual servers on demand through its Nova component. Users can launch and manage virtual machines with various operating systems and configurations.

2. **Storage**: OpenStack provides object and block storage through its Swift and Cinder components, respectively. Users can store and retrieve data in a scalable and redundant manner.

3. **Networking**: OpenStack provides virtual networking through its Neutron component. Users can create and manage virtual networks, routers, and firewalls.

4. **Dashboard**: OpenStack provides a web-based dashboard through its Horizon component. Users can manage their cloud resources through a graphical user interface.

5. **Identity**: OpenStack provides identity and access management through its Keystone component. Users can manage authentication, authorization, and access control for their cloud resources.

OpenStack is widely used by enterprises, service providers, and government organizations to build and manage their own private and public clouds. It is also used by academic and research institutions for scientific computing and data analysis. OpenStack is supported by a large and active community of developers, users, and vendors. It is considered one of the leading open-source cloud computing platforms.



### Federation in the Cloud

- Federation in the cloud is the ability to connect two or more cloud computing environments of distinct cloud service providers.
- Cloud federation manages consistency and access controls when two or more independent geographically distributed clouds share either authentication, files, computing resources, command and control, or access to storage resources.
- Cloud Federation, also known as Federated Cloud, is the deployment and management of several external and internal cloud computing services to match business needs. It is a multi-national cloud system that integrates private, community, and public clouds into scalable computing platforms.
- Cloud Federation would address many existing limitations in cloud computing, such as cloud end-users being tied to a unique cloud provider, because of the different APIs, image formats, and access methods exposed by different providers that make it very difficult for an average user to move its applications from one cloud to another.
- To satisfy the demand for collective and collaborative cloud use, academia and industry want to interconnect heterogeneous clouds to form a federated system. This approach is promising but also faces significant challenges.



### Four Levels of Federation for the notes of the Unit 5 - Cloud Technologies And Advancements Hadoop in the subject of Cloud Computing

Federation is the process of combining multiple data sources into a single, unified view. There are four levels of federation in the context of cloud computing and Hadoop:

1. **Data-level federation**: This level of federation involves combining data from multiple sources into a single data store. This can be achieved through techniques such as data integration, data replication, and data virtualization.

2. **Schema-level federation**: This level of federation involves combining the schemas of multiple data sources into a single, unified schema. This can be achieved through techniques such as schema mapping and schema integration.

3. **Query-level federation**: This level of federation involves combining queries from multiple data sources into a single, unified query. This can be achieved through techniques such as query rewriting and query optimization.

4. **Application-level federation**: This level of federation involves combining multiple applications into a single, unified application. This can be achieved through techniques such as application integration and application orchestration.

Each level of federation provides its own benefits and challenges, and the appropriate level of federation will depend on the specific needs and requirements of the organization. It is important to carefully consider the trade-offs and implications of each level of federation when designing and implementing a federated system.



### Federated Services and Applications

- Cloud Federation, also known as Federated Cloud, is the deployment and management of several external and internal cloud computing services to match business needs. It is a multi-national cloud system that integrates private, community, and public clouds into scalable computing platforms .
- Hadoop is a Java-based framework used to manipulate data in the cloud or on-premises. It can be installed on cloud servers to manage Big Data, whereas cloud alone cannot manage data without Hadoop in it .
- Hadoop is designed to scale up from a single computer to thousands of clustered computers, with each machine offering local computation and storage. In this way, Hadoop can efficiently store and process large amounts of data .
- A new IEEE standard has been developed to advance Federated Cloud Computing. Based on the cloud federation roadmap outlined in NIST Special Publication 500-332: The NIST Cloud Federation Reference Architecture, it describes a functional model that supports all of the governance and processes required to design and implement a successful, effective cloud federation .
- One of the future challenges in Federated Cloud Computing is to cut through the jungle of standards to help the adoption of cloud computing by encouraging compliance of cloud services with respect to standards and thus providing evidence of compliance to legal and audit obligations .



### Future of Federation for the notes of the Unit 5 - Cloud Technologies And Advancements Hadoop in the subject of Cloud Computing

- Federation in the cloud refers to the integration of multiple cloud services and applications to provide a seamless user experience.
- There are four levels of federation: data, application, platform, and infrastructure.
- Federated services and applications are the future of federation, allowing for greater flexibility and scalability in the cloud.
- Hadoop is an open-source framework that allows for distributed processing of large datasets across clusters of computers using simple programming models.
- Hadoop is designed to scale up from a single server to thousands of machines, each offering local computation and storage.
- Hadoop runs applications using the MapReduce algorithm, where the data is processed in parallel on different CPU nodes.
- The Apache Hadoop project develops open-source software for reliable, scalable, distributed computing, including Hadoop Core, HBase, and Pig.
- Hadoop Core provides a distributed filesystem (HDFS) and support for the MapReduce distributed computing metaphor.
- HBase builds on Hadoop Core to provide a scalable, distributed database.
- Pig is a high-level platform for creating MapReduce programs used with Hadoop.

