

# IOT ARCHITECTURE AND PROTOCOLS

- IoT architecture refers to the many ways that IoT devices are structured to meet user needs. Based on complexity, IoT system elements are grouped into 3 to 7 layers, each with its own role.
- IoT protocols are the set of rules that enable communication between IoT devices, gateways, services, and data centers. Different IoT protocols have been designed and optimized for different scenarios and usage.
- A common IoT architecture consists of the following layers  :
  - Device layer: This layer contains the sensors and actuators that collect data and perform actions in the physical world. They can be embedded, wearable, or standalone devices. They can communicate using wired or wireless connections, and use various protocols depending on their capabilities and requirements.
  - Gateway layer: This layer acts as a bridge between the device layer and the cloud layer. It can aggregate, filter, process, and transmit data from multiple devices to the cloud, and vice versa. It can also provide security, authentication, and device management functions. Gateways can be hardware or software-based, and can use various protocols depending on the device and cloud platforms.
  - Cloud layer: This layer provides the storage, processing, and analysis of the data collected from the devices and gateways. It can also provide services such as device management, data visualization, analytics, machine learning, and application development. Cloud platforms can use various protocols depending on the service and gateway platforms.
  - Application layer: This layer serves as the interface between the user and the device within a given IoT protocol. It can provide functions such as user authentication, data presentation, notification, and control. Application platforms can use various protocols depending on the cloud and user platforms.
- Some of the common IoT protocols are :
  - Message queue telemetry transport (MQTT): A lightweight, publish-subscribe protocol that is designed for low-bandwidth, high-latency, and unreliable networks. It is widely used for IoT applications that require real-time data delivery, such as smart home, industrial automation, and healthcare.
  - Constrained application protocol (CoAP): A web-based protocol that is designed for constrained devices and networks. It uses a request-response model and supports various features such as multicast, caching, and discovery. It is widely used for IoT applications that require interoperability, such as smart city, smart grid, and environmental monitoring.
  - Advanced message queuing protocol (AMQP): A binary, peer-to-peer protocol that is designed for high-performance, reliable, and secure messaging. It supports various features such as routing, queuing, transactions, and acknowledgments. It is widely used for IoT applications that require scalability, such as cloud computing, big data, and social media.
  - Hypertext transfer protocol (HTTP): A web-based protocol that is designed for general-purpose data exchange. It uses a request-response model and supports various features such as caching, compression, and authentication. It is widely used for IoT applications that require simplicity, such as web services, mobile applications, and web browsers.



## Unit 1 - IoT-An Architectural Overview

- IoT stands for Internet of Things, which refers to the network of physical devices, sensors, actuators, and software that can collect, process, and exchange data over the internet.
- IoT enables various applications and services that can improve the quality of life, efficiency, and productivity of individuals, organizations, and society.
- IoT architecture consists of four main layers: device layer, network layer, service layer, and application layer.
- Device layer: This layer includes the physical devices, sensors, and actuators that can sense, measure, and control the physical world. Devices can have different capabilities, such as computing, storage, communication, and security. Devices can also be embedded, wearable, or mobile.
- Network layer: This layer provides the connectivity and communication between devices and other layers. Network layer can use different technologies, such as wired, wireless, cellular, or satellite. Network layer can also support different protocols, such as TCP/IP, MQTT, CoAP, or HTTP.
- Service layer: This layer provides the data processing, storage, and management functions for the IoT system. Service layer can use different platforms, such as cloud, fog, or edge computing. Service layer can also provide different services, such as data analytics, machine learning, security, or privacy.
- Application layer: This layer provides the user interface and interaction for the IoT system. Application layer can use different devices, such as smartphones, tablets, or computers. Application layer can also support different applications, such as smart home, smart city, smart health, or smart agriculture.



Hello, I am Sydney, your AI assistant. I can help you with building an architecture for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS. Here is a possible outline for your notes:

### Building an architecture for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Introduction
  - Define IoT and its characteristics
  - Explain the motivation and benefits of IoT
  - Describe the challenges and issues of IoT
- IoT Architecture
  - Identify the main components and layers of IoT architecture
  - Compare and contrast different IoT architecture models (such as 3-tier, 4-tier, 5-tier, etc.)
  - Discuss the design principles and requirements of IoT architecture
- IoT Protocols
  - Define protocols and their role in IoT communication
  - Classify IoT protocols based on their functions and features (such as application layer, transport layer, network layer, etc.)
  - Analyze the advantages and disadvantages of various IoT protocols (such as MQTT, CoAP, HTTP, TCP, UDP, IPv6, 6LoWPAN, etc.)
- IoT Applications
  - Provide examples of IoT applications in different domains (such as smart home, smart city, smart health, smart agriculture, etc.)
  - Explain the use cases and scenarios of IoT applications
  - Evaluate the performance and impact of IoT applications
- Conclusion
  - Summarize the main points and concepts of the unit
  - Highlight the key takeaways and learning outcomes of the unit
  - Suggest some further readings and resources for the unit




### Main design principles and needed capabilities for IoT

IoT is the interconnection of physical devices, sensors, actuators, and interactive devices that can communicate and exchange data over the internet. IoT design is the practice of creating meaningful user experiences by considering the whole system, the role of each device and service, and the conceptual model of how the user understands and perceives the entire IoT system.

Some of the main design principles and needed capabilities for IoT are:

- **Do the research**: The first step in the design process is to research the device's purpose and its user base. To define its main features, designers should think like the device's eventual users to identify how the IoT product will solve pain points and help overcome obstacles .
- **Align features with user value**: The IoT product should provide clear and tangible benefits to the user, such as convenience, efficiency, security, or entertainment. The features should be aligned with the user's needs, goals, and expectations, and avoid unnecessary complexity or confusion .
- **Look at the whole picture**: The IoT product should be designed as part of a larger system, not as an isolated device. The designer should consider how the device interacts with other devices, services, and platforms, and how the data flows and is processed across the system. The designer should also consider the user's context, such as location, time, activity, and mood, and how the device adapts to different situations .
- **Consider the operating settings**: The IoT product should be designed to work reliably and securely in various environments and conditions, such as indoors, outdoors, online, offline, hot, cold, wet, dry, etc. The designer should also account for the device's power consumption, battery life, connectivity, and maintenance .
- **Incorporate security early**: The IoT product should be designed with security in mind from the beginning, not as an afterthought. The designer should ensure that the device and the data are protected from unauthorized access, tampering, or theft, and that the user has control over their personal information and privacy. The designer should also follow the best practices and standards for encryption, authentication, and authorization .
- **Deploy effective data management**: The IoT product should be designed to collect, store, analyze, and present data in a meaningful and useful way. The designer should consider what data is relevant, how often it is collected, where it is stored, how it is processed, and how it is visualized. The designer should also ensure that the data is accurate, reliable, and consistent, and that it complies with the legal and ethical regulations .
- **Include scalability**: The IoT product should be designed to scale up or down according to the demand and the availability of resources. The designer should consider how the device and the system can handle increasing or decreasing numbers of users, devices, data, and features, and how they can adapt to changing requirements and expectations .
- **Prepare for different use cases**: The IoT product should be designed to accommodate different scenarios and possibilities that may arise from the user's interaction with the device and the system. The designer should consider how the device and the system can handle errors, failures, exceptions, and feedback, and how they can provide guidance, assistance, and recovery options to the user .



# An IoT architecture outline for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- IoT architecture is the system of numerous elements that enable IoT devices to communicate with each other and perform various tasks.
- A basic IoT architecture consists of three layers: perception, network, and application.
- Perception layer: This layer comprises the sensors, actuators, and other smart devices that collect data from the physical environment and perform actions on it .
- Network layer: This layer comprises the network devices and communications types and protocols that transmit the data from the perception layer to the application layer or vice versa  . Examples of network devices are routers, gateways, and switches. Examples of communications types and protocols are 5G, Wi-Fi, Bluetooth, MQTT, and CoAP.
- Application layer: This layer comprises the cloud services, platforms, and applications that store, process, and analyze the data from the network layer and provide feedback or commands to the perception layer  . Examples of cloud services are AWS IoT, Azure IoT, and Google Cloud IoT. Examples of platforms and applications are smart home, smart city, smart health, and smart agriculture.
- Some IoT architectures may have additional layers or components, such as edge computing, middleware, security, and analytics  .
- Edge computing: This is a component that enables data processing and analysis at the edge of the network, near the perception layer, to reduce latency and bandwidth consumption .
- Middleware: This is a layer that provides interoperability and integration between different IoT devices, platforms, and applications, as well as data management and processing services .
- Security: This is a component that ensures the confidentiality, integrity, and availability of the IoT data and devices, as well as the protection from cyberattacks and unauthorized access .
- Analytics: This is a component that applies advanced techniques such as machine learning, artificial intelligence, and big data to extract meaningful insights and patterns from the IoT data .



# Standards considerations for the notes of the Unit 1 - IoT-An Architectural Overview

- The notes should provide a clear and concise introduction to the concept, definition, and characteristics of the Internet of Things (IoT).
- The notes should explain the main components and layers of a basic IoT architecture, such as perception, network, cloud, and application.
- The notes should describe the different architectural views and design objectives of IoT, such as functional, deployment, information, and operational views.
- The notes should highlight the key challenges and requirements of IoT, such as scalability, interoperability, security, and privacy.
- The notes should include relevant examples and diagrams to illustrate the IoT concepts and architectures.
- The notes should cite the sources of information and use a consistent referencing style, such as APA or IEEE.



### M2M and IoT Technology Fundamentals

- M2M stands for Machine-to-Machine communication, which is the direct exchange of data between devices without human intervention.
- IoT stands for Internet of Things, which is the network of physical objects embedded with sensors, software and connectivity that enables data collection and analysis.
- M2M is a subset of IoT, as IoT involves communication between machines without human input, making it by definition a form of M2M communication.
- However, IoT expands the power and potential of M2M technology in new ways. The biggest difference between M2M and IoT is that an M2M system uses point-to-point communication, while an IoT system typically situates its devices within a global cloud network that allows larger-scale integration and more sophisticated applications .
- Scalability is another key difference between M2M and IoT. M2M systems are usually limited by the number of devices that can be connected and the bandwidth that can be used, while IoT systems can leverage the cloud infrastructure to accommodate millions of devices and data streams.
- M2M technology was first adopted in manufacturing and industrial settings, where other technologies, such as SCADA and remote monitoring, helped remotely manage and control data from equipment. M2M has since found applications in other sectors, such as healthcare, business and insurance .
- IoT works through a combination of wireless networking technology, physical devices, advanced data analytics and cloud computing. The basic process of how IoT works is as follows:
  - A group of physical devices is wired or wirelessly linked to each other and/or a central area. The devices collect data from the external world using some kind of sensor.
  - The data is transmitted to a cloud platform or a local server, where it is stored and processed using various algorithms and tools.
  - The processed data is then used to generate insights, actions or feedback, which can be delivered to the devices, the users or other systems.
  - The devices can also receive commands or updates from the cloud platform or the local server, enabling bidirectional communication and control.
- Some of the benefits of IoT technology are:
  - Improved efficiency and productivity, as IoT can automate tasks, optimize processes and reduce human errors.
  - Enhanced customer experience and satisfaction, as IoT can provide personalized services, real-time feedback and proactive solutions.
  - Increased innovation and competitiveness, as IoT can enable new business models, revenue streams and value propositions.
  - Reduced costs and risks, as IoT can monitor and manage resources, assets and operations, and prevent failures and damages.



### Devices and gateways for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Devices are the physical objects that are connected to the Internet of Things (IoT) network and can sense, actuate, communicate, and process data. Examples of devices are sensors, actuators, cameras, smart phones, smart watches, etc.
- Gateways are the central hubs that connect devices to the cloud and enable data transfer, protocol translation, data aggregation, security, and device management. Examples of gateways are routers, modems, edge servers, etc.
- The architecture of IoT gateways consists of the following components    :
  - Security: This is one of the most critical factors in an IoT gateway architecture throughout the design phase. It involves encryption, authentication, authorization, and firewall mechanisms to protect the data and devices from unauthorized access and cyberattacks.
  - Device layer: This is the hardware of an IoT infrastructure that includes IoT sensors, protective circuits, networking modules, and a processor or microcontroller. The device layer is responsible for sensing, actuating, and communicating with the gateway and other devices.
  - Data management: This is the software that handles the data collected from the devices and prepares it for transmission to the cloud. It involves data filtering, compression, transformation, and validation to ensure data quality and efficiency.
  - Operating system: This is the software that runs the gateway hardware and other programs on the device. It provides an interface for the user and the applications, and manages the resources and processes of the gateway. Examples of operating systems for IoT gateways are Linux, Windows, Android, etc.
  - Hardware abstraction: This is the software that enables the communication between the device layer and the operating system. It provides a common interface for different types of devices and sensors, and hides the hardware details from the applications.
  - Gateway data transfer: This is the software that enables the communication between the gateway and the cloud. It involves the use of communication protocols, such as MQTT, HTTP, CoAP, etc., to send and receive data over the network.
  - Communication protocols: These are the rules and standards that govern the data exchange between the devices, the gateway, and the cloud. They define the format, structure, and semantics of the data, as well as the methods of error detection and correction. Examples of communication protocols for IoT are Bluetooth, Wi-Fi, ZigBee, LoRaWAN, etc.
  - Cloud connectivity manager: This is the software that manages the connection between the gateway and the cloud. It involves the use of cloud services, such as AWS IoT, Azure IoT Hub, Google Cloud IoT, etc., to store, process, and analyze the data, and to provide device management and security features.



### Local and Wide Area Networking for IoT

- Local area networks (LAN) and wide area networks (WAN) are two types of networks that can be used to connect IoT devices to each other and to the internet.
- A LAN is a group of devices that are connected within a short geographic area, typically less than 1000 meters, such as a home, office, or building. A LAN can use wired or wireless technologies, such as Ethernet, WiFi, or Bluetooth, to enable data transmission and device communication. A LAN can also have multiple access points that extend the network coverage and allow devices to roam within the network. A LAN can be connected to a WAN through a router or a gateway .
- A WAN is a group of devices that are connected over a large geographic area, such as a city, country, or the world. A WAN can use wired or wireless technologies, such as cellular, satellite, or radio, to enable data transmission and device communication. A WAN can also have multiple nodes that relay the data and provide network access to remote devices. A WAN can be connected to a LAN through a router or a gateway.
- LAN and WAN have different advantages and disadvantages for IoT applications, depending on the requirements and constraints of the devices and the network. Some of the factors that affect the choice of network type are:
  - Data rate: The amount of data that can be transmitted per unit time. LAN typically offers higher data rates than WAN, but also consumes more power and bandwidth. WAN typically offers lower data rates than LAN, but also consumes less power and bandwidth. The data rate depends on the network technology, the distance between the devices, and the interference from other sources .
  - Latency: The delay between sending and receiving data. LAN typically offers lower latency than WAN, but also requires more synchronization and coordination among the devices. WAN typically offers higher latency than LAN, but also allows more flexibility and scalability for the devices. The latency depends on the network technology, the number of hops between the devices, and the congestion in the network .
  - Coverage: The area that can be covered by the network. LAN typically offers smaller coverage than WAN, but also provides more reliability and security for the devices. WAN typically offers larger coverage than WAN, but also exposes the devices to more risks and challenges. The coverage depends on the network technology, the topology of the network, and the environmental factors .
  - Cost: The expense of setting up and maintaining the network. LAN typically has lower cost than WAN, but also requires more infrastructure and management for the devices. WAN typically has higher cost than LAN, but also requires less infrastructure and management for the devices. The cost depends on the network technology, the number of devices, and the service providers .
- Some examples of IoT applications that use LAN and WAN are:
  - Smart home: A smart home is a LAN that connects various devices, such as sensors, cameras, lights, thermostats, and appliances, to enable automation and remote control. A smart home can also be connected to a WAN, such as the internet, to enable cloud services and remote access.
  - Smart city: A smart city is a WAN that connects various devices, such as sensors, cameras, traffic lights, parking meters, and vehicles, to enable monitoring and optimization. A smart city can also be connected to a LAN, such as a municipal network, to enable local services and communication.



### Data management for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

Data management is the process of collecting, storing, processing, and analyzing data from various sources, such as sensors, devices, applications, and networks, in order to generate insights and value for the business or organization. Data management is a crucial aspect of the Internet of Things (IoT), which is the network of physical objects that are embedded with sensors, software, and other technologies to connect and exchange data with other devices and systems over the Internet.

Some of the key points to consider for data management for IoT are:

- Identify the business needs and objectives for implementing IoT and how it will benefit the organization. For example, IoT can help improve operational efficiency, customer satisfaction, product quality, safety, and sustainability.
- Ensure that the network connectivity is reliable, secure, and scalable to support the data transmission and communication between the IoT devices and the cloud or edge platforms. Network connectivity can be achieved through various protocols, such as Wi-Fi, Bluetooth, Zigbee, LoRaWAN, or cellular networks.
- Set up connectivity to the right platform that can handle the data ingestion, storage, processing, and analysis for IoT. The platform can be cloud-based, edge-based, or hybrid, depending on the latency, bandwidth, security, and cost requirements. The platform should also provide tools and services for data integration, quality, governance, and security.
- Assign roles and responsibilities for data collection and analysis, such as data engineers, data scientists, data analysts, and business users. Data collection and analysis can involve various methods and techniques, such as data cleansing, filtering, aggregation, transformation, visualization, and machine learning.
- Analyze data to generate insights and actions that can improve the performance, efficiency, and value of the IoT system. Data analysis can help identify patterns, trends, anomalies, and correlations in the data, and provide recommendations, predictions, and alerts for decision making and optimization.
- Review and update the data management strategy regularly to ensure that it meets the changing needs and expectations of the organization and the IoT system. Data management strategy should be aligned with the business goals and objectives, and should be flexible and adaptable to the evolving technologies and standards of IoT.



