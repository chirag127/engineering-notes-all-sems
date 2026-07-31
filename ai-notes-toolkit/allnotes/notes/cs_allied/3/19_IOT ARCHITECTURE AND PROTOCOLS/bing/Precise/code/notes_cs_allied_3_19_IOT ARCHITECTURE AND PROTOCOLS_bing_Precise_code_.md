

# IOT ARCHITECTURE AND PROTOCOLS

IoT architecture refers to the many ways that IoT devices are structured to meet user needs. Based on complexity, IoT system elements are grouped into 3 to 7 layers, each with its own role. Notably, IoT architecture lacks standardized protocols, raising compatibility, security, and other challenges.

An IoT system has four types of transmission channels for data communication. Each IoT protocol in the IoT system architecture enables device-to-device, device-to-gateway, gateway-to-data center, or gateway-to-cloud communication, as well as communication between data centers.

There are two types of IoT protocols. Message queue telemetry transport (MQTT) protocol is one of them. Another one is Constrained application protocol (CoAP). Advanced message queuing protocol (AMQP) is also an IoT protocol.

Internet protocol (IP) is a set of rules that dictates how data gets sent to the internet. IoT protocols ensure that information from one device or sensor gets read and understood by another device, a gateway, a service. Different IoT protocols have been designed and optimized for different scenarios and usage.



## Unit 1 - IoT-An Architectural Overview

The Internet of Things (IoT) is a network of interconnected devices that can communicate with each other and with the internet. These devices can range from simple sensors to complex machines, and they can be used in a variety of applications, including home automation, healthcare, and transportation.

1. **IoT Architecture**: The architecture of an IoT system typically consists of four main layers: the device layer, the communication layer, the information processing layer, and the application layer.
2. **Device Layer**: The device layer is made up of the physical devices that make up the IoT system. These devices can include sensors, actuators, and other types of hardware that can collect and transmit data.
3. **Communication Layer**: The communication layer is responsible for transmitting data between the devices in the IoT system and the information processing layer. This can be done using a variety of communication protocols, including Wi-Fi, Bluetooth, and cellular networks.
4. **Information Processing Layer**: The information processing layer is responsible for processing the data collected by the devices in the IoT system. This can include tasks such as data analysis, data storage, and data visualization.
5. **Application Layer**: The application layer is responsible for providing the user with access to the data collected by the IoT system. This can include user interfaces, such as mobile apps or web portals, that allow the user to interact with the data.

These four layers work together to create a complete IoT system that can collect, transmit, process, and present data to the user. Each layer plays a critical role in the overall functionality of the system, and it is important to carefully design and implement each layer to ensure that the IoT system is reliable, secure, and efficient.



### Building an architecture for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. **Introduction to IoT**: Define the Internet of Things (IoT) and its key components, including sensors, actuators, and connectivity.
2. **IoT Architecture**: Describe the layered architecture of IoT systems, including the perception, network, and application layers.
3. **Perception Layer**: Discuss the role of the perception layer in collecting data from the physical world through sensors and actuators.
4. **Network Layer**: Explain how the network layer facilitates communication between devices and the cloud, including the use of protocols such as MQTT and CoAP.
5. **Application Layer**: Describe the role of the application layer in processing and presenting data to the user, including the use of cloud computing and data analytics.
6. **Security and Privacy**: Discuss the importance of security and privacy in IoT systems, including the use of encryption and access control.
7. **Case Studies**: Provide examples of real-world IoT applications, such as smart homes, smart cities, and industrial IoT.




### Main design principles and needed capabilities for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. The overall design objective of IoT architecture shall be to target a horizontal system of real-world services that are open, service-oriented, secure, and offer trust.
2. Design for reuse of deployed IoT resources across application domains.
3. Design for a set of support services that provide open service-oriented capabilities and can be used for application development and execution.
4. The architecture relies on the separation of resources providing sensing and actuation from the actual devices, a set of contextual and real world entity-centric services, and the users of the services.
5. With defined IoT design principles, product designers can make devices that align well with end-user expectations, protect data at all levels and are scalable to all deployment sizes.
6. The network layer of an IoT architecture is responsible for providing communication and connectivity between devices in the IoT system. It includes protocols and technologies that enable devices to connect and communicate with each other and with the wider internet.



### An IoT architecture outline for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. **Introduction:** IoT (Internet of Things) refers to the interconnection of physical devices, vehicles, buildings, and other items embedded with electronics, software, sensors, and network connectivity that enable these objects to collect and exchange data.

2. **IoT Architecture:** The architecture of IoT can be divided into four main layers: the sensing layer, the network layer, the service layer, and the application layer.

3. **Sensing Layer:** This layer is responsible for collecting data from the physical world through sensors and actuators. These devices can measure various parameters such as temperature, humidity, light, and motion.

4. **Network Layer:** This layer is responsible for transmitting the data collected by the sensing layer to the service layer. It can use various communication technologies such as Wi-Fi, Bluetooth, cellular, and satellite.

5. **Service Layer:** This layer is responsible for processing the data received from the network layer and providing services to the application layer. It can include data storage, data analysis, and data visualization.

6. **Application Layer:** This layer is responsible for providing the user interface and enabling the user to interact with the IoT system. It can include various applications such as home automation, health monitoring, and smart transportation.

7. **Conclusion:** The architecture of IoT is essential for understanding how different components of an IoT system interact with each other. By understanding the different layers of the architecture, one can design and implement an efficient and effective IoT system.



### Standards considerations for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. **Introduction to IoT:** The Internet of Things (IoT) is a system of interconnected devices, machines, and objects that are able to collect and exchange data using embedded sensors and software.

2. **IoT Architecture:** The architecture of IoT can be divided into four main layers: the sensing layer, the network layer, the service layer, and the application layer.

3. **Sensing Layer:** The sensing layer is responsible for collecting data from the physical world using sensors and actuators.

4. **Network Layer:** The network layer is responsible for transmitting the data collected by the sensing layer to the service layer.

5. **Service Layer:** The service layer is responsible for processing the data received from the network layer and providing services to the application layer.

6. **Application Layer:** The application layer is responsible for presenting the data and services provided by the service layer to the end user.

7. **IoT Protocols:** There are several protocols used in IoT, including MQTT, CoAP, and HTTP.

8. **IoT Security:** Security is a major concern in IoT, and measures must be taken to ensure the security of data and devices.

9. **IoT Standards:** There are several organizations working on developing standards for IoT, including the IEEE, the IETF, and the ITU.

10. **Conclusion:** IoT is a rapidly growing field with many potential applications. Understanding the architecture and protocols of IoT is essential for its successful implementation. Standards are also important to ensure interoperability and security in IoT systems.



### M2M and IoT Technology Fundamentals

M2M (Machine-to-Machine) and IoT (Internet of Things) are two closely related technologies that enable devices to communicate with each other and with the internet. Here are some key points to understand about these technologies:

1. **M2M** refers to the direct communication between devices, without the need for human intervention. This can include wired or wireless communication, and can be used for a wide range of applications, such as remote monitoring and control, asset tracking, and predictive maintenance.

2. **IoT** refers to the broader concept of connecting devices to the internet, allowing them to collect and share data. This can include M2M communication, but also extends to other types of communication, such as between devices and cloud services, or between devices and human users.

3. Both M2M and IoT technologies rely on a range of underlying technologies, including sensors, actuators, communication protocols, and data processing and analysis tools.

4. One of the key benefits of M2M and IoT technologies is the ability to collect and analyze large amounts of data, enabling improved decision-making, automation, and predictive capabilities.

5. Security and privacy are important considerations when implementing M2M and IoT technologies, as the collection and sharing of data can create potential vulnerabilities.

6. M2M and IoT technologies are being used in a wide range of industries, including manufacturing, transportation, healthcare, and smart homes and cities.

7. The development of M2M and IoT technologies is ongoing, with new applications and use cases emerging regularly. As these technologies continue to evolve, they are likely to play an increasingly important role in many aspects of our lives.




### Devices and Gateways

#### Unit 1 - IoT-An Architectural Overview

In the context of IoT architecture and protocols, devices and gateways play a crucial role in the overall system. Here are some key points to consider:

1. **Devices** refer to the physical objects that are connected to the internet and are capable of collecting and transmitting data. These can include sensors, actuators, and other types of hardware that are embedded in various objects and environments.

2. **Gateways** act as intermediaries between the devices and the cloud or other remote systems. They are responsible for aggregating data from multiple devices, performing some level of processing or analysis, and then transmitting the data to the cloud or other systems for further processing and storage.

3. Devices and gateways can communicate with each other using various protocols, such as MQTT, CoAP, and HTTP. The choice of protocol will depend on factors such as the type of data being transmitted, the power and bandwidth constraints of the devices, and the requirements of the overall system.

4. In many IoT systems, the devices and gateways are designed to operate with minimal human intervention. This means that they must be able to function autonomously, and be able to recover from failures or disruptions in the network.

5. Security is a major concern when it comes to devices and gateways in IoT systems. It is important to ensure that the data being transmitted is protected from unauthorized access or tampering, and that the devices and gateways themselves are secure from attacks or hacking attempts.

Overall, devices and gateways are essential components of any IoT system, and their design and implementation must be carefully considered in order to ensure the reliability, scalability, and security of the overall system.



### Local and Wide Area Networking

