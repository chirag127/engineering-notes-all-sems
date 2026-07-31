

# IOT ARCHITECTURE AND PROTOCOLS

IoT architecture refers to the many ways that IoT devices are structured to meet user needs. Based on complexity, IoT system elements are grouped into 3 to 7 layers, each with its own role. Notably, IoT architecture lacks standardized protocols, raising compatibility, security, and other challenges.

An IoT system has four types of transmission channels for data communication. Each IoT protocol in the IoT system architecture enables device-to-device, device-to-gateway, gateway-to-data center, or gateway-to-cloud communication, as well as communication between data centers. The application layer serves as the interface between the user and the device within a given IoT protocol.

There are several IoT protocols, including Message Queue Telemetry Transport (MQTT), Constrained Application Protocol (CoAP), and Advanced Message Queuing Protocol (AMQP). These protocols ensure that information from one device or sensor gets read and understood by another device, a gateway, or a service. Different IoT protocols have been designed and optimized for different scenarios and usage.



## Unit 1 - IoT-An Architectural Overview

1. **Introduction to IoT:** IoT stands for the Internet of Things. It refers to the interconnection of physical devices, vehicles, buildings, and other objects, embedded with electronics, software, sensors, and network connectivity, which enables these objects to collect and exchange data.

2. **IoT Architecture:** The architecture of IoT can be divided into four main layers: the sensing layer, the network layer, the service layer, and the application layer.

    - The **sensing layer** is responsible for collecting data from the physical world through sensors and actuators.
    - The **network layer** is responsible for transmitting the data collected by the sensing layer to the service layer through various communication technologies.
    - The **service layer** is responsible for processing and managing the data collected by the sensing layer, and providing services to the application layer.
    - The **application layer** is responsible for providing the user interface and delivering the services provided by the service layer to the end-users.

3. **IoT Protocols:** There are several communication protocols used in IoT, including MQTT, CoAP, HTTP, and WebSocket.

4. **IoT Security:** Security is a major concern in IoT, as the interconnection of devices and the collection and exchange of data can pose risks to privacy and security. Various security measures, such as encryption and authentication, are used to ensure the security of IoT systems.

5. **IoT Applications:** IoT has a wide range of applications, including smart homes, smart cities, healthcare, transportation, and agriculture.



### Building an architecture for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. Introduction to IoT
    - Definition of IoT
    - Importance of IoT
    - Applications of IoT
2. IoT Architecture
    - Overview of IoT architecture
    - Layers of IoT architecture
    - Components of each layer
3. IoT Protocols
    - Overview of IoT protocols
    - Types of IoT protocols
    - Comparison of different IoT protocols
4. IoT Devices
    - Overview of IoT devices
    - Types of IoT devices
    - Comparison of different IoT devices
5. IoT Security
    - Overview of IoT security
    - Threats to IoT security
    - Measures to enhance IoT security
6. Conclusion
    - Summary of key points
    - Future developments in IoT architecture and protocols
    - Importance of continued research in this field.



### Main design principles and needed capabilities for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. The overall design objective of IoT architecture shall be to target a horizontal system of real-world services that are open, service-oriented, secure, and offer trust.
2. Design for reuse of deployed IoT resources across application domains.
3. Design for a set of support services that provide open service-oriented capabilities and can be used for application development and execution.
4. The architecture relies on the separation of resources providing sensing and actuation from the actual devices, a set of contextual and real world entity-centric services, and the users of the services.
5. Connectivity is a key capability, with options including WiFi through a hub or gateway, 2G, or 3G cellular networks.
6. Product designers must simultaneously address industrial product requirements, IT components, business needs, and UX design.




### An IoT architecture outline for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. **Introduction:** IoT (Internet of Things) is a network of interconnected devices that can communicate with each other and exchange data over the internet. These devices can be anything from simple sensors to complex machines.

2. **IoT Architecture:** The architecture of an IoT system can be divided into four main layers: the perception layer, the network layer, the middleware layer, and the application layer.

    - **Perception Layer:** This layer is responsible for collecting data from the physical world using sensors and other devices. The data collected by the perception layer is then sent to the network layer for further processing.

    - **Network Layer:** The network layer is responsible for transmitting the data collected by the perception layer to the middleware layer. This layer can use various communication technologies such as Wi-Fi, Bluetooth, and cellular networks.

    - **Middleware Layer:** The middleware layer is responsible for managing the data received from the network layer. This layer can perform tasks such as data storage, data processing, and data analysis.

    - **Application Layer:** The application layer is responsible for providing the user with a user-friendly interface to interact with the IoT system. This layer can include various applications such as home automation, health monitoring, and smart city management.

3. **Conclusion:** The architecture of an IoT system is complex and consists of multiple layers. Each layer has its own responsibilities and plays a crucial role in the overall functioning of the system. Understanding the architecture of an IoT system is essential for designing and implementing effective IoT solutions.



### Standards Considerations for Unit 1 - IoT: An Architectural Overview

1. **Interoperability:** IoT devices and systems must be able to communicate and exchange data with each other, regardless of the manufacturer, operating system, or other factors. This requires the use of common communication protocols and data formats.

2. **Security:** IoT devices and systems must be designed with security in mind to protect against unauthorized access and data breaches. This includes the use of encryption, secure authentication methods, and regular security updates.

3. **Privacy:** IoT devices and systems must respect the privacy of users and protect their personal data. This includes providing clear and transparent privacy policies, allowing users to control their data, and complying with relevant privacy regulations.

4. **Reliability:** IoT devices and systems must be reliable and able to operate without interruption. This requires robust design, regular maintenance, and the ability to recover from failures.

5. **Scalability:** IoT systems must be able to scale to accommodate the growing number of connected devices and the increasing volume of data they generate. This requires flexible and scalable architectures, as well as the ability to handle large amounts of data in real-time.

6. **Energy Efficiency:** IoT devices and systems must be energy-efficient to reduce their environmental impact and minimize their operating costs. This requires the use of low-power technologies, efficient data transmission methods, and smart power management.




### M2M and IoT Technology Fundamentals

M2M (Machine-to-Machine) and IoT (Internet of Things) are two closely related technologies that enable devices to communicate with each other and with the internet. Here are some key points to understand about M2M and IoT technology fundamentals:

1. **M2M** refers to the direct communication between devices, without the need for human intervention. This communication can take place over various types of networks, including wired and wireless.

2. **IoT** refers to the network of physical objects or "things" that are embedded with sensors, software, and other technologies to connect and exchange data with other devices and systems over the internet.

3. M2M and IoT technologies are used in a wide range of applications, including smart homes, industrial automation, healthcare, transportation, and more.

4. M2M and IoT devices use various types of sensors to collect data, such as temperature, humidity, motion, and more. This data is then transmitted to other devices or systems for analysis and decision-making.

5. M2M and IoT technologies rely on various communication protocols to transmit data, including Wi-Fi, Bluetooth, cellular, and more.

6. Security is a major concern in M2M and IoT systems, as these devices can collect and transmit sensitive data. Various security measures, such as encryption and authentication, are used to protect the data and prevent unauthorized access.

7. M2M and IoT technologies are constantly evolving, with new devices, sensors, and communication protocols being developed to improve the capabilities and performance of these systems.

This is a brief overview of M2M and IoT technology fundamentals. These technologies are essential for enabling devices to communicate and interact with each other and with the internet, and they have a wide range of applications in various industries.



### Devices and Gateways

#### Unit 1 - IoT-An Architectural Overview

In the context of IoT architecture and protocols, devices and gateways play a crucial role in the overall system. Here are some key points to consider:

1. **Devices** refer to the physical objects that are connected to the internet and are capable of collecting, processing, and transmitting data. These devices can range from simple sensors to complex machines and can be embedded in a variety of objects such as home appliances, vehicles, and industrial equipment.

2. **Gateways** act as intermediaries between the devices and the cloud. They are responsible for aggregating data from multiple devices, performing local processing and analysis, and transmitting the data to the cloud for further processing and storage.

3. Gateways can also perform other functions such as device management, security, and protocol translation. They can be implemented as standalone hardware devices or as software running on a general-purpose computer.

4. The use of gateways can help to reduce the complexity and cost of connecting devices to the cloud, as well as improve the reliability and security of the overall system.

5. In summary, devices and gateways are essential components of any IoT system, providing the means for collecting, processing, and transmitting data from the physical world to the digital realm. Their proper design and implementation are critical to the success of any IoT deployment.



### Local and Wide Area Networking

Local Area Network (LAN) and Wide Area Network (WAN) are two types of computer networks that are used to connect devices and facilitate communication and data sharing.

1. **Local Area Network (LAN):** A LAN is a network that connects devices within a limited geographical area, such as a home, school, or office building. LANs are typically used to connect personal computers, printers, and other devices, and to share resources such as files and internet connections.

2. **Wide Area Network (WAN):** A WAN is a network that connects devices over a large geographical area, such as between cities or even countries. WANs are typically used by businesses and organizations to connect their various locations and to share resources and information.