### Business processes in IoT

- A business process is a collection of related events, activities and decisions that involve a number of factors and resources, which collectively lead to an outcome that is of value for the organisation and the customer.
- IoT (Internet of Things) is the network of physical objects embedded with sensors, software and other technologies that enable them to connect and exchange data with other devices and systems over the internet.
- IoT can improve business processes by automating, monitoring, optimizing and extending them, as well as providing valuable information, analytics and insights.
- Some examples of business processes that can benefit from IoT are:
  - Manufacturing: IoT can enable smart factories, where machines can communicate with each other, adjust to changing conditions, detect faults and perform preventive maintenance, resulting in improved efficiency, quality and safety.
  - Logistics: IoT can enable smart tracking, where sensors can monitor the location, condition and status of goods and vehicles, providing real-time visibility, security and optimization of the supply chain.
  - Healthcare: IoT can enable smart healthcare, where devices can monitor the vital signs, activity and medication adherence of patients, providing remote diagnosis, treatment and prevention of diseases.
  - Retail: IoT can enable smart retail, where sensors can collect data on customer behavior, preferences and feedback, providing personalized recommendations, offers and loyalty programs.
- Some recommendations on implementing IoT business processes are:
  - To define the business process to improve and identify the problem to solve.
  - To use an end-to-end approach, considering the entire value chain and the interactions among the stakeholders.
  - To make agile design and start with proof of concept prototyping, testing and validating the solution before scaling it up.
  - To get on board the right people, with the best knowledge and skills, and keep the team size low.
  - To be persistent but acknowledgeable to failure, learning from mistakes and adapting to changes.
  - To be aware of the potential disruption, but not go crazy about it, focusing on the customer value and the business goals.



# Everything as a Service (XaaS) for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Everything as a Service (XaaS) is a general term that describes the delivery of any IT function as a service over the internet, using cloud computing and remote access technologies  .
- XaaS originated from the Software as a Service (SaaS) model, which provides software applications on demand, without requiring installation or maintenance on the user's device .
- XaaS has expanded to include other types of services, such as Infrastructure as a Service (IaaS), Platform as a Service (PaaS), Storage as a Service (STaaS), Desktop as a Service (DaaS), Disaster Recovery as a Service (DRaaS), and more   .
- XaaS enables users to access and consume IT resources on demand, without having to invest in or manage the underlying infrastructure, software, or hardware   .
- XaaS offers benefits such as scalability, flexibility, cost-efficiency, innovation, and agility for both providers and consumers of IT services     .
- XaaS also poses challenges such as security, privacy, compliance, integration, performance, and reliability, which require careful evaluation and management by both providers and consumers of IT services     .
- XaaS is relevant for the Internet of Things (IoT) because it enables the creation, deployment, and management of IoT applications and devices as services, without requiring complex or costly infrastructure or software development .
- XaaS can also facilitate the integration of IoT data and services with other cloud-based services, such as analytics, artificial intelligence, and machine learning, to generate insights and value from the IoT .
- XaaS can help IoT providers and consumers to leverage the benefits of cloud computing, such as scalability, flexibility, cost-efficiency, innovation, and agility, while addressing the challenges of IoT, such as security, privacy, compliance, integration, performance, and reliability .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on M2M and IoT Analytics for the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS.

### M2M and IoT Analytics

- M2M and IoT are both technologies that enable remote communication and data exchange among machines without human intervention.
- M2M is the connection of two or more devices with the Internet for data sharing and analytics, while IoT is the connection of any device to the Internet for better performance.
- M2M is more of a vertical application that meets internal demands, while IoT is more of a horizontal application that has overarching results or open-ended capabilities.
- M2M systems use point-to-point communications between machines, sensors and hardware over cellular or wired networks, while IoT systems rely on IP-based networks to send data collected from IoT-connected devices to gateways, the cloud or middleware platforms.
- M2M and IoT analytics are the processes of collecting, processing, and analyzing the data generated by M2M and IoT devices to gain insights and improve decision making.
- M2M and IoT analytics can be used for various purposes, such as monitoring, optimization, prediction, diagnosis, and control of devices and systems.
- M2M and IoT analytics can benefit various domains, such as healthcare, manufacturing, transportation, energy, agriculture, and smart cities.
- M2M and IoT analytics face some challenges, such as data quality, security, privacy, scalability, interoperability, and standardization.



### Knowledge Management for the notes of the Unit 1 - IoT-An Architectural Overview

- Knowledge management (KM) is the process of creating, sharing, using and managing the knowledge and information of an organization or a network of entities.
- KM can help improve the performance, innovation and competitiveness of organizations or networks by leveraging the data, information and knowledge generated by the Internet of Things (IoT) devices and systems  .
- IoT is the network of physical objects or things embedded with sensors, software, and other technologies for the purpose of connecting and exchanging data with other devices and systems over the Internet.
- IoT can be seen as a series of disruptive technologies that influence the daily life of both individuals and companies, and offer new opportunities to improve KM.
- IoT can act as a knowledge creation mediator, enabling the generation of new knowledge from the data collected by the sensors and devices, and facilitating the sharing and transfer of knowledge among different actors and stakeholders .
- IoT can also help in creating an open and collaborative ecosystem, where knowledge flows across different domains and boundaries, and where innovation capacity is enhanced by exploiting the synergies and complementarities of knowledge.
- IoT can be divided into three main layers: the perception layer, the network layer, and the application layer.
- The perception layer is responsible for sensing the physical world and collecting data from the environment. It consists of various types of sensors, actuators, RFID tags, cameras, etc. that are attached to the objects or things.
- The network layer is responsible for transmitting and processing the data collected by the perception layer. It consists of various communication technologies, protocols, and standards that enable the connectivity and interoperability of the IoT devices and systems.
- The application layer is responsible for providing the services and functionalities to the end-users and consumers. It consists of various software platforms, applications, and systems that use the data and information from the network layer to create value and solve problems.
- Some of the challenges and issues related to KM in IoT are: data quality, security, privacy, ethics, governance, standardization, integration, scalability, and sustainability  .



## Unit 2 - Reference Architecture

- A reference architecture is a **generic** and **abstract** model that defines the structure, behavior, and properties of a system or a domain.
- A reference architecture provides a **common vocabulary**, **guidelines**, **best practices**, **patterns**, and **standards** for designing and implementing specific systems.
- A reference architecture is **not** a concrete architecture or a blueprint for a specific system, but rather a **template** or a **framework** that can be **adapted** and **customized** to meet specific requirements and constraints.
- A reference architecture can be **domain-specific** (such as cloud computing, IoT, or cybersecurity) or **cross-domain** (such as enterprise architecture or service-oriented architecture).
- A reference architecture can be **represented** using different **views** and **perspectives**, such as **functional**, **logical**, **physical**, **deployment**, **security**, **performance**, **quality**, and **governance**.
- A reference architecture can be **documented** using different **notations** and **languages**, such as **UML**, **SysML**, **ArchiMate**, or **TOGAF**.
- A reference architecture can be **evaluated** and **validated** using different **methods** and **criteria**, such as **trade-off analysis**, **scenario analysis**, **simulation**, **prototyping**, or **testing**.
- A reference architecture can be **reused** and **shared** across different **projects**, **organizations**, and **communities**, to **promote** **interoperability**, **compatibility**, **consistency**, **efficiency**, and **quality** of systems.



### IoT Architecture-State of the Art

- A reference model is a model that describes the main conceptual entities and how they are related to each other, while the reference architecture aims at describing the main functional components of a system as well as how the system works, how the system is deployed, what information the system processes, etc.
- The principles of Reactive Systems define the state-of-the-art programming models for IoT. Reactive Systems are responsive, resilient, elastic, and message-driven. They can handle high concurrency, low latency, and high throughput, which are essential for IoT applications.
- IoT platforms must tackle asset management as a foundational problem and provide facilities for managing the provisioning of devices and services, public key infrastructure (PKI), software and firmware updates, and desired-state configuration of devices, at huge scale.
- IoT architecture and sensors used in development and security have potential applications, such as system tuning and diagnosis, fog computing, 6G, and cloud computing.
- IoT architecture can be classified into three main layers: perception layer, network layer, and application layer. The perception layer is responsible for sensing and collecting data from the physical world. The network layer is responsible for transmitting and processing the data. The application layer is responsible for providing services and applications to the end-users.
- IoT architecture can also be classified into three main types: centralized, decentralized, and distributed. Centralized architecture relies on a central server or cloud to manage and control the IoT devices and services. Decentralized architecture relies on a network of nodes or gateways to manage and control the IoT devices and services. Distributed architecture relies on the IoT devices and services themselves to manage and control their own behavior and interactions.



### Introduction for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- In this unit, we will learn about the concept of reference architecture for the Internet of Things (IoT) and its benefits and challenges.
- A reference architecture is a generic blueprint that defines the structure, components, interfaces, and interactions of a system or a domain of interest.
- A reference architecture can be used as a guide or a template for designing and implementing specific architectures for concrete applications or scenarios.
- A reference architecture can also facilitate interoperability, standardization, and reuse of existing solutions and best practices.
- A reference architecture for IoT can help address the complexity, heterogeneity, and scalability of IoT systems and enable the integration of various IoT devices, platforms, and services.
- A reference architecture for IoT can also support the development of common IoT functionalities, such as device management, data processing, security, privacy, and governance.
- There are different approaches and models for developing and representing a reference architecture for IoT, such as the ISO/IEC 30141, the IoT-A, the IIRA, and the RAMI 4.0.
- In this unit, we will compare and contrast these different reference architectures for IoT and analyze their strengths and weaknesses.
- We will also discuss the key design principles and challenges for developing and applying a reference architecture for IoT.



### State of the art for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- A reference model is a model that describes the main conceptual entities and how they are related to each other.
- A reference architecture is a blueprint that describes the main functional components of a system, how the system works, how the system is deployed, what information the system processes, etc.
- A reference architecture for IoT should address the following aspects:
  - The heterogeneity and diversity of IoT devices and applications
  - The scalability and interoperability of IoT systems
  - The security and privacy of IoT data and services
  - The intelligence and adaptability of IoT systems
  - The integration and collaboration of IoT with other technologies, such as cloud, fog, and 6G
- The state of the art for IoT reference architecture can be classified into three main categories:
  - Three-layer architecture: This is the most common and simple architecture, which consists of three layers: perception, network, and application. The perception layer is responsible for sensing and collecting data from the physical world. The network layer is responsible for transmitting and processing the data. The application layer is responsible for providing services and functionalities to the end-users.
  - Five-layer architecture: This is an extension of the three-layer architecture, which adds two more layers: middleware and business. The middleware layer is responsible for providing common services and functionalities, such as data management, device management, security, and discovery. The business layer is responsible for providing business logic and value-added services, such as analytics, decision making, and optimization.
  - Cloud-based architecture: This is an architecture that leverages the cloud computing paradigm to provide IoT services and functionalities. The cloud-based architecture can be seen as a combination of the three-layer and the five-layer architectures, where the network, middleware, and business layers are hosted on the cloud. The cloud-based architecture can provide benefits such as scalability, elasticity, reliability, and cost-efficiency.
- The state of the art for IoT reference architecture is also influenced by the principles of Reactive Systems, which define the programming models for IoT. Reactive Systems are systems that are responsive, resilient, elastic, and message-driven. Responsive means that the system should respond to user requests and events in a timely manner. Resilient means that the system should recover from failures and maintain its functionality. Elastic means that the system should scale up and down according to the workload and resource availability. Message-driven means that the system should communicate asynchronously and non-blocking.
- The state of the art for IoT reference architecture is also evolving with the emergence of new technologies and paradigms, such as fog computing, edge computing, and 6G. Fog computing and edge computing are approaches that aim to bring computation and storage closer to the data sources and users, to reduce latency, bandwidth, and energy consumption. 6G is the next generation of wireless communication, which promises to provide ultra-high speed, ultra-low latency, ultra-high reliability, and ultra-high connectivity.



### Reference Model and Architecture for IoT

- A reference model is a conceptual framework that defines the common terminology, concepts, and principles for designing and developing IoT systems.
- A reference architecture is a concrete instantiation of the reference model that provides specific guidelines, standards, and best practices for implementing IoT solutions.
- A reference model and architecture for IoT should cover the following aspects:
  - The cloud or server-side architecture that allows monitoring, managing, interacting with, and processing the data from the IoT devices.
  - The networking model that enables communication between the IoT devices and the cloud or server-side components.
  - The agents and code on the IoT devices themselves, as well as the requirements on what sort of device can support the reference architecture.
- One example of a reference model and architecture for IoT is the IoT World Forum Reference Model, which consists of seven layers:
  - Device layer: This layer includes the physical devices and sensors that generate data and act on commands.
  - Connectivity layer: This layer provides the network protocols and standards for connecting the devices to the cloud or server-side components.
  - Edge computing layer: This layer provides the local processing and storage capabilities for the devices, as well as the edge analytics and intelligence.
  - Data accumulation layer: This layer provides the cloud or server-side storage and database services for the IoT data.
  - Data abstraction layer: This layer provides the data normalization, transformation, and integration services for the IoT data.
  - Application layer: This layer provides the business logic and functionality for the IoT solutions, such as dashboards, analytics, and automation.
  - Collaboration and processes layer: This layer provides the collaboration and communication services for the IoT solutions, such as workflows, notifications, and social media.
- Another example of a reference model and architecture for IoT is the IoT Architectural Reference Model (IoT ARM), which consists of four views:
  - Functional view: This view describes the functional components and their interactions in an IoT system, such as devices, gateways, brokers, and services.
  - Information view: This view describes the information model and semantics for the IoT data, such as data types, formats, and ontologies.
  - Communication view: This view describes the communication protocols and standards for the IoT system, such as MQTT, CoAP, and HTTP.
  - Deployment and operation view: This view describes the deployment and operation aspects of the IoT system, such as security, privacy, scalability, and management.



### IoT reference model

The IoT reference model is a framework that defines the main concepts, components, and relationships of the Internet of Things (IoT) systems. It aims to establish a common grounding and a common language for IoT architectures and IoT systems. It consists of the following sub-models:

- **IoT Domain Model**: This model introduces the main concepts of the IoT, such as devices, IoT services, and virtual entities (VEs), and the relations between them. A device is a physical object that can interact with the physical world and communicate with other devices or services. An IoT service is a software component that provides functionality to devices, VEs, or other services. A VE is a digital representation of a device, a group of devices, or a physical or logical entity that is not a device. A VE can have properties, behaviors, and events, and can be accessed through an IoT service.

- **IoT Functional View**: This model describes the main functions and processes that are performed by the IoT system components, and how they interact with each other. The functions are grouped into five functional groups: device management, communication, information processing, service management, and security. The processes are defined as sequences of functions that achieve a specific goal, such as device registration, data collection, or service discovery.

- **IoT Information View**: This model defines the main types of information that are exchanged or stored by the IoT system components, and how they are structured and represented. The information types include device information, service information, VE information, event information, and context information. The information structure and representation are based on common data models and formats, such as JSON, XML, or RDF.

- **IoT Deployment and Operational View**: This model describes the main aspects of deploying and operating an IoT system, such as the physical and logical distribution of the components, the network topology and protocols, the scalability and reliability issues, and the monitoring and maintenance activities.

- **IoT Governance View**: This model defines the main policies and rules that govern the IoT system, such as the ownership and access rights of the components and information, the quality of service and performance requirements, the security and privacy measures, and the compliance and auditing mechanisms.

The IoT reference model provides the concepts and definitions on which IoT architectures can be built. It also helps to identify the commonalities and differences among different IoT systems, and to facilitate the interoperability and integration of IoT components and services.



### IoT Reference Architecture

- IoT reference architecture is a conceptual framework that defines the components, interactions, and principles of an IoT solution.
- IoT reference architecture can help to guide the design, development, and deployment of IoT solutions that are scalable, secure, interoperable, and adaptable.
- IoT reference architecture can also facilitate the communication and collaboration among different stakeholders, such as developers, vendors, customers, and regulators, by providing a common language and understanding of IoT systems.
- There are different IoT reference architectures proposed by various organizations, such as IBM, Microsoft, and the IoT-A project. However, they share some common elements and layers, such as:

  - **Things layer**: This layer consists of the physical or virtual devices that generate, collect, process, and transmit data. These devices can have different capabilities, such as sensing, actuating, computing, and communicating. They can also have different protocols, standards, and interfaces, such as Bluetooth, ZigBee, MQTT, and CoAP.
  - **Network layer**: This layer provides the connectivity and communication between the things and the cloud or edge services. This layer can use different technologies, such as cellular, Wi-Fi, LoRaWAN, and satellite. This layer also handles the routing, addressing, security, and quality of service of the data packets.
  - **Service layer**: This layer consists of the cloud or edge services that store, process, analyze, and manage the data from the things. These services can provide different functionalities, such as data ingestion, transformation, aggregation, filtering, enrichment, and visualization. They can also provide different capabilities, such as machine learning, artificial intelligence, and blockchain.
  - **Application layer**: This layer consists of the applications that consume the data and services from the service layer and provide value to the end users. These applications can have different domains, such as smart home, smart city, smart agriculture, and smart health. They can also have different interfaces, such as web, mobile, and voice.