Local Area Network (LAN) and Wide Area Network (WAN) are two types of computer networks that are used to connect devices and facilitate communication and data sharing.

1. **Local Area Network (LAN):** A LAN is a network that connects devices within a limited geographical area, such as a home, school, or office building. LANs are typically used to connect personal computers, printers, and other devices, and allow users to share resources such as files, applications, and internet connections.

2. **Wide Area Network (WAN):** A WAN is a network that connects devices over a large geographical area, such as between cities or even countries. WANs are typically used by businesses and organizations to connect their various locations and allow for communication and data sharing between them.

In the context of IoT, LANs and WANs play an important role in connecting IoT devices and allowing them to communicate and share data. LANs are often used to connect IoT devices within a home or building, while WANs are used to connect IoT devices across larger distances.



### Data Management for Unit 1 - IoT: An Architectural Overview

Data management is an essential aspect of IoT architecture and protocols. It involves the collection, storage, processing, and analysis of data generated by IoT devices. Here are some key points to consider when studying data management in the context of IoT:

1. **Data Collection:** IoT devices generate large amounts of data, which must be collected and transmitted to a central location for processing and analysis. This data can include sensor readings, device status information, and user interactions.

2. **Data Storage:** Once collected, data must be stored in a way that allows for efficient retrieval and analysis. This can involve the use of databases, data lakes, or other storage solutions.

3. **Data Processing:** Data processing involves the transformation of raw data into a format that can be analyzed and used to make decisions. This can include data cleaning, aggregation, and normalization.

4. **Data Analysis:** Data analysis involves the use of statistical and machine learning techniques to extract insights and knowledge from the data. This can include trend analysis, anomaly detection, and predictive modeling.

5. **Data Security:** Data security is a critical concern in IoT systems, as the data generated by these devices can be sensitive and valuable. Measures must be taken to ensure the confidentiality, integrity, and availability of the data.

Overall, data management is a crucial component of IoT architecture and protocols, and it is essential to have a solid understanding of its principles and practices when studying this subject.



### Business processes in IoT

Business processes in IoT refer to the various activities and tasks that are involved in the implementation and management of IoT systems in a business context. These processes can include:

1. **Planning and strategy:** This involves identifying the business goals and objectives that can be achieved through the implementation of IoT systems, and developing a strategy for achieving these goals.

2. **Design and development:** This involves designing the IoT system architecture, selecting the appropriate hardware and software components, and developing the necessary software and applications.

3. **Implementation and deployment:** This involves installing and configuring the IoT system, integrating it with existing business systems and processes, and deploying it to the intended users.

4. **Operation and maintenance:** This involves monitoring and managing the performance of the IoT system, ensuring its availability and reliability, and performing regular maintenance and updates.

5. **Data management and analysis:** This involves collecting, storing, and analyzing the data generated by the IoT system, and using this data to derive insights and make informed business decisions.

6. **Security and compliance:** This involves ensuring the security and privacy of the data collected by the IoT system, and complying with relevant regulations and standards.

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

- **M2M** stands for **Machine-to-Machine** and refers to the connection of two or more devices with the Internet for data sharing and analytics.
- **IoT** stands for **Internet of Things** and refers to the connection of any device to the Internet for better performance.
- Both IoT and M2M provide remote access for exchanging information among machines without human intervention.
- The key difference between IoT and M2M is that IoT has overarching results or open-ended capabilities, while M2M is more of a vertical application which meets internal demands.
- Data is different and its use is different in IoT application development from M2M.
- M2M systems use point-to-point communications between machines, sensors, and hardware over cellular or wired networks, while IoT systems rely on IP-based networks to send data collected from IoT-connected devices to gateways, the cloud, or middleware platforms.



### Knowledge Management for Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. Knowledge management is the process of creating, sharing, using and managing the knowledge and information of an organization.
2. It refers to a multidisciplinary approach to achieving organizational objectives by making the best use of knowledge.
3. In the context of IoT, knowledge management plays a crucial role in the architectural overview of the system.
4. IoT devices generate a large amount of data, which needs to be managed and analyzed to extract useful information and knowledge.
5. Knowledge management in IoT involves the collection, storage, processing, and analysis of data generated by IoT devices.
6. This knowledge can then be used to improve the performance and efficiency of the IoT system, as well as to make informed decisions.
7. Effective knowledge management in IoT requires the use of advanced data analytics techniques and tools, as well as the integration of various data sources.
8. It also involves the development of knowledge-sharing platforms and collaboration tools to facilitate the exchange of information and knowledge among different stakeholders.
9. In summary, knowledge management is a key component of the architectural overview of IoT systems, and plays a crucial role in ensuring the success and sustainability of IoT initiatives.



## Unit 2 - Reference Architecture

1. A reference architecture is a document or set of documents that provides a common framework and best practices for the design and implementation of a specific type of system.
2. It serves as a blueprint for the development of systems within a particular domain, providing guidance on the selection of technologies, the organization of components, and the definition of interfaces.
3. Reference architectures are typically developed by industry consortia, standards organizations, or vendors, and are intended to promote interoperability and reduce development costs by providing a common foundation for the design of systems.
4. They are often accompanied by reference implementations, which are concrete examples of systems built according to the reference architecture.
5. Reference architectures can be applied to a wide range of systems, including enterprise systems, cloud computing environments, and Internet of Things (IoT) systems.
6. They are particularly useful for complex systems that involve the integration of multiple technologies and components.
7. By providing a common framework and vocabulary, reference architectures can facilitate communication and collaboration among stakeholders, including architects, developers, and business analysts.
8. They can also help to ensure that systems are designed with scalability, security, and other non-functional requirements in mind.




### IoT Architecture-State of the Art

- A reference model is a model that describes the main conceptual entities and how they are related to each other.
- The reference architecture aims at describing the main functional components of a system as well as how the system works, how the system is deployed, what information the system processes, etc.
- The principles of Reactive Systems define the state-of-the-art programming models for IoT.
- IoT platforms must tackle asset management as a foundational problem and all of these platforms have facilities for managing the provisioning of devices and services, public key infrastructure (PKI), software and firmware updates, and desired-state configuration of devices, at huge scale.
- IoT constitutes one of the most important technological development in the last decade. It has the potential to deeply affect our life style.



### Introduction for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. The Internet of Things (IoT) is a network of interconnected devices that can communicate with each other and exchange data.
2. IoT devices can range from simple sensors to complex systems such as smart homes and autonomous vehicles.
3. The reference architecture for IoT provides a framework for designing and implementing IoT systems.
4. The reference architecture includes various layers such as the device layer, the communication layer, the data processing layer, and the application layer.
5. Each layer has its own set of protocols and standards that enable the smooth functioning of the IoT system.
6. The reference architecture also includes security and privacy considerations to ensure the safety and security of the data being exchanged between the devices.
7. Understanding the reference architecture is crucial for designing and implementing effective and efficient IoT systems.




### State of the art for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. The Internet of Things (IoT) is a rapidly evolving field that involves the interconnection of physical devices, vehicles, buildings, and other items embedded with electronics, software, sensors, and network connectivity.
2. The reference architecture for IoT provides a framework for the development and deployment of IoT systems.
3. The reference architecture includes several layers, including the device layer, the network layer, the service layer, and the application layer.
4. The device layer consists of the physical devices and sensors that collect data and perform actions.
5. The network layer provides the connectivity between the devices and the service layer.
6. The service layer provides the necessary services for the management and processing of the data collected by the devices.
7. The application layer provides the user interface and the necessary tools for the analysis and visualization of the data.
8. The reference architecture also includes security and privacy considerations, as well as the integration of IoT systems with other systems and technologies.
9. Several reference architectures have been proposed by different organizations, including the Industrial Internet Consortium (IIC), the OpenFog Consortium, and the European Telecommunications Standards Institute (ETSI).
10. The state of the art in IoT reference architecture is constantly evolving as new technologies and standards are developed.




### Reference Model and Architecture

1. A reference model is a standard framework that is used to organize and understand the various components and layers of a system.
2. In the context of IoT, a reference model provides a common language and understanding of the different elements that make up an IoT system.
3. The reference architecture is a blueprint for the design and implementation of an IoT system. It provides a detailed description of the components, their relationships, and the interactions between them.
4. The reference architecture is based on the reference model and provides a more concrete and specific representation of an IoT system.
5. The reference architecture can be used as a guide for the development of IoT systems, ensuring that all the necessary components are included and that they are properly integrated.
6. There are several reference models and architectures for IoT, including the IoT-A Reference Model and Architecture, the Industrial Internet Reference Architecture, and the Reference Architecture Model for Industry 4.0.
7. These reference models and architectures provide a common framework for the development of IoT systems, enabling interoperability and the integration of different components and technologies.




### IoT Reference Model

The IoT Reference Model, officially known as the IoT World Forum Reference Model, is an architecture that is similar to other technical models, but with a few new layers. These layers exist in all IoT implementations, but will be configured and built differently within each to meet the goals of the project .

The first major contribution of the IoT Architectural Reference Model (IoT ARM) is the IoT Reference Model itself. Besides models, the IoT Reference Model provides the concepts and definitions on which IoT architectures can be built .

An ARM consists of two main parts: a Reference Model and a Reference Architecture. A reference model describes the domain using a number of sub-models. The IoT Reference Model provides a platform for IoT architecture and IoT system to build a common grounding and common language .