In the context of IoT, LANs and WANs play an important role in connecting IoT devices and facilitating communication between them. IoT devices can be connected to a LAN, for example, to share data and communicate with other devices within the same network. WANs, on the other hand, can be used to connect IoT devices located in different geographical locations and to facilitate communication and data sharing between them.



### Data Management for Unit 1 - IoT: An Architectural Overview

Data management is an essential component of IoT architecture and protocols. It involves the collection, storage, processing, and analysis of data generated by IoT devices. Here are some key points to consider when studying data management in the context of IoT:

1. **Data Collection:** IoT devices generate large amounts of data, which must be collected and transmitted to a central location for processing and analysis. This data can include sensor readings, device status information, and user interactions.

2. **Data Storage:** Once collected, data must be stored in a way that allows for efficient retrieval and analysis. This can involve the use of databases, data lakes, and other storage technologies.

3. **Data Processing:** Data processing involves the transformation of raw data into a format that can be analyzed and used to generate insights. This can include data cleaning, aggregation, and normalization.

4. **Data Analysis:** Data analysis involves the use of statistical and machine learning techniques to extract insights from data. This can include trend analysis, anomaly detection, and predictive modeling.

5. **Data Security:** Data security is a critical concern in IoT systems, as data can often contain sensitive information. Measures must be taken to ensure the confidentiality, integrity, and availability of data.

Overall, data management is a crucial aspect of IoT architecture and protocols, and a thorough understanding of its principles and techniques is essential for anyone studying the subject.



### Business processes in IoT

Business processes in IoT refer to the various activities and tasks that are involved in the implementation and management of IoT systems in a business context. These processes can include:

1. **Planning and Strategy:** This involves identifying the business goals and objectives that can be achieved through the implementation of IoT systems, and developing a plan for how to achieve these goals.

2. **Design and Development:** This involves designing the IoT system architecture, selecting the appropriate hardware and software components, and developing the necessary software and applications.

3. **Implementation and Deployment:** This involves installing and configuring the IoT system, integrating it with existing business systems, and deploying it to the intended users.

4. **Operation and Maintenance:** This involves monitoring the performance of the IoT system, performing regular maintenance and updates, and addressing any issues that arise.

5. **Data Management:** This involves collecting, storing, and analyzing the data generated by the IoT system, and using this data to inform business decisions and improve operations.

6. **Security and Compliance:** This involves ensuring that the IoT system is secure and complies with relevant regulations and standards.

These business processes are essential for the successful implementation and management of IoT systems in a business context, and can help organizations to achieve their goals and objectives through the use of IoT technology.



### Everything as a Service(XaaS)

- XaaS is short for Everything-as-a-Service and sometimes Anything-as-a-Service.
- XaaS reflects how organizations across the globe are adopting the as-a-Service method for delivering just about, well, everything.
- XaaS, an acronym for Anything-as-a-Service (or even Everything-as-a-Service), refers to the growing diversity of services available over the Internet via cloud computing as opposed to being provided locally, or on premises.
- 'X' in the acronym represents anything derived from SaaS, PaaS, NaaS, DRaaS etc.
- “Anything as a service” (XaaS) describes a general category of services related to cloud computing and remote access.
- It recognizes the vast number of products, tools, and technologies that are now delivered to users as a service over the internet.
- In Everything as a Service, various tools and technologies, and services are provided to users as a service.
- Before XaaS and cloud services, companies have to buy licensed products and install them, had to all securities on their site and provide infrastructure for business purposes.
- XaaS— everything-as-a-service or anything-as-a-service —refers to products, tools, and capabilities that are delivered to users as services.
- For purposes of this article, we’re considering only enterprise IT as-a-service.



### M2M and IoT Analytics

- M2M (Machine-to-Machine) and IoT (Internet of Things) provide remote access for exchanging information among machines without human intervention .
- The key difference between IoT and M2M is that IoT connects any device to the Internet for better performance, and M2M is the connection of two or more than two devices with the Internet for data sharing and analytics .
- M2M is more of a vertical application which meets internal demands, whereas IoT can be considered as one with overarching results or one with open-ended capabilities .
- Consequently, data is different and its use is different in IoT application development from M2M .
- M2M systems use point-to-point communications between machines, sensors and hardware over cellular or wired networks, while IoT systems rely on IP-based networks to send data collected from IoT-connected devices to gateways, the cloud or middleware platforms .



### Knowledge Management for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Knowledge management is the process of creating, sharing, using and managing the knowledge and information of an organization.
- It refers to a multidisciplinary approach to achieving organizational objectives by making the best use of knowledge.
- In the context of IoT, knowledge management is crucial for the effective implementation and operation of IoT systems.
- IoT systems generate large amounts of data, which must be properly managed and analyzed to extract valuable insights and knowledge.
- Knowledge management in IoT involves the use of various tools and techniques to collect, store, process, and analyze data generated by IoT devices.
- This knowledge can then be used to improve the performance and efficiency of IoT systems, as well as to support decision-making processes.
- Effective knowledge management in IoT requires the integration of various technologies, including data analytics, machine learning, and artificial intelligence.
- It also involves the development of appropriate data governance and security measures to ensure the protection of sensitive information.
- In summary, knowledge management is a key component of IoT architecture and protocols, and is essential for the successful deployment and operation of IoT systems.



## Unit 2 - Reference Architecture

1. A reference architecture is a document or set of documents that provides a common framework and best practices for the design and implementation of a specific type of system or solution.
2. It serves as a blueprint for the development of systems within a particular domain, providing guidance on the selection and integration of components, as well as on the overall structure and organization of the system.
3. Reference architectures are typically developed by industry consortia, standards organizations, or vendors, and are intended to promote interoperability and reduce complexity and risk in the development of new systems.
4. They are often accompanied by reference implementations, which provide concrete examples of how the architecture can be realized in practice.
5. The use of reference architectures can help to ensure that systems are designed and built in a consistent and repeatable manner, and can facilitate the reuse of proven design patterns and components.
6. Some common examples of reference architectures include the TOGAF standard for enterprise architecture, the NIST Cybersecurity Framework, and the AWS Well-Architected Framework.



### IoT Architecture-State of the Art

1. A reference model is a model that describes the main conceptual entities and how they are related to each other, while the reference architecture aims at describing the main functional components of a system as well as how the system works, how the system is deployed, what information the system processes, etc. 
2. The principles of Reactive Systems define the state-of-the-art programming models for IoT. Because IoT devices are sensing and actuating physical systems, many of which are critical infrastructure for energy, food, healthcare, and transportation, it is important that they stay responsive, and operate safely and securely. 
3. IoT platforms must tackle asset management as a foundational problem and all of these platforms have facilities for managing the provisioning of devices and services, public key infrastructure (PKI), software and firmware updates, and desired-state configuration of devices, at huge scale. 
4. IoT has the potential to deeply affect our life style. However, its success relies greatly on a well-defined architecture that will provide scalable, dynamic, and secure basement to its deployment. 




### Introduction for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The Internet of Things (IoT) is a network of interconnected devices that can collect and exchange data.
- IoT devices can range from simple sensors to complex systems such as smart homes and autonomous vehicles.
- The reference architecture for IoT provides a framework for designing and implementing IoT systems.
- It defines the key components and their interactions, as well as the standards and protocols used for communication.
- The reference architecture can help ensure interoperability, scalability, and security in IoT systems.
- In this unit, we will explore the reference architecture for IoT and its key components, including the device layer, the network layer, and the application layer.
- We will also discuss the standards and protocols used in IoT, such as MQTT and CoAP, and their role in enabling communication between devices.
- By understanding the reference architecture for IoT, we can design and implement effective and efficient IoT systems.



### State of the art for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. A reference model is a model that describes the main conceptual entities and how they are related to each other.
2. The reference architecture aims at describing the main functional components of a system as well as how the system works, how the system is deployed, what information the system processes, etc.
3. Reference architecture is a discipline of enterprise architecture intended to provide a common vocabulary to express implementations.
4. A common vocabulary can be further expressed as a repository of architecture artifacts that practitioners across a large enterprise can use to develop designs.
5. The practice of architecture is employed to fulfill both practical and expressive requirements, and thus it serves both utilitarian and aesthetic ends.
6. The Internet of things (IoT) constitutes one of the most important technological development in the last decade. It has the potential to deeply affect our life style.
7. The IoT reference Model includes Functional View, Information View, Deployment and Operational View, Real World Design Constraints- Introduction, Technical Design constraints, Data representation and visualization.



### Reference Model and Architecture

#### Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. A reference model is an abstract framework that organizes the elements of a system and the relationships between them.
2. It provides a common language for discussing the system and a foundation for building concrete architectures.
3. In the context of IoT, a reference model can help to identify the components and layers of an IoT system, and to define the interfaces and protocols between them.
4. A reference architecture is a concrete instantiation of a reference model, providing a blueprint for building a specific system.
5. It defines the components, their relationships, and the technologies to be used.
6. There are several reference models and architectures for IoT, including the IoT-A Reference Model, the Industrial Internet Reference Architecture, and the Reference Architecture Model for Industry 4.0.
7. These models and architectures provide a common understanding of the IoT system and can facilitate the development and deployment of IoT solutions.