- IoT reference architecture can be customized and extended according to the specific requirements and characteristics of each IoT solution, such as the use case, the business model, the security level, and the performance criteria.



### Introduction for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The Internet of Things (IoT) is a network of physical objects or things that can communicate, sense, and interact with each other and other entities over the Internet.
- IoT systems consist of various components, such as devices, gateways, cloud platforms, applications, and services, that work together to provide functionalities and value to the users and stakeholders.
- A reference architecture is a conceptual model that defines the structure, behavior, and interfaces of an IoT system, as well as the principles and guidelines for its design and evolution.
- A reference architecture provides a common vocabulary, a shared vision, and a set of best practices for the development and integration of IoT systems.
- A reference architecture also facilitates interoperability, scalability, security, and reliability of IoT systems, by defining the standards, protocols, and technologies that should be used in each layer and component of the system.
- There are different reference architectures proposed by various organizations and initiatives, such as the IoT-Architecture (IoT-A) project, the IEEE P2413 standard, the Industrial Internet Consortium (IIC), and the OpenFog Consortium.
- These reference architectures have different scopes, perspectives, and objectives, but they share some common elements and concepts, such as the IoT device, the IoT gateway, the IoT cloud, the IoT application, and the IoT service.
- In this unit, we will study the main features, components, and layers of some of the most prominent reference architectures for IoT systems, and compare their similarities and differences. We will also discuss the challenges and opportunities of applying reference architectures to IoT systems.



### Functional View for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

The functional view of the IoT reference architecture describes the system's runtime functional components, their responsibilities, default functions, interfaces and primary interactions. The functional view is use-case- and application-independent and is therefore not compatible to the concept of views and viewpoints one-by-one. The functional view follows the modular structure of functional blocks organized into layers, as it was proposed e.g. in SENSEI.

The functional view consists of the following layers:

- Device Layer: This layer contains the physical devices that are connected to the IoT system, such as sensors, actuators, gateways, etc. The device layer is responsible for providing data acquisition, data processing, data storage, data communication and device management functions.
- Network Layer: This layer provides the communication infrastructure and services for the IoT system, such as routing, addressing, security, quality of service, etc. The network layer is responsible for enabling data transmission, data aggregation, data filtering, data fusion and network management functions.
- Service Layer: This layer provides the application logic and services for the IoT system, such as data analysis, data visualization, data mining, data processing, etc. The service layer is responsible for enabling data access, data management, data discovery, data sharing and service management functions.
- Application Layer: This layer contains the specific applications and use cases that are built on top of the IoT system, such as smart home, smart city, smart health, etc. The application layer is responsible for providing user interface, user interaction, user feedback and application management functions.

The functional view also defines the cross-layer functions that span across multiple layers, such as security, privacy, trust, identity, interoperability, etc. These functions are responsible for ensuring the reliability, safety, usability and scalability of the IoT system.

The functional view can be represented by a diagram that shows the functional components, their interfaces and their interactions. An example of such a diagram is shown below:

Functional view diagram

The functional view can be used to understand the main functions and responsibilities of the IoT system, as well as the dependencies and interactions among the functional components. The functional view can also be used to identify the commonalities and differences among different IoT use cases and applications, and to derive the requirements and specifications for the IoT system.



### Information View for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The information view describes the data and information that the system handles, such as the types, formats, sources, destinations, and flows of data.
- The information view also defines the data models, schemas, and structures that are used to store, process, and exchange data in the system.
- The information view can be divided into three sub-views: data sources, data processing, and data consumption.
- Data sources are the devices, sensors, and microcontrollers that connect with the cloud to send and receive data. They can be classified into different categories based on their capabilities, such as constrained, smart, or intelligent devices.
- Data processing is the set of functions and services that transform, analyze, and aggregate data in the cloud or at the edge. They can include data ingestion, data storage, data processing, data analytics, and data visualization.
- Data consumption is the set of applications and users that access and use the data generated by the system. They can include web apps, mobile apps, dashboards, reports, alerts, and notifications.
- The information view can be represented by a data flow diagram that shows the data sources, data processing, and data consumption components and their interactions. An example of a data flow diagram for an IoT system is shown below:

Data flow diagram for an IoT system

- The information view can help to identify the data requirements, data quality, data security, and data governance aspects of the system. It can also help to select the appropriate data technologies and services for the system.



### Deployment and Operational View

- The deployment and operational view describes the main real world components of the system such as devices, network routers, servers, etc. and how they are deployed and operated .
- The deployment view focuses on the physical layout and configuration of the system, such as the hardware, software, and network components, and how they are interconnected and distributed .
- The operational view focuses on the runtime behavior and management of the system, such as the data flows, communication protocols, security mechanisms, and monitoring and maintenance activities .
- The deployment and operational view can vary depending on the specific IoT domain, application, and scenario, and may have different levels of abstraction and granularity.
- Some aspects of the deployment and operational view that are common across the IoT domain are:
  - The IoT devices, which are the sensors, actuators, and embedded systems that interact with the physical world and collect data or perform actions.
  - The IoT gateways, which are the intermediate devices that connect the IoT devices to the network and provide data processing, filtering, aggregation, and protocol translation functions.
  - The IoT network, which is the communication infrastructure that enables data transmission and exchange between the IoT devices, gateways, and cloud services.
  - The IoT cloud, which is the collection of cloud services that provide data storage, analysis, processing, and visualization functions, as well as application logic and business rules.
  - The IoT users, which are the human or machine entities that consume the data and services provided by the IoT system, or interact with the IoT devices and cloud services.



### Other Relevant Architectural Views for IoT

- Apart from the reference architecture, there are other ways to design and describe IoT systems based on different perspectives and goals.
- Some of the common architectural views for IoT are:

  - **Application-specific view**: This view focuses on the specific requirements and features of a particular IoT application domain, such as smart home, smart city, smart health, etc. It defines the functional components, data flows, and interfaces for each application scenario. It may also include the business models, user roles, and value propositions for the application domain. 
  - **Open platform view**: This view emphasizes the scalability and interoperability of IoT systems across different domains and technologies. It defines the common standards, protocols, and platforms that enable the integration and communication of heterogeneous IoT devices and services. It may also include the security, privacy, and governance aspects of IoT systems. 
  - **Network as a Service (NaaS) view**: This view considers the IoT network as a service that can be provisioned, managed, and optimized by a provider. It defines the network architecture, topology, and resources that support the connectivity and quality of service for IoT devices and applications. It may also include the network slicing, virtualization, and orchestration techniques for IoT networks. 
  - **Basic view**: This view consists of three layers: perception, network, and application. The perception layer includes the sensors, gadgets, and other devices that collect and process data from the physical world. The network layer includes the connectivity and communication technologies that transmit and receive data between devices and applications. The application layer includes the user interfaces and business logic that provide value and functionality to the end users. 
  - **Functional view**: This view describes the functional components and capabilities of an IoT system, such as device management, data management, analytics, security, etc. It defines the roles, responsibilities, and interactions of each component, as well as the interfaces and protocols that enable the information exchange and service orchestration. It may also include the use cases, scenarios, and sequence charts that illustrate the system behavior and functionality.  
  - **Core and common view**: This view distinguishes between the core and common layers of an IoT system. The core layers are specific to IoT workloads and include the device, gateway, and cloud layers. The device layer includes the physical devices that generate and consume data. The gateway layer includes the edge devices that aggregate and preprocess data. The cloud layer includes the cloud services that store and analyze data. The common layers are not specific to IoT workloads and include the identity, security, management, and integration layers. The identity layer includes the mechanisms that authenticate and authorize users and devices. The security layer includes the policies and practices that protect the data and devices from threats. The management layer includes the tools and processes that monitor and control the system performance and health. The integration layer includes the methods and technologies that enable the data and service integration with other systems and applications.



# Real-World Design Constraints for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Real-world design constraints are the factors that limit or influence the design and implementation of IoT solutions in various domains and applications.
- Some of the common real-world design constraints are:
  - Technical challenges: These include the issues related to the hardware, software, communication, interoperability, scalability, security, and reliability of IoT devices and networks. For example, how to design low-power, low-cost, and small-sized devices that can communicate with each other and the cloud, how to ensure the compatibility and integration of different IoT standards and protocols, how to manage the massive amount of data generated by IoT devices, how to protect the data and devices from cyberattacks, and how to ensure the availability and quality of service of IoT applications.
  - Social challenges: These include the issues related to the human factors, user acceptance, ethical implications, and social impact of IoT solutions. For example, how to design user-friendly and intuitive interfaces for IoT devices and applications, how to ensure the privacy and consent of the users and the data owners, how to address the ethical and legal issues of IoT data collection and usage, and how to evaluate the social benefits and risks of IoT solutions.
  - Compromising privacy and performance tradeoffs: These include the issues related to the balance between the functionality and efficiency of IoT solutions and the protection of the privacy and security of the users and the data. For example, how to design IoT solutions that can provide useful and personalized services to the users without compromising their privacy and security, how to encrypt and anonymize the IoT data without affecting the performance and quality of the IoT applications, and how to optimize the resource utilization and energy consumption of IoT devices and networks without sacrificing the functionality and reliability of IoT solutions.
- Real-world design constraints vary depending on the specific domain and application of IoT solutions, such as smart home, smart city, smart health, smart agriculture, smart industry, etc. Each domain and application has its own requirements, challenges, and opportunities for IoT solutions.
- Real-world design constraints also evolve over time, as the technology, society, and environment change. Therefore, IoT solutions need to be adaptable and flexible to cope with the dynamic and complex real-world scenarios.



### Introduction for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- In this unit, we will learn about the concept of reference architecture for the Internet of Things (IoT) and its benefits and challenges.
- A reference architecture is a generic blueprint that defines the structure, components, interfaces, and interactions of a system or a domain of interest.
- A reference architecture can be used as a guide or a template for designing and implementing specific architectures for concrete applications or scenarios.
- A reference architecture can also facilitate interoperability, standardization, and reuse of existing solutions and best practices.
- A reference architecture for IoT can help address the complexity, diversity, and heterogeneity of IoT systems and applications, which involve various devices, networks, platforms, services, and data sources.
- A reference architecture for IoT can also enable the integration of IoT with other domains, such as cloud computing, big data, artificial intelligence, and cyber-physical systems.
- A reference architecture for IoT can provide a common vocabulary, a shared vision, and a set of principles and guidelines for the IoT community and stakeholders.
- However, a reference architecture for IoT also faces some challenges, such as the lack of a universally agreed definition and scope of IoT, the dynamic and evolving nature of IoT technologies and requirements, and the trade-offs between generality and specificity, flexibility and rigidity, and simplicity and completeness.
- In this unit, we will review some of the existing reference architectures for IoT that have been proposed by different organizations, such as the International Telecommunication Union (ITU), the Internet Engineering Task Force (IETF), the Institute of Electrical and Electronics Engineers (IEEE), the European Telecommunications Standards Institute (ETSI), and the Open Group.
- We will also compare and contrast these reference architectures in terms of their goals, scope, structure, components, and features, and identify their strengths and weaknesses.
- We will also discuss some of the open issues and future directions for the development and adoption of reference architectures for IoT.



### Technical Design Constraints of Hardware in IoT

- Hardware design for IoT involves creating embedded systems that can communicate with other devices and networks securely and efficiently.
- Hardware design constraints are the limitations or challenges that affect the performance, functionality, cost, and reliability of IoT hardware systems.
- Some of the common hardware design constraints for IoT are:

  - **Power consumption**: IoT devices often need to operate on batteries or harvest energy from the environment, which limits the amount of power available for sensing, processing, and communication. Power consumption also affects the lifetime and maintenance of IoT devices. Designers need to optimize the power management and energy efficiency of IoT hardware systems using techniques such as low-power modes, duty cycling, adaptive voltage scaling, and energy harvesting.
  - **Security**: IoT devices are exposed to various security threats such as physical tampering, eavesdropping, spoofing, denial-of-service, and malware attacks. Security is essential to protect the data, privacy, and integrity of IoT devices and networks. Designers need to implement security mechanisms such as encryption, authentication, access control, and intrusion detection in IoT hardware systems using techniques such as secure boot, trusted platform modules, hardware security modules, and secure elements.
  - **Flexibility**: IoT devices need to support various applications and protocols that may change over time. Flexibility is the ability of IoT hardware systems to adapt to different requirements and scenarios without compromising the performance and functionality. Designers need to provide flexibility in IoT hardware systems using techniques such as reconfigurable hardware, software-defined radio, and over-the-air updates.
  - **Testing**: IoT devices are often deployed in large numbers and in remote or harsh environments, which makes testing and debugging difficult and costly. Testing is the process of verifying and validating the functionality, performance, and reliability of IoT hardware systems. Designers need to facilitate testing in IoT hardware systems using techniques such as built-in self-test, fault tolerance, and remote diagnosis.
  - **Functional safety**: IoT devices are often involved in safety-critical applications such as healthcare, transportation, and industrial control, where failures can have severe consequences. Functional safety is the ability of IoT hardware systems to avoid or mitigate hazards that can cause harm to people, property, or the environment. Designers need to ensure functional safety in IoT hardware systems using techniques such as safety standards, safety analysis, and safety certification.
  - **Cost and time-to-market**: IoT devices are often expected to be low-cost and fast to produce and deploy, which puts pressure on the hardware design process. Cost and time-to-market are the factors that affect the profitability and competitiveness of IoT hardware systems. Designers need to reduce the cost and time-to-market of IoT hardware systems using techniques such as design reuse, modular design, and rapid prototyping.



### Data representation and visualization for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Data representation and visualization are important aspects of IoT systems, as they enable users to understand and interact with the data collected from various smart devices in real-time.
- Data representation refers to the process of transforming raw data into a format that can be easily stored, processed, and transmitted by IoT devices and applications. Data representation can involve data compression, encryption, encoding, serialization, and standardization.
- Data visualization refers to the process of presenting data in a graphical or pictorial form that can reveal patterns, trends, and insights. Data visualization can involve data analysis, aggregation, filtering, transformation, and mapping.
- Some of the benefits of data representation and visualization in IoT are:
  - They can improve the efficiency and accuracy of data analysis and decision making by highlighting the most relevant and meaningful information.
  - They can enhance the user experience and engagement by providing interactive and intuitive interfaces for data exploration and manipulation.
  - They can facilitate the communication and collaboration among different stakeholders by providing a common and consistent view of the data.
  - They can support the scalability and security of IoT systems by reducing the data size and complexity, and by protecting the data integrity and privacy.
- Some of the challenges of data representation and visualization in IoT are:
  - They have to deal with the heterogeneity and diversity of IoT data sources, formats, and types, which may require different representation and visualization techniques and tools.
  - They have to cope with the high volume and velocity of IoT data, which may pose performance and resource constraints for data processing and rendering.
  - They have to adapt to the dynamic and evolving nature of IoT data, which may require real-time and adaptive representation and visualization solutions.
  - They have to address the usability and accessibility issues of IoT data, which may require user-friendly and device-agnostic representation and visualization approaches.
- Some of the tools and methodologies for data representation and visualization in IoT are:
  - JSON, XML, and CBOR are some of the common data representation formats for IoT data, as they are lightweight, human-readable, and interoperable.
  - MQTT, CoAP, and HTTP are some of the common data transmission protocols for IoT data, as they are reliable, efficient, and secure.
  - Grafana, Kibana, and ThingSpeak are some of the common data visualization platforms for IoT data, as they provide rich and customizable dashboards, charts, and widgets for data display and interaction.
  - Data mining, machine learning, and statistical analysis are some of the common data analysis techniques for IoT data, as they provide advanced and intelligent methods for data extraction, classification, clustering, and prediction.
  - Data mapping, transformation, and aggregation are some of the common data processing techniques for IoT data, as they provide flexible and scalable methods for data integration, normalization, and summarization.



### Interaction and remote control for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Interaction and remote control are two important aspects of IoT applications that enable users and service providers to access and manipulate IoT devices from different locations and platforms.
- Interaction refers to the interfaces and methods that allow users to communicate with IoT devices, such as mobile applications, web browsers, voice commands, touchscreens, etc. Interaction can be used for monitoring, configuring, or controlling IoT devices, depending on the application and user needs.
- Remote control refers to the ability to access and manage IoT devices over the internet, without requiring physical presence or direct connection. Remote control can be used for troubleshooting, maintenance, updates, or customization of IoT devices, depending on the service provider and customer needs.
- Some of the benefits of interaction and remote control in IoT are:
  - Improved user experience and convenience, as users can access and control IoT devices from anywhere and anytime, using their preferred devices and platforms.
  - Enhanced service quality and efficiency, as service providers can monitor and manage IoT devices remotely, reducing operational costs and downtime.
  - Increased security and reliability, as IoT devices can be secured and updated remotely, preventing unauthorized access and malicious attacks.
- Some of the challenges of interaction and remote control in IoT are:
  - Complexity and heterogeneity, as IoT devices may have different capabilities, protocols, standards, and interfaces, requiring interoperability and compatibility solutions.
  - Scalability and performance, as IoT devices may generate large amounts of data and traffic, requiring efficient and robust network and cloud infrastructure.
  - Privacy and trust, as IoT devices may collect and transmit sensitive and personal data, requiring encryption and authentication mechanisms .