Some of the most important components of an IoT reference model are terminology definition, interface definitions, interaction model, standards, communication model, and security and information models .



### IoT Reference Architecture

- The Internet of Things (IoT) reference architecture defines an approach to IoT solutions. Such solutions use information from devices, people, and applications with cloud or on-premises services and systems to generate insights and value .
- The IoT Reference Model aims at establishing a common grounding and a common language for IoT architectures and IoT systems. It consists of sub-models, which are used as the basis for one another .
- This IoT Reference Architecture is designed as a reference for the generation of compliant IoT concrete architectures that are tailored to one’s specific needs .
- Azure IoT reference architecture describes terminology, technology principles, common configuration environments, and composition of Azure IoT services. The purpose of the document is to provide an overview of the recommended architecture and implementation technology choices for how to build Azure IoT solutions .



### Introduction for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The Internet of Things (IoT) is a network of interconnected devices that can communicate with each other and with the internet.
- IoT devices can be anything from sensors and actuators to home appliances and wearable devices.
- The IoT architecture is the framework that defines how these devices interact with each other and with the internet.
- A reference architecture is a standardized architecture that serves as a template for designing and implementing IoT systems.
- The reference architecture for IoT includes several layers, including the device layer, the communication layer, the data processing layer, and the application layer.
- Each layer has its own set of protocols and standards that enable communication and data exchange between devices and the internet.
- The reference architecture provides a common language and framework for designing and implementing IoT systems, making it easier to develop and deploy IoT solutions.
- In this unit, we will explore the different layers of the reference architecture for IoT and the protocols and standards used in each layer. We will also discuss the challenges and considerations when designing and implementing IoT systems using the reference architecture.



### Functional View

The functional view of the reference architecture for IoT systems focuses on the functional components and their interactions. This view is useful for understanding the overall functionality of the system and how the different components work together to achieve the desired goals.

Some key points to consider when studying the functional view of the reference architecture for IoT systems are:

1. The functional view identifies the main functional components of the system, such as sensors, actuators, gateways, and cloud services.
2. The interactions between these components are also described, including data flow and control flow.
3. The functional view can help to identify potential bottlenecks or areas for optimization in the system.
4. This view is useful for understanding the overall functionality of the system and how the different components work together to achieve the desired goals.
5. The functional view can also be used to identify potential security risks and to design appropriate security measures.

In summary, the functional view of the reference architecture for IoT systems provides a high-level overview of the system's functionality and the interactions between its components. This view is useful for understanding the overall system design and for identifying potential areas for improvement.



### Information View

The Information View is one of the views in the Reference Architecture for the Internet of Things (IoT). It is part of Unit 2 - Reference Architecture in the subject of IoT Architecture and Protocols.

- The Information View focuses on the data and information aspects of an IoT system.
- It describes the data models, data flows, and data storage and management within the system.
- The Information View is important for understanding how data is collected, processed, and used within an IoT system.
- It helps to ensure that the data is accurate, consistent, and available to the appropriate parties.
- The Information View also addresses issues such as data security, privacy, and ownership.

In summary, the Information View provides a detailed understanding of the data and information aspects of an IoT system, which is essential for the effective design and operation of the system. It is an important part of the overall Reference Architecture for IoT.



### Deployment and Operational View

The deployment and operational view of the reference architecture for IoT systems focuses on the physical deployment of the system components and their operational characteristics. This view is important for understanding how the system will be deployed and maintained in the real world.

1. **Physical Deployment:** This aspect of the deployment and operational view deals with the physical placement of the system components. This includes the location of sensors, actuators, gateways, and other devices that make up the IoT system. The physical deployment must take into account the environmental conditions, power requirements, and connectivity options for each component.

2. **Operational Characteristics:** This aspect of the deployment and operational view deals with the operational characteristics of the system components. This includes the power consumption, data transmission rates, and maintenance requirements of each component. The operational characteristics must be considered when designing the system to ensure that it can operate efficiently and effectively.

3. **Maintenance and Support:** The deployment and operational view also includes considerations for the maintenance and support of the IoT system. This includes the procedures for updating software, replacing hardware components, and providing technical support to users. A well-designed deployment and operational view will ensure that the IoT system can be maintained and supported throughout its lifecycle.

Overall, the deployment and operational view is an important part of the reference architecture for IoT systems. It provides a framework for understanding how the system will be deployed and operated in the real world, and helps to ensure that the system can be maintained and supported over time.



### Other Relevant Architectural Views

1. **Functional View:** This view describes the functional elements of the system, their responsibilities, interfaces, and primary interactions. It is used to represent the system's functional requirements and to design the system's high-level structure.

2. **Information View:** This view describes the system's data and information structures, their relationships, and the data flows between the system's functional elements. It is used to represent the system's information requirements and to design the system's data architecture.

3. **Concurrency View:** This view describes the system's concurrency and synchronization mechanisms, including the system's threads, processes, and inter-process communication mechanisms. It is used to represent the system's concurrency requirements and to design the system's concurrency architecture.

4. **Development View:** This view describes the system's software modules, their dependencies, and the system's build, packaging, and deployment processes. It is used to represent the system's development requirements and to design the system's development architecture.

5. **Deployment View:** This view describes the system's hardware and network infrastructure, including the system's servers, storage devices, network devices, and network topology. It is used to represent the system's deployment requirements and to design the system's deployment architecture.




### Real-World Design Constraints

When designing an IoT system, there are several real-world constraints that must be taken into consideration. These constraints can impact the design and functionality of the system, and must be carefully considered in order to create a successful and effective IoT solution. Some of the most important real-world design constraints include:

1. **Power consumption:** IoT devices often need to operate on battery power, and must be designed to consume as little power as possible in order to maximize battery life.

2. **Connectivity:** IoT devices need to be able to connect to the internet in order to transmit and receive data. This means that the devices must be designed to work with a variety of connectivity options, including Wi-Fi, cellular, and other wireless technologies.

3. **Security:** IoT devices can collect and transmit sensitive data, and must be designed with security in mind in order to protect this data from unauthorized access or tampering.

4. **Cost:** The cost of IoT devices can be a significant constraint, particularly for large-scale deployments. Designers must work to keep costs down while still delivering the necessary functionality.

5. **Scalability:** IoT systems must be able to scale to accommodate large numbers of devices and users. This means that the system must be designed to handle increasing amounts of data and traffic as the number of devices and users grows.

6. **Reliability:** IoT devices must be reliable and able to operate in a variety of conditions. This means that the devices must be designed to withstand environmental factors such as temperature, humidity, and vibration.

7. **Interoperability:** IoT devices must be able to work with other devices and systems. This means that the devices must be designed to use standard protocols and interfaces in order to ensure interoperability with other systems.

These are just some of the real-world design constraints that must be taken into consideration when designing an IoT system. By carefully considering these constraints, designers can create effective and successful IoT solutions that meet the needs of users and businesses.



### Introduction for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The Internet of Things (IoT) is a network of interconnected devices that can communicate with each other and exchange data.
- The IoT reference architecture is a framework that defines the various components and their interactions in an IoT system.
- The reference architecture provides a common language and understanding for designing and implementing IoT solutions.
- It helps to ensure interoperability, scalability, and security in IoT systems.
- The reference architecture is not a fixed design, but rather a flexible guide that can be adapted to the specific needs of different IoT applications.
- There are several reference architectures proposed by different organizations, such as the Industrial Internet Consortium (IIC) and the OpenFog Consortium.
- These reference architectures share common elements, such as the use of edge computing, cloud computing, and data analytics.
- Understanding the reference architecture is essential for designing and implementing effective IoT solutions.



### Technical Design Constraints

When designing an IoT system, there are several technical design constraints that must be taken into consideration. These constraints can affect the hardware, software, and overall architecture of the system. Some of the key technical design constraints to consider include:

1. **Power consumption**: IoT devices often need to operate on battery power, so it is important to design the system to minimize power consumption. This can be achieved through the use of low-power hardware components, efficient software algorithms, and power management techniques.

2. **Connectivity**: IoT devices need to be able to communicate with other devices and systems, so it is important to ensure that the system has reliable and robust connectivity. This can be achieved through the use of appropriate communication protocols and technologies, such as Wi-Fi, Bluetooth, cellular, or LPWAN.

3. **Scalability**: As the number of IoT devices in a system grows, it is important to ensure that the system can scale to accommodate the increased load. This can be achieved through the use of scalable architectures, such as cloud-based systems or distributed architectures.

4. **Security**: IoT systems can be vulnerable to security threats, so it is important to design the system with security in mind. This can be achieved through the use of secure communication protocols, encryption, and other security measures.

5. **Reliability**: IoT systems need to be reliable, so it is important to design the system to minimize the risk of failure. This can be achieved through the use of robust hardware and software, as well as through the use of redundancy and fault tolerance techniques.

6. **Cost**: The cost of an IoT system can be a significant constraint, so it is important to design the system to minimize costs. This can be achieved through the use of cost-effective hardware and software, as well as through the use of efficient system architectures.

These are some of the key technical design constraints to consider when designing an IoT system. By taking these constraints into account, it is possible to design a system that is efficient, reliable, and cost-effective.



### Data Representation and Visualization

Data representation and visualization are important aspects of the Unit 2 - Reference Architecture in the subject of IoT Architecture and Protocols. Here are some key points to consider:

1. **Data representation** refers to the methods and techniques used to encode and store data in a format that can be easily understood and processed by computers and humans.