### IoT Reference Model

The IoT Reference Model aims at establishing a common grounding and a common language for IoT architectures and IoT systems. It consists of several sub-models that set the scope for the IoT design space and address architectural views and perspectives. The primary and key model is the IoT Domain Model, which describes all the concepts that are relevant in the Internet of Things, such as Devices, IoT Services, and Virtual Entities (VE), and it also introduces relations between these concepts .

The IoT Reference Model is designed to provide a common understanding and a common language for IoT architectures and IoT systems. The sub-models of the IoT Reference Model show how concepts and aspects of one model are used as the basis for another .



### IoT Reference Architecture

IoT Reference Architecture is a framework that outlines the various components and their interactions in an IoT system. It provides a common language and understanding for IoT architectures and systems. 

- The **Internet of Things (IoT) reference architecture** defines an approach to IoT solutions that use information from devices, people, and applications with cloud or on-premises services and systems to generate insights and value.
- The **IoT Reference Model** aims at establishing a common grounding and a common language for IoT architectures and IoT systems. It consists of sub-models, which are used as the basis for one another.
- The **IoT Reference Architecture** is designed as a reference for the generation of compliant IoT concrete architectures that are tailored to one’s specific needs.
- Companies such as **IBM** and **Microsoft** have their own IoT reference architectures, which outline their approach to building IoT solutions using their respective cloud platforms .



### Introduction for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The Internet of Things (IoT) is a network of interconnected devices that can collect and exchange data.
- IoT devices can range from simple sensors to complex systems such as smart homes and autonomous vehicles.
- The reference architecture for IoT provides a framework for designing and implementing IoT systems.
- It defines the components and their interactions within an IoT system.
- The reference architecture can be used as a guide for developing IoT solutions and ensuring interoperability between different systems.
- It is important to have a well-defined reference architecture to ensure that IoT systems are scalable, secure, and reliable.
- In this unit, we will explore the different components of the reference architecture for IoT and their roles in an IoT system.



### Functional View

The functional view of the reference architecture for IoT systems focuses on the functional components and their interactions. This view is useful for understanding the overall functionality of the system and how the different components work together to achieve the desired goals. Some key points to consider when studying the functional view of the reference architecture for IoT systems are:

1. The functional view identifies the main functional components of the system, such as sensors, actuators, gateways, and cloud services.
2. The interactions between these components are also described, such as how data is collected from sensors, processed by gateways, and sent to cloud services for further analysis.
3. The functional view can help to identify the key capabilities of the system, such as data collection, data processing, and data analysis.
4. This view can also be used to identify potential bottlenecks or limitations in the system, such as limited processing power at the gateway level or limited bandwidth for data transmission.
5. The functional view is useful for designing and implementing IoT systems, as it provides a clear understanding of the system's functionality and how the different components work together.




### Information View

Information view is one of the views in the reference architecture of IoT. It focuses on the data and information aspects of an IoT system. Here are some key points to consider when studying the information view of the reference architecture in IoT:

1. The information view deals with the representation, storage, and exchange of information in an IoT system.
2. It defines the data models and formats used to represent information, as well as the protocols and interfaces used to exchange information between different components of the system.
3. The information view also addresses issues related to data quality, such as accuracy, completeness, and consistency.
4. It is important to consider the security and privacy of information in the information view, as IoT systems often deal with sensitive data.
5. The information view is closely related to other views in the reference architecture, such as the functional view and the deployment view, as the design of the information architecture affects the functionality and deployment of the system.

These are some of the key points to consider when studying the information view of the reference architecture in IoT. It is important to have a thorough understanding of this view in order to design and implement effective IoT systems.



### Deployment and Operational View

The deployment and operational view of a reference architecture for IoT systems focuses on the physical deployment of the system components and their interactions during operation. This view is important for understanding the system's scalability, reliability, and maintainability.

1. **Physical Deployment:** This aspect of the deployment and operational view deals with the physical placement of the system components, such as sensors, actuators, gateways, and servers. The physical deployment should be designed to optimize the system's performance, scalability, and reliability.

2. **Component Interactions:** This aspect of the deployment and operational view deals with the interactions between the system components during operation. The interactions should be designed to ensure the system's reliability, maintainability, and security.

3. **Scalability:** The deployment and operational view should consider the system's ability to scale to accommodate increasing numbers of devices and users. This includes the ability to add new components and to distribute the system's workload across multiple servers.

4. **Reliability:** The deployment and operational view should consider the system's ability to operate reliably, even in the face of component failures or network disruptions. This includes the use of redundant components and the ability to recover from failures.

5. **Maintainability:** The deployment and operational view should consider the system's ability to be maintained and updated over time. This includes the ability to update the system's software and firmware, and to replace failed components.

Overall, the deployment and operational view is an important part of the reference architecture for IoT systems, as it provides a framework for understanding the system's physical deployment and operational interactions. This view can help to ensure that the system is designed to be scalable, reliable, and maintainable.



### Other Relevant Architectural Views

1. **Information View:** This view focuses on the management of information within the IoT system. It includes the representation, storage, and exchange of information between different components of the system.

2. **Functional View:** This view describes the functional components of the IoT system and their interactions. It includes the identification of the main functions of the system and the definition of the interfaces between them.

3. **Deployment View:** This view describes the physical deployment of the components of the IoT system. It includes the mapping of the functional components to the physical hardware and the definition of the network topology.

4. **Operational View:** This view focuses on the operational aspects of the IoT system. It includes the definition of the processes and procedures required to operate and maintain the system.

5. **Development View:** This view describes the development process of the IoT system. It includes the definition of the development methodology, the tools and technologies used, and the management of the development process.




### Real-World Design Constraints

When designing an IoT system, there are several real-world constraints that must be taken into consideration. These constraints can affect the design and implementation of the system, and must be carefully considered in order to ensure that the system is effective, efficient, and meets the needs of its users. Some of the most important real-world design constraints to consider when designing an IoT system include:

1. **Cost:** The cost of the system is a major constraint, as it can affect the feasibility of the project and its potential for success. The cost of the hardware, software, and other components of the system must be carefully considered and balanced against the potential benefits of the system.

2. **Power:** IoT devices often have limited power resources, and must be designed to operate efficiently in order to maximize their battery life. This can be a major constraint, as it can affect the functionality and usability of the system.

3. **Connectivity:** IoT devices must be able to connect to the internet in order to function, and this can be a major constraint in areas with limited or unreliable connectivity. The system must be designed to operate effectively even in areas with poor connectivity.

4. **Security:** Security is a major concern for IoT systems, as they can be vulnerable to hacking and other forms of cyber attack. The system must be designed with security in mind, in order to protect the data and privacy of its users.

5. **Scalability:** IoT systems must be scalable, in order to accommodate growth and change over time. The system must be designed to be easily expandable, in order to meet the changing needs of its users.

6. **Reliability:** IoT systems must be reliable, in order to ensure that they function effectively and meet the needs of their users. The system must be designed to be robust and resilient, in order to minimize the risk of failure.

7. **Usability:** The usability of the system is a major constraint, as it can affect the adoption and success of the system. The system must be designed to be easy to use and intuitive, in order to maximize its effectiveness.

These are just some of the many real-world design constraints that must be considered when designing an IoT system. By carefully considering these constraints and designing the system accordingly, it is possible to create an effective, efficient, and successful IoT system that meets the needs of its users.



### Introduction for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The Internet of Things (IoT) is a network of interconnected devices that can communicate with each other and exchange data.
- The IoT reference architecture is a framework that defines the various components and their interactions in an IoT system.
- The reference architecture provides a common language and understanding for designing and implementing IoT solutions.
- It helps to ensure interoperability, scalability, and security in IoT systems.
- The reference architecture is not a fixed design, but rather a flexible guide that can be adapted to meet the specific needs of different IoT applications.
- Some common components of an IoT reference architecture include sensors, actuators, gateways, communication protocols, data storage, and analytics.
- By understanding the reference architecture, developers and engineers can design and build more effective and efficient IoT systems.



### Technical Design Constraints: Hardware is Popular Again

Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. **Hardware constraints:** Hardware constraints refer to the limitations of the physical components of a system. These can include size, weight, power consumption, and processing capabilities.

2. **Hardware selection:** The selection of hardware components for an IoT system is critical to its success. The hardware must be able to support the desired functionality, while also meeting the constraints of the system.

3. **Hardware trends:** There has been a resurgence in the popularity of hardware in recent years. This is due to the increasing demand for connected devices and the need for more powerful and efficient hardware to support them.

4. **Hardware and IoT:** Hardware plays a crucial role in the IoT ecosystem. It provides the physical interface between the digital and physical worlds, allowing data to be collected, processed, and acted upon.

5. **Hardware design:** The design of hardware for IoT systems must take into account the constraints of the system, as well as the needs of the end user. This can include considerations such as power consumption, size, and processing capabilities.

6. **Hardware and reference architecture:** The reference architecture for an IoT system provides a framework for the design and implementation of the hardware components. It defines the relationships between the different components and provides guidance on how they should interact.