- Some of the examples of interaction and remote control in IoT are:
  - Smart home systems, where users can interact and control various home appliances, such as lights, air-conditioning, security cameras, etc., using mobile applications or voice assistants.
  - Industrial IoT systems, where service providers can remotely monitor and manage various industrial machines, such as sensors, actuators, robots, etc., using web portals or dashboards.
  - Healthcare IoT systems, where patients and doctors can interact and control various medical devices, such as wearable sensors, implants, monitors, etc., using mobile applications or web browsers.



# Unit 3 - IOT Data Link Layer & Network Layer Protocols

The data link layer and the network layer are two important layers in the IoT technology stack. They are responsible for providing reliable and efficient communication between IoT devices and other networks.

## Data Link Layer Protocols

The data link layer provides service to the network layer. It is responsible for framing, error detection, medium access control, and link management. There are various protocols and standard technologies specified by different organizations for data link protocols. Some of the common data link protocols for IoT are:

- **Bluetooth**: Bluetooth is a short-range wireless communication network over a radio frequency. It is widely used for connecting IoT devices such as smartphones, wearables, speakers, etc. Bluetooth supports low-power and low-cost devices, and offers data rates up to 24 Mbps. Bluetooth has different versions, such as Bluetooth Low Energy (BLE), Bluetooth Mesh, and Bluetooth 5, that offer different features and capabilities for IoT applications. 
- **Wi-Fi**: Wi-Fi is a wireless local area network (WLAN) technology that uses radio waves to provide high-speed internet access. Wi-Fi is one of the most popular and ubiquitous data link protocols for IoT, as it can connect a large number of devices over a wide range of distances. Wi-Fi supports data rates up to 1.3 Gbps, and offers security, scalability, and interoperability. Wi-Fi has different standards, such as Wi-Fi 4, Wi-Fi 5, Wi-Fi 6, and Wi-Fi HaLow, that cater to different IoT scenarios and requirements. 
- **Zigbee**: Zigbee is a low-power and low-data-rate wireless network that operates in the industrial, scientific, and medical (ISM) radio bands. Zigbee is designed for IoT applications that require long battery life, low cost, and mesh networking. Zigbee supports data rates up to 250 kbps, and can connect up to 65,000 devices in a network. Zigbee is based on the IEEE 802.15.4 standard, and uses a star, tree, or mesh topology. Zigbee is suitable for IoT applications such as smart home, smart lighting, smart metering, etc. 
- **Z-Wave**: Z-Wave is another low-power and low-data-rate wireless network that operates in the sub-GHz frequency band. Z-Wave is similar to Zigbee, but uses a proprietary protocol that is not based on any IEEE standard. Z-Wave supports data rates up to 100 kbps, and can connect up to 232 devices in a network. Z-Wave uses a mesh topology, and offers security, reliability, and interoperability. Z-Wave is also suitable for IoT applications such as smart home, smart lighting, smart metering, etc. 
- **LoRa**: LoRa is a long-range and low-power wireless network that operates in the sub-GHz frequency band. LoRa is designed for IoT applications that require wide-area coverage, low bandwidth, and low cost. LoRa supports data rates up to 50 kbps, and can connect millions of devices in a network. LoRa uses a star-of-stars topology, and offers security, scalability, and robustness. LoRa is suitable for IoT applications such as smart agriculture, smart city, smart environment, etc. 

## Network Layer Protocols

The network layer provides service to the transport layer. It is responsible for addressing, routing, and forwarding of data packets. There are various protocols and standard technologies specified by different organizations for network layer protocols. Some of the common network layer protocols for IoT are:

- **IPv4**: IPv4 is the fourth version of the Internet Protocol (IP), which is the most widely used network layer protocol for the internet. IPv4 provides logical addressing and routing for data packets over different networks. IPv4 supports data packets up to 65,535 bytes, and offers reliability, fragmentation, and checksum. IPv4 uses 32-bit addresses, which can accommodate up to 4.3 billion devices in a network. However, IPv4 has some limitations, such as address exhaustion, security, and scalability, that make it unsuitable for IoT applications. 
- **IPv6**: IPv6 is the sixth version of the Internet Protocol (IP), which is the successor of IPv4. IPv6 is designed to overcome the limitations of IPv4, and to provide better support for IoT applications. IPv6 supports data packets up to 4 GB, and offers reliability, fragmentation, and checksum. IPv6 uses



### PHY/MAC Layer(3GPP MTC

- 3GPP MTC stands for 3rd Generation Partnership Project Machine Type Communication, which is a term used to describe various applications that involve communication between machines or devices without human intervention.
- 3GPP MTC can be categorized into two major challenges: massive MTC and critical MTC, depending on the requirements of latency, reliability, scalability, and complexity.
- 3GPP MTC can be supported by different radio access technologies, such as GSM, UMTS, LTE, and NR (New Radio), which have different physical and MAC layer specifications and procedures  .
- The physical layer (PHY) is responsible for the modulation, coding, multiplexing, and transmission of data over the radio channel, as well as the detection, demodulation, decoding, and demultiplexing of the received data.
- The medium access control (MAC) layer is responsible for the allocation and management of radio resources, such as frequency, time, and power, as well as the scheduling and coordination of data transmissions and receptions between different users and devices.
- The PHY and MAC layers of 3GPP MTC have to address various challenges and trade-offs, such as:
  - How to achieve low complexity and low cost for MTC devices, which may have limited battery life, processing power, and memory?
  - How to support massive number of MTC devices, which may generate infrequent and small size data traffic, and avoid congestion and collision in the radio network ?
  - How to ensure high reliability and low latency for critical MTC applications, which may have stringent quality of service (QoS) requirements and involve safety-critical or mission-critical scenarios?
  - How to enable flexible and scalable PHY and MAC layer solutions, which can adapt to different MTC scenarios and requirements, and coexist with other types of communication, such as human-to-human or human-to-machine ?
- Some of the PHY and MAC layer solutions developed for 3GPP MTC include:
  - Narrowband IoT (NB-IoT), which is a low power wide area (LPWA) technology that uses a narrowband (180 kHz) carrier in the LTE spectrum to provide low data rate, long range, and low complexity MTC services .
  - Enhanced Machine Type Communication (eMTC), which is another LPWA technology that uses a wider bandwidth (1.4 MHz) carrier in the LTE spectrum to provide higher data rate, shorter latency, and higher mobility MTC services .
  - LTE-M, which is a generic term that covers both NB-IoT and eMTC technologies, and provides a unified framework for MTC services over LTE networks .
  - 5G NR, which is the next generation radio access technology that supports both massive MTC and critical MTC applications, and provides a flexible and scalable PHY and MAC layer design that can accommodate different numerologies, waveforms, frame structures, and channel coding schemes .



# IEEE 802.11

- IEEE 802.11 is a set of standards for wireless local area networks (WLANs) that operate in the 2.4 GHz, 5 GHz, and 60 GHz frequency bands .
- IEEE 802.11 defines the physical layer (PHY) and the medium access control (MAC) layer specifications for WLANs.
- IEEE 802.11 has several amendments that extend or modify the original standard, such as IEEE 802.11a, IEEE 802.11b, IEEE 802.11g, IEEE 802.11n, IEEE 802.11p, and IEEE 802.11ad .
- Some of the main features and characteristics of the IEEE 802.11 amendments are:

  - IEEE 802.11a: Provides up to 54 Mbps data rate in the 5 GHz band and uses orthogonal frequency-division multiplexing (OFDM) as the modulation technique.
  - IEEE 802.11b: Provides up to 11 Mbps data rate in the 2.4 GHz band and uses direct-sequence spread spectrum (DSSS) or complementary code keying (CCK) as the modulation technique.
  - IEEE 802.11g: Provides up to 54 Mbps data rate in the 2.4 GHz band and uses OFDM or DSSS/CCK as the modulation technique. It is backward compatible with IEEE 802.11b.
  - IEEE 802.11n: Provides up to 600 Mbps data rate in the 2.4 GHz or 5 GHz band and uses multiple-input multiple-output (MIMO) technology and OFDM as the modulation technique. It supports channel bonding, frame aggregation, and spatial multiplexing.
  - IEEE 802.11p: Provides wireless access in vehicular environments (WAVE) and operates in the 5.9 GHz band. It supports vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) communication and uses OFDM as the modulation technique.
  - IEEE 802.11ad: Provides up to 7 Gbps data rate in the 60 GHz band and uses single-carrier or OFDM as the modulation technique. It supports beamforming, directional antennas, and multi-gigabit wireless docking.

- IEEE 802.11 is also known as Wi-Fi and is widely used in home and office networks, as well as in public hotspots, to allow wireless devices to communicate with each other and access the Internet .
- IEEE 802.11 is also a basis for other wireless technologies, such as IEEE 802.11p for vehicular networks, IEEE 802.11s for mesh networks, and IEEE 802.11ah for low-power wide-area networks (LPWANs) .



### IEEE 802.15