2. **Data visualization** is the graphical representation of data and information, using visual elements such as charts, graphs, and maps to help users understand and analyze data.

3. Data representation and visualization are important in IoT systems because they allow users to easily understand and interact with the data generated by IoT devices.

4. There are many different data representation and visualization techniques, including tables, charts, graphs, and maps. The choice of technique depends on the type of data being represented and the intended audience.

5. Effective data representation and visualization can help users to identify patterns and trends in the data, make informed decisions, and communicate their findings to others.

6. It is important to choose the right data representation and visualization techniques to ensure that the data is presented in a clear and meaningful way.

7. Data representation and visualization are constantly evolving fields, with new techniques and tools being developed to help users better understand and interact with data.




### Interaction and Remote Control

Interaction and remote control are important aspects of the Internet of Things (IoT) architecture and protocols. These concepts allow users to interact with and control IoT devices from a distance, using various methods such as mobile applications, web interfaces, and voice commands.

1. **Mobile Applications:** Many IoT devices come with accompanying mobile applications that allow users to interact with and control the device from their smartphone or tablet. These applications often use Bluetooth or Wi-Fi to communicate with the device and provide a user-friendly interface for controlling its functions.

2. **Web Interfaces:** Some IoT devices can be controlled through a web interface, which allows users to interact with the device using a web browser on their computer or mobile device. This method of interaction is particularly useful for devices that are connected to a local network or the internet.

3. **Voice Commands:** Voice-controlled IoT devices are becoming increasingly popular, allowing users to interact with and control the device using voice commands. This method of interaction is particularly useful for hands-free operation and can be used in conjunction with other methods such as mobile applications and web interfaces.

In summary, interaction and remote control are essential components of the IoT architecture and protocols, allowing users to interact with and control IoT devices from a distance using a variety of methods. These methods include mobile applications, web interfaces, and voice commands, each with its own advantages and use cases.



## Unit 3 - IOT Data Link Layer & Network Layer Protocols

The Internet of Things (IoT) is a network of interconnected devices that can communicate with each other and exchange data. The data link layer and network layer protocols are essential components of the IoT architecture, as they enable the transmission of data between devices.

### Data Link Layer Protocols

The data link layer is responsible for providing a reliable link between two devices on a network. Some of the key functions of the data link layer include:

- Framing: The data link layer divides the data into frames for transmission.
- Error Control: The data link layer detects and corrects errors that may occur during transmission.
- Flow Control: The data link layer ensures that the sender does not overwhelm the receiver by sending too much data at once.

Some common data link layer protocols used in IoT include:

- **Zigbee**: A low-power, wireless mesh network protocol designed for IoT applications.
- **Z-Wave**: A wireless communication protocol used for home automation.
- **Thread**: A low-power, IPv6-based mesh networking protocol for IoT devices.

### Network Layer Protocols

The network layer is responsible for routing data between devices on a network. Some of the key functions of the network layer include:

- Addressing: The network layer assigns unique addresses to devices on the network.
- Routing: The network layer determines the best path for data to travel between devices.
- Fragmentation: The network layer divides large packets of data into smaller packets for transmission.

Some common network layer protocols used in IoT include:

- **IPv6**: The latest version of the Internet Protocol, designed to accommodate the growing number of IoT devices.
- **6LoWPAN**: A protocol that enables the transmission of IPv6 packets over low-power wireless networks.
- **RPL**: A routing protocol designed for low-power and lossy networks, commonly used in IoT applications.

In summary, the data link layer and network layer protocols play a crucial role in enabling communication between IoT devices. These protocols provide the necessary functions for reliable data transmission and efficient routing of data on the network. Understanding these protocols is essential for anyone working with IoT systems.



### PHY/MAC Layer(3GPP MTC) for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The **PHY layer** defines the physical and electrical characteristics of the network. It is responsible for managing the hardware that modulates and demodulates the RF bits.
- The **MAC layer** is responsible for sending and receiving RF frames.
- The top five protocols in the Link Layer are Ethernet, Wifi, WImax, Low rate WPAN and mobile communication such as 5G, 4G and 3G. PHY and MAC protocols use this layer.
- 3GPP MTC is one of the PHY/MAC Layer protocols used in IoT Data Link Layer & Network Layer Protocols.
- Other PHY/MAC Layer protocols include IEEE 802.11, IEEE 802.15, Wireless HART, ZWave, Bluetooth Low Energy, and Zigbee Smart Energy.



### IEEE 802.11

IEEE 802.11 is a set of standards for implementing wireless local area network (WLAN) computer communication in the 2.4, 3.6, 5, and 60 GHz frequency bands. They are created and maintained by the IEEE LAN/MAN Standards Committee (IEEE 802).

- IEEE 802.11 is used in most home and office networks to allow laptops, printers, smartphones, and other devices to communicate with each other and access the Internet without connecting wires.
- IEEE 802.11 is also a basis for vehicle-based communication networks with IEEE 802.11p.
- IEEE 802.11ad is an amendment that defines a new physical layer for 802.11 networks to operate in the 60 GHz millimeter wave spectrum. This frequency band has significantly different propagation characteristics than the 2.4 GHz and 5 GHz bands where Wi-Fi networks operate.
- IEEE 802.11 was the original version released in 1997. It provided 1 Mbps or 2 Mbps data rate in the 2.4 GHz band and used either frequency-hopping spread spectrum (FHSS) or direct-sequence spread spectrum (DSSS). It is obsolete now.
- IEEE 802.11 standard, popularly known as WiFi, lays down the architecture and specifications of wireless LANs (WLANs). WiFi or WLAN uses high frequency radio waves for connecting the nodes. There are several standards of IEEE 802.11 WLANs. The prominent among them are 802.11, 802.11a, 802.11b, 802.11g, 802.11n and 802.11p.
- IEEE Standard for Information Technology - Telecommunications and information exchange between systems - Local and Metropolitan Area networks - Specific requirements - Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) specifications. This standard is a revision of IEEE Std 802.11-1997.
- The IEEE has made available IEEE 802 standards for free download. Under this program, a standard may be downloaded for free six months after the initial publication of the standard. All relevant IEEE 802.11 Standard, Amendments, and Recommended Practices are listed. IEEE 802.11 Working Group Outgoing Liaison Statments and External Communications.



### IEEE 802.15

IEEE 802.15 is a working group of the Institute of Electrical and Electronics Engineers (IEEE) IEEE 802 standards committee which specifies Wireless Specialty Networks (WSN) standards. The working group was formerly known as Working Group for Wireless Personal Area Networks.

- IEEE 802.15.4a (formally called IEEE 802.15.4a-2007) is an amendment to IEEE 802.15.4 specifying additional physical layers (PHYs) to the original standard.
- The IEEE 802.15 Working Group is part of the 802 Local and Metropolitan Area Network Standards Committee of the IEEE Computer Society.
- The IEEE-SA is an international membership organization serving today's industries with a complete portfolio of standards programs. The IEEE has more than 400,000 members in approximately 150 countries.
- 802.15.4-2020 - IEEE Standard for Low-Rate Wireless Networks Abstract: The physical layer (PHY) and medium access control (MAC) sublayer specifications for low-data-rate wireless connectivity with fixed, portable, and moving devices with no battery or very limited battery consumption requirements are defined in this standard.



### WirelessHART

WirelessHART is a wireless communications protocol for process automation applications. It adds wireless capabilities to HART technology while maintaining compatibility with existing HART devices, commands, and tools. It is a subset of the HART industrial instrument communication standard as of version 7, communicating process data over 2.4 GHz radio waves.

- Individual instruments communicate with a common “gateway” device serving as an interface between the wireless network and a wired network or a host control system.
- WirelessHART uses mesh networking technology by design.
- It is a wireless sensor networking technology based on the Highway Addressable Remote Transducer Protocol (HART).
- Developed as a multi-vendor, interoperable wireless standard, WirelessHART was defined for the requirements of process field device networks.
- Designed as a self-healing, mesh technology that ensures 99.99% data reliability, this protocol enables communication between devices, eliminating the need for direct device.
- At the data-link layer, WirelessHART utilizes 10ms time slots for communications. These time slots can be dedicated to individual devices or shared amongst a group.




### ZWave

Z-Wave is a wireless communication protocol that operates at a frequency of 900MHz. It is suitable for small messages in IoT applications for home automation, with a range of 30 to 100 meters and a data transfer rate of 100kbps .

The Z-Wave protocol stack contains five layers: physical layer, MAC layer, transport layer, network layer, and application layer. The physical layer is responsible for modulation and coding, and data is transferred in 8-bit blocks with the most significant bit sent first .

The Z-Wave Network Layer (NWK) defines a multi-hop routing protocol, which is employed by Z-Wave nodes to extend their communication range. This means that Z-Wave nodes can send frames to nodes that are not in direct radio communication range .

Z-Wave technology is based on low power RF (Radio Frequency) technology and is considered to be more secure .