7. **Hardware and protocols:** The hardware components of an IoT system must be able to support the communication protocols used by the system. This can include protocols for data transfer, device management, and security.

8. **Hardware and security:** Security is a critical consideration in the design of hardware for IoT systems. The hardware must be able to support the security measures necessary to protect the data and devices in the system.

9. **Hardware and scalability:** The hardware components of an IoT system must be able to support the scalability of the system. This means that the hardware must be able to accommodate growth in the number of devices and the amount of data being processed.

10. **Hardware and interoperability:** Interoperability is the ability of different systems to work together. The hardware components of an IoT system must be able to support interoperability with other systems and devices. This can include support for common communication protocols and data formats.



### Data Representation and Visualization

Data representation and visualization are important aspects of the Unit 2 - Reference Architecture in the subject of IoT Architecture and Protocols. Here are some key points to consider:

1. **Data representation** refers to the methods and techniques used to encode and store data in a format that can be easily understood and processed by computers and humans.

2. **Data visualization** is the graphical representation of data and information, using visual elements such as charts, graphs, and maps to communicate insights and trends.

3. Effective data representation and visualization can help to make complex data more accessible and understandable, enabling users to identify patterns, trends, and relationships that might otherwise be difficult to discern.

4. There are many different tools and techniques available for data representation and visualization, including programming languages such as Python and R, and software packages such as Tableau and Microsoft Excel.

5. When selecting a data representation and visualization tool, it is important to consider factors such as the type and complexity of the data, the intended audience, and the desired level of interactivity.

6. Data representation and visualization can be particularly useful in the context of IoT, where large amounts of data are generated by sensors and other devices. By visualizing this data, it is possible to gain insights into the behavior and performance of IoT systems, and to identify opportunities for optimization and improvement.

7. In summary, data representation and visualization are essential skills for anyone working with IoT data, and can help to unlock the full potential of IoT systems.



### Interaction and Remote Control

Interaction and remote control are important aspects of the Internet of Things (IoT) architecture and protocols. These features enable users to interact with and control IoT devices from a remote location.

1. **Interaction** refers to the ability of a user to communicate with an IoT device. This can be achieved through various means, such as voice commands, touch screens, or physical buttons. Interaction allows users to input data or commands to the device, and receive feedback or responses from the device.

2. **Remote control** refers to the ability of a user to control an IoT device from a remote location. This can be achieved through various means, such as a mobile app, web interface, or remote control device. Remote control allows users to perform actions on the device, such as turning it on or off, adjusting settings, or monitoring its status.

3. The use of interaction and remote control in IoT architecture and protocols enables users to have greater control and flexibility over their IoT devices. This can improve the user experience and increase the functionality of the devices.

4. There are various protocols and standards that enable interaction and remote control in IoT, such as MQTT, CoAP, and HTTP. These protocols provide a means for devices to communicate with each other and with users, enabling interaction and remote control.

5. Security is an important consideration when implementing interaction and remote control in IoT architecture and protocols. Measures such as encryption and authentication should be used to ensure that only authorized users can interact with and control IoT devices.

6. In summary, interaction and remote control are important features of IoT architecture and protocols that enable users to communicate with and control IoT devices from a remote location. These features improve the user experience and increase the functionality of IoT devices. Security measures should be implemented to ensure that only authorized users can interact with and control the devices.



## Unit 3 - IOT Data Link Layer & Network Layer Protocols

The Internet of Things (IoT) is a network of interconnected devices that can communicate with each other and exchange data. The data link layer and network layer protocols are essential components of the IoT architecture, as they enable the transmission of data between devices.

### Data Link Layer Protocols

The data link layer is responsible for providing a reliable link between two devices on a network. Some of the key functions of the data link layer include:

- Framing: The data link layer divides the data into frames for transmission.
- Error Control: The data link layer detects and corrects errors that may occur during transmission.
- Flow Control: The data link layer regulates the flow of data to prevent the receiver from being overwhelmed.

Some common data link layer protocols used in IoT include:

- **Zigbee**: A low-power, wireless mesh network protocol designed for IoT applications.
- **Z-Wave**: A wireless protocol used for home automation and smart home devices.
- **Bluetooth Low Energy (BLE)**: A low-power wireless protocol used for short-range communication between devices.

### Network Layer Protocols

The network layer is responsible for routing data between devices on a network. Some of the key functions of the network layer include:

- Addressing: The network layer assigns unique addresses to devices on the network to enable routing.
- Routing: The network layer determines the best path for data to travel between devices on the network.
- Congestion Control: The network layer manages network congestion to ensure efficient data transmission.

Some common network layer protocols used in IoT include:

- **IPv6**: The latest version of the Internet Protocol (IP), designed to accommodate the growing number of devices on the internet.
- **6LoWPAN**: A protocol that enables the transmission of IPv6 packets over low-power wireless networks.
- **RPL**: A routing protocol designed for low-power and lossy networks, commonly used in IoT applications.

In summary, the data link layer and network layer protocols play a crucial role in enabling communication and data exchange between IoT devices. These protocols provide the necessary functions to ensure reliable and efficient data transmission.



### PHY/MAC Layer (3GPP MTC)

The PHY (Physical) layer defines the physical and electrical characteristics of the network. It is responsible for managing the hardware that modulates and demodulates the RF (Radio Frequency) bits . The MAC (Media Access Control) layer is responsible for sending and receiving RF frames .

3GPP (3rd Generation Partnership Project) MTC (Machine Type Communication) is a standard for wireless communication that is designed to support the long-range massive machine-type connections with low power, low data rates, low complexity, and hence low cost .

The PHY and MAC protocols use the Link Layer, which is one of the top five protocols in the Link Layer, along with Ethernet, Wifi, WImax, Low rate WPAN, and mobile communication such as 5G, 4G, and 3G .



### IEEE 802.11

IEEE 802.11 is a set of standards for implementing wireless local area network (WLAN) computer communication in the 2.4, 3.6, 5, and 60 GHz frequency bands. They are created and maintained by the IEEE LAN/MAN Standards Committee (IEEE 802).

- IEEE 802.11 is used in most home and office networks to allow laptops, printers, smartphones, and other devices to communicate with each other and access the Internet without connecting wires.
- IEEE 802.11 is also a basis for vehicle-based communication networks with IEEE 802.11p.
- IEEE 802.11ad is an amendment that defines a new physical layer for 802.11 networks to operate in the 60 GHz millimeter wave spectrum. This frequency band has significantly different propagation characteristics than the 2.4 GHz and 5 GHz bands where Wi-Fi networks operate.
- IEEE 802.11 was the original version released in 1997. It provided 1 Mbps or 2 Mbps data rate in the 2.4 GHz band and used either frequency-hopping spread spectrum (FHSS) or direct-sequence spread spectrum (DSSS). It is obsolete now.
- IEEE 802.11 standard, popularly known as WiFi, lays down the architecture and specifications of wireless LANs (WLANs). WiFi or WLAN uses high frequency radio waves for connecting the nodes. There are several standards of IEEE 802.11 WLANs. The prominent among them are 802.11, 802.11a, 802.11b, 802.11g, 802.11n and 802.11p.
- IEEE Standard for Information Technology - Telecommunications and information exchange between systems - Local and Metropolitan Area networks - Specific requirements - Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) specifications. This standard is a revision of IEEE Std 802.11-1997.



### IEEE 802.15

IEEE 802.15 is a working group of the Institute of Electrical and Electronics Engineers (IEEE) IEEE 802 standards committee which specifies Wireless Specialty Networks (WSN) standards. The working group was formerly known as Working Group for Wireless Personal Area Networks.

- IEEE 802.15.4a (formally called IEEE 802.15.4a-2007) is an amendment to IEEE 802.15.4 specifying additional physical layers (PHYs) to the original standard.
- The IEEE 802.15 Working Group is part of the 802 Local and Metropolitan Area Network Standards Committee of the IEEE Computer Society. The IEEE-SA is an international membership organization serving today's industries with a complete portfolio of standards programs. The IEEE has more than 400,000 members in approximately 150 countries.
- 802.15.4-2020 - IEEE Standard for Low-Rate Wireless Networks Abstract: The physical layer (PHY) and medium access control (MAC) sublayer specifications for low-data-rate wireless connectivity with fixed, portable, and moving devices with no battery or very limited battery consumption requirements are defined in this standard.



### WirelessHART

WirelessHART is a wireless communications protocol for process automation applications. It adds wireless capabilities to HART technology while maintaining compatibility with existing HART devices, commands, and tools . It is a subset of the HART industrial instrument communication standard as of version 7, communicating process data over 2.4 GHz radio waves .

Individual instruments communicate with a common “gateway” device serving as an interface between the wireless network and a wired network or a host control system . WirelessHART is designed as a self-healing, mesh technology that ensures 99.99% data reliability, this protocol enables communication between devices, eliminating the need for direct device .

At the data-link layer, WirelessHART utilizes 10ms time slots for communications. These time slots can be dedicated to individual devices or shared amongst a group . WirelessHART is the evolution of HART and is designed for process automation and has focused on robustness and security .