- IEEE 802.15 is a working group of the Institute of Electrical and Electronics Engineers (IEEE) IEEE 802 standards committee which specifies Wireless Specialty Networks (WSN) standards .
- The working group was formerly known as Working Group for Wireless Personal Area Networks (WPANs) .
- The working group develops standards for low-data-rate, low-power, and low-cost wireless communications among devices .
- The working group has several task groups (TGs) that focus on different aspects of WSNs, such as physical layer (PHY), medium access control (MAC), security, mesh networking, coexistence, and applications .
- Some of the standards developed by the working group are:
  - IEEE 802.15.1: Bluetooth, a short-range wireless technology for personal area networks (PANs) .
  - IEEE 802.15.4: Low-Rate Wireless Networks (LR-WPANs), a standard for low-data-rate, low-power, and low-cost wireless connectivity with fixed, portable, and moving devices  .
  - IEEE 802.15.4a: an amendment to IEEE 802.15.4 specifying additional physical layers (PHYs) to the original standard, such as ultra-wideband (UWB) and chirp spread spectrum (CSS) .
  - IEEE 802.15.4e: an amendment to IEEE 802.15.4 specifying enhancements to the MAC sublayer, such as time-slotted channel hopping (TSCH), low-latency deterministic network (LLDN), and deterministic and synchronous multi-channel extension (DSME) .
  - IEEE 802.15.4f: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for active radio frequency identification (RFID) systems .
  - IEEE 802.15.4g: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for smart utility networks (SUNs) .
  - IEEE 802.15.4k: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for low-energy critical infrastructure monitoring (LECIM) networks .
  - IEEE 802.15.4n: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for medical body area networks (MBANs) .
  - IEEE 802.15.4p: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for rail communication and control (RCC) networks .
  - IEEE 802.15.4q: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for wireless access in vehicular environments (WAVE) networks .
  - IEEE 802.15.4r: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for high-density impulse radio (HD-IR) networks .
  - IEEE 802.15.4s: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for low-data-rate wireless smart metering utility networks (LDR-WiSUNs) .
  - IEEE 802.15.4t: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for point-to-point wireless bridging for personal area networks (PANs) .
  - IEEE 802.15.4u: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for long-range low-data-rate wireless smart metering utility networks (LR-WiSUNs) .
  - IEEE 802.15.4v: an amendment to IEEE 802.15.4 specifying physical layer (PHY) specifications for low-latency deterministic networks for industrial automation (LLDN-IA) [^



### WirelessHART

- WirelessHART is a wireless communications protocol for process automation applications.
- It is a subset of the HART industrial instrument communication standard as of version 7, communicating process data over 2.4 GHz radio waves .
- It adds wireless capabilities to HART technology while maintaining compatibility with existing HART devices, commands, and tools.
- It is based on the IEEE 802.15.4 standard for low-rate wireless personal area networks (LR-WPANs).
- It uses mesh networking technology, which means that each device can act as a router and relay messages from other devices.
- It supports self-organization, self-healing, and channel hopping to ensure reliable and secure data transmission.
- It uses 128-bit AES encryption and a join key to authenticate devices and protect data integrity.
- It has a network manager that coordinates the network operation and assigns time slots and channels to each device.
- It has a gateway that serves as an interface between the wireless network and a wired network or a host control system .
- It supports up to 250 devices per network and has a typical range of 200 meters per hop.
- It has a data rate of 250 kbps and a latency of 100 ms to 1 s depending on the network size and configuration.
- It is designed for low-power operation and can use batteries or energy harvesting devices as power sources.
- It is a multi-vendor, interoperable wireless standard that is supported by the FieldComm Group .
- It is suitable for applications such as monitoring, control, asset management, diagnostics, and safety  .



### ZWave

ZWave is a wireless communication protocol designed for smart home and IoT devices. It operates on the low-frequency 800 to 900 MHz band, which avoids interference with the 2.4 GHz band where Wi-Fi and Bluetooth operate. ZWave uses a mesh network topology, where each device can relay messages to other devices within range, increasing the network coverage and reliability. ZWave supports encryption and security features to protect the data and devices from unauthorized access. ZWave is a proprietary protocol developed by Sigma Designs, Inc., but there is also an open source implementation called OpenZWave.

Some of the main features and advantages of ZWave are:

- Low power consumption: ZWave devices can run on batteries for years, making them suitable for sensors and controllers that do not need constant power supply.
- Scalability: ZWave networks can support up to 232 devices, which can be added or removed easily without affecting the network performance.
- Interoperability: ZWave devices from different manufacturers can work together, as long as they comply with the ZWave certification standards and use the same frequency band.
- Compatibility: ZWave devices can integrate with other smart home and IoT platforms, such as Amazon Alexa, Google Home, Apple HomeKit, Samsung SmartThings, etc.
- Simplicity: ZWave devices are easy to install and configure, as they use a plug-and-play approach and do not require complex settings or passwords.

Some of the main challenges and limitations of ZWave are:

- Proprietary: ZWave is not an open standard, which means that it is controlled by a single company and may not be compatible with future technologies or regulations.
- Cost: ZWave devices are typically more expensive than other wireless protocols, such as Wi-Fi or Bluetooth, due to the licensing fees and the specialized hardware required.
- Range: ZWave devices have a limited range of about 30 meters indoors and 100 meters outdoors, which may not be enough for large or complex environments. However, the mesh network can extend the range by using intermediate devices as repeaters.
- Bandwidth: ZWave devices have a low data rate of about 100 kbps, which may not be sufficient for high-definition video or audio streaming or other data-intensive applications.



### Bluetooth Low Energy

- Bluetooth Low Energy (BLE) is a wireless personal area network technology designed and marketed by the Bluetooth Special Interest Group (Bluetooth SIG) aimed at novel applications in the healthcare, fitness, beacons, security, and home entertainment industries.
- BLE is distinct from the previous (often called "classic") Bluetooth Basic Rate/Enhanced Data Rate (BR/EDR) protocol, but the two protocols can both be supported by one device: the Bluetooth 4.0 specification permits devices to implement either or both of the LE and BR/EDR systems.
- BLE has the following advantages over classic Bluetooth:
  - Lower power consumption: BLE devices can operate for months or years on a coin cell battery, while classic Bluetooth devices require frequent recharging.
  - Faster connection time: BLE devices can connect in a few milliseconds, while classic Bluetooth devices may take seconds.
  - Simpler pairing process: BLE devices can use a variety of methods to pair, such as scanning a QR code, tapping a NFC tag, or proximity detection, while classic Bluetooth devices require a PIN code or a confirmation button.
  - Higher scalability: BLE devices can support up to 20 connections simultaneously, while classic Bluetooth devices are limited to 7 connections.
- BLE uses two protocols for discovery and communication between devices: the Generic Access Profile (GAP) and the Generic Attribute Profile (GATT).
  - GAP defines how devices advertise themselves and discover other devices. GAP also defines the roles of devices, such as peripheral (device that advertises and provides data) and central (device that scans and consumes data).
  - GATT defines how devices exchange data using services, characteristics, and descriptors. GATT also defines the roles of devices, such as server (device that provides data) and client (device that requests data).
- BLE devices can operate in different modes, such as broadcast, connection, or mesh.
  - Broadcast mode: A device sends data to all nearby devices without establishing a connection. This mode is useful for applications such as beacons, which provide location or contextual information to nearby devices.
  - Connection mode: A device establishes a connection with another device and exchanges data using GATT. This mode is useful for applications such as fitness trackers, which provide biometric data to a smartphone or a smartwatch.
  - Mesh mode: A device connects with multiple devices and relays data between them. This mode is useful for applications such as smart home, which allow devices to communicate with each other and with a gateway device.



### Zigbee Smart Energy

- Zigbee Smart Energy (Zigbee SE) is a protocol designed for monitoring and actively managing energy consumption at the end-user level .
- Zigbee SE is based on the Zigbee standard, which is a low-cost and low-power wireless technology that operates in the 2.4 GHz and SubGHz frequency bands .
- Zigbee SE enables utilities and consumers to reduce waste, energy consumption and emissions footprint, and to optimize the generation and consumption of energy, gas and water .
- Zigbee SE supports various applications, such as smart metering, demand response, load control, pricing, prepayment, home area network, distributed energy resources, and electric vehicle charging .
- Zigbee SE is interoperable and secure, as it uses standard Internet Protocol (IP) and Zigbee Cluster Library (ZCL) for communication and data exchange, and Zigbee Public Key Infrastructure (PKI) and Zigbee Smart Energy Certificate Authority (SECA) for authentication and encryption .
- Zigbee SE is scalable and flexible, as it can support different network topologies, such as star, tree, and mesh, and can integrate with other Zigbee profiles, such as Zigbee Home Automation and Zigbee Green Power .



### DASH7

- DASH7 is an open-source wireless sensor and actuator network protocol, which operates in the 433 MHz, 868 MHz and 915 MHz unlicensed ISM band /SRD band.
- DASH7 is based on the ISO 18000-7 standard for active radio frequency identification (RFID) and supports bi-directional communication, mobility, low power consumption, security and scalability .
- DASH7 can be used for various applications such as asset tracking, building automation, smart metering, environmental monitoring, industrial control, logistics, security and access control .
- DASH7 has several advantages over other wireless protocols such as Zigbee, Bluetooth and Wi-Fi, such as:
  - Longer range: DASH7 can reach up to 2 km in line-of-sight and up to 200 m in non-line-of-sight conditions, while Zigbee and Bluetooth have a range of about 10-100 m and Wi-Fi has a range of about 50-100 m .
  - Lower power consumption: DASH7 devices can operate for years on a single battery, while Zigbee and Bluetooth devices need frequent recharging and Wi-Fi devices need constant power supply .
  - Better penetration: DASH7 can communicate through walls, metal, water and other obstacles, while Zigbee, Bluetooth and Wi-Fi suffer from attenuation and interference .
  - Higher mobility: DASH7 can support fast-moving devices up to 300 km/h, while Zigbee, Bluetooth and Wi-Fi are designed for stationary or slow-moving devices .
  - Greater security: DASH7 can provide end-to-end encryption, authentication and anti-jamming features, while Zigbee, Bluetooth and Wi-Fi have more vulnerabilities and limitations .
  - More scalability: DASH7 can support up to 16 million devices per network, while Zigbee and Bluetooth can support up to 65,000 devices and Wi-Fi can support up to 256 devices .
- DASH7 has a layered architecture, consisting of four layers: physical layer, data link layer, network layer and application layer .
  - Physical layer: This layer defines the modulation, coding, frequency hopping and channel access schemes for DASH7 devices. It uses binary phase shift keying (BPSK) modulation and forward error correction (FEC) coding to achieve robust and reliable communication. It also uses frequency hopping spread spectrum (FHSS) to avoid interference and increase security. It supports two channel access methods: slotted ALOHA and listen before talk (LBT) .
  - Data link layer: This layer defines the frame format, addressing, error detection and correction, and medium access control (MAC) protocols for DASH7 devices. It uses a 16-bit CRC for error detection and correction. It supports two MAC protocols: contention-based and reservation-based. The contention-based MAC protocol uses slotted ALOHA with random backoff and retransmission to handle collisions. The reservation-based MAC protocol uses a centralized controller to allocate time slots to devices based on their priority and traffic demand .
  - Network layer: This layer defines the routing, addressing, discovery, mobility and security protocols for DASH7 devices. It uses a hierarchical addressing scheme, where each device has a 64-bit unique identifier (UID) and a 16-bit network identifier (NID). It supports two routing protocols: flooding and source routing. The flooding protocol broadcasts every packet to all devices in the network, while the source routing protocol specifies the path of each packet in the header. It also supports device discovery, mobility management and security features such as encryption, authentication and anti-jamming .
  - Application layer: This layer defines the application programming interface (API), data representation and service discovery protocols for DASH7 devices. It uses a command-response model, where each device can send or receive commands and responses to or from other devices. It also uses a tag data standard (TDS), which defines the format and semantics of the data exchanged between devices. It also supports service discovery, which allows devices to advertise and discover the services offered by other devices .



### Network Layer

The network layer is the third layer of the OSI model and the second layer of the TCP/IP model. It is responsible for addressing and routing of data packets in a network. It also performs functions such as fragmentation, reassembly, congestion control, and error detection.

Some of the main topics related to the network layer are:

- **IP addressing**: IP addressing is a method of assigning unique identifiers to devices in a network. IP addresses are usually represented in dotted decimal notation, such as 192.168.1.1. There are two versions of IP addressing: IPv4 and IPv6. IPv4 uses 32-bit addresses, which can support up to 4.3 billion devices. IPv6 uses 128-bit addresses, which can support up to 3.4 x 10^38 devices. IP addresses are divided into network and host portions, which are determined by the subnet mask. IP addresses can be classified into different classes, such as A, B, C, D, and E, based on the size and number of networks and hosts. IP addresses can also be categorized into static and dynamic, depending on whether they are assigned manually or automatically by a server.
- **Routing**: Routing is the process of finding the best path for a data packet to reach its destination. Routing can be performed by routers, which are devices that connect different networks and forward packets based on their IP addresses. Routing can be classified into two types: static and dynamic. Static routing is when the routes are manually configured by the network administrator. Dynamic routing is when the routes are automatically updated by routing protocols, such as RIP, OSPF, EIGRP, and BGP. Routing can also be categorized into unicast, multicast, broadcast, and anycast, depending on the number and type of destinations for a packet.
- **Encapsulation**: Encapsulation is the process of adding headers and trailers to the data from the upper layers to form a data packet. The header contains information such as the source and destination IP addresses, the protocol type, the packet length, and the time to live (TTL). The trailer contains information such as the checksum, which is used to verify the integrity of the packet. Encapsulation enables the network layer to communicate with the lower and upper layers of the OSI model.
- **Fragmentation and reassembly**: Fragmentation and reassembly are the processes of breaking down and recombining large data packets into smaller ones. Fragmentation is performed by the network layer when the packet size exceeds the maximum transmission unit (MTU) of the underlying network. The network layer adds a fragmentation header to each fragment, which contains information such as the identification, the offset, and the flag. Reassembly is performed by the network layer at the destination, which uses the fragmentation header to reconstruct the original packet.
- **Congestion control and error detection**: Congestion control and error detection are the processes of managing and correcting the problems that occur in the network layer. Congestion control is the process of preventing and reducing the overload of data packets in the network, which can cause delays, losses, and retransmissions. Congestion control can be performed by the network layer using techniques such as windowing, buffering, queuing, dropping, and feedback. Error detection is the process of identifying and correcting the errors that occur in the data packets, such as bit errors, checksum errors, and routing errors. Error detection can be performed by the network layer using techniques such as parity, checksum, and cyclic redundancy check (CRC).

The network layer is an essential component of the IoT architecture, as it enables the communication and connectivity between devices in the IoT system. Some of the network layer protocols that are used in IoT are:

- **IPv4 and IPv6**: IPv4 and IPv6 are the standard IP addressing protocols for the internet and IoT. IPv4 is widely used, but it has limitations such as address exhaustion, security issues, and scalability problems. IPv6 is designed to overcome these limitations, by providing larger address space, enhanced security, and improved performance. IPv6 also supports features such as stateless address autoconfiguration (SLAAC), neighbor discovery protocol (NDP), and multicast listener discovery (MLD), which are useful for IoT devices.
- **6LoWPAN**: 6LoWPAN is a protocol that enables the transmission of IPv6 packets over low-power wireless personal area networks (LoWPANs), such as IEEE 802.15.4. 6LoWPAN adapts the IPv6 packets to the constraints of LoWPANs, such as low bandwidth, low power, and small frame size. 6LoWPAN performs



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of IPv4 for the unit 3 of IOT Architecture and Protocols.

### IPv4
- IPv4 stands for Internet Protocol version 4. It is the most widely used protocol for data communication over the internet.
- IPv4 uses 32-bit addresses to identify devices on the network. Each address consists of four octets (8 bits) separated by dots, such as 192.168.1.1.
- IPv4 addresses are divided into two parts: network prefix and host identifier. The network prefix indicates the network to which the device belongs, and the host identifier indicates the specific device on that network.
- The network prefix can vary in length depending on the address class or the subnet mask. There are five address classes: A, B, C, D, and E. Each class has a different range of network prefixes and host identifiers.
- Class A addresses have a network prefix of 8 bits and a host identifier of 24 bits. They can support up to 126 networks and 16,777,214 hosts per network. The first octet of a class A address ranges from 1 to 126.
- Class B addresses have a network prefix of 16 bits and a host identifier of 16 bits. They can support up to 16,384 networks and 65,534 hosts per network. The first octet of a class B address ranges from 128 to 191.
- Class C addresses have a network prefix of 24 bits and a host identifier of 8 bits. They can support up to 2,097,152 networks and 254 hosts per network. The first octet of a class C address ranges from 192 to 223.
- Class D addresses are reserved for multicast communication. They have a network prefix of 28 bits and a host identifier of 4 bits. The first octet of a class D address is 224.
- Class E addresses are reserved for experimental purposes. They have a network prefix of 32 bits and no host identifier. The first octet of a class E address is 240.
- A subnet mask is a 32-bit binary number that indicates which part of the address is the network prefix and which part is the host identifier. For example, a subnet mask of 255.255.255.0 means that the first 24 bits are the network prefix and the last 8 bits are the host identifier.
- IPv4 uses a hierarchical addressing scheme, which means that the addresses are assigned and managed by different levels of authorities. The top-level authority is the Internet Assigned Numbers Authority (IANA), which allocates blocks of addresses to regional internet registries (RIRs). The RIRs then distribute the addresses to local internet registries (LIRs), such as internet service providers (ISPs) or organizations. The LIRs then assign the addresses to end users or customers.
- IPv4 has some limitations, such as the exhaustion of address space, the lack of security and quality of service features, and the complexity of configuration and management. To overcome these limitations, a new version of the internet protocol, IPv6, was developed and is gradually being adopted.



# IPv6

IPv6 is the next generation Internet Protocol (IP) standard intended to eventually replace IPv4, the protocol many Internet services still use today. IPv6 is designed to solve many of the problems of IPv4, such as address depletion, security, auto-configuration, extensibility, and so on. IPv6 expands the capabilities of the Internet to enable new kinds of applications, including peer-to-peer and mobile applications.

Some of the important features and uses of IPv6 are:

- IPv6 addresses: An IPv6 address uses 128 bits, four times more than the IPv4 address, which uses only 32 bits. This allows for a much larger address space, which can accommodate more devices and networks on the Internet. IPv6 addresses are written using hexadecimal, as opposed to dotted decimal in IPv4. For example, an IPv6 address may look like this: 2001:db8:0:1234:0:567:8:1.
- Network and node addresses: In IPv4, address classes were used to split an address into two components: a network component and a node component. In IPv6, the address is divided into two parts: a 64-bit network prefix and a 64-bit interface identifier. The network prefix identifies the network to which the device belongs, and the interface identifier identifies the device on that network. The interface identifier can be derived from the MAC address of the device, or randomly generated.
- IPv6 address types and scope: IPv6 defines different types of addresses for different purposes and scopes. Some of the common address types are:

  - Link-local: These addresses are used for communication within a single network segment, and are not routable across the Internet. They start with fe80::/10.
  - Global unicast: These addresses are used for communication across the Internet, and are globally unique and routable. They start with 2000::/3.
  - Unique local: These addresses are used for communication within a private network, and are not routable across the Internet. They are similar to IPv4 private addresses, but are globally unique to avoid conflicts. They start with fc00::/7.
  - Multicast: These addresses are used for sending a single packet to multiple destinations. They start with ff00::/8.
  - Anycast: These addresses are used for sending a packet to the nearest or best destination among a group of devices that share the same address. They are a subset of global unicast or unique local addresses.

- Using IPv6 addresses in uniform resource locators (URLs): To use an IPv6 address in a URL, the address must be enclosed in square brackets, followed by the port number if needed. For example, http://[2001:db8:0:1234:0:567:8:1]:80/index.html.
- IPv6 loopback: The loopback address is used for testing the connectivity of the device with itself. In IPv4, the loopback address is 127.0.0.1. In IPv6, the loopback address is ::1.



### 6LoWPAN

- 6LoWPAN stands for IPv6 over Low-power Wireless Personal Area Networks.
- It is an open standard defined by the Internet Engineering Task Force (IETF) that enables low-power devices with limited processing capabilities to participate in the Internet of Things (IoT) by using IPv6 over IEEE 802.15.4 based networks .
- 6LoWPAN defines mechanisms for:
  - Encapsulation: how to fragment and reassemble IPv6 datagrams over the IEEE 802.15.4 frame size limit of 127 bytes.
  - Header compression: how to reduce the size of IPv6 and UDP headers to fit in the IEEE 802.15.4 frame payload.
  - Neighbor discovery: how to discover and register IPv6 addresses and prefixes of other nodes in the network.
  - Routing: how to forward IPv6 datagrams over multiple hops using different routing protocols, such as RPL (Routing Protocol for Low-Power and Lossy Networks).
- 6LoWPAN networks can be connected to other IPv6 networks, such as the Internet, through edge routers that support IPv6 transition mechanisms, such as NAT64, which allows IPv6 nodes to communicate with IPv4 nodes.
- 6LoWPAN networks can support various applications that require wireless internet connectivity at lower data rates, such as residential and office automation, smart grid, industrial monitoring, etc.



# 6TiSCH

- 6TiSCH stands for IPv6 over the Time Slotted Channel Hopping (TSCH) mode of IEEE 802.15.4e.
- It is a protocol stack that combines the industrial performance of TSCH with the Internet integration of IPv6.
- It is intended to provide reliable and delay bounded communication in multi-hop and scalable Industrial Internet of Things (IIoT) networks.
- It is a working group at the IETF that is standardizing the 6TiSCH architecture and protocol suite.

## TSCH
- TSCH is a link layer protocol that allows the nodes to change their physical channel after each transmission to eliminate the effects of interference and multipath fading.
- TSCH uses a Time Division Multiple Access (TDMA) schedule that defines when and on which channel a node can transmit or receive.
- TSCH can achieve high reliability, low power consumption, and deterministic latency by avoiding collisions and minimizing idle listening.

## 6TiSCH Architecture
- The 6TiSCH architecture consists of the following components:
  - The IEEE 802.15.4 PHY and MAC layers that provide the physical and link layer services.
  - The 6TiSCH Operation Sublayer (6top) that manages the TSCH schedule and provides an interface between the MAC and the network layer.
  - The 6top Protocol (6P) that enables the nodes to negotiate the TSCH schedule with their neighbors.
  - The 6LoWPAN adaptation layer that compresses the IPv6 headers and fragments the packets to fit the MAC frame size.
  - The IPv6 layer that provides the network layer services and assigns a global address to each node.
  - The IP-in-IP encapsulation that allows the nodes to tunnel the IPv6 packets over the TSCH network.
  - The Routing Protocol for Low-Power and Lossy Networks (RPL) that builds a routing topology and selects the best paths for the IPv6 packets.

## 6TiSCH Benefits
- Some of the benefits of 6TiSCH are :
  - It enables the seamless integration of the IIoT devices with the Internet and the cloud services.
  - It supports a large number of devices with a single IPv6 subnet and a global address space.
  - It provides high reliability, low power consumption, and deterministic latency for the IIoT applications.
  - It allows the dynamic adaptation of the TSCH schedule to the network conditions and the application requirements.
  - It leverages the existing standards and protocols for the IIoT communication.



# ND for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

## Data Link Layer Protocols

- The data link layer provides service to the network layer and is responsible for reliable and efficient transmission of data frames between nodes on a network.
- There are various protocols and standard technologies specified by different organizations for data link protocols.
- Some of the common data link protocols in IoT are:
  - Bluetooth: A short-range wireless communication network over a radio frequency. It supports low-power and low-cost devices and enables data exchange between them.
  - Wi-Fi: A wireless LAN technology that uses radio waves to provide high-speed internet access and network connections. It supports various standards such as IEEE 802.11a/b/g/n/ac/ax.
  - ZigBee: A low-rate wireless personal area network (WPAN) that operates in the 2.4 GHz frequency band. It is based on the IEEE 802.15.4 standard and supports mesh networking, low-power consumption, and security features.
  - Z-Wave: A wireless home automation network that operates in the sub-GHz frequency band. It is designed for low-latency, low-data-rate, and low-power devices and supports interoperability, encryption, and routing.
  - LoRa: A long-range, low-power, and low-data-rate wireless technology that uses spread spectrum modulation and operates in the sub-GHz frequency band. It is suitable for IoT applications that require wide-area coverage, such as smart cities, agriculture, and logistics.
  - Cellular: A mobile communication technology that uses radio waves to provide voice and data services over a cellular network. It supports various generations such as 2G, 3G, 4G, and 5G, each with different features and capabilities.

## Network Layer Protocols

- The network layer is responsible for addressing and routing of data packets between different networks.
- There are various protocols and standard technologies specified by different organizations for network layer protocols.
- Some of the common network layer protocols in IoT are:
  - IPv4: The fourth version of the internet protocol that uses 32-bit addresses to identify devices on a network. It supports various features such as fragmentation, checksum, and header options.
  - IPv6: The sixth version of the internet protocol that uses 128-bit addresses to identify devices on a network. It supports various features such as auto-configuration, security, and mobility.
  - 6LoWPAN: A protocol that enables IPv6 packets to be transmitted over low-power and low-data-rate wireless networks, such as IEEE 802.15.4. It supports various features such as header compression, fragmentation, and adaptation.
  - RPL: A routing protocol for low-power and lossy networks (LLNs) that operates on top of 6LoWPAN. It supports various features such as topology formation, routing metrics, and loop avoidance.
  - CoAP: A web transfer protocol for constrained devices and networks that operates on top of UDP. It supports various features such as request/response model, caching, and observe.
  - MQTT: A publish/subscribe messaging protocol for lightweight and reliable communication between devices and servers. It operates on top of TCP and supports various features such as quality of service, retain, and last will.

: https://www.javatpoint.com/iot-data-link-communication-protocol
: https://techvidvan.com/tutorials/communication-protocols-in-iot/
: https://www.engineersgarage.com/network-layer-protocols-iot-part-8/



# DHCP

- DHCP stands for Dynamic Host Configuration Protocol  .
- It is a network management protocol that automatically provides an Internet Protocol (IP) host with its IP address and other related configuration information such as the subnet mask and default gateway .
- It uses a client-server architecture, where a DHCP server allocates IP addresses and other parameters to DHCP clients that request them .
- It is based on the Bootstrap Protocol (BOOTP), which was designed for diskless workstations .
- It is defined by RFCs 2131 and 2132, and is an Internet Engineering Task Force (IETF) standard.
- It operates on four basic steps: discover, offer, request, and acknowledge (DORA)  .
  - Discover: The DHCP client broadcasts a DHCPDISCOVER message to find a DHCP server on the network  .
  - Offer: The DHCP server responds with a DHCPOFFER message, which contains an IP address and other configuration information for the client  .
  - Request: The DHCP client sends a DHCPREQUEST message to accept the offer from the server  .
  - Acknowledge: The DHCP server sends a DHCPACK message to confirm the allocation of the IP address and other parameters to the client  .
- It supports different types of IP address allocation, such as static, dynamic, and automatic .
  - Static: The DHCP server assigns a fixed IP address to a specific client based on its MAC address .
  - Dynamic: The DHCP server assigns an IP address from a pool of available addresses for a limited period of time (lease) .
  - Automatic: The DHCP server assigns an IP address from a pool of available addresses permanently .
- It has many benefits, such as reducing manual configuration, avoiding IP address conflicts, saving network resources, and simplifying network administration  .



### ICMP

- ICMP stands for Internet Control Message Protocol  .
- It is a network layer protocol used by network devices to diagnose network communication issues  .
- It is not associated with any transport layer protocol, such as TCP or UDP .
- It is a connectionless protocol, meaning a device does not need to open a connection with the target device before sending a message.
- It is used to generate error messages to the source IP address when network problems prevent delivery of IP packets .
- It is also used to determine whether or not data is reaching its intended destination in a timely manner .
- It is also used for inter-device communication, carrying everything from redirect instructions to timestamps for synchronization between devices.
- Some common types of ICMP messages are:
  - Echo request and echo reply: used to test the reachability and latency of a destination device   .
  - Destination unreachable: used to inform the source device that the destination device or network is unreachable   .
  - Time exceeded: used to inform the source device that the time to live (TTL) of a packet has expired   .
  - Parameter problem: used to inform the source device that there is a problem with the header of a packet   .
  - Source quench: used to inform the source device that the destination device is congested and cannot process more packets  .
  - Redirect: used to inform the source device that there is a better route to the destination device or network  .
  - Router advertisement and router solicitation: used to discover and advertise routers on a network  .
  - Timestamp request and timestamp reply: used to measure the round-trip time between devices  .
- ICMP is important for IOT because it helps to monitor and troubleshoot the connectivity and performance of IOT devices and networks .
- ICMP can also be used for malicious purposes, such as denial-of-service (DoS) attacks, ping floods, ping of death, and ICMP tunneling   .
- ICMP can be blocked or filtered by firewalls or routers to prevent or mitigate such attacks   .



### RPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The network layer is divided into two sublayers: routing layer which handles the transfer of packets from source to destination, and an encapsulation layer that forms the packets  .
- RPL stands for Routing Protocol for Low-Power and Lossy Network. It is a routing protocol designed for low-power and lossy networks (LLNs), which are resource-constrained networks that have high packet loss, low bandwidth, and dynamic topology   .
- RPL constructs a tree-like structure for the data transmission, called a Destination Oriented Directed Acyclic Graph (DODAG). A DODAG is a directed graph that has no cycles and has a single root node, which is the destination of the data packets   .
- RPL uses an objective function (OF) to select the best path for the data packets based on certain metrics and constraints, such as hop count, latency, energy consumption, link quality, etc. The OF is defined by the network administrator or the application requirements   .
- RPL supports both upward and downward routing. Upward routing is from the leaf nodes to the root node, and downward routing is from the root node to the leaf nodes. RPL uses two types of messages for the routing process: control messages and data messages   .
- RPL control messages are used to discover, maintain, and repair the DODAG. They include DODAG Information Object (DIO), DODAG Information Solicitation (DIS), Destination Advertisement Object (DAO), and Destination Advertisement Object Acknowledgment (DAO-ACK)   .
- RPL data messages are used to carry the application data from the source to the destination. They include IPv6 packets with RPL Option (RPL-OPT) and RPL Source Routing Header (RPL-SRH)   .
- RPL has several advantages, such as scalability, adaptability, energy efficiency, and support for multiple traffic patterns. However, it also has some drawbacks, such as overhead, complexity, security issues, and performance degradation .
- RPL is one of the standard network layer protocols for IoT applications. It is compatible with IPv6 and 6LoWPAN, which are the encapsulation protocols for the network layer. It is also suitable for various IoT scenarios, such as smart grid, smart city, smart home, etc  .



# CORPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- CORPL stands for **C**ontrol **O**bjective **R**outing **P**rotocol for **L**ow-Power and Lossy Networks.
- It is a network layer protocol that is designed for IoT applications that require reliable and energy-efficient data delivery.
- It is based on the RPL protocol, which is the standard routing protocol for low-power and lossy networks (LLNs) defined by the IETF .
- CORPL differs from RPL in the following aspects:
  - It uses a control objective function (COF) to optimize the routing performance according to different application requirements, such as delay, reliability, or energy consumption.
  - It employs a proactive route maintenance mechanism to detect and repair routing failures in advance, reducing the packet loss rate and the control overhead.
  - It supports multiple routing metrics and multiple paths for load balancing and path diversity, enhancing the network resilience and scalability.
- CORPL has been evaluated through simulations and experiments, and has shown better performance than RPL in terms of packet delivery ratio, end-to-end delay, energy consumption, and control overhead.
- CORPL can be applied to various IoT scenarios, such as smart grid, smart city, smart home, and industrial IoT.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on CARP for the unit 3 of IOT architecture and protocols:

### CARP
- CARP stands for Channel-Aware Routing Protocol.
- It is a distributed routing protocol designed for underwater communication.
- It has lightweight packets so that it can be used for Internet of Things (IoT).
- It performs two different functionalities: network initialization and data forwarding.
- It does not support previously collected data.
- It keeps track of data communication history to select nodes for data transfer.
- It adapts to the dynamic channel conditions and node mobility.
- It reduces the end-to-end delay and packet loss rate.
- It improves the network throughput and energy efficiency.



# Unit 4 - Transport & Session Layer Protocols

- The transport layer is the fourth layer in the OSI model, which provides end-to-end communication services for applications.
- The transport layer protocols are responsible for:
  - Establishing, maintaining, and terminating connections between hosts.
  - Segmenting and reassembling data into packets or datagrams.
  - Providing reliable or unreliable delivery of data, depending on the protocol.
  - Providing flow control and congestion control mechanisms to avoid network overload.
  - Providing error detection and correction mechanisms to ensure data integrity.
  - Providing port numbers to identify different applications or processes on the same host.
- The two most common transport layer protocols are TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).
  - TCP is a connection-oriented, reliable, and stream-based protocol that guarantees the delivery of data in the same order as it was sent. TCP uses a three-way handshake to establish a connection, and a four-way handshake to terminate a connection. TCP also uses acknowledgments, sequence numbers, and timers to ensure reliability and avoid data loss or duplication. TCP provides flow control using a sliding window mechanism, and congestion control using algorithms such as slow start, congestion avoidance, fast retransmit, and fast recovery.
  - UDP is a connectionless, unreliable, and datagram-based protocol that does not guarantee the delivery or order of data. UDP does not use any handshakes, acknowledgments, or timers to establish or terminate a connection, or to ensure reliability. UDP does not provide any flow control or congestion control mechanisms, and relies on the application layer to handle these issues. UDP is suitable for applications that require low latency, high throughput, or real-time communication, such as voice over IP, video streaming, or online gaming.