### Bluetooth Low Energy for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Bluetooth Low Energy (BLE) is a short-range communication network protocol with PHY (physical layer) and MAC (Medium Access Control) layer.
- BLE is designed for IOT devices that could be powered for a few years on a small battery.
- Both physical and data link layers of OSI model are implemented on Bluetooth Low Energy.
- The BLE protocol stack has two parts – controller and host.
- The Link layer is the second lowest protocol in the Bluetooth Low Energy protocol stack. It’s responsible for managing the state of the LE radio, among other things.
- Bluetooth Low Energy is also known as Bluetooth smart which is a wireless PAN (Personal Area Network).
- The range is similar to that of Bluetooth but it consumes low power than Bluetooth.
- In 2011 BLE was introduced as Bluetooth 4.0.
- BLE goes to sleep mode when there is no transmission of data.
- Bluetooth LE is an ultra-low-energy network in the 2.4 GHz band that connects devices in a short range.
- It consumes minimal energy and is designed to connect devices in a short-range.
- BLE is a low-power version of the popular Bluetooth 2.4 GHz wireless communication protocol.
- It is designed for short-range (no more than 100 meters) communication, typically in a star configuration, with a single primary device that controls several secondary devices.




### Zigbee Smart Energy

- Zigbee Smart Energy (Zigbee SE) is a protocol designed for monitoring and actively managing energy consumption at the end-user level.
- Zigbee SE can help reduce waste, energy consumption and enables utilities to monitor and manage customers’ energy use.
- Zigbee Smart Energy (SE) is a standard for interconnecting and interoperating devices, via radio frequency, directed towards monitoring, managing and automating energy, gas and water usage.
- It seeks to be a useful tool for creating “Green Homes”, and is aimed at coordinating energy usage, optimizing its generation and consumption.
- Smart Energy is the world’s leading standard for interoperable products that monitor, control, inform and automate the delivery and use of energy, gas, and water.
- Smart energy revolutionizes consumer knowledge to optimize energy consumption to reduce emissions footprint and ease regulatory compliance.
- The Zigbee Smart Energy 2.0 specifications define an Internet Protocol-based communication protocol to monitor, control, inform, and automate the delivery and use of energy and water.
- It is an enhancement of the Zigbee Smart Energy version 1 specifications.



### DASH7

DASH7 is a communication protocol that uses active RFID and is designed to be used within Industrial IoT applications for secure long-range communication. It is an open-source wireless sensor and actuator network protocol, which operates in the 433 MHz, 868 MHz, and 915 MHz unlicensed ISM band/SRD band. DASH7 provides multi-year battery life, a range of up to 2 km, low latency for connecting with moving things, and a very small open-source protocol stack.

Compared to Zigbee, DASH7 is more scalable, has greater network coverage, and greater data rates. It is not only a physical and MAC layer protocol but also includes IPv6 addressing for the network layer. The protocol uses unique identifiers along with 16-bit network identifiers for addressing in the IoT network.



### Network Layer

The network layer is responsible for routing data packets from the source device to the destination device in an Internet of Things (IoT) network. This layer is responsible for the logical addressing of devices and the translation of logical addresses to physical addresses.

Some of the key functions of the network layer in an IoT network include:

1. Routing: The network layer is responsible for determining the best path for data packets to travel from the source device to the destination device. This is done using routing algorithms and protocols such as the Open Shortest Path First (OSPF) protocol and the Border Gateway Protocol (BGP).

2. Addressing: The network layer is responsible for the logical addressing of devices in an IoT network. This is done using Internet Protocol (IP) addresses, which are unique identifiers assigned to each device in the network.

3. Fragmentation and reassembly: The network layer is responsible for breaking down large data packets into smaller packets that can be transmitted over the network. This is known as fragmentation. The network layer is also responsible for reassembling these smaller packets into the original data packet at the destination device.

4. Quality of Service (QoS): The network layer is responsible for ensuring that data packets are transmitted with the desired level of quality. This is done using Quality of Service (QoS) mechanisms, which prioritize certain types of data traffic over others.

5. Security: The network layer is responsible for ensuring the security of data transmitted over the network. This is done using security mechanisms such as encryption and authentication.

The network layer is a crucial component of the IoT architecture and plays a key role in ensuring the efficient and secure transmission of data in an IoT network. It is important to have a thorough understanding of the network layer and its functions when studying IoT architecture and protocols.



### IPv4 for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- **Internet Protocol Version 4 (IPv4)** is the fourth revision of the Internet Protocol and a widely used protocol in data communication over different kinds of networks.
- IPv4 is a **connectionless protocol** used in packet-switched layer networks, such as Ethernet.
- The **Network Layer** protocols used in IoT are IPv4 (used previously), the recent IPv6 layer handles 128 bit addresses and 6LoWPAN. 6LoWPAN is called the adaptation layer.
- The Internet Protocol, and specifically the Internet Protocol version 4, defines how the addressing works and how network hosts can be identified and found on the network.
- IPv4 addresses are represented by 32-bit values organized into four octets (4x8), usually expressed by dotted decimal numbers that look like this: 172.140.153.12.
- Ethernet is a LAN technology in which the devices are wired connection which provides data transfer rates as high as 100 Mbps. Choosing Ethernet for IoT ecosystem is a little bit costly in terms of setup and management.
- IoT network technologies to be aware of toward the bottom of the protocol stack include cellular, wifi, and Ethernet, as well as more specialized solutions such as LPWAN, Bluetooth Low Energy (BLE), ZigBee, NFC, and RFID. NB-IoT is becoming the standard for LPWAN networks, according to Gartner.



### IPv6 for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- **IPv6** or **Internet Protocol Version 6** is a network layer protocol that allows communication to take place over the network.
- It is used for transferring data and communication in the Internet of Things (IoT).
- Each IoT device has an IP address and networking is the key aspect in the Internet of Things.
- The network layer of an IoT protocol helps individual devices communicate with the router.
- Many IoT protocols utilize IPv4, while more recent implementations use IPv6.
- IPv6 is commonly adopted for IoT device addressing.
- **6LoWPAN** (IPv6 Low Power Wireless Personal Area Network) is an IPv6 standard-based network layer protocol for Wireless Personal Area Networks.
- Based on the 802.15.4 protocol at the physical layer, the standard has been developed for addressing IoT sensors and devices in a Wireless Sensor Network (WSN).



### 6LoWPAN

6LoWPAN stands for IPv6 over Low-Power Wireless Personal Area Networks. It is a protocol that enables the transmission of IPv6 packets over low-power wireless networks, such as those used in the Internet of Things (IoT) devices.

Some key points to note about 6LoWPAN are:

- It is designed to operate over IEEE 802.15.4 wireless networks, which are commonly used in IoT devices.
- It enables the use of IPv6, the latest version of the Internet Protocol, in low-power wireless networks.
- It uses header compression to reduce the size of IPv6 packets, making them more suitable for transmission over low-power wireless networks.
- It supports mesh networking, allowing devices to forward packets on behalf of other devices in the network.
- It is an open standard, developed by the Internet Engineering Task Force (IETF).

6LoWPAN is an important protocol for the IoT, as it enables the use of the IPv6 protocol in low-power wireless networks. This allows IoT devices to be directly addressable on the Internet, making it easier to develop and deploy IoT applications. Additionally, the use of header compression and mesh networking helps to improve the efficiency and reliability of IoT networks.



### 6TiSCH

6TiSCH is a working group at the IETF (Internet Engineering Task Force) that develops standards for IPv6. It is an IPv6 standard for 802.15.4 MAC layer protocols . The standard allows IPv6 addresses to pass through the Time-Slotted Channel Hopping (TSCH) mode of IEEE 802.15.4e MAC layer . This enables the use of the IPv6 adaption layer for industrial automation and Low Power Lossy Networks (LLN) .

The 6TiSCH network is intended to provide reliable and delay bounded communication in multi-hop and scalable Industrial Internet of Things (IIoT). The IEEE 802.15.4e Time Slotted Channel Hopping (TSCH) link layer protocol allows the nodes to change their physical channel after each transmission to eliminate interference.



### ND for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. The Data Link Layer is responsible for providing a reliable link between two directly connected nodes.
2. It is responsible for framing, flow control, error control, and media access control.
3. The Network Layer is responsible for routing packets from the source to the destination.
4. It is responsible for logical addressing, routing, and forwarding.
5. Some common Data Link Layer protocols used in IoT are Bluetooth, Zigbee, and Z-Wave.
6. Some common Network Layer protocols used in IoT are IPv6, 6LoWPAN, and RPL.
7. Bluetooth is a short-range wireless technology that operates in the 2.4 GHz ISM band.
8. Zigbee is a wireless technology that operates in the 2.4 GHz ISM band and is based on the IEEE 802.15.4 standard.
9. Z-Wave is a wireless technology that operates in the sub-1 GHz band and is designed for home automation.
10. IPv6 is the latest version of the Internet Protocol and is designed to replace IPv4.
11. 6LoWPAN is a protocol that enables the transmission of IPv6 packets over low-power wireless networks.
12. RPL is a routing protocol designed for low-power and lossy networks.




### DHCP for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- **DHCP** stands for **Dynamic Host Configuration Protocol**.
- It is a **network management protocol** present in the **application layer**.
- With its help, an **Internet Protocol (IP) address** can be assigned to any device or node on a network **dynamically** so that they can communicate using this IP.
- DHCP is an **application layer protocol** which is used to provide **subnet mask**.
- IoT protocols can be divided into two categories: **IoT network protocols** and **IoT data protocols**.
- **Data protocols** mainly focus on **information exchange**, while **network protocols** provide methods of connecting IoT edge devices with other edge devices or the Internet.