### ZWave

- Z-Wave is a wireless communication protocol that creates a wireless Mesh network. It is based on low power RF (Radio Frequency) based technology .
- It operates in the 900 MHz frequency band .
- It is mainly used for home automation applications and devices .
- It is a more secure technology .
- The range of Z-Wave lies between 30 meters to 100 meters with a data transfer rate of 100kbps, making it suitable for small messages in IoT applications for home automation .
- The Z-Wave Network Layer (NWK) defines a multi-hop routing protocol, employed by Z-Wave nodes to extend their communication range .
- Z-Wave nodes can send frames to nodes that are not in direct radio communication range, with a maximum of 4 hops supported for Z-Wave source routing .



### Bluetooth Low Energy

Bluetooth Low Energy (BLE) is a short-range communication network protocol with PHY (physical layer) and MAC (Medium Access Control) layer. It is designed for low-power devices which uses less data . BLE is also known as Bluetooth smart which is a wireless PAN (Personal Area Network). The range is similar to that of Bluetooth but it consumes low power than Bluetooth. In 2011 BLE was introduced as Bluetooth 4.0. BLE goes to sleep mode when there is no transmission of data .

The IoT Data Link communication protocol provides service to the Network Layer. There are various protocols and standard technologies specified by the different organization for data link protocols .

The Link layer is the second lowest protocol in the Bluetooth Low Energy protocol stack. It’s responsible for managing the state of the LE radio, among other things .

BLE is a low-power version of the popular Bluetooth 2.4 GHz wireless communication protocol. It is designed for short-range (no more than 100 meters) communication, typically in a star configuration, with a single primary device that controls several secondary devices .

Bluetooth LE is an ultra-low-energy network in the 2.4 GHz band that connects devices in a short range. It consumes minimal energy and is designed to connect devices in a short-range .



### Zigbee Smart Energy

Zigbee Smart Energy (Zigbee SE) is a protocol designed for monitoring and actively managing energy consumption at the end-user level. It is a standard for interconnecting and interoperating devices, via radio frequency, directed towards monitoring, managing and automating energy, gas and water usage. It seeks to be a useful tool for creating “Green Homes”, and is aimed at coordinating energy usage, optimizing its generation and consumption .

For both utilities and consumers, Zigbee SE can help reduce waste, energy consumption and enables utilities to monitor and manage customers’ energy use. Smart energy revolutionizes consumer knowledge to optimize energy consumption to reduce emissions footprint and ease regulatory compliance .

The Zigbee Smart Energy 2.0 specifications define an Internet Protocol-based communication protocol to monitor, control, inform, and automate the delivery and use of energy and water. It is an enhancement of the Zigbee Smart Energy version 1 specifications.



### DASH7

DASH7 is a communication protocol that uses active RFID and is designed to be used within Industrial IoT applications for secure long-range communication. It originates from the ISO/IEC 18000-7 standard describing a 433 MHz ISM band air interface for active RFID. This standard was mainly used for military logistics. The DASH7 Alliance re-purposed the original 18000-7 technology in 2011 and made it evolve toward a wireless sensor network technology for commercial applications.

Compared to Zigbee, DASH7 is more scalable, has greater network coverage and greater data rates. It is not only a physical and MAC layer protocol but also includes IPv6 addressing for the network layer. The protocol uses unique identifiers along with 16-bit network identifiers for addressing in the IoT network.



### Network Layer

The network layer is responsible for routing data packets from the source device to the destination device in an Internet of Things (IoT) network. This layer is responsible for the logical addressing of devices and the forwarding of data packets based on their destination addresses.

Some of the key functions of the network layer in an IoT network include:

1. Addressing: Assigning unique addresses to devices in the network to enable communication between them.
2. Routing: Determining the best path for data packets to travel from the source device to the destination device.
3. Packet forwarding: Forwarding data packets from one network device to another based on their destination addresses.
4. Fragmentation and reassembly: Dividing large data packets into smaller packets for transmission and reassembling them at the destination device.
5. Congestion control: Managing network traffic to prevent congestion and ensure efficient data transmission.

Some of the common network layer protocols used in IoT networks include IPv4, IPv6, 6LoWPAN, and RPL. These protocols are designed to enable efficient routing and data transmission in IoT networks with a large number of connected devices.

In summary, the network layer plays a crucial role in enabling communication between devices in an IoT network by providing logical addressing, routing, and packet forwarding services. It also helps to manage network traffic and ensure efficient data transmission.



### IPv4 for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- **Internet Protocol Version 4 (IPv4)** is the fourth revision of the Internet Protocol and a widely used protocol in data communication over different kinds of networks.
- IPv4 is a **connectionless protocol** used in packet-switched layer networks, such as Ethernet.
- The **Network Layer** protocols used in IoT are IPv4 (used previously), the recent IPv6 layer handles 128 bit addresses and 6LoWPAN. 6LoWPAN is called the adaptation layer.
- The Internet Protocol, and specifically the Internet Protocol version 4, defines how the addressing works and how network hosts can be identified and found on the network.
- IPv4 addresses are represented by 32-bit values organized into four octets (4x8), usually expressed by dotted decimal numbers that look like this: 172.140.153.12.
- Ethernet is a LAN technology in which the devices are wired connection which provides data transfer rates as high as 100 Mbps. Choosing Ethernet for IoT ecosystem is a little bit costly in terms of setup and management.
- IoT network technologies to be aware of toward the bottom of the protocol stack include cellular, wifi, and Ethernet, as well as more specialized solutions such as LPWAN, Bluetooth Low Energy (BLE), ZigBee, NFC, and RFID. NB-IoT is becoming the standard for LPWAN networks.



### IPv6 for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- IPv6 or Internet Protocol Version 6 is a network layer protocol that allows communication to take place over the network.
- IoT works mostly with IPv6 which is the latest internet protocol version and it is used for transferring data and communication.
- Each IoT device has an IP address and networking is the key aspect in the Internet of Things.
- IPv6 Low Power Wireless Personal Area Network (6LoWPAN) is an IPv6 standard based network layer protocol for Wireless Personal Area Networks.
- Based on 802.15.4 protocol at physical layer, the standard has been developed for addressing of IoT sensors and devices in a Wireless Sensor Network (WSN).
- Many IoT protocols utilize IPv4, while more recent executions use IPv6.
- This recent update to IP routes traffic across the internet and identifies and locates devices on the network.
- IPv6 is commonly adopted for IoT device addressing.
- The transport layer (Layer 4 in OSI) focuses on end-to-end communication and provides features such as reliability, congestion avoidance, and guaranteeing that packets will be delivered in the same order that they were sent.



### 6LoWPAN

6LoWPAN stands for IPv6 over Low-Power Wireless Personal Area Networks. It is a protocol that allows for the transmission of IPv6 packets over low-power wireless networks, such as those used in the Internet of Things (IoT) devices.

Some key points to note about 6LoWPAN are:

- It is designed to operate over IEEE 802.15.4, which is a standard for low-power wireless personal area networks.
- 6LoWPAN enables the use of IPv6, which is the latest version of the Internet Protocol, in low-power wireless networks.
- It uses header compression to reduce the size of IPv6 packets, making them more suitable for transmission over low-power wireless networks.
- 6LoWPAN also supports mesh networking, which allows for the creation of large-scale wireless networks using multiple interconnected devices.
- It is an important protocol for IoT devices, as it allows them to connect to the Internet and communicate with other devices using IPv6.

6LoWPAN is a key component of the IoT Data Link Layer and Network Layer Protocols, as it enables the transmission of IPv6 packets over low-power wireless networks. This is essential for the operation of IoT devices, which often have limited power and processing capabilities. By using 6LoWPAN, these devices can connect to the Internet and communicate with other devices, enabling the creation of large-scale IoT networks.



# 6TiSCH

6TiSCH is an IPv6 standard for 802.15.4 MAC layer protocols developed by IETF. The standard allows IPv6 addresses to pass through Time-Slotted Channel Hopping (TSCH) mode of IEEE 802.15.4e MAC layer, so that the IPv6 adaption layer can be used for industrial automation and Low Power Lossy Networks (LLN).

The suite also defined protocol extensions to transport routing information (RFC6553) and enable downward source routes (RFC6554). 6TiSCH provides a mechanism by which the link layer topology is matched with the routing topology, enabling the nodes to maintain synchronization with their best-connected parent.

This standard is intended to provide reliable and delay bounded communication in multi-hop and scalable Industrial Internet of Things (IIoT).

6TiSCH architecture and protocol suite includes the 6TiSCH Operation Sublayer (6top), the 6top Protocol (6P), and how it uses 6LoWPAN, IP-in-IP encapsulation, and RPL.



### Unit 3 - IOT Data Link Layer & Network Layer Protocols

#### Data Link Layer Protocols
- The data link layer is responsible for providing reliable data transfer between two devices on the same network.
- Some common data link layer protocols used in IoT include:
  - Ethernet: a widely used wired networking technology that provides high-speed data transfer.
  - Wi-Fi: a wireless networking technology that provides high-speed data transfer over short distances.
  - Bluetooth: a short-range wireless technology used for data transfer between devices.
  - Zigbee: a wireless technology used for low-power, low-data-rate communication between devices.