- Some other transport layer protocols that have been defined and implemented include DCCP (Datagram Congestion Control Protocol) and SCTP (Stream Control Transmission Protocol).
  - DCCP is a connection-oriented, unreliable, and datagram-based protocol that provides congestion control for applications that use UDP. DCCP uses a four-way handshake to establish a connection, and a three-way handshake to terminate a connection. DCCP also uses acknowledgments, sequence numbers, and timers to provide feedback and control the sending rate. DCCP supports different congestion control algorithms, such as TCP-like, TCP-friendly, or delay-based, depending on the application requirements.
  - SCTP is a connection-oriented, reliable, and message-based protocol that provides multiple streams of data within a single connection. SCTP uses a four-way handshake to establish a connection, and a four-way handshake to terminate a connection. SCTP also uses acknowledgments, sequence numbers, and timers to ensure reliability and avoid data loss or duplication. SCTP provides flow control using a sliding window mechanism, and congestion control using algorithms similar to TCP. SCTP also provides features such as multihoming, partial reliability, and unordered delivery, which are not supported by TCP.

- The session layer is the fifth layer in the OSI model, which provides session management services for applications.
- The session layer protocols are responsible for:
  - Creating, maintaining, and terminating sessions between hosts.
  - Synchronizing the data exchange between hosts using checkpoints or tokens.
  - Managing the dialog control between hosts using modes such as simplex, half-duplex, or full-duplex.
  - Handling the authentication and authorization of hosts using passwords or certificates.
  - Providing security and encryption mechanisms to protect the data confidentiality and integrity.
- The session layer protocols are not widely used in the TCP/IP model, as most of these functions are either supported by the transport layer protocols, such as TCP or SCTP, or by the application layer protocols, such as HTTP, FTP, or SSH.
- Some examples of session layer protocols are RPC (Remote Procedure Call), NFS (Network File System), SQL (Structured Query Language), and X.225 (ISO Transport Service on top of TCP).



### Transport Layer

The transport layer is the fourth layer of the OSI model and the TCP/IP model. It is responsible for end-to-end communication between devices in an IoT system. It provides features such as reliability, congestion control, flow control, error detection, and ordering of packets. Some of the common transport layer protocols used in IoT are:

- **TCP (Transmission Control Protocol):** TCP is a connection-oriented protocol that establishes a logical connection between the sender and the receiver before transmitting data. TCP ensures reliable and ordered delivery of data by using acknowledgments, retransmissions, and sequence numbers. TCP also implements congestion control and flow control mechanisms to avoid network overload and data loss. TCP is suitable for IoT applications that require high reliability and data integrity, such as remote monitoring, firmware updates, and file transfers. However, TCP also has some drawbacks, such as high overhead, latency, and complexity, which may affect the performance and energy efficiency of IoT devices.

- **UDP (User Datagram Protocol):** UDP is a connectionless protocol that does not establish a logical connection between the sender and the receiver. UDP sends data as datagrams without any guarantee of reliability, ordering, or error detection. UDP has low overhead, latency, and complexity, which makes it suitable for IoT applications that require high speed, real-time, and multicast communication, such as video streaming, voice over IP, and sensor data aggregation. However, UDP also has some drawbacks, such as lack of reliability, congestion control, and flow control, which may result in data loss, duplication, or corruption.

- **CoAP (Constrained Application Protocol):** CoAP is a specialized protocol designed for constrained IoT devices and networks. CoAP is based on the RESTful architecture and uses UDP as the underlying transport protocol. CoAP provides features such as lightweight messaging, asynchronous communication, resource discovery, caching, and security. CoAP is suitable for IoT applications that require low power consumption, scalability, and interoperability, such as smart home, smart city, and smart grid. However, CoAP also has some drawbacks, such as lack of reliability, congestion control, and flow control, which may be addressed by using extensions or adaptations of CoAP.

- **MQTT (Message Queuing Telemetry Transport):** MQTT is a publish-subscribe protocol that enables efficient and reliable communication between IoT devices and applications. MQTT uses TCP as the underlying transport protocol and introduces a broker as an intermediary between the publishers and the subscribers. MQTT provides features such as quality of service, lightweight messaging, topic-based filtering, and security. MQTT is suitable for IoT applications that require low bandwidth, high scalability, and loose coupling, such as industrial automation, smart agriculture, and healthcare. However, MQTT also has some drawbacks, such as dependency on the broker, lack of resource discovery, and complexity of topic naming.



### TCP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- TCP stands for Transmission Control Protocol and it is a transport layer or routing protocol that works with the Internet Protocol (IP) to provide reliable and ordered data delivery over the Internet .
- TCP guarantees the ordered data delivery by using an acknowledgment function that requires the receiver to send back a confirmation message to the sender for each packet received.
- TCP also performs retransmission of lost packets, error control and flow control to ensure the data integrity and avoid congestion .
- TCP is best suited whenever a program wants to send a lot of data because TCP does fragmentation of data and sends it in the form of small packets that can be reassembled at the destination.
- TCP supports both IPv4 and IPv6, which are network layer or adaption layer protocols that define the addressing and routing of packets across the Internet .
- TCP is traditionally neglected as a transport-layer protocol for the Internet of Things (IoT) because of its perceived complexity, overhead and unsuitability for constrained-node networks (CNNs) that have limited resources and capabilities .
- However, recent trends and industry needs are favoring TCP presence in IoT environments, such as cloud computing, edge computing, fog computing, web services, remote management, firmware updates, security and privacy .
- TCP can be implemented and used in IoT scenarios with some adaptations and optimizations, such as lightweight TCP stacks, TCP header compression, TCP option negotiation, TCP congestion control algorithms, TCP timeout estimation and TCP proxying  .
- TCP can also coexist and interoperate with other transport-layer protocols for IoT, such as UDP, CoAP, MQTT and QUIC, depending on the application requirements and network conditions  .



### MPTCP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- MPTCP stands for Multipath TCP, which is an extension of TCP for simultaneous transmission over several paths .
- MPTCP can improve the throughput, reliability, and security of data transmission in IoT networks, especially when IoT devices are equipped with multiple network access interfaces .
- MPTCP has several working modes, such as backup mode, which uses one path as the primary path and the others as backup paths, and load balancing mode, which distributes the load among all available paths .
- MPTCP has been implemented and evaluated on various platforms, such as Linux, Android, and Apple iOS, but there are no official MPTCP kernels for IoT devices yet.
- MPTCP can be combined with opportunistic routing, which is a routing technique that exploits the broadcast nature of wireless networks and selects the best next hop based on the current network conditions.
- MPTCP and opportunistic routing can enhance the performance and resilience of IoT networks, especially in scenarios where there are frequent link failures, congestion, or interference.



### UDP

- UDP stands for User Datagram Protocol. It is one of the core communication protocols of the Internet protocol suite used to send messages (transported as datagrams in packets) to other hosts on an Internet Protocol (IP) network.
- UDP is a simple message-oriented transport layer protocol that is documented in RFC 768. It provides integrity verification (via checksum) of the header and payload, but it does not provide any guarantees to the upper layer protocol for message delivery and the UDP layer retains no state of UDP messages once sent .
- UDP is primarily used to establish low-latency and loss-tolerating connections between applications on the internet. UDP speeds up transmissions by enabling the transfer of data before an agreement is provided by the receiving party.
- UDP is a part of the Internet Protocol suite, referred to as UDP/IP suite. Unlike TCP, it is an unreliable and connectionless protocol. So, there is no need to establish a connection prior to data transfer.
- UDP provides a mechanism to detect corrupt data in packets, but it does not attempt to solve other problems that arise with packets, such as lost or out of order packets. UDP is suitable for applications that require speed and efficiency, such as streaming media, online gaming, voice over IP, etc .
- UDP has a header of 8 bytes, consisting of four fields: source port, destination port, length, and checksum. The source and destination ports identify the endpoints of the communication. The length field specifies the total length of the UDP datagram, including the header and the data. The checksum field is used to verify the integrity of the header and the data .
- UDP does not provide any flow control, congestion control, or error recovery mechanisms. These functions are left to the application layer or the upper layer protocols that use UDP as the underlying transport protocol. Some examples of such protocols are RTP, RTCP, DNS, DHCP, SNMP, etc .



### DCCP

- DCCP stands for **Datagram Congestion Control Protocol**.
- It is a **message-oriented** transport layer protocol.
- It is designed to solve issues present in UDP and TCP, particularly for **real-time and multimedia** (streaming) traffic.
- It implements **reliable connection setup**, **teardown**, **Explicit Congestion Notification (ECN)**, **congestion control**, and **feature negotiation**.
- It divides into a base protocol (RFC 4340) and pluggable congestion control modules called **CCIDs** (Congestion Control IDentifiers).
- It allows applications to access congestion control mechanisms without implementing them at the application layer.
- It supports both **acknowledged** and **unacknowledged** modes of data delivery.
- It uses a **packet header** that contains a **sequence number**, a **type**, a **CCID**, and other optional fields.
- It uses a **three-way handshake** to establish a connection and a **four-way handshake** to close a connection.
- It uses a **feature negotiation mechanism** to allow endpoints to agree on optional protocol parameters.
- It uses a **slow-start** and **congestion avoidance** algorithm to adjust the sending rate according to the network conditions.
- It supports different **congestion control profiles** that can be selected by the application according to its requirements.
- Some examples of CCIDs are:
  - CCID 2: TCP-like congestion control with acknowledgments and retransmissions.
  - CCID 3: TCP-friendly rate control with feedback packets and no retransmissions.
  - CCID 4: TCP-friendly rate control for unidirectional flows.
  - CCID 5: TCP-friendly rate control for bidirectional flows.