### ICMP for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- ICMP stands for Internet Control Message Protocol.
- It is a network layer protocol used by network devices to send error messages and operational information.
- ICMP is used by routers, hosts, and network devices to communicate network layer information.
- ICMP messages are typically generated by network devices to indicate errors in datagram processing.
- ICMP messages are also used for diagnostic or control purposes, such as ping and traceroute.
- ICMP is an integral part of the Internet Protocol suite and is defined in RFC 792.
- ICMP messages are encapsulated within IP datagrams and are therefore routed using the same mechanisms as other IP traffic.
- ICMP messages have a specific format, consisting of an 8-bit type field, an 8-bit code field, and a variable-length data field.
- Common ICMP message types include destination unreachable, time exceeded, and echo request/reply (ping).
- ICMP is not a transport layer protocol and does not provide reliable delivery or flow control.
- ICMP messages are typically used for network management and troubleshooting purposes.




### RPL

RPL (Routing Protocol for Low-Power and Lossy Networks) is a routing protocol designed for wireless sensor networks and other low-power and lossy networks. It is a distance-vector protocol that uses a Directed Acyclic Graph (DAG) to represent the network topology.

Some key features of RPL include:
- It is designed to support a wide range of network topologies, including point-to-point, point-to-multipoint, and mesh networks.
- It uses a DAG to represent the network topology, which allows for efficient routing and loop prevention.
- It supports multiple instances, allowing for multiple DAGs to coexist in the same network.
- It includes mechanisms for efficient route repair and maintenance.
- It supports both unicast and multicast routing.

RPL is commonly used in IoT (Internet of Things) networks, where devices have limited power and processing capabilities. It is also used in other low-power and lossy networks, such as industrial control systems and smart grid networks.

RPL is defined in RFC 6550, which was published by the Internet Engineering Task Force (IETF) in 2012. It is an open standard and is widely implemented in IoT devices and networks.



### CORPL

CORPL (Constrained RESTful Protocol) is a protocol designed for use in the Internet of Things (IoT) and is used in the Data Link and Network Layers of the IoT architecture. It is a lightweight protocol that is designed to be used in resource-constrained environments, such as those found in IoT devices.

Some key features of CORPL include:

1. It is based on the RESTful architecture, which means that it uses standard HTTP methods such as GET, POST, PUT, and DELETE to interact with resources.
2. It is designed to be used in resource-constrained environments, which means that it is lightweight and efficient.
3. It supports the use of CoAP (Constrained Application Protocol), which is a protocol designed specifically for use in IoT devices.
4. It is designed to be easily integrated with other IoT protocols, such as MQTT (Message Queuing Telemetry Transport) and XMPP (Extensible Messaging and Presence Protocol).

Overall, CORPL is an important protocol in the IoT architecture, as it provides a lightweight and efficient way for IoT devices to communicate with each other and with the wider internet. It is designed to be used in resource-constrained environments, which makes it well-suited for use in IoT devices. Its support for other IoT protocols, such as CoAP, MQTT, and XMPP, makes it a versatile and flexible protocol that can be easily integrated into a wide range of IoT systems.



### CARP

CARP, or the Common Address Redundancy Protocol, is a protocol used in computer networking. It is designed to allow multiple hosts on the same network segment to share an IP address. This is useful for providing redundancy and failover capabilities, as traffic can be automatically redirected to a backup host if the primary host fails.

Some key points to note about CARP include:

1. CARP is a free, open, and non-proprietary protocol.
2. It is commonly used in conjunction with other redundancy protocols, such as VRRP and HSRP.
3. CARP operates at the Data Link Layer of the OSI model.
4. It uses multicast to communicate with other CARP-enabled hosts on the network.
5. CARP can be used to provide redundancy for both IPv4 and IPv6 addresses.

In summary, CARP is a useful protocol for providing redundancy and failover capabilities in a network environment. It is free, open, and non-proprietary, and can be used in conjunction with other redundancy protocols to provide a robust and reliable network infrastructure.



## Unit 4 - Transport & Session Layer Protocols

The transport layer and session layer are two of the seven layers in the OSI model. These layers are responsible for the end-to-end communication between two devices on a network.

### Transport Layer
- The transport layer is responsible for providing reliable data transfer between two devices on a network.
- It is responsible for error control, flow control, and congestion control.
- The two main transport layer protocols are TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).
- TCP is a connection-oriented protocol that provides reliable data transfer, while UDP is a connectionless protocol that provides faster but less reliable data transfer.

### Session Layer
- The session layer is responsible for establishing, managing, and terminating sessions between two devices on a network.
- It provides services such as authentication, authorization, and synchronization.
- The session layer uses protocols such as NetBIOS, PPTP, and L2TP to establish and manage sessions.

These two layers play a crucial role in ensuring that data is transmitted reliably and efficiently between two devices on a network. They work together to provide a seamless communication experience for the user.



### Transport Layer

The Transport Layer is the fourth layer in the OSI model and is responsible for end-to-end communication between devices. It provides services such as connection-oriented data stream support, reliability, flow control, and multiplexing.

Some of the key features of the Transport Layer include:

1. **Segmentation and reassembly**: The Transport Layer divides the data into smaller segments that can be transmitted over the network. At the receiving end, these segments are reassembled into the original data.

2. **Connection-oriented communication**: The Transport Layer can establish a connection between two devices before transmitting data. This ensures that the data is transmitted reliably and in the correct order.

3. **Flow control**: The Transport Layer can regulate the flow of data between devices to prevent the receiver from being overwhelmed by incoming data.

4. **Error control**: The Transport Layer can detect and correct errors that may occur during transmission.

5. **Multiplexing**: The Transport Layer can combine data from multiple applications into a single data stream for transmission over the network.

Some common Transport Layer protocols include TCP (Transmission Control Protocol) and UDP (User Datagram Protocol). TCP is a connection-oriented protocol that provides reliable data transmission, while UDP is a connectionless protocol that is used for faster, but less reliable, data transmission.

In the context of IoT (Internet of Things) architecture and protocols, the Transport Layer plays a crucial role in ensuring reliable and efficient communication between devices. It is responsible for managing the transmission of data between devices and ensuring that the data is transmitted reliably and efficiently.



### TCP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- TCP stands for Transmission Control Protocol.
- It is one of the main protocols in the Internet protocol suite.
- TCP provides reliable, ordered, and error-checked delivery of data between applications running on different devices.
- It is a connection-oriented protocol, which means that a connection is established and maintained until the data exchange is complete.
- TCP uses a three-way handshake to establish a connection between two devices.
- The three-way handshake involves the exchange of SYN and ACK packets between the two devices.
- Once the connection is established, data can be exchanged between the devices using segments.
- TCP uses flow control to ensure that the sender does not overwhelm the receiver with data.
- It also uses congestion control to avoid overwhelming the network with data.
- TCP can recover from lost or corrupted data by retransmitting the affected segments.
- When the data exchange is complete, the connection is terminated using a four-way handshake.




### MPTCP

- MPTCP stands for Multipath TCP.
- It is an ongoing effort of the Internet Engineering Task Force's (IETF) Multipath TCP working group.
- The aim of MPTCP is to allow a Transmission Control Protocol (TCP) connection to use multiple paths to maximize throughput and increase redundancy.
- Transport is the OSI Level 4 layer and is recognized by the same name in the TCP-IP model.
- The transport layer is part of the infrastructure layer in IOT reference architecture.
- The transport layer is the protocol supporting the movement of the data, such as Transmission Control Protocol (TCP), HTTP or User Datagram Protocol (UDP).
- The application layer is the interface between the IoT device and the network with which it will communicate.
- MPTCP is one of the transport layer protocols, along with TCP, UDP, DCCP, SCTP, TLS, and DTLS.



### UDP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- **User Datagram Protocol (UDP)** is a Transport Layer protocol.
- UDP is a part of the Internet Protocol suite, referred to as **UDP/IP suite**.
- Unlike TCP, it is an **unreliable** and **connectionless** protocol.
- UDP is the **simplest** Transport Layer communication protocol available of the TCP/IP protocol suite.
- It involves **minimum** amount of communication mechanism.
- UDP is said to be an unreliable transport protocol but it uses IP services which provides **best effort delivery** mechanism.
- UDP is often adopted for IoT transport for **performance** reasons.
- The application layer is the interface between the IoT device and the network with which it will communicate.
- HTTP/S is an example of an application layer protocol that is widely adopted across the internet.
- Although UDP provides **integrity verification** (via checksum) of the header and payload, it provides no guarantees to the upper layer protocol for message delivery and the UDP layer retains no state of UDP messages once sent.




### DCCP

DCCP (Datagram Congestion Control Protocol) is a transport layer protocol that provides a way to send unreliable datagrams with congestion control. It is designed for applications that require fast delivery of data, but can tolerate some loss of data, such as multimedia streaming or online gaming.

Some key features of DCCP include:

1. Congestion control: DCCP uses a congestion control mechanism to avoid overwhelming the network with too much traffic. This helps to ensure that the network remains stable and usable for all users.

2. Unreliable delivery: DCCP does not guarantee that all data will be delivered, and it does not retransmit lost packets. This makes it suitable for applications that can tolerate some loss of data.

3. Connection-oriented: DCCP is a connection-oriented protocol, which means that a connection must be established between two endpoints before data can be transmitted.

4. Bidirectional communication: DCCP allows for bidirectional communication, meaning that data can be sent in both directions between two endpoints.