#### Network Layer Protocols
- The network layer is responsible for routing data between devices on different networks.
- Some common network layer protocols used in IoT include:
  - IPv4: a widely used protocol for routing data over the internet.
  - IPv6: an updated version of IPv4 that provides a larger address space and improved routing capabilities.
  - 6LoWPAN: a protocol that enables the transmission of IPv6 packets over low-power wireless networks.
  - RPL: a routing protocol designed for low-power and lossy networks, commonly used in IoT applications.




# DHCP for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- DHCP stands for Dynamic Host Configuration Protocol. It is a network management protocol present in the application layer.
- With its help, an Internet Protocol (IP) address can be assigned to any device or node on a network dynamically so that they can communicate using this IP.
- DHCP is an application layer protocol which is used to provide: Subnet Mask (Option 1 – e.g., 255.255.255.0).
- IoT protocols can be divided into two categories: IoT network protocols and IoT data protocols. Data protocols mainly focus on information exchange, while network protocols provide methods of connecting IoT edge devices with other edge devices or the Internet.




### ICMP for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- ICMP stands for Internet Control Message Protocol.
- It is a network layer protocol.
- ICMP is mainly used to determine whether or not data is reaching its intended destination in a timely manner.
- It is used for error handling in the network layer.
- ICMP is primarily used on network devices such as routers.
- ICMP is a layer 3 protocol by the 7 layer OSI model.
- Based on the 4 layer TCP/IP model, ICMP is an internet-layer protocol.
- The most important protocols at the network layer are IP and ICMP.
- Several Communication Protocols are used in Internet of Things (IoT) to provide service to the network layer.
- IoT is based on networking of things where smart devices communicate with each other by sending and receiving data.
- Several network protocols (Communication protocols) are used to connect the IoT enabled devices.



### RPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for Routing Protocol for Low-Power and Lossy Networks.
- It is a distance-vector routing protocol designed for low-power and lossy networks (LLNs).
- RPL is used in Internet of Things (IoT) networks to enable communication between devices.
- RPL uses a Directed Acyclic Graph (DAG) to represent the network topology.
- The DAG is constructed using an objective function that determines the best path for data transmission.
- RPL supports both point-to-point and point-to-multipoint communication.
- RPL is designed to be scalable and can support networks with thousands of nodes.
- RPL is energy-efficient and can operate in networks with limited power resources.
- RPL supports multiple instances, allowing for multiple DAGs to coexist in the same network.
- RPL is a standard protocol defined by the Internet Engineering Task Force (IETF) in RFC 6550.




### CORPL

CORPL (Constrained RESTful Protocol) is a protocol used in the Internet of Things (IoT) for communication between devices. It is designed to be used in constrained environments, where resources such as memory, processing power, and energy are limited.

Some key features of CORPL include:

- It is based on the REST (Representational State Transfer) architecture, which is a widely used architectural style for building web services.
- It uses the CoAP (Constrained Application Protocol) as its underlying transport protocol, which is a lightweight protocol designed for use in constrained environments.
- It supports the use of URIs (Uniform Resource Identifiers) to identify resources, which makes it easy to integrate with other web-based systems.
- It provides support for caching, which can help to reduce the amount of data that needs to be transmitted and can improve the responsiveness of the system.
- It includes support for content negotiation, which allows devices to specify the format of the data they are sending or receiving.

Overall, CORPL is a protocol that is well-suited for use in IoT systems, where devices may have limited resources and may need to communicate with each other and with other systems in an efficient and reliable manner. It provides a range of features that can help to improve the performance and scalability of IoT systems.



### CARP

CARP stands for Common Address Redundancy Protocol. It is a protocol that allows multiple hosts on the same local network to share a set of IP addresses. Its primary purpose is to provide failover redundancy, especially when used with firewalls and routers.

Here are some key points to remember about CARP:

1. CARP is a free, open, and non-proprietary protocol.
2. It is used to allow multiple hosts on the same local network to share a set of IP addresses.
3. The primary purpose of CARP is to provide failover redundancy.
4. CARP is commonly used with firewalls and routers.
5. It works by having one host act as a master, while the other hosts act as backups.
6. In the event that the master fails, one of the backup hosts will take over as the new master.
7. CARP uses multicast to communicate between hosts.
8. It uses Virtual Host IDs (VHIDs) to identify different groups of hosts.




## Unit 4 - Transport & Session Layer Protocols

The transport layer is responsible for end-to-end communication between two devices. It provides services such as connection-oriented data stream support, reliability, flow control, and multiplexing.

Some of the key protocols in the transport layer include:
- Transmission Control Protocol (TCP): This is a connection-oriented protocol that provides reliable data transfer between two devices. It uses a three-way handshake to establish a connection and provides flow control and error recovery mechanisms.
- User Datagram Protocol (UDP): This is a connectionless protocol that provides fast, but unreliable data transfer. It is commonly used for real-time applications such as online gaming and video streaming.

The session layer is responsible for establishing, managing, and terminating sessions between two devices. It provides services such as authentication, authorization, and synchronization.

Some of the key protocols in the session layer include:
- Session Initiation Protocol (SIP): This is a signaling protocol used for initiating, maintaining, modifying, and terminating real-time sessions of multimedia communication.
- Remote Procedure Call (RPC): This is a protocol that allows a program to request a service from a program located on another computer in a network without having to understand the network's details.




### Transport Layer

The transport layer is responsible for providing end-to-end communication between applications on different devices. It is the fourth layer in the OSI model and is responsible for the following functions:

1. **Segmentation and reassembly:** The transport layer divides the data into smaller segments that can be transmitted over the network. At the receiving end, these segments are reassembled into the original data.

2. **Connection-oriented and connectionless communication:** The transport layer can provide both connection-oriented and connectionless communication. In connection-oriented communication, a connection is established between the sender and receiver before data is transmitted. In connectionless communication, data is transmitted without establishing a connection.

3. **Flow control:** The transport layer is responsible for controlling the flow of data between the sender and receiver. It ensures that the sender does not overwhelm the receiver by sending too much data at once.

4. **Error control:** The transport layer is responsible for detecting and correcting errors that may occur during transmission. It uses techniques such as checksums and retransmission to ensure that the data is transmitted correctly.

5. **Multiplexing:** The transport layer is responsible for multiplexing multiple communication streams between applications on the same device. This allows multiple applications to share the same network connection.

The transport layer protocols used in the Internet include the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP). TCP provides connection-oriented communication, while UDP provides connectionless communication. Both protocols provide segmentation and reassembly, error control, and multiplexing. However, TCP also provides flow control, while UDP does not.



### TCP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. **TCP** stands for **Transmission Control Protocol**. It is a **transport layer protocol** that facilitates the transmission of packets from source to destination.
2. It is a **connection-oriented protocol**, which means it establishes the connection prior to the communication that occurs between the computing devices in a network.
3. TCP is a **reliable protocol** as it follows the flow and error control mechanism. It also supports the acknowledgment mechanism, which checks the state and sound arrival of the data.
4. Applications can interact with one another using TCP as though they were physically connected by a circuit. TCP transmits data in a way that resembles character-by-character transmission rather than separate packets.
5. The transport layer is the protocol supporting the movement of the data, such as Transmission Control Protocol (TCP), HTTP or User Datagram Protocol (UDP). The application layer is the interface between the IoT device and the network with which it will communicate.
6. The network, transport, and session layers facilitate data transfer over the connection, with a focus on logical addressing, traffic directing, error correction, flow control, congestion avoidance, session management, and reliability.




### MPTCP

MPTCP, or Multipath TCP, is an ongoing effort of the Internet Engineering Task Force's (IETF) Multipath TCP working group. The aim of MPTCP is to allow a Transmission Control Protocol (TCP) connection to use multiple paths to maximize throughput and increase redundancy .

MPTCP is a transport layer protocol, which is the OSI Level 4 layer and is recognized by the same name in the TCP-IP model. The transport layer is part of the infrastructure layer in the IOT reference architecture .

In the context of IoT, the transport layer is the protocol supporting the movement of the data, such as Transmission Control Protocol (TCP), HTTP or User Datagram Protocol (UDP). The application layer is the interface between the IoT device and the network with which it will communicate .

Other transport layer protocols include TCP, UDP, DCCP, SCTP, TLS, and DTLS .



### UDP

- UDP stands for User Datagram Protocol.
- It is a transport layer protocol used for transmitting data over the internet.
- UDP is a connectionless protocol, meaning that it does not establish a connection before transmitting data.
- It is considered to be a faster protocol than TCP because it does not have the overhead of error checking and retransmission of lost packets.
- UDP is commonly used for real-time applications such as online gaming, video conferencing, and streaming media.
- UDP does not guarantee the delivery of packets, so it is not suitable for applications that require reliable data transmission.
- UDP packets are called datagrams and have a fixed size header of 8 bytes.
- The header contains information such as the source and destination port numbers, the length of the datagram, and a checksum for error checking.
- UDP is a simple protocol and does not provide advanced features such as flow control or congestion control.
- Applications that use UDP must implement their own error checking and recovery mechanisms.