### SCTP

- SCTP stands for **Stream Control Transmission Protocol**.
- It is a **transport layer** protocol in the Internet protocol suite.
- It is a **connection-oriented** protocol that supports **multiple streams** of data between two endpoints.
- It ensures **reliable** and **in-sequence** data transmission, so that data units arrive completely and in the right order to the application or user.
- It can **fragment** a message into multiple data chunks, but each data chunk contains data from only one user message.
- It **bundles** the chunks into SCTP packets, each identified by a chunk header.
- It is designed to transport **PSTN** (Public Switched Telephone Network) signaling messages over IP networks, but is capable of broader applications.
- It provides features such as **multihoming**, **congestion control**, **flow control**, **error detection**, **security** and **graceful shutdown**.



### Session Layer for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The session layer is the fifth layer of the OSI model that manages the connection between two endpoints of a network by controlling data between sender and receiver  .
- The session layer protocols are responsible for the actual transmission of data in the IoT ecosystem. That’s why these session layer protocols are called as IoT Messaging Protocols or sometimes referred as IoT Data Protocols .
- The session layer protocols review standards and protocols for message passing. Different standardization organizations introduce the IoT session layer protocols. There are different types of session layer protocol available with different functionality and range.
- Some of the common session layer protocols in IoT are:
  - MQTT (Message Queuing Telemetry Transport): A lightweight publish-subscribe protocol that works on top of TCP/IP and supports QoS levels, authentication, and encryption  .
  - CoAP (Constrained Application Protocol): A web transfer protocol that is designed for constrained devices and networks. It uses UDP as the transport layer and supports RESTful architecture, caching, and multicast  .
  - AMQP (Advanced Message Queuing Protocol): An open standard protocol that provides reliable and secure messaging between applications or organizations. It uses TCP as the transport layer and supports message orientation, queuing, routing, and security  .
  - XMPP (Extensible Messaging and Presence Protocol): An XML-based protocol that enables real-time communication and collaboration between devices and applications. It uses TCP or HTTP as the transport layer and supports presence, chat, group chat, and file transfer  .
- The session layer also provides some functions such as:
  - Dialog control: It allows systems to communicate in either half-duplex mode or full-duplex mode.
  - Token management: It prevents two users to simultaneously access or transmit data over the network.
  - Synchronization: It allows the addition of checkpoints into a data stream so that the data can be re-synchronized in case of failure or interruption.



### HTTP

HTTP stands for Hypertext Transfer Protocol. It is an application layer protocol in the Internet protocol suite model for distributed, collaborative, hypermedia information systems. It is used for transmitting hypermedia documents, such as HTML, between web browsers and web servers.

Some points to note about HTTP are:

- HTTP is a stateless protocol, which means that each request and response pair is independent and does not remember any previous interaction.
- HTTP uses TCP as the underlying and reliable transport layer protocol. TCP establishes a connection between the client and the server, and ensures that the data is delivered in order and without errors.
- HTTP follows a request-response model, where the client sends a request message to the server, and the server sends back a response message to the client. The request and response messages have a similar structure, consisting of a start-line, zero or more header fields, an empty line, and an optional message body.
- HTTP defines a set of methods, also known as verbs, that indicate the desired action to be performed on the resource identified by the request URI. Some common methods are GET, POST, PUT, DELETE, HEAD, and OPTIONS.
- HTTP defines a set of status codes, also known as response codes, that indicate the result of the request. Some common status codes are 200 (OK), 404 (Not Found), 301 (Moved Permanently), and 500 (Internal Server Error).
- HTTP can be extended by adding new header fields, methods, status codes, or media types. For example, HTTP/1.1 introduced persistent connections, chunked transfer encoding, and content negotiation.
- HTTP can also be modified or replaced by other protocols that offer different features or performance. For example, HTTPS is a secure version of HTTP that uses SSL/TLS encryption, HTTP/2 is a binary and multiplexed version of HTTP that reduces latency and overhead, and HTTP/3 is a version of HTTP that uses QUIC as the transport layer protocol.



### CoAP

- CoAP stands for **Constrained Application Protocol** and it is defined in **RFC 7252** .
- CoAP is an **application-layer protocol** that is intended for use in **resource-constrained Internet devices**, such as wireless sensor network nodes.
- CoAP is designed to easily translate to **HTTP** for simplified integration with the web, while also meeting specialized requirements such as **multicast support**, **very low overhead**, and **simplicity**.
- CoAP is a **client-server protocol** that enables clients to make requests for web transfers and servers to respond to them.
- CoAP is based on the **REST** (Representational State Transfer) architectural style, which means that resources are identified by **URIs** (Uniform Resource Identifiers) and manipulated by using **methods** such as GET, PUT, POST, and DELETE.
- CoAP uses **UDP** (User Datagram Protocol) as the underlying transport layer, which makes it suitable for unreliable and low-power networks.
- CoAP also supports **reliability**, **congestion control**, **security**, **asynchronous message exchanges**, and **content negotiation** by using additional features such as **message types**, **message IDs**, **tokens**, **options**, and **CoAP observe**.
- CoAP is one of the most popular and widely used **IoT protocols**, along with others such as **MQTT**, **AMQP**, and **DDS**. CoAP is especially useful for applications that require low latency, low bandwidth, and low power consumption.



# XMPP

- XMPP stands for **Extensible Messaging and Presence Protocol** .
- It is an **open communication protocol** designed for **instant messaging (IM)**, **presence information**, and **contact list maintenance** .
- It is based on **XML (Extensible Markup Language)**, which enables the **near-real-time exchange of structured data** between two or more network entities.
- It is a **decentralized protocol**, meaning that anyone can run their own XMPP server and communicate with other servers.
- It is a **living standard**, meaning that engineers actively extend and improve it.
- It supports various features and applications, such as:
  - **IoT (Internet of Things)**: XMPP can be used to connect and control devices, sensors, and actuators.
  - **WebRTC (Web Real-Time Communication)**: XMPP can be used to establish peer-to-peer audio and video calls, as well as data channels.
  - **Online Gaming**: XMPP can be used to create multiplayer games, chat rooms, and social networks.
  - **Realtime Social**: XMPP can be used to create microblogging, activity streams, and social profiles.
- It has a **modular architecture**, meaning that it can be extended with **extensions (XEPs)** that define additional features and functionality.
- Some of the common extensions are:
  - **XEP-0030: Service Discovery**: This extension allows XMPP entities to discover information about other entities, such as their capabilities, identities, and services.
  - **XEP-0045: Multi-User Chat**: This extension allows XMPP entities to create and join chat rooms, where they can communicate with multiple participants.
  - **XEP-0060: Publish-Subscribe**: This extension allows XMPP entities to publish and subscribe to topics, where they can receive notifications about events and data.
  - **XEP-0163: Personal Eventing Protocol**: This extension allows XMPP entities to publish and subscribe to personal events, such as their presence, mood, location, and avatar.
  - **XEP-0198: Stream Management**: This extension allows XMPP entities to resume interrupted streams, as well as to acknowledge and request retransmission of lost packets.
  - **XEP-0363: HTTP File Upload**: This extension allows XMPP entities to upload and share files via HTTP, without requiring a direct connection between the sender and the receiver.

: https://en.wikipedia.org/wiki/XMPP
: https://xmpp.org/
: https://xmpp.org/extensions/xep-0030.html
: https://xmpp.org/extensions/xep-0045.html
: https://xmpp.org/extensions/xep-0060.html
: https://xmpp.org/extensions/xep-0163.html
: https://xmpp.org/extensions/xep-0198.html
: https://xmpp.org/extensions/xep-0363.html



### AMQP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- AMQP stands for Advanced Message Queuing Protocol. It is an open standard, binary application layer protocol designed for message-oriented middleware.
- AMQP enables encrypted and interoperable messaging between organizations and applications. The protocol is used in client/server messaging and in IoT device management. AMQP is efficient, portable, multichannel and secure.
- AMQP protocol standardizes messaging using Producers, Brokers and Consumers. Producers send messages to a broker, which stores them in queues or topics. Consumers receive messages from the broker, either by subscribing to topics or by requesting from queues.
- AMQP has the following features and benefits for IoT applications:
  - Reliable: AMQP ensures that messages are delivered exactly once, in order, and without duplication or loss.
  - Secure: AMQP supports encryption, authentication, and authorization of messages and connections.
  - Interoperable: AMQP is based on a common data model and a common wire format, which allows different implementations and platforms to communicate seamlessly.
  - Open: AMQP is an open standard, published by OASIS, and supported by a large community of vendors and users.
  - Standard: AMQP is a standard protocol, which reduces the complexity and cost of integration and maintenance of IoT systems.
  - Low overhead: AMQP has a binary wire format, which minimizes the bandwidth and processing requirements of IoT devices and networks.
- AMQP can be used to connect to an IoT hub by using the claims-based security (CBS) or Simple Authentication and Security Layer (SASL) authentication. The following information is required for the service client:
  - IoT hub hostname: `<iot-hub-name>.azure-devices.net`
  - Key name: `iothubowner`
  - Key value: `<iothubowner-key>`
  - Event hub-compatible name: `<iot-hub-name>`
  - Event hub-compatible endpoint: `sb://<iot-hub-name>.servicebus.windows.net/`
  - Consumer group: `$Default`
  - Partition ID: `0` to `n-1`, where `n` is the number of partitions in the IoT hub
- AMQP can also be used to connect to an IoT hub by using the WebSockets protocol, which allows AMQP to work over HTTP proxies and firewalls. The following information is required for the device client:
  - IoT hub hostname: `<iot-hub-name>.azure-devices.net`
  - Device ID: `<device-id>`
  - Device key: `<device-key>`
  - Port: `443`
  - Path: `/devices/<device-id>/messages/events`
  - Subprotocol: `AMQPWSB10`



### MQTT

MQTT stands for **MQ Telemetry Transport**. It is a lightweight, publish-subscribe, machine to machine network protocol for message queue / message queuing service. It is designed for connections with remote locations that have devices with resource constraints or limited network bandwidth, such as in the Internet of Things (IoT).

Some of the main features of MQTT are:

- It uses a **broker** to manage the communication between multiple **clients**. The broker is a server that receives messages from publishers and delivers them to subscribers.
- It follows a **publish-subscribe** model, where clients can publish messages to a **topic** and subscribe to one or more topics to receive messages.
- It supports **quality of service (QoS)** levels, which determine how reliably a message is delivered. There are three QoS levels: 0 (at most once), 1 (at least once), and 2 (exactly once).
- It supports **retain** and **last will** messages, which allow clients to store the last message on a topic or send a message when they disconnect.
- It supports **wildcards** and **hierarchical topics**, which allow clients to subscribe to multiple topics with a single subscription.

Some of the advantages of MQTT are:

- It is **simple** and **easy** to implement, with a small code footprint and minimal network overhead .
- It is **scalable** and **efficient**, with a high throughput and low latency .
- It is **reliable** and **secure**, with support for TLS/SSL encryption and authentication .
- It is **flexible** and **interoperable**, with support for various platforms, languages, and devices .

Some of the applications of MQTT are:

- **Smart home** and **building automation**, where MQTT can be used to control and monitor devices such as lights, thermostats, cameras, and sensors .
- **Industrial IoT** and **manufacturing**, where MQTT can be used to collect and analyze data from machines, sensors, and actuators .
- **Healthcare** and **wearables**, where MQTT can be used to transmit and receive vital signs, alerts, and notifications from medical devices and wearables .
- **Transportation** and **logistics**, where MQTT can be used to track and manage vehicles, assets, and shipments .
- **Agriculture** and **environment**, where MQTT can be used to monitor and control irrigation, soil, weather, and livestock .



## Unit 5 - Service Layer Protocols & Security

- The service layer is a layer in the telecommunication network architecture that provides capability servers owned by a network service provider, accessed through open and secure Application Programming Interfaces (APIs) by application layer servers owned by third-party content providers.
- The service layer also provides an interface to core networks at a lower resource layer.
- Service layer protocols are protocols that operate at the service layer and enable communication between different applications or services over the network.
- Some examples of service layer protocols are HTTP, SMTP, FTP, DNS, DHCP, etc.
- Security service is a service that enhances the security of data processing systems and information transfers of an organization.
- Security service implements security policies and provides security functions that are used to counter security attacks.
- Security service can be provided at different layers of the network architecture, such as the application layer, the transport layer, the network layer, or the data link layer.
- Some examples of security services are authentication, confidentiality, integrity, non-repudiation, access control, availability, etc.
- Security protocol is a protocol that implements security service using cryptographic methods and other techniques.
- Some examples of security protocols are SSL, TLS, IPSec, VPN, Kerberos, OSPF, SNMPv3, etc.
- SSL (Secure Socket Layer) is a security protocol that provides authentication and confidentiality for data exchanged between a web browser and a web server.
- TLS (Transport Layer Security) is a security protocol that is based on SSL and provides similar security services for data exchanged between any two applications over the network.
- IPSec (Internet Protocol Security) is a security protocol that provides authentication, confidentiality, and integrity for data exchanged at the network layer.
- VPN (Virtual Private Network) is a security service that creates a secure and encrypted connection over a public network, such as the internet, between two or more private networks or devices.
- Kerberos is a security protocol that provides authentication and authorization for distributed systems using a trusted third party called the Key Distribution Center (KDC).
- OSPF (Open Shortest Path First) is a routing protocol that provides authentication for routing updates exchanged between routers using a shared secret key.
- SNMPv3 (Simple Network Management Protocol version 3) is a network management protocol that provides authentication, confidentiality, and integrity for network management information exchanged between network devices.



### Service Layer for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The service layer is the layer that provides the interface between the application layer and the network layer in the IoT architecture.
- The service layer is responsible for enabling the discovery, management, and communication of IoT devices, services, and resources over the internet or other networks.
- The service layer also provides security mechanisms to protect the data and devices from unauthorized access, modification, or attack.
- Some of the main functions of the service layer are:

  - Service discovery: This function allows IoT devices to find other devices, services, and resources that they need to interact with. Service discovery can be performed using different protocols, such as CoAP, MQTT, XMPP, or DNS-SD.
  - Service management: This function allows IoT devices to register, update, or deregister their information and capabilities on the network. Service management can be performed using protocols such as LWM2M, OMA-DM, or TR-069.
  - Service communication: This function allows IoT devices to exchange data and messages with other devices, services, or applications. Service communication can be performed using protocols such as HTTP, WebSocket, AMQP, or MQTT-SN.
  - Service security: This function provides the means to ensure the confidentiality, integrity, and availability of the data and devices in the IoT network. Service security can be achieved using protocols such as TLS, DTLS, IPSec, or ZigBee Security.

- Some of the main challenges and requirements of the service layer are:

  - Scalability: The service layer should be able to handle the large number and diversity of IoT devices and services that are expected to be connected to the network.
  - Interoperability: The service layer should be able to support different protocols and standards that are used by different IoT devices and applications.
  - Reliability: The service layer should be able to provide reliable and consistent service delivery and communication, even in the presence of network failures or congestion.
  - Efficiency: The service layer should be able to optimize the use of network resources and minimize the overhead and latency of service discovery, management, and communication.
  - Security: The service layer should be able to protect the data and devices from various threats and attacks, such as eavesdropping, spoofing, tampering, or denial-of-service.



### oneM2M

- oneM2M is a global partnership project founded in 2012 and constituted by 8 of the world's leading ICT standards development organizations.
- oneM2M aims to develop a common M2M service layer that can be embedded within various hardware and software, and connect the myriad of devices in the field with M2M application servers worldwide.
- oneM2M is creating a single horizontal platform for the exchange and sharing of data among all applications. It is also creating a distributed software layer—similar to an operating system—which is facilitating that unification by providing a framework for interworking with different technologies.
- oneM2M has released four sets of technical specifications and work program deliverables, covering functional architecture, security, protocols, data models, testing and certification, and more .
- oneM2M adopts a RESTful approach to enable resource-oriented interactions between entities using HTTP or CoAP as the underlying protocols.
- oneM2M defines three types of entities: Application Entities (AEs), Common Services Entities (CSEs), and Network Services Entities (NSEs). AEs are the endpoints of the M2M system, providing or consuming services. CSEs are the core components of the M2M service layer, providing common functions such as registration, discovery, security, data management, etc. NSEs are the interfaces to the underlying network services, such as transport, routing, addressing, etc.
- oneM2M supports a hierarchical and distributed architecture, where CSEs can be deployed at different levels: Infrastructure Node (IN), Middle Node (MN), and Application Service Node (ASN). IN-CSEs are located at the network side, providing access to NSEs and enabling interworking with other M2M systems. MN-CSEs are located at the intermediate level, providing aggregation and mediation functions. ASN-CSEs are located at the application side, providing hosting and execution environment for AEs.
- oneM2M provides a comprehensive security framework, covering aspects such as authentication, authorization, encryption, integrity, confidentiality, and privacy. oneM2M defines four security levels: Level 0 (no security), Level 1 (transport security), Level 2 (end-to-end security), and Level 3 (application security). oneM2M also defines various security mechanisms, such as certificates, tokens, access control policies, etc.