5. Support for multiple congestion control mechanisms: DCCP allows for the use of different congestion control mechanisms, depending on the needs of the application.

DCCP is one of several transport layer protocols that can be used in the context of IoT (Internet of Things) architecture and protocols. It provides a useful alternative to other protocols such as TCP and UDP, depending on the specific needs of the application.



### SCTP (Stream Control Transmission Protocol)

SCTP is a transport layer protocol that provides reliable, connection-oriented communication between two endpoints. It is used in the Internet of Things (IoT) architecture and protocols, specifically in the transport and session layer protocols.

Some key features of SCTP include:

1. **Multi-streaming:** SCTP allows multiple streams of data to be sent simultaneously over a single connection, reducing the head-of-line blocking problem that can occur with TCP.

2. **Multi-homing:** SCTP supports multi-homing, where an endpoint can have multiple IP addresses. This provides redundancy and increases the reliability of the connection.

3. **Selective Acknowledgment:** SCTP uses selective acknowledgment (SACK) to acknowledge received data. This allows for more efficient retransmission of lost packets.

4. **Congestion Control:** SCTP uses a similar congestion control mechanism to TCP, which helps to prevent network congestion.

5. **Message-oriented:** Unlike TCP, which is a byte-stream protocol, SCTP is message-oriented. This means that messages are treated as individual units, rather than as a continuous stream of bytes.

SCTP is used in various applications, including telephony signaling, web browsing, and file transfer. It is also used in the transport of SS7 signaling messages over IP networks. SCTP provides a reliable and efficient transport mechanism for IoT devices and applications.



### Session Layer

The session layer is the fifth layer of the OSI model and is responsible for establishing, managing, and terminating connections between applications. This layer provides the mechanism for controlling the dialogue between the two end systems and for managing data exchange. Some of the key functions of the session layer include:

1. **Session establishment, maintenance, and termination**: The session layer allows two application processes on different systems to establish, use, and terminate a connection, called a session.
2. **Dialogue control**: The session layer allows the communication between two processes to be half-duplex (one way at a time) or full-duplex (two way at the same time).
3. **Token management**: The session layer can provide token management to prevent two parties from attempting the same critical operation at the same time.
4. **Synchronization**: The session layer can add checkpoints to the data stream, so if the connection fails during a data transfer, only the data after the last checkpoint needs to be retransmitted.

The session layer is commonly implemented in application environments that use remote procedure calls (RPCs). Some examples of session layer protocols include the Network File System (NFS), Structured Query Language (SQL), and Remote Procedure Call (RPC).



### HTTP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- HTTP stands for Hypertext Transfer Protocol.
- It is an application layer protocol used for transmitting data over the internet.
- HTTP is the foundation of data communication for the World Wide Web.
- It is a request-response protocol, where a client sends a request to a server and the server responds with the requested data.
- HTTP uses a reliable transport protocol, typically TCP, to establish a connection between the client and server.
- HTTP is a stateless protocol, meaning that each request is treated independently and the server does not retain any information about previous requests.
- HTTP/1.1 is the most widely used version of the protocol, but HTTP/2 and HTTP/3 have been developed to improve performance and security.
- HTTP can be used with other protocols such as HTTPS, which adds a layer of security by encrypting the data transmitted between the client and server.
- HTTP is commonly used in IoT applications to transmit data from sensors and devices to a server for processing and storage.




### CoAP

- CoAP stands for Constrained Application Protocol.
- It is a protocol architecture used in IoT (Internet of Things) .
- The CoAP protocol is specified in RFC 7252 .
- The WWW and the constraints ecosystem are the 2 foundational elements of the CoAP protocol architecture .
- The server monitors and helps in communication happening using CoAP and HTTP while proxy devices bridge the existing gap for these 2 ecosystems, making the communication smoother .
- CoAP is a very lightweight protocol and it uses DTLS (Datagram Transport Layer Security) for providing more security and reliable communications .
- IoT protocols ensure that information from one device or sensor gets read and understood by another device, a gateway, a service .
- Different IoT protocols have been designed and optimized for different scenarios and usage .
- CoAP is an IoT protocol that has interesting features specifically designed for constrained devices .



### XMPP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- XMPP stands for Extensible Messaging and Presence Protocol.
- It is an open protocol for streaming XML elements in order to exchange messages and presence information in close to real-time.
- XMPP protocol works as per typical client-server architecture, in which the XMPP client utilizes the XMPP server using a TCP socket .
- XMPP technologies use a decentralized client-server architecture related to the architecture used for the World Wide Web and the email network.
- In decentralized client-server architecture, client developers can focus on user experience, and server developers can focus on reliability and scalability.
- XMPP provides a general framework for messaging across a network, offering a multitude of applications beyond traditional instant messaging (IM) and the distribution of presence data.
- XMPP is an excellent protocol for use within the Internet of Things (IoT).
- It can help build solid, secure, and interoperable devices, services, and applications for the Internet of Things.




### AMQP

- AMQP stands for Advanced Message Queuing Protocol.
- It is a session layer protocol that runs over the TCP layer.
- It is based on a publish/subscribe architecture, similar to the MQTT protocol architecture.
- AMQP version 1.0 supports various broker architectures that may be used to receive, queue, route, and deliver messages or be used peer-to-peer.
- There are three major pieces specified in the scope of AMQP 1.0. These define the networking protocol, a representation for message envelope data, and the basic semantics of broker services.
- Both MQTT and AMQP run over TCP connections, both are client-server in architecture and bi-directional.
- AMQP was designed to provide general-purpose high-performance enterprise messaging, whereas MQTT was created as an IoT protocol.
- AMQP has many features to cater to a range of messaging scenarios and is more complex than MQTT.



### MQTT

MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol that is commonly used in the Internet of Things (IoT) for communication between devices. It is designed for constrained devices and low-bandwidth, high-latency or unreliable networks.

Here are some key points about MQTT:

1. MQTT is a publish/subscribe protocol, which means that devices can publish messages to a topic and other devices can subscribe to that topic to receive the messages.
2. MQTT uses a broker to manage the communication between devices. The broker is responsible for receiving messages from publishers and sending them to subscribers.
3. MQTT is designed to be lightweight and efficient, with a small code footprint and low network overhead.
4. MQTT supports Quality of Service (QoS) levels, which allow devices to specify the reliability of message delivery.
5. MQTT supports retained messages, which allow devices to receive the last message published to a topic even if they were not subscribed at the time the message was published.
6. MQTT supports Last Will and Testament (LWT) messages, which allow devices to specify a message that will be published by the broker if the device unexpectedly disconnects.




## Unit 5 - Service Layer Protocols & Security

Service layer protocols are responsible for providing end-to-end communication services between applications running on different hosts. Some of the most commonly used service layer protocols include:

1. **Hypertext Transfer Protocol (HTTP)**: This protocol is used for transmitting web pages and other information over the internet. It is the foundation of data communication for the World Wide Web.

2. **File Transfer Protocol (FTP)**: This protocol is used for transferring files between hosts over a TCP-based network, such as the internet.

3. **Simple Mail Transfer Protocol (SMTP)**: This protocol is used for sending and receiving email messages over the internet.

4. **Domain Name System (DNS)**: This protocol is used for resolving human-readable domain names into IP addresses, which are used by network devices to communicate with each other.

Security is an important aspect of service layer protocols, as they are responsible for transmitting sensitive information over the internet. Some of the security measures that can be implemented to protect data transmitted using service layer protocols include:

1. **Encryption**: This involves encoding data in such a way that only authorized parties can access it. Encryption can be used to protect data transmitted over the internet, as well as data stored on a device.

2. **Authentication**: This involves verifying the identity of a user or device before granting access to sensitive information. Authentication can be achieved using methods such as passwords, biometric data, or digital certificates.

3. **Firewalls**: These are hardware or software-based systems that monitor and control incoming and outgoing network traffic. Firewalls can be used to block unauthorized access to a network or device, and to prevent the transmission of malicious data.

4. **Virtual Private Networks (VPNs)**: These are private networks that use encryption and other security measures to provide a secure connection between two devices over the internet. VPNs can be used to protect sensitive data transmitted over the internet, as well as to provide remote access to a private network.

In conclusion, service layer protocols are responsible for providing end-to-end communication services between applications running on different hosts, and security measures such as encryption, authentication, firewalls, and VPNs can be implemented to protect data transmitted using these protocols.



### Service Layer

The service layer is a component of the Internet of Things (IoT) architecture that provides a range of services to support IoT applications. These services include:

1. **Device management:** This service manages the registration, authentication, and configuration of IoT devices.

2. **Data management:** This service manages the storage, processing, and retrieval of data generated by IoT devices.

3. **Security:** This service provides security measures to protect the data and devices in the IoT system.

4. **Application enablement:** This service provides APIs and tools to enable the development of IoT applications.

The service layer protocols are responsible for providing these services to the IoT system. Some common service layer protocols used in IoT include:

1. **Message Queuing Telemetry Transport (MQTT):** This is a lightweight messaging protocol designed for IoT devices with limited resources.

2. **Constrained Application Protocol (CoAP):** This is a web transfer protocol designed for use with constrained devices and networks.

3. **Advanced Message Queuing Protocol (AMQP):** This is a messaging protocol that provides reliable and secure messaging for IoT systems.

Security is a critical concern in IoT systems, and the service layer plays a key role in ensuring the security of the system. Some common security measures implemented at the service layer include:

1. **Encryption:** Data transmitted between devices and the service layer is encrypted to protect against interception and tampering.

2. **Authentication:** Devices and users are authenticated before being allowed to access the system.

3. **Access control:** Access to data and services is controlled based on the identity and permissions of the user or device.

These are some of the key concepts and components of the service layer in IoT architecture. It is important to have a thorough understanding of these concepts when studying IoT architecture and protocols.



### oneM2M

oneM2M is a global standard for Machine to Machine (M2M) and Internet of Things (IoT) systems. It was established in 2012 by several national standardization bodies to avoid regional variations and promote a global IoT market on par with the cellular industry .

The oneM2M architecture divides IoT functions into three major domains: the application layer, the services layer, and the network layer .

- **Application Layer**: This layer gives major attention to connectivity between devices and their applications. It includes the application layer protocols and attempts to standardize northbound API definitions for interaction with Business Intelligence (BI) Systems .

- **Services Layer**: This layer is a vendor-independent software Middleware between processing and communication hardware and IoT applications providing a set of functions commonly needed by IoT applications. The oneM2M Service Layer provides use case-independent functions .

- **Network Layer**: This layer is responsible for the communication between devices and the services layer.

oneM2M follows a modular standardization roadmap, allowing for future IoT requirements and new common service functions .



### ETSI M2M

- The European Telecommunications Standards Institute (ETSI) IoT Standard, also known as the ESTI M2M Reference Architecture, is the high-level functional architecture that consists of Device and Gateway Domain and Network Domain .
- The main ETSI IoT standardization activities are conducted at radio layer in 3GPP (LTE-M, NB-IoT and EC-GSM-IoT) and at service layer in oneM2M .
- ETSI is one of the founding partners in oneM2M, the global standards initiative that covers requirements, architecture, Application Programming Interface (API) specifications, security solutions and interoperability for M2M and IoT technologies .
- The ETSI M2M service capabilities layer (SCL) provides functions that are shared by different applications enabled by the M2M technologies .
- Security is an important aspect of the ETSI M2M Framework .




### OMA

OMA, or the Open Mobile Alliance, is an organization that develops open standards for the mobile phone industry. It was formed in 2002 by the consolidation of several industry forums, including the WAP Forum, the Wireless Village, the Location Interoperability Forum, and others.

OMA's goal is to deliver high-quality, open technical specifications based on market requirements that drive modularity, extensibility, and consistency among enablers to reduce industry implementation efforts.

Some of the key service layer protocols and security standards developed by OMA include:

1. **OMA Device Management (OMA DM):** This protocol is used for managing mobile devices over-the-air. It allows network operators to remotely configure and update devices, as well as perform diagnostics and repairs.

2. **OMA Digital Rights Management (OMA DRM):** This standard provides a framework for protecting digital content, such as music, videos, and images, on mobile devices. It allows content owners to specify usage rights and restrictions for their content.

3. **OMA Client Provisioning (OMA CP):** This protocol is used for over-the-air provisioning of mobile devices. It allows network operators to remotely configure devices with the necessary settings for accessing network services.

4. **OMA Browsing (OMA Browsing):** This standard defines a set of protocols and interfaces for mobile web browsing. It includes support for features such as offline browsing, push notifications, and location-based services.

These are just a few examples of the many standards developed by OMA to enhance the security and functionality of mobile devices and services. By adhering to these open standards, industry players can ensure interoperability and a consistent user experience across devices and networks.



### BBF for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- BBF stands for Broadband Forum, which is a non-profit industry organization focused on engineering smarter and faster broadband networks.
- The BBF's work encompasses home and business connectivity, 5G, cloud services, the Internet of Things (IoT), and emerging technologies.
- The BBF develops technical specifications and implementation guides to help service providers and vendors create and deploy secure and interoperable IoT services.
- The BBF has several working groups focused on IoT, including the Device:2 Working Group, which develops data models for IoT devices, and the User Services Platform (USP) Working Group, which develops a protocol for managing IoT devices.
- The BBF also has a Security Working Group, which focuses on developing security best practices and guidelines for broadband networks, including IoT networks.
- The BBF's work on IoT security includes developing a framework for secure onboarding of IoT devices, as well as guidelines for securing IoT data in transit and at rest.
- The BBF's work on service layer protocols for IoT includes developing technical specifications for the USP protocol, which enables remote management of IoT devices and services.
- The USP protocol is designed to be scalable, secure, and interoperable, and can be used to manage a wide range of IoT devices and services.
- The BBF's work on IoT is ongoing, and the organization continues to develop new technical specifications and best practices to help service providers and vendors create and deploy secure and interoperable IoT services.



### Security in IoT Protocols

1. **Security breaches**: IoT protocols have to deal with security breaches at the site of the cloud service provider.
2. **Data privacy**: IoT protocols have to deal with security issues pertaining to data privacy.
3. **Authentication**: IoT protocols have to deal with security issues pertaining to authentication.
4. **Authorization**: IoT protocols have to deal with security issues pertaining to authorization.
5. **Trust management**: IoT protocols have to deal with security issues pertaining to trust management in a distributed heterogeneous environment.
6. **Security attacks**: IoT protocols have to deal with various security attacks and the solutions offered by IoT protocols.
7. **Data security**: A core aspect of IoT security is to maintain security, privacy, and integrity of data in storage (stored in the IoT device, in the network server, the cloud, etc.), and also during transit.
8. **Top 5 IoT Security Protocols**: MQTT is one of the most common security protocols used in internet of things security. It was invented by Dr Andy Stanford-Clark and Arlen Nipper in 1999. MQTT stands for Message Queuing Telemetry Transport and is a client-server communicating messaging transport protocol.
9. **IoT platforms**: IoT platforms manage hardware and software protocols, offer security and authentication, and provide user interfaces. The exact definition of an IoT platform varies because more than 400 service providers offer features that range from software and hardware to SDKs and APIs.
10. **Security concerns**: Security concerns must be prioritized in order to minimize the attack surface and prevent security issues, since IoT technology is intended to be used in numerous critical sectors, particularly the economy and national security, with varying industry standards and specifications.



### MAC 802.15.4

- MAC 802.15.4 is a standard that defines the operation of low-rate wireless personal area networks (LR-WPANs).
- It specifies the physical layer and media access control for LR-WPANs, and is maintained by the IEEE 802.15 working group.
- The standard is commonly used for wireless sensor networks, home automation, and other low-power, low-data-rate applications.
- MAC 802.15.4 provides two types of network topologies: star and peer-to-peer.
- In a star topology, devices communicate with a central coordinator, while in a peer-to-peer topology, devices can communicate directly with each other.
- The standard supports multiple frequency bands, including 868 MHz, 915 MHz, and 2.4 GHz.
- MAC 802.15.4 provides several security mechanisms, including encryption and authentication, to protect the data transmitted over the network.
- The standard is designed to be power-efficient, with devices able to enter a low-power mode when not transmitting or receiving data.
- MAC 802.15.4 is the basis for several higher-layer protocols, including Zigbee, Z-Wave, and Thread.




### 6LoWPAN

6LoWPAN is a protocol definition that enables IPv6 packets to be carried on top of low power wireless networks, specifically IEEE 802.15.4. The concept was born from the idea that the Internet Protocol could and should be applied to even the smallest of devices.

The 6LoWPAN protocol stack includes different networking topologies such as star and mesh, low bandwidth (250/40/20 kbps), low power consumption, typically battery-operated, relatively low cost, scalable networks, reliability, mobility, and long sleep times.

In the network layer, IPv6 is used. This makes it fit to support several devices, hence preferred in building IoT based system. The channels have varying data rates and are allocated into different frequency bands with a total of twenty seven channels being defined in the layer.

6LoWPAN only specifies operation of IPv6 over the IEEE 802.15.4 standard, edge routers may also support IPv6 transition mechanisms to connect 6LoWPAN networks to IPv4 networks, such as NAT64 defined in RFC 6146. These IPv6 transition mechanisms do not require the 6LoWPAN nodes to implement IPv4 in whole or in part.

The 6LoWPAN architecture is made up of low-power wireless area networks (LoWPANs), which are IPv6 stub networks. Three different kinds of LoWPANs have been defined: Simple LoWPANs, Extended LoWPANs, and Ad hoc LoWPANs.



### RPL for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for Routing Protocol for Low-Power and Lossy Network .
- It is a routing protocol for low-power and lossy networks .
- Low power and loss networks are resource-constrained networks meaning based on the available resources the networks adapt themselves .
- The network layer in IoT is mainly divided into two parts: the routing layer and the encapsulation layer .
- The routing layer sends packages from origin to destination and the encapsulation layer is largely responsible for creating packets .
- Security is an important aspect of RPL-based protocols in IoT  .
- There are various security issues that occur specifically at the network layer in IoT .




### Application Layer

The application layer is the topmost layer in the OSI model and the TCP/IP model. It provides services to the user and interacts with the software applications. Some of the key points to remember about the application layer are:

1. The application layer is responsible for providing services to the user such as file transfer, email, and web browsing.
2. It interacts with the software applications and provides a user interface for the user to interact with the network.
3. The application layer protocols are used to exchange data between programs running on different devices.
4. Some of the common application layer protocols are HTTP, FTP, SMTP, and DNS.
5. The application layer is also responsible for providing security services such as authentication and encryption.