### DCCP

DCCP (Datagram Congestion Control Protocol) is a transport layer protocol that provides a way to send unreliable datagrams with congestion control. It is designed for applications that require fast delivery of data, but can tolerate some loss of data, such as multimedia streaming or online gaming.

Some key features of DCCP include:

1. Congestion control: DCCP uses a congestion control mechanism to avoid overwhelming the network with too much traffic.
2. Unreliable delivery: DCCP does not guarantee delivery of datagrams, which means that some data may be lost during transmission.
3. Connection-oriented: DCCP is a connection-oriented protocol, which means that a connection must be established between two endpoints before data can be transmitted.
4. Bidirectional communication: DCCP allows for bidirectional communication between two endpoints, meaning that data can be sent in both directions.
5. Support for multiple congestion control mechanisms: DCCP allows for the use of different congestion control mechanisms, depending on the needs of the application.

DCCP is used in applications where fast delivery of data is more important than reliable delivery. It is commonly used in multimedia streaming and online gaming, where some loss of data is acceptable. DCCP provides a way to send data quickly, while still avoiding congestion in the network. It is an alternative to other transport layer protocols, such as TCP and UDP.



### SCTP (Stream Control Transmission Protocol)

SCTP is a transport layer protocol used in the Internet Protocol Suite. It is a reliable, message-oriented protocol that provides several features not found in other transport protocols such as TCP and UDP.

Some of the key features of SCTP include:

1. **Multi-homing:** SCTP allows for the establishment of an association between two endpoints that have multiple IP addresses. This provides redundancy and increases the reliability of the connection.

2. **Multi-streaming:** SCTP allows for multiple streams of data to be sent within a single SCTP association. This can improve the performance of applications that send multiple types of data.

3. **Selective Acknowledgments:** SCTP uses selective acknowledgments to improve the efficiency of data transmission. This allows the receiver to acknowledge specific data segments, rather than acknowledging all data up to a certain point.

4. **Congestion Control:** SCTP includes congestion control mechanisms to avoid overwhelming the network with too much data.

SCTP is used in several applications, including telephony signaling and web browsing. It is also used in the Internet of Things (IoT) to provide reliable communication between devices.



### Session Layer

The Session Layer is the fifth layer of the OSI model and is responsible for establishing, managing, and terminating connections between applications. This layer provides the mechanism for controlling the dialogue between the two end systems and managing data exchange. Some of the key functions of the Session Layer include:

1. **Session establishment, maintenance, and termination**: The Session Layer is responsible for setting up and maintaining the connection between two applications, as well as terminating the connection when it is no longer needed.

2. **Dialogue control**: This layer allows two systems to enter into a dialogue, which can be either half-duplex or full-duplex.

3. **Synchronization**: The Session Layer provides synchronization services, such as checkpointing and recovery, to ensure that data is exchanged in an orderly and reliable manner.

4. **Token management**: In some cases, the Session Layer may use tokens to control the dialogue between the two end systems.

The Session Layer is an important component of the OSI model, as it provides the necessary services for managing and controlling the communication between two applications. It is responsible for ensuring that the connection is established and maintained in an orderly and reliable manner, and that data is exchanged according to the agreed-upon rules and procedures.



### HTTP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- HTTP stands for Hypertext Transfer Protocol.
- It is an application layer protocol used for transmitting data over the internet.
- HTTP is the foundation of data communication for the World Wide Web.
- It is a request-response protocol between a client and a server.
- A client sends an HTTP request to the server, and the server responds with an HTTP response.
- HTTP is a stateless protocol, meaning that each request is treated independently and the server does not retain any information about previous requests.
- HTTP uses TCP as its underlying transport protocol.
- HTTP/1.1 is the most widely used version of HTTP, but HTTP/2 is gaining popularity due to its improved performance.
- HTTP supports several methods, including GET, POST, PUT, DELETE, and others, to perform different actions on the server.
- HTTP also supports various status codes to indicate the outcome of a request, such as 200 OK, 404 Not Found, and 500 Internal Server Error.




### CoAP

CoAP (Constrained Application Protocol) is a protocol architecture used in IoT (Internet of Things). It is specified in RFC 7252 . The CoAP protocol is designed to be lightweight and uses DTLS (Datagram Transport Layer Security) to provide security and reliable communications .

#### CoAP Architecture
The WWW and the constraints ecosystem are the two foundational elements of the CoAP protocol architecture. The server monitors and helps in communication happening using CoAP and HTTP while proxy devices bridge the existing gap for these two ecosystems, making the communication smoother .

#### CoAP Message Format
CoAP messages are exchanged between the CoAP client and the CoAP server. The message format and exchanges are mentioned in the CoAP architecture .

#### CoAP in IoT
CoAP is one of the important protocols in the Internet of Things. IoT protocols ensure that information from one device or sensor gets read and understood by another device, a gateway, or a service. Different IoT protocols have been designed and optimized for different scenarios and usage .



### XMPP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- XMPP stands for Extensible Messaging and Presence Protocol.
- It is an open protocol for streaming XML elements in order to exchange messages and presence information in close to real-time .
- The XMPP protocol is based on the typical client-server architecture, in which the XMPP client uses the XMPP server with the TCP socket .
- XMPP technologies use a decentralized client-server architecture related to the architecture used for the World Wide Web and the email network .
- In decentralized client-server architecture, client developers can focus on user experience, and server developers can focus on reliability and scalability .
- XMPP provides a general framework for messaging across a network, offering a multitude of applications beyond traditional instant messaging (IM) and the distribution of presence data .
- XMPP is an excellent protocol for use within the Internet of Things .




### AMQP

- AMQP stands for Advanced Message Queuing Protocol.
- It is a session layer protocol which runs over TCP layer.
- It is based on publish/subscribe architecture similar to MQTT protocol architecture .
- AMQP version 1.0 supports various broker architectures that may be used to receive, queue, route, and deliver messages or be used peer-to-peer .
- There are three major pieces specified in the scope of AMQP 1.0. These define the networking protocol, a representation for message envelope data and the basic semantics of broker services .
- Both MQTT and AMQP run over TCP connections, both are client-server in architecture and bi-directional .
- AMQP was designed to provide general purpose high performance enterprise messaging, whereas MQTT was created as an IoT protocol .
- AMQP has many features to cater for a range of messaging scenarios and is more complex than MQTT .



### MQTT

MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol designed for machine-to-machine (M2M) communication. It is commonly used in IoT (Internet of Things) and IIoT (Industrial Internet of Things) infrastructure .

#### MQTT Architecture

The MQTT architecture is made up of two key parts: the MQTT broker and the MQTT client. The broker is responsible for receiving messages from clients and distributing them to the appropriate subscribers. The client is responsible for publishing messages to the broker and subscribing to topics to receive messages .

#### MQTT Protocol

MQTT uses a publish/subscribe pattern, which is ideal for small devices that require efficient bandwidth and battery use. The protocol supports persistent sessions, which reduces the time to reconnect the client with the broker. MQTT also makes it easy to encrypt messages using TLS and authenticate clients using modern authentication protocols, such as OAuth .

#### MQTT Use Cases

MQTT is used in a variety of IoT applications, including wireless IoT technologies such as Zigbee and LoRaWAN. Other protocols, such as AMPQ, CoAP, and JMS, also use a broker-based architecture similar to MQTT .

#### Transport Layer

In any IoT protocol, the transport layer enables and safeguards the communication of data as it travels between layers. MQTT uses the Transmission Control Protocol (TCP) as its transport layer .



## Unit 5 - Service Layer Protocols & Security

Service layer protocols are responsible for providing end-to-end communication services between applications. These protocols operate at the application layer of the OSI model and are responsible for providing services such as file transfer, email, and remote login.

Some common service layer protocols include:

1. **Hypertext Transfer Protocol (HTTP)**: This protocol is used for transmitting web pages over the internet.
2. **File Transfer Protocol (FTP)**: This protocol is used for transferring files between computers over a network.
3. **Simple Mail Transfer Protocol (SMTP)**: This protocol is used for sending and receiving email messages.
4. **Telnet**: This protocol is used for remote login to a computer over a network.

Security is an important aspect of service layer protocols. These protocols must ensure that the data being transmitted is protected from unauthorized access and tampering. Some common security measures used by service layer protocols include encryption, authentication, and access control.

Encryption is the process of converting plaintext data into ciphertext, which is unreadable without the proper decryption key. This ensures that even if the data is intercepted, it cannot be read by unauthorized parties.

Authentication is the process of verifying the identity of a user or system. This is typically done using a username and password, but other methods such as biometric authentication or smart cards can also be used.

Access control is the process of determining who is allowed to access a particular resource and what actions they are allowed to perform. This can be done using access control lists or role-based access control.

In summary, service layer protocols provide end-to-end communication services between applications and must ensure the security of the data being transmitted. Common security measures include encryption, authentication, and access control.



### Service Layer