### ETSI M2M

- ETSI M2M stands for European Telecommunications Standards Institute Machine-to-Machine.
- It is a standardization body that develops standards for IoT and M2M technologies.
- It is one of the founding partners of oneM2M, the global standards initiative for IoT and M2M interoperability.
- ETSI M2M defines a high-level architecture for M2M systems, as shown in the figure below.

ETSI M2M high-level architecture

- The architecture consists of three main layers: the network layer, the service layer, and the application layer.
- The network layer provides connectivity and transport services for M2M devices and gateways.
- The service layer provides common functions and capabilities for M2M applications, such as device management, data management, security, discovery, and subscription.
- The service layer is implemented by the Service Capability Layer (SCL), which is a software component that exposes a RESTful API for M2M interactions.
- The application layer contains the M2M applications that use the service layer to communicate with M2M devices and other applications.
- The architecture supports different types of M2M networks, such as M2M area networks, access networks, and core networks.
- The architecture also supports interworking with other IoT and M2M standards, such as CoAP, MQTT, OMA LWM2M, and IEEE 802.15.4.

- ETSI M2M provides a reference ontology for M2M systems, which defines the concepts, relationships, and properties of M2M entities and resources.
- The ontology is based on the SCL resource structure, which is a hierarchical representation of the M2M system state and configuration.
- The ontology enables semantic interoperability and reasoning among M2M applications and devices.



### OMA for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- OMA stands for Open Mobile Alliance, an organization that develops standards and specifications for the mobile and IoT industry.
- OMA LwM2M (Lightweight Machine to Machine) is a protocol from OMA for device management and service enablement in IoT .
- OMA LwM2M is based on IETF CoRE (Constrained RESTful Environments) RFCs and drafts, such as CoAP (Constrained Application Protocol), DTLS (Datagram Transport Layer Security), CBOR (Concise Binary Object Representation), and SenML (Sensor Measurement Lists).
- OMA LwM2M defines the application layer communication protocol between an LwM2M Server and an LwM2M Client, which is located in an IoT device.
- OMA LwM2M supports four main operations: Bootstrap, Register, Manage, and Report.
  - Bootstrap: The LwM2M Client obtains the necessary security credentials and server information from a Bootstrap Server to access other LwM2M Servers.
  - Register: The LwM2M Client registers with one or more LwM2M Servers and provides information about its capabilities and resources.
  - Manage: The LwM2M Server can perform device management and service enablement tasks on the LwM2M Client, such as read, write, execute, observe, create, delete, and write-attributes.
  - Report: The LwM2M Client can report its status and measurements to the LwM2M Server, either periodically or upon request.
- OMA LwM2M uses a resource model to represent the data and functionality of the IoT device.
  - A resource is a piece of information or an action that can be accessed by the LwM2M Server.
  - A resource can have a single or multiple value, and a data type, such as integer, float, string, boolean, opaque, time, or object link.
  - A resource can have attributes, such as minimum and maximum period, greater than, less than, step, and cancel.
  - A resource can be part of an object, which is a collection of resources that share a common purpose.
  - An object can have one or more object instances, which are individual representations of the object with specific values for the resources.
  - An object can have a mandatory or optional flag, and a single or multiple flag, indicating whether the object or its instances are required or allowed to exist on the LwM2M Client.
  - An object can have an object ID and an object version, which are unique identifiers for the object.
  - An object, an object instance, or a resource can be addressed by a URI, which consists of the object ID, the object instance ID, and the resource ID.
- OMA LwM2M defines a set of standard objects and resources for common IoT scenarios, such as device, server, security, access control, firmware update, location, connectivity monitoring, connectivity statistics, etc.
- OMA LwM2M also allows the definition of custom objects and resources for specific IoT applications, using a web-based tool called LwM2M Editor.
- OMA LwM2M provides end-to-end security for the IoT communication, using DTLS for the transport layer and OSCORE (Object Security for Constrained RESTful Environments) for the application layer.
  - DTLS provides security features such as confidentiality, integrity, and authentication for the CoAP messages exchanged between the LwM2M Server and the LwM2M Client.
  - OSCORE provides security features such as end-to-end protection, group communication, and proxy compatibility for the CoAP messages exchanged between the LwM2M Server and the LwM2M Client, even if they pass through intermediate nodes or gateways.
  - OSCORE is based on COSE (CBOR Object Signing and Encryption), which is a format for signing and encrypting CBOR data.
- OMA LwM2M



# BBF for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The service layer protocols are the application layer protocols that enable the communication and interaction among IoT devices and services.
- The service layer protocols have to deal with the challenges of security, scalability, interoperability, and resource constraints in the IoT environment.
- Some of the common service layer protocols in IoT are:
  - Constrained Application Protocol (CoAP): A lightweight protocol that is HTTP-friendly and uses request-response messages. It supports multicast, asynchronous, and observe modes of communication. It also provides security features such as encryption, authentication, and authorization using Datagram Transport Layer Security (DTLS)  .
  - Message Queuing Telemetry Transport (MQTT): A publish-subscribe protocol that uses a broker to route messages between publishers and subscribers. It is designed for low-bandwidth, high-latency, and unreliable networks. It also provides security features such as encryption, authentication, and authorization using Transport Layer Security (TLS)  .
  - Advanced Message Queuing Protocol (AMQP): A peer-to-peer protocol that uses exchanges and queues to route messages between producers and consumers. It is designed for high-performance, reliable, and secure messaging. It also provides security features such as encryption, authentication, and authorization using TLS and Simple Authentication and Security Layer (SASL)  .
  - HyperText Transfer Protocol (HTTP): A request-response protocol that uses Uniform Resource Identifiers (URIs) to identify resources and methods to manipulate them. It is widely used for web-based applications and services. It also provides security features such as encryption, authentication, and authorization using TLS and HTTP Secure (HTTPS)  .
  - User Services Platform (USP): A protocol that enables the management and control of IoT devices and services. It is based on the Broadband Forum (BBF) data model and uses CoAP, MQTT, or WebSocket as the underlying transport protocol. It also provides security features such as encryption, authentication, and authorization using DTLS, TLS, or WebSocket Secure (WSS) .
- The security of service layer protocols is of paramount importance since these protocols are at the basis of the communications among applications and services running on different IoT devices and on cloud/edge infrastructures.
- The security of service layer protocols has to address the following aspects:
  - Data privacy: The protection of the confidentiality and integrity of the data exchanged among IoT devices and services. This can be achieved by using encryption, hashing, and digital signatures.
  - Data provenance: The verification of the origin and history of the data exchanged among IoT devices and services. This can be achieved by using certificates, timestamps, and blockchain.
  - Authentication: The verification of the identity of the IoT devices and services that communicate with each other. This can be achieved by using passwords, tokens, or biometrics.
  - Authorization: The verification of the permissions and roles of the IoT devices and services that communicate with each other. This can be achieved by using access control lists, policies, or roles.
  - Trust management: The establishment and maintenance of the trustworthiness and reputation of the IoT devices and services that communicate with each other. This can be achieved by using trust models, ratings, or feedback.
- The security of service layer protocols has to deal with various security attacks and threats, such as:
  - Eavesdropping: The interception and analysis of the data exchanged among IoT devices and services. This can be prevented by using encryption and secure channels.
  - Replay: The retransmission of the data exchanged among IoT devices and services to cause malicious effects. This can be prevented by using nonce, sequence number, or timestamp.
  - Modification: The alteration or tampering of the data exchanged among IoT devices and services. This can be prevented by using hashing, digital signatures, or checksums.
  - Impersonation: The masquerading as a legitimate IoT device or service to gain unauthorized access or privileges. This can be prevented by using authentication and authorization mechanisms.
  - Denial of service: The disruption or degradation of the availability and performance of the IoT devices and services. This can be prevented by using rate limiting, filtering, or redundancy.



# Security in IoT Protocols

- Security is a major challenge for IoT devices and networks, as they are exposed to various threats and attacks from malicious actors.
- Security in IoT protocols involves ensuring the confidentiality, integrity, availability, and authenticity of data and communications in IoT systems.
- Security in IoT protocols also involves addressing the issues of data privacy, authentication, authorization, and trust management in a distributed and heterogeneous environment.
- Some of the common security protocols for IoT are:

  - MQTT: Message Queuing Telemetry Transport, a lightweight and publish-subscribe protocol for IoT messaging. It supports encryption, authentication, and authorization using TLS/SSL, username/password, and access control lists. It also supports quality of service levels and retained messages .
  - CoAP: Constrained Application Protocol, a web transfer protocol for constrained devices and networks. It supports encryption, authentication, and authorization using DTLS, pre-shared keys, certificates, and raw public keys. It also supports resource discovery, caching, and observe mechanisms.
  - LwM2M: Lightweight Machine to Machine, a device management protocol for IoT devices. It supports encryption, authentication, and authorization using DTLS, pre-shared keys, certificates, and raw public keys. It also supports bootstrapping, registration, device management, information reporting, and firmware update.
  - HTTPS: Hypertext Transfer Protocol Secure, a widely used protocol for secure web communication. It supports encryption, authentication, and authorization using TLS/SSL, certificates, and digital signatures. It also supports cookies, sessions, and redirects.
  - DTLS: Datagram Transport Layer Security, a protocol that provides security for datagram-based protocols such as UDP, CoAP, and LwM2M. It supports encryption, authentication, and authorization using TLS/SSL, pre-shared keys, certificates, and raw public keys. It also supports anti-replay protection, fragmentation, and retransmission.

- Some of the common security threats and attacks for IoT are:

  - Eavesdropping: The interception of data or communication by unauthorized parties. It can compromise the confidentiality and privacy of data and lead to information leakage, identity theft, or data manipulation .
  - Replay: The retransmission of data or communication by unauthorized parties. It can compromise the integrity and availability of data and lead to denial of service, impersonation, or data corruption .
  - Tampering: The modification of data or communication by unauthorized parties. It can compromise the integrity and authenticity of data and lead to data corruption, falsification, or injection .
  - Spoofing: The impersonation of data or communication by unauthorized parties. It can compromise the authenticity and authorization of data and lead to identity theft, access violation, or data manipulation .
  - Denial of Service: The prevention of data or communication by unauthorized parties. It can compromise the availability and functionality of data and lead to network congestion, resource exhaustion, or service disruption .



### MAC 802.15.4

- MAC 802.15.4 is a standard for low-rate wireless personal area networks (LR-WPANs) that defines the physical layer (PHY) and medium access control (MAC) sublayer specifications  .
- MAC 802.15.4 supports low-data-rate wireless connectivity with fixed, portable, and moving devices with no battery or very limited battery consumption requirements .
- MAC 802.15.4 provides the basis of other higher-layer standards, such as ZigBee, WirelessHart, 6LoWPAN and MiWi.
- MAC 802.15.4 supports multiple PHY options, such as frequency-hopping spread spectrum (FHSS), direct-sequence spread spectrum (DSSS), orthogonal frequency-division multiplexing (OFDM), and high-rate pulse ultra-wideband (HRP UWB) .
- MAC 802.15.4 defines two types of devices: full-function devices (FFDs) and reduced-function devices (RFDs). FFDs can operate in any topology and communicate with any other device, while RFDs can only operate in star or peer-to-peer topologies and communicate only with FFDs .
- MAC 802.15.4 defines two types of networks: star and peer-to-peer. In a star network, a single FFD acts as a coordinator and controls the access to the medium, while other devices are RFDs or FFDs that communicate only with the coordinator. In a peer-to-peer network, any FFD can act as a coordinator and form a cluster with other devices, and multiple clusters can be interconnected to form a mesh network .
- MAC 802.15.4 uses a slotted or unslotted carrier sense multiple access with collision avoidance (CSMA/CA) mechanism for channel access. In slotted CSMA/CA, the coordinator divides the time into equal slots and allocates them to the devices using a superframe structure. In unslotted CSMA/CA, the devices can transmit at any time without synchronization .
- MAC 802.15.4 supports two types of data transfers: data and acknowledgment. Data transfers are used to send data frames from a device to another device or the coordinator, and acknowledgment transfers are used to confirm the successful reception of a data frame .
- MAC 802.15.4 supports two types of addressing modes: short and extended. Short addressing uses 16-bit addresses that are assigned by the coordinator, while extended addressing uses 64-bit addresses that are globally unique .
- MAC 802.15.4 supports four types of security services: access control, message integrity, message confidentiality, and replay protection. MAC 802.15.4 uses the advanced encryption standard (AES) with 128-bit keys for encryption and authentication .



### 6LoWPAN

- 6LoWPAN stands for IPv6 over Low-power Wireless Personal Area Networks.
- It is an open standard defined by the Internet Engineering Task Force (IETF) that enables low-power devices with limited processing capabilities to participate in the Internet of Things (IoT) using IPv6.
- It provides mechanisms for encapsulation, header compression, neighbor discovery, routing, security, and interoperability with other IPv6 networks.
- It operates over IEEE 802.15.4 based networks, which are low-rate wireless personal area networks (LR-WPANs) that support data rates of 250 kbps, 40 kbps, or 20 kbps, and have a maximum frame size of 127 bytes .
- It uses a 6LoWPAN edge router to connect the 6LoWPAN network to other IPv6 networks, such as the Internet. The edge router may also support IPv6 transition mechanisms to connect 6LoWPAN networks to IPv4 networks, such as NAT64.
- It supports various applications that require wireless internet connectivity at lower data rates, such as residential and office automation, smart grid, industrial monitoring, healthcare, and environmental sensing.



### RPL for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for Routing Protocol for Low-Power and Lossy Networks, which are networks that have limited resources, high packet loss, and dynamic topology changes.
- RPL is designed for IoT applications that require reliable and energy-efficient data delivery, such as smart grid, smart city, and environmental monitoring.
- RPL operates on the network layer and uses IPv6 as the underlying protocol. It supports both unicast and multicast routing, and can adapt to different traffic patterns and network conditions.
- RPL organizes the network into a Destination Oriented Directed Acyclic Graph (DODAG), which is a tree-like structure rooted at a destination node. Each node in the DODAG has a rank, which indicates its distance from the root. The rank is calculated based on an objective function, which defines the metrics and constraints for the optimal path selection.
- RPL uses two types of control messages: DIO (DODAG Information Object) and DAO (Destination Advertisement Object). DIO messages are used to build and maintain the DODAG, and DAO messages are used to propagate the routing information from the leaf nodes to the root.
- RPL also supports local repair mechanisms, such as storing mode, non-storing mode, and source routing, to handle link failures and topology changes without affecting the entire DODAG.
- RPL has several security challenges and vulnerabilities, such as spoofing, replay, selective forwarding, sinkhole, wormhole, rank attack, version number attack, DAO inconsistency attack, DIO suppression attack, and Sybil attack.
- RPL security can be enhanced by using cryptographic techniques, such as digital signatures, message authentication codes, and encryption, to protect the integrity, authenticity, and confidentiality of the control messages and data packets.
- RPL security can also be improved by using trust management schemes, such as reputation systems, trust models, and anomaly detection, to evaluate the trustworthiness and reliability of the nodes and links in the network.
- RPL security is an active research area, and there are many open issues and challenges, such as scalability, interoperability, energy efficiency, and performance evaluation, that need to be addressed.



### Application Layer for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The application layer is the interface between the IoT device and the network with which it will communicate .
- It handles data formatting and presentation and serves as the bridge between what the IoT device is doing and the network handoff of the data it produces.
- It also provides services such as data storage, processing, analysis, visualization, and management.
- In IoT architecture, this layer lies above the service discovery layer, which is responsible for finding and connecting to other devices and services.
- Some of the common application layer protocols in IoT are :
  - MQTT: Message Queuing Telemetry Transport, a lightweight publish-subscribe protocol that is designed for low-bandwidth and unreliable networks.
  - CoAP: Constrained Application Protocol, a web transfer protocol that is optimized for constrained devices and networks, using UDP as the transport layer.
  - HTTP: Hypertext Transfer Protocol, a widely used web protocol that supports request-response and RESTful interactions, using TCP as the transport layer.
  - AMQP: Advanced Message Queuing Protocol, a binary protocol that supports reliable and secure messaging between applications and devices, using TCP as the transport layer.
  - XMPP: Extensible Messaging and Presence Protocol, an XML-based protocol that supports instant messaging, presence, and pubsub services, using TCP as the transport layer.
- The application layer protocols in IoT should be chosen based on the requirements and characteristics of the devices, networks, and applications involved.
- Some of the factors that influence the choice of application layer protocols are:
  - Data volume and frequency: How much and how often data is generated and transmitted by the IoT devices.
  - Data reliability and quality of service: How important and time-sensitive the data is, and what level of guarantee is needed for its delivery and acknowledgment.
  - Data security and privacy: How sensitive and confidential the data is, and what level of encryption and authentication is needed to protect it.
  - Network bandwidth and latency: How much and how fast the data can be transferred over the network, and what is the acceptable delay for the data transmission and processing.
  - Device power and memory: How much battery and storage capacity the IoT devices have, and how much they can afford to consume for data communication and processing.
  - Device interoperability and scalability: How compatible and adaptable the IoT devices are with different protocols and platforms, and how well they can handle the growth and change of the IoT system.