The service layer is a component of the Internet of Things (IoT) architecture that provides a range of services to applications and users. It is responsible for managing the communication between the application layer and the network layer. The service layer protocols and security measures are essential for ensuring the reliable and secure transmission of data in IoT systems.

Some key points to note about the service layer in the context of IoT architecture and protocols are:

1. The service layer provides a range of services to applications and users, including device management, data management, and event processing.

2. Service layer protocols are responsible for managing the communication between the application layer and the network layer. Some common service layer protocols used in IoT systems include MQTT, CoAP, and AMQP.

3. Security is a critical concern in IoT systems, and the service layer plays an important role in ensuring the secure transmission of data. Security measures at the service layer may include encryption, authentication, and access control.

4. The service layer is an essential component of the IoT architecture, providing the necessary services and security measures to support the reliable and secure operation of IoT systems.




### oneM2M

oneM2M is a global standard for IoT (Internet of Things) service layer protocols and security. It is designed to provide a common service layer for IoT devices, servers, and applications to communicate with each other, regardless of the underlying communication technologies.

- **Service Layer for multivendor interoperability**: The architecture standardized by oneM2M defines an IoT Service Layer, i.e. a vendor-independent software Middleware between processing and communication hardware and IoT applications providing a set of functions commonly needed by IoT applications.

- **Unlimited addressing capability**: oneM2M provides unlimited addressing capability, for example through IPv6.

- **M2M Service Layer**: The M2M Service Layer is a software layer between transport and application protocol layers. It provides data transport, security, device discovery, and device management across a multitude of vertical domains, independent of communication technologies in the lower layers.

- **oneM2M Architecture**: The oneM2M architecture divides IoT functions into three major domains: the application layer, the services layer, and the network layer. The oneM2M architecture gives major attention to connectivity between devices and their applications.

- **Interoperability and Cost-effectiveness**: oneM2M's main goal is to create consistency in how devices, servers, and applications communicate through a standardized M2M Service Layer. This leads to interoperability, cost-effectiveness, economies of scale, reduced fragmentation, and a larger market.




### ETSI M2M

The European Telecommunications Standards Institute (ETSI) IoT Standard, also known as the ESTI M2M Reference Architecture, is the high-level functional architecture that consists of Device and Gateway Domain and Network Domain . ETSI, as a standard body in the telecommunication industry, has defined a comprehensive set of common security mechanisms to protect the IoT/M2M system. They are Service Bootstrapping, Service Connection, and mId Security. For each mechanism, there are several protocols that we can choose .

ETSI is one of the founding partners in oneM2M, the global standards initiative that covers requirements, architecture, Application Programming Interface (API) specifications, security solutions, and interoperability for M2M and IoT technologies .

The ETSI M2M service capabilities layer (SCL) provides functions that are shared by different applications enabled by the M2M technologies .



### OMA for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- OMA SpecWorks has responded to market demand in the M2M area, understanding that a common set of standards for managing lightweight and low capability devices on a variety of networks is not just a nice option, but a mandatory approach to realize the potential of the Internet of Things (IoT).
- The OMA Lightweight M2M 1.1 standard (LwM2M 1.1) supports managing a broad spectrum of IoT devices including devices operating in LPWAN networks. LwM2M provides device management and service enablement capabilities for managing the entire lifecycle of the IoT device. LwM2M 1.1 adds support for a Non-IP transport binding.
- Application-layer security is needed for many IoT service topologies to prevent critical data from becoming unprotected in middleboxes. The paper gives real-world use cases for application-layer end-to-end IoT security and describes the Open Mobile Alliance solution to these types of use cases.
- In this case, an IoT service needs more than TLS to achieve end-to-end security: Security at the application layer preserves end-to-end security over middleboxes and IoT gateways. Security is applied to the application layer to make it unchangeable and unreadable between application endpoints .
- It's helpful to divide your IoT architecture into several zones as part of the threat modeling exercise: Device, Field gateway, Cloud gateway, Service. Each zone often has its own data and authentication and authorization requirements.



### BBF for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

BBF stands for Broadband Forum, which is a non-profit industry organization that focuses on engineering smarter and faster broadband networks. Here are some key points to note about BBF in the context of Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS:

1. BBF develops technical specifications and implementation guidelines for service providers and equipment manufacturers to promote interoperability and improve the performance of broadband networks.
2. BBF has a working group dedicated to the development of service layer protocols and security for IoT devices.
3. BBF's work in this area includes the development of the User Services Platform (USP), which is a protocol for managing and controlling IoT devices.
4. USP provides a secure and standardized way for service providers to remotely manage and control IoT devices, enabling the delivery of new services and improving the user experience.
5. BBF also works on the development of security standards for IoT devices, including the use of encryption and authentication mechanisms to protect data and prevent unauthorized access.




# Unit 5 - Service Layer Protocols & Security

### Security in IoT Protocols

- IoT protocols have to deal with security breaches at the site of the cloud service provider and the security issues pertaining to data privacy, authentication, authorization, and trust management in a distributed heterogeneous environment.
- A core aspect of IoT security is to maintain security, privacy, and integrity of data in storage (stored in the IoT device, in the network server, the cloud, etc.), and also during transit.
- Security concerns must be prioritized in order to minimize the attack surface and prevent security issues, since IoT technology is intended to be used in numerous critical sectors, particularly the economy and national security, with varying industry standards and specifications.
- MQTT is one of the most common security protocols used in internet of things security. It was invented by Dr. Andy Stanford-Clark and Arlen Nipper in 1999. MQTT stands for Message Queuing Telemetry Transport and is a client-server communicating messaging transport protocol.
- IoT platforms manage hardware and software protocols, offer security and authentication, and provide user interfaces. The exact definition of an IoT platform varies because more than 400 service providers offer features that range from software and hardware to SDKs and APIs.



### MAC 802.15.4

MAC 802.15.4 is a standard that specifies the physical layer and media access control for low-rate wireless personal area networks (LR-WPANs). It is maintained by the IEEE 802.15 working group.

Some key features of MAC 802.15.4 include:
- It operates in the unlicensed frequency bands: 868 MHz in Europe, 915 MHz in North America, and 2.4 GHz worldwide.
- It supports data rates of 20 kbps, 40 kbps, and 250 kbps.
- It supports star, peer-to-peer, and mesh topologies.
- It provides mechanisms for channel access, device association and disassociation, and frame validation.
- It supports both beacon-enabled and non-beacon-enabled modes.
- It provides security services such as access control, message integrity, and message confidentiality.

MAC 802.15.4 is commonly used in applications such as industrial monitoring and control, home automation, and medical data collection. It is the basis for other wireless communication standards such as ZigBee, Z-Wave, and Thread.



### 6LoWPAN

6LoWPAN stands for IPv6 over Low-power Wireless Personal Area Networks. It was a working group of the Internet Engineering Task Force (IETF) created with the intention of applying the Internet Protocol (IP) even to the smallest devices, enabling low-power devices with limited processing capabilities to participate in the Internet of Things (IoT).

The 6LoWPAN group defined encapsulation, header compression, neighbor discovery and other mechanisms that allow IPv6 to operate over IEEE 802.15.4 based networks. An open standard defined by the IETF, 6LoWPAN transmits IPv6 datagrams over low-power wireless mesh networks targeting residential and office automation, smart grid, industrial monitoring, and other applications that require wireless internet connectivity at lower data rates.

6LoWPAN only specifies operation of IPv6 over the IEEE 802.15.4 standard, edge routers may also support IPv6 transition mechanisms to connect 6LoWPAN networks to IPv4 networks, such as NAT64 defined in RFC 6146. These IPv6 transition mechanisms do not require the 6LoWPAN nodes to implement IPv4 in whole or in part.



### RPL

RPL stands for Routing Protocol for Low Power and Lossy Networks. It is a graph-based IPv6 protocol . RPL is considered the de facto routing protocol for the Internet of Things (IoT) . It supports multipoint-to-point (MP-to-P), point-to-point (P-to-P) and point-to-multipoint (P-to-MP) communications .

The Internet Engineering Task Force (IETF) developed RPL as the routing protocol for low power and lossy networks (LLNs) and standardized it in RFC6550 in 2012 . Since its standardization, RPL has contributed to the advancement of communications in the world of tiny, embedded networking devices by providing, along with other standards, a baseline architecture for IoT .

After deployment, the root node designated as DODAG sends DIO messages to the neighboring nodes .



### Application Layer

The application layer is the topmost layer in the OSI model of computer networking. It provides services to the user and interacts with the software applications. This layer is responsible for providing protocols and services that are required for communication between applications.

Some of the key points to remember about the application layer are:

1. It is the topmost layer in the OSI model.
2. It provides services to the user and interacts with the software applications.
3. It is responsible for providing protocols and services that are required for communication between applications.
4. Some of the common protocols used in the application layer are HTTP, FTP, SMTP, and DNS.
5. The application layer is responsible for providing a user interface to the network services.

In the context of IoT Architecture and Protocols, the application layer plays a crucial role in enabling communication between devices and applications. It provides the necessary protocols and services to ensure that data can be transmitted and received by the devices and applications in a secure and reliable manner.

