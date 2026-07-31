

# IOT ARCHITECTURE AND PROTOCOLS

- IoT architecture refers to the many ways that IoT devices are structured to meet user needs. Based on complexity, IoT system elements are grouped into 3 to 7 layers, each with its own role.
- IoT protocols are the set of rules that enable communication between IoT devices, gateways, services, and data centers. Different IoT protocols have been designed and optimized for different scenarios and usage.
- A common IoT architecture consists of the following layers  :
  - Device layer: This layer contains the sensors and actuators that collect data and perform actions. Devices can be embedded, wearable, or standalone. Devices can communicate with each other, with gateways, or with the cloud using various IoT protocols.
  - Gateway layer: This layer acts as a bridge between the device layer and the cloud layer. Gateways can aggregate, filter, process, and secure data from multiple devices before sending it to the cloud. Gateways can also perform edge computing, which is the execution of analytics and logic at the edge of the network, reducing latency and bandwidth consumption.
  - Cloud layer: This layer provides the storage, processing, and analytics capabilities for the IoT data. Cloud services can also enable device management, security, and integration with other applications and systems. Cloud services can be public, private, or hybrid.
  - Application layer: This layer serves as the interface between the user and the device within a given IoT protocol. Application layer protocols define how data is formatted, transmitted, and received by the user. Application layer protocols can also provide features such as discovery, authentication, and encryption.
- Some of the common IoT protocols are :
  - Message queue telemetry transport (MQTT): This is a lightweight, publish-subscribe protocol that is ideal for low-power, low-bandwidth, and unreliable networks. MQTT enables devices to publish data to a broker, which then distributes it to the subscribers. MQTT is widely used for IoT applications such as smart home, industrial automation, and healthcare.
  - Constrained application protocol (CoAP): This is a web-based protocol that is designed for constrained devices and networks. CoAP uses the same methods and formats as HTTP, but with a binary header and UDP transport. CoAP enables devices to perform RESTful operations such as GET, PUT, POST, and DELETE. CoAP is suitable for IoT applications such as smart lighting, smart metering, and environmental monitoring.
  - Advanced message queuing protocol (AMQP): This is an open, reliable, and secure protocol that supports message-oriented middleware. AMQP enables devices to exchange messages through a broker, which can route, queue, and deliver them. AMQP supports various message patterns, such as point-to-point, publish-subscribe, and request-reply. AMQP is used for IoT applications such as smart grid, smart city, and logistics.
  - Hypertext transfer protocol (HTTP): This is the most widely used protocol for web communication. HTTP enables devices to send and receive data using the standard methods and formats of the web. HTTP is simple, flexible, and interoperable, but also consumes more power and bandwidth than other IoT protocols. HTTP is used for IoT applications such as web-based dashboards, APIs, and cloud services.



## Unit 1 - IoT-An Architectural Overview

- IoT stands for Internet of Things, which refers to the network of physical devices, sensors, actuators, and software that can collect, process, and exchange data over the internet.
- IoT enables various applications and services that can improve the quality of life, efficiency, productivity, and sustainability of different domains, such as smart cities, smart homes, smart health, smart agriculture, smart industry, etc.
- IoT architecture is the conceptual framework that defines the components, functions, interactions, and protocols of an IoT system.
- IoT architecture can be divided into four main layers: perception layer, network layer, service layer, and application layer.

### Perception Layer
- The perception layer is the lowest layer of the IoT architecture, which consists of the physical devices and sensors that can sense, measure, and capture data from the environment.
- The perception layer can also include actuators that can perform actions based on the commands from the upper layers.
- The perception layer can use various technologies and protocols to communicate with the network layer, such as RFID, NFC, Bluetooth, ZigBee, Wi-Fi, etc.

### Network Layer
- The network layer is the layer that connects the perception layer with the service layer, and provides data transmission, routing, and management functions.
- The network layer can use various technologies and protocols to transport data, such as cellular networks, satellite networks, optical networks, IP networks, etc.
- The network layer can also perform data processing, aggregation, compression, encryption, and authentication functions to ensure the quality, security, and privacy of the data.

### Service Layer
- The service layer is the layer that provides the core functionalities and services of the IoT system, such as data storage, analysis, processing, and management.
- The service layer can use various technologies and platforms to provide the services, such as cloud computing, edge computing, fog computing, big data, artificial intelligence, etc.
- The service layer can also perform data mining, machine learning, decision making, and optimization functions to extract useful information and knowledge from the data, and provide feedback and control to the perception layer and the application layer.

### Application Layer
- The application layer is the highest layer of the IoT architecture, which consists of the end-user applications and interfaces that can utilize the data and services from the service layer.
- The application layer can provide various applications and services for different domains and scenarios, such as smart home, smart health, smart city, smart agriculture, smart industry, etc.
- The application layer can also provide user-friendly and interactive interfaces, such as web, mobile, voice, gesture, etc., to enable the users to access and control the IoT system.



### Building an architecture for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- IoT stands for Internet of Things, which refers to the scenarios where network connectivity and computing capability extends to objects, sensors and everyday items not normally considered computers, allowing these devices to generate, exchange and consume data with minimal human intervention.
- IoT architecture consists of the devices, network structure, and cloud technology that allows IoT devices to communicate with each other. A basic IoT architecture consists of three layers: Perception (the sensors, gadgets, and other devices), Network (the communication protocols, gateways, and cloud services), and Application (the data analysis, visualization, and user interface).
- IoT architecture can be designed according to different requirements, use cases, and scenarios. Some of the common architectural models are: 
  - Device-centric architecture: This model focuses on the devices and their capabilities, and uses a direct connection between the devices and the cloud or a central server. This model is simple and scalable, but may have security and reliability issues.
  - Data-centric architecture: This model focuses on the data and its processing, and uses a distributed data storage and analytics platform to handle the large volume and variety of data generated by the devices. This model is efficient and flexible, but may have latency and complexity issues.
  - Service-centric architecture: This model focuses on the services and their orchestration, and uses a service-oriented approach to expose the functionality of the devices and the data as reusable and interoperable services. This model is modular and adaptable, but may have performance and compatibility issues.
- IoT architecture can also be classified into different levels of abstraction, such as: 
  - Conceptual level: This level provides an overview of the functional interactions between events, insights, and actions in IoT solutions, and defines the key components and concepts, such as devices, gateways, cloud services, data sources, data processing, data storage, data visualization, and user applications.
  - Logical level: This level provides a detailed description of the data flow and the communication protocols in IoT solutions, and defines the specific technologies and standards, such as sensors, actuators, MQTT, CoAP, HTTP, REST, JSON, XML, SQL, NoSQL, and APIs.
  - Physical level: This level provides a concrete implementation of the hardware and software in IoT solutions, and defines the actual devices, platforms, and tools, such as Raspberry Pi, Arduino, ESP32, Azure IoT Hub, AWS IoT Core, Google Cloud IoT, and IoT Edge.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a summary of the main design principles and needed capabilities for IoT:

### Main design principles and needed capabilities for IoT

- IoT design is the practice of gathering data from various IoT systems and their interactions with a goal of creating meaningful user experiences.
- IoT design takes a holistic look across the whole system, the role of each device and service, and the conceptual model of how the user understands and perceives the entire IoT system.
- Some of the main design principles for IoT are :
  - Do the research: The first step in the design process is to research the device's purpose and its user base. To define its main features, designers should think like the device's eventual users to identify how the IoT product will solve pain points and help overcome obstacles.
  - Align features with user value: The features of the IoT product should provide clear and tangible benefits to the users, not just technical capabilities. Designers should prioritize the features that deliver the most value and avoid feature creep that can complicate the user experience and increase the cost and complexity of the product.
  - Look at the whole picture: The IoT product should be designed as part of a larger ecosystem of devices, services, and users. Designers should consider how the product will interact with other elements in the system, such as data sources, cloud platforms, mobile apps, and user interfaces. The product should also be compatible with existing standards and protocols to ensure interoperability and security.
  - Consider the operating settings: The IoT product should be designed to function in different environments and contexts, such as indoors, outdoors, urban, rural, noisy, quiet, etc. Designers should account for the physical, social, and cultural factors that can affect the product's performance and user experience, such as weather, power, connectivity, privacy, and regulations.
  - Incorporate security early: The IoT product should be designed with security in mind from the start, not as an afterthought. Designers should identify the potential threats and vulnerabilities that the product may face, such as data breaches, unauthorized access, malware, and denial-of-service attacks. The product should implement appropriate security measures, such as encryption, authentication, authorization, and updates, to protect the data and the device at all levels.
  - Deploy effective data management: The IoT product should be designed to collect, store, process, and analyze the data that it generates and receives. Designers should define the data requirements and objectives of the product, such as what data to collect, how often, how much, and for what purpose. The product should also use efficient data management techniques, such as compression, filtering, aggregation, and edge computing, to optimize the data quality, quantity, and latency.
  - Include scalability: The IoT product should be designed to scale up or down according to the changing needs and demands of the users and the system. Designers should anticipate the potential growth and evolution of the product, such as adding new features, devices, users, or services. The product should also use scalable technologies, such as cloud computing, microservices, and containers, to enable flexibility and adaptability.
  - Prepare for different use cases: The IoT product should be designed to accommodate different use cases and scenarios that the users may encounter. Designers should test and validate the product with real users and real data, and collect feedback and insights to improve the product. The product should also be designed to learn from the user behavior and preferences, and provide personalized and contextualized experiences.



### An IoT architecture outline

IoT architecture is the system of numerous elements that enable IoT devices to communicate with each other and perform various tasks. A basic IoT architecture consists of the following layers and components    :

- **Physical/device layer**: This comprises the sensors, actuators and other smart devices and connected devices that collect data from the environment or perform actions based on commands. Examples of devices are cameras, thermostats, smartwatches, etc.
- **Network layer**: This comprises the network devices and communications types and protocols that enable the data transmission between the devices and the cloud or other devices. Examples of network devices are routers, gateways, switches, etc. Examples of communications types and protocols are 5G, Wi-Fi, Bluetooth, MQTT, CoAP, etc.
- **Data/database layer**: This comprises the data storage and management systems that store and organize the data collected from the devices or sent to the devices. Examples of data storage and management systems are cloud platforms, databases, data lakes, etc.
- **Processing/analysis layer**: This comprises the data processing and analysis tools and techniques that transform the raw data into meaningful insights and actions. Examples of data processing and analysis tools and techniques are machine learning, artificial intelligence, big data analytics, etc.
- **Application layer**: This comprises the applications and services that provide the user interface and functionality for the IoT system. Examples of applications and services are web apps, mobile apps, dashboards, etc.
- **Security layer**: This comprises the security mechanisms and policies that ensure the confidentiality, integrity and availability of the IoT system and its data. Examples of security mechanisms and policies are encryption, authentication, authorization, firewall, etc.

The following diagram illustrates a simple IoT architecture with the above layers and components:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Application    |     |  Processing/    |     |  Data/Database  |
|  Layer          |     |  Analysis Layer |     |  Layer          |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       ^                       ^                       ^
       |                       |                       |
       v                       v                       v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Security       |     |  Network        |     |  Physical/      |
|  Layer          |     |  Layer          |     |  Device Layer   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```



### Standards considerations for the notes of the Unit 1 - IoT-An Architectural Overview

- IoT standards are the specifications and protocols that enable interoperability and communication among different IoT devices, platforms, and applications.
- IoT standards can be classified into different layers, such as physical, network, transport, application, and service layers, depending on their functionality and scope.
- Some of the most important and widely used IoT standards are:

  - Bluetooth Smart: A low-power wireless technology that allows IoT devices to communicate with smartphones, tablets, and other Bluetooth-enabled devices. Bluetooth Smart supports various profiles, such as health, fitness, proximity, and smart home.
  - ULE: Ultra-low emission, a wireless technology that operates in the 1900 MHz frequency band and provides long-range, low-power, and secure communication for IoT devices. ULE is suitable for smart home, security, and healthcare applications.
  - IEEE 802.11ah: A Wi-Fi standard that operates in the sub-1 GHz frequency band and provides low-power, long-range, and high-density connectivity for IoT devices. IEEE 802.11ah supports various modes, such as station, access point, and relay, and can coexist with other Wi-Fi standards.
  - Thread: A mesh networking protocol that leverages IPv6 to enable secure, reliable, and scalable communication among IoT devices. Thread supports various application layers, such as CoAP, MQTT, and Zigbee, and can integrate with cloud services and smart phones.
  - IEEE P2413-2019: A standard for the architectural framework for the IoT, which defines various IoT domains, abstractions, and commonalities, and promotes cross-domain interaction, system interoperability, and functional compatibility. IEEE P2413-2019 conforms to the international standard ISO/IEC/IEEE 42010:2011 .
  - ISO/IEC 30141:2018: A standard for the IoT reference architecture, which provides a common vocabulary, reusable designs, and industry best practices. ISO/IEC 30141:2018 uses a top-down approach, starting from the most important characteristics of IoT, abstracting them into a generic IoT conceptual model, and deriving a high-level system based architecture.

- IoT standards are essential for the development, deployment, and management of IoT systems, as they enable interoperability, security, scalability, and quality of service among different IoT components and stakeholders.



### M2M and IoT Technology Fundamentals

- M2M stands for Machine-to-Machine communication, which is the exchange of data between devices without human intervention  .
- IoT stands for Internet of Things, which is the network of physical objects embedded with sensors, software and connectivity that enables data collection and analysis .
- M2M and IoT are related but not identical concepts. M2M is a subset of IoT, as IoT involves communication between machines without human input, making it by definition a form of M2M communication.
- However, IoT expands the power and potential of M2M technology in new ways. The biggest difference between M2M and IoT is that an M2M system uses point-to-point communication, while an IoT system typically situates its devices within a global cloud network that allows larger-scale integration and more sophisticated applications.
- Scalability is another key difference between M2M and IoT. M2M systems are often limited by the number of devices that can be connected and the bandwidth that can be used, while IoT systems can leverage the cloud and the internet to connect millions of devices and handle large amounts of data.
- M2M technology was first adopted in manufacturing and industrial settings, where other technologies, such as SCADA and remote monitoring, helped remotely manage and control data from equipment. M2M has since found applications in other sectors, such as healthcare, business and insurance.
- IoT technology emerged from the convergence of wireless technologies, micro-electromechanical systems (MEMS), microservices and the internet. IoT enables new possibilities for smart homes, smart cities, smart agriculture, smart healthcare and smart transportation.
- The basic process of how IoT works is as follows:
  - A group of physical devices is wired or wirelessly linked to each other and/or a central area.
  - The devices collect data from the external world using some kind of sensor.
  - That data is then stored somewhere, whether it be in the cloud, an intermediary network location, or on the device itself.
  - The data is then processed and analyzed using software, algorithms or artificial intelligence.
  - The data is then used to trigger some kind of action, such as sending a notification, adjusting a parameter, or controlling a device.
- M2M and IoT technologies have many benefits, such as improving efficiency, productivity, safety, security, convenience, and customer satisfaction. They also have some challenges, such as privacy, security, interoperability, standardization, and regulation.



### Devices and gateways

- Devices are the physical objects that are connected to the Internet of Things (IoT) network and can sense, actuate, communicate, and process data. Examples of devices are sensors, actuators, cameras, smart phones, smart watches, etc.
- Gateways are the central hubs that connect devices to the cloud and enable data transfer, protocol translation, data aggregation, security, and device management. Examples of gateways are routers, modems, edge servers, etc.
- The architecture of IoT gateways consists of the following components    :
  - Security: This is one of the most critical factors in an IoT gateway architecture throughout the design phase. It involves encryption, authentication, authorization, and firewall mechanisms to protect the data and devices from unauthorized access and cyberattacks.
  - Device layer: This is the hardware of an IoT infrastructure, which includes IoT sensors, protective circuits, networking modules, and a processor or microcontroller. The device layer is responsible for sensing, actuating, and communicating with the gateway and other devices.
  - Data management: This is the software that handles the data collected from the devices and prepares it for transmission to the cloud. It involves data filtering, compression, transformation, and validation.
  - Operating system: This is the software that runs the gateway hardware and other programs on the device. It provides an interface for the user and the applications, and manages the resources and processes of the gateway. Examples of operating systems for IoT gateways are Linux, Windows, Android, etc.
  - Hardware abstraction: This is the software that enables the gateway to communicate with different types of devices and sensors, regardless of their hardware specifications and communication protocols. It provides a common interface for the device layer and the gateway data transfer layer.
  - Gateway data transfer: This is the software that enables the gateway to send and receive data to and from the cloud and other gateways. It involves communication protocols, such as MQTT, CoAP, HTTP, etc., and data formats, such as JSON, XML, etc.
  - Communication protocols: These are the rules and standards that govern the data exchange between the devices, gateways, and the cloud. They define the syntax, semantics, and synchronization of the data. Examples of communication protocols for IoT are Bluetooth, Wi-Fi, Zigbee, LoRaWAN, etc.
  - Cloud connectivity manager: This is the software that manages the connection between the gateway and the cloud. It handles the authentication, authorization, encryption, and configuration of the cloud services and applications. It also monitors the status and performance of the gateway and the cloud.



Hello, I am Sydney, your AI assistant. I can help you with your topic of local and wide area networking. Here are some notes that you can use for your study material:

### Local and wide area networking

- A **local area network (LAN)** is a computer network that interconnects computers within a limited area such as a residence, school, laboratory, university campus or office building .
- A **wide area network (WAN)** is a computer network that covers a larger geographic distance, such as a city, a country or the world, and generally involves leased telecommunication circuits .
- The main differences between LAN and WAN are:
  - **Size**: LANs are smaller and have a limited number of devices, while WANs are larger and can connect multiple LANs or other networks .
  - **Speed**: LANs have higher bandwidth and faster data transmission than WANs, due to the shorter distance and lower interference .
  - **Cost**: LANs are cheaper and easier to set up and maintain than WANs, as they use less expensive hardware and software, and do not require leased lines or routers .
  - **Security**: LANs are more secure and reliable than WANs, as they have less exposure to external threats and errors, and can use encryption and firewalls to protect data .
- The main advantages of LAN and WAN are:
  - **LAN**: LANs allow users to share resources, such as printers, scanners, files and applications, within a local network, and to communicate and collaborate with each other . LANs also provide faster and more consistent access to data and services than WANs.
  - **WAN**: WANs enable users to access remote resources, such as websites, databases, cloud services and other networks, across a wide geographic area, and to communicate and collaborate with users in different locations . WANs also provide more scalability and flexibility than LANs, as they can connect multiple networks and devices.
- The main challenges of LAN and WAN are:
  - **LAN**: LANs have limited scalability and mobility, as they can only accommodate a certain number of devices and users within a fixed area, and require physical connections or wireless access points . LANs also have higher risk of congestion and collision, as they use a shared medium for data transmission, such as Ethernet or Wi-Fi .
  - **WAN**: WANs have higher cost and complexity, as they require expensive and sophisticated hardware and software, such as routers, switches, modems and protocols, to establish and maintain connections between networks . WANs also have lower security and reliability, as they are more vulnerable to external threats and errors, such as hackers, viruses, power outages and natural disasters .
- The main technologies and protocols used for LAN and WAN are:
  - **LAN**: LANs use technologies such as Ethernet, Wi-Fi, Bluetooth and Powerline, and protocols such as TCP/IP, UDP, ARP, DHCP and DNS, to enable data transmission and communication within a local network .
  - **WAN**: WANs use technologies such as DSL, cable, fiber optic, satellite and cellular, and protocols such as TCP/IP, UDP, ICMP, BGP and MPLS, to enable data transmission and communication across a wide area network  .



Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of data management for the unit 1 - IoT-An Architectural Overview in the subject of IoT Architecture and Protocols. Here is a summary of the main points:

- Data management is the process of collecting, storing, processing, and analyzing data from IoT devices and applications.
- Data management challenges in IoT include:
  - Data volume: IoT devices generate large amounts of data, which require scalable and efficient storage and processing solutions.
  - Data variety: IoT data can be structured, semi-structured, or unstructured, and can come from different sources, formats, and types, which require interoperable and flexible data models and schemas.
  - Data velocity: IoT data can be generated at high rates and in real-time, which require low-latency and high-throughput data processing and analytics solutions.
  - Data veracity: IoT data can be noisy, incomplete, inconsistent, or inaccurate, which require data quality and integrity techniques and methods.
  - Data value: IoT data can provide valuable insights and information for decision making and optimization, which require data mining and machine learning techniques and methods.
- Data management solutions in IoT include:
  - Data storage: IoT data can be stored in different types of databases, such as relational, NoSQL, or NewSQL, depending on the data characteristics and requirements. IoT data can also be stored in different locations, such as edge, fog, or cloud, depending on the network and latency constraints and trade-offs.
  - Data processing: IoT data can be processed in different ways, such as batch, stream, or hybrid, depending on the data velocity and timeliness requirements. IoT data can also be processed in different locations, such as edge, fog, or cloud, depending on the computation and communication resources and trade-offs.
  - Data analytics: IoT data can be analyzed using different techniques and methods, such as descriptive, predictive, or prescriptive, depending on the data value and objectives. IoT data can also be analyzed using different tools and frameworks, such as Hadoop, Spark, or TensorFlow, depending on the data complexity and scalability requirements.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of business processes in IoT:

### Business processes in IoT

- A business process is a collection of related events, activities and decisions that involve a number of factors and resources, which collectively lead to an outcome that is of value for the organisation and the customer.
- IoT (Internet of Things) is the network of physical objects embedded with sensors, software and other technologies that enable them to connect and exchange data with other devices and systems over the internet.
- IoT can improve business processes by automating, optimizing, extending, triggering, sourcing and transforming them, depending on the problem to be solved and the objective to be achieved.
- Some examples of IoT business processes are:
  - Smart manufacturing: IoT devices can monitor and control the production process, collect data for quality assurance, enable predictive maintenance, reduce waste and energy consumption, and improve safety and efficiency.
  - Smart logistics: IoT devices can track and trace the location and condition of goods, vehicles and containers, optimize routes and schedules, reduce costs and risks, and enhance customer satisfaction.
  - Smart home: IoT devices can automate and personalize the functions of household appliances, lighting, heating, security and entertainment systems, provide remote access and control, and save energy and money.
- Some recommendations on implementing IoT business processes are:
  - To define the business process to improve and identify the problem to be solved and the value to be delivered.
  - To use an end-to-end approach that covers the entire lifecycle of the IoT solution, from design and development to deployment and maintenance.
  - To make agile design and start with POC (proof of concept) prototyping to test the feasibility and viability of the IoT solution.
  - To get on board the right people, better if you keep it low but with the best knowledge, skills and experience, and foster collaboration and communication among them.
  - To be persistent but acknowledgeable to failure, and learn from the feedback and data collected from the IoT solution.
  - To be aware of the potential disruption that IoT can bring to the existing business models, processes and culture, but don't go crazy about it, and instead embrace the opportunities and challenges.



### Everything as a Service (XaaS) for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Everything as a Service (XaaS) is a general term that describes the delivery of any IT function as a service over the internet, using cloud computing and remote access technologies  .
- XaaS originated from the Software as a Service (SaaS) model, which provides software applications on demand, without requiring installation or maintenance on the user's device .
- XaaS has expanded to include other types of services, such as Infrastructure as a Service (IaaS), which provides computing resources such as servers, storage, and networks; Platform as a Service (PaaS), which provides development and deployment tools and environments; and more functionally-specific models, such as Storage as a Service, Desktop as a Service, and Disaster Recovery as a Service  .
- XaaS enables users to access and consume IT services on demand, without having to invest in or manage the underlying infrastructure or software  .
- XaaS offers benefits such as scalability, flexibility, cost-efficiency, innovation, and agility for both providers and consumers of IT services     .
- XaaS also poses challenges such as security, privacy, reliability, integration, and governance for both providers and consumers of IT services     .
- XaaS is closely related to the Internet of Things (IoT), which is the network of physical devices, sensors, and actuators that can communicate and exchange data over the internet.
- XaaS can enable IoT devices to access and leverage cloud-based services, such as data analytics, artificial intelligence, and machine learning, to enhance their functionality and value .
- XaaS can also enable IoT devices to offer their own services to other devices or users, such as sensor data, device control, or device status .
- XaaS and IoT can create new opportunities and challenges for businesses and consumers, such as new business models, revenue streams, customer experiences, and security risks  .



### M2M and IoT Analytics

- M2M and IoT are both technologies that enable remote communication and data exchange among machines without human intervention.
- M2M stands for Machine-to-Machine, and IoT stands for Internet of Things.
- The main difference between M2M and IoT is the type and scope of the connection.
  - M2M is a point-to-point connection between two or more devices over cellular or wired networks. M2M is usually a vertical application that meets internal demands, such as monitoring, control, or automation.
  - IoT is a network of devices that connect to the Internet for better performance, interoperability, and scalability. IoT is usually a horizontal application that has overarching results or open-ended capabilities, such as smart cities, smart homes, or smart health.
- M2M and IoT analytics are the processes of collecting, processing, and analyzing the data generated by M2M and IoT devices, respectively.
- M2M and IoT analytics have different purposes and challenges.
  - M2M analytics aims to optimize the performance, efficiency, and reliability of the connected devices and systems. M2M analytics faces challenges such as data volume, variety, and velocity, as well as security and privacy issues.
  - IoT analytics aims to create value, insights, and opportunities from the data collected by the IoT devices and platforms. IoT analytics faces challenges such as data integration, quality, and governance, as well as scalability and complexity issues.



### Knowledge Management for the notes of the Unit 1 - IoT-An Architectural Overview

- Knowledge management (KM) is the process of creating, sharing, using and managing the knowledge and information of an organization.
- KM can help organizations leverage their data and information assets to improve decision making, innovation, collaboration and performance.
- IoT is a network of physical objects embedded with sensors, actuators, software and connectivity that enable data exchange and interaction with other devices, systems and humans.
- IoT can enhance KM by providing new sources of data, enabling real-time monitoring and feedback, facilitating knowledge creation and dissemination, and supporting open and collaborative ecosystems  .
- IoT architecture consists of four main layers: device layer, network layer, service layer and application layer.
- Device layer includes the physical objects that are equipped with sensing, computing and communication capabilities, such as sensors, actuators, RFID tags, smartphones, etc.
- Network layer provides the connectivity and communication protocols for data transmission and routing, such as Wi-Fi, Bluetooth, ZigBee, 5G, etc.
- Service layer offers the functionalities and services for data processing, storage, analysis and management, such as cloud computing, edge computing, big data, artificial intelligence, etc.
- Application layer delivers the end-user applications and solutions that utilize the data and services from the lower layers, such as smart home, smart city, smart health, smart agriculture, etc.



## Unit 2 - Reference Architecture

- A reference architecture is a general and reusable solution to a commonly occurring problem in a specific domain or context.
- It provides a set of principles, guidelines, standards, patterns, and best practices for designing, implementing, and managing a system or a subsystem.
- It also defines the key components, interfaces, relationships, and interactions among them, as well as the non-functional requirements and quality attributes of the system or subsystem.
- A reference architecture is not a complete and detailed design, but rather a blueprint or a template that can be instantiated and customized for a specific system or subsystem.
- A reference architecture can be used for various purposes, such as:
  - Communicating and aligning the vision and goals of the system or subsystem among different stakeholders.
  - Providing a common vocabulary and terminology for the system or subsystem domain or context.
  - Establishing a baseline for evaluating and comparing different design alternatives and trade-offs.
  - Facilitating reuse and interoperability of components and services across different systems or subsystems.
  - Enhancing the quality, consistency, and maintainability of the system or subsystem.
  - Accelerating the development and deployment of the system or subsystem by reducing the complexity and uncertainty.
- A reference architecture can be represented in different ways, such as:
  - A conceptual model that shows the high-level concepts and abstractions of the system or subsystem domain or context.
  - A logical model that shows the functional and structural decomposition of the system or subsystem into components and interfaces.
  - A physical model that shows the mapping of the components and interfaces to the hardware and software platforms and technologies.
  - A deployment model that shows the distribution and configuration of the components and interfaces across the network and the environment.
  - A view model that shows the different perspectives and concerns of the system or subsystem, such as the functional, behavioral, informational, operational, developmental, and quality aspects.



### IoT Architecture-State of the Art

- A reference model is a model that describes the main conceptual entities and how they are related to each other, while the reference architecture aims at describing the main functional components of a system as well as how the system works, how the system is deployed, what information the system processes, etc.
- The principles of Reactive Systems define the state-of-the-art programming models for IoT. Because IoT devices are sensing and actuating physical systems, many of which are critical infrastructure for energy, food, healthcare, and transportation, it is important that they stay responsive, and operate safely and securely.
- IoT platforms must tackle asset management as a foundational problem and all of these platforms have facilities for managing the provisioning of devices and services, public key infrastructure (PKI), software and firmware updates, and desired-state configuration of devices, at huge scale.
- The paper will address the topic of IoT, the state of the art of IoT, and how IoT is used for fog, in 6G, and cloud computing. It surveys IoT architecture and sensors used in development and security together with their potential applications, such as system tuning and diagnosis.
- Internet of things (IoT) constitutes one of the most important technological development in the last decade. It has the potential to deeply affect our life style. However, its success relies greatly on a well-defined architecture that will provide scalable, dynamic, and secure basement to its deployment.



### Introduction

- In this unit, we will learn about the reference architecture for the Internet of Things (IoT), which is a conceptual framework that defines the components, interfaces, and interactions of an IoT system.
- A reference architecture provides a common vocabulary, a set of principles and best practices, and a logical structure for designing and implementing IoT solutions.
- A reference architecture can also facilitate interoperability, scalability, security, and manageability of IoT systems, as well as support innovation and evolution of IoT technologies and applications.
- There are different reference architectures proposed by various organizations and standardization bodies for the IoT, such as the IoT-A, the IEEE P2413, the oneM2M, and the IIC.
- In this unit, we will focus on the IoT-A reference architecture, which is one of the most comprehensive and widely adopted reference architectures for the IoT.
- The IoT-A reference architecture was developed by the IoT-Architecture (IoT-A) project, which was a European research project funded by the European Commission under the Seventh Framework Programme (FP7).
- The IoT-A project aimed to create a unified architectural reference model for the IoT, along with the definition of an initial set of key building blocks.
- The IoT-A reference architecture consists of three main layers: the Device Layer, the Network Layer, and the Application Layer, as well as two cross-cutting functions: the Management and Security Functions.
- The Device Layer comprises the physical devices and gateways that are connected to the IoT system, and provides the sensing, actuation, and communication capabilities.
- The Network Layer provides the connectivity and data transmission between the devices and the applications, and supports various communication protocols and technologies.
- The Application Layer provides the logic and functionality of the IoT system, and supports various application domains and services.
- The Management Function provides the mechanisms for configuring, monitoring, and controlling the IoT system, and supports various management tasks and policies.
- The Security Function provides the mechanisms for ensuring the confidentiality, integrity, and availability of the IoT system, and supports various security requirements and solutions.



### State of the art for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- A reference model is a model that describes the main conceptual entities and how they are related to each other .
- A reference architecture aims at describing the main functional components of a system as well as how the system works, how the system is deployed, what information the system processes, etc .
- A reference architecture can be derived from a reference model by adding more details and specifications.
- A reference architecture can also be used as a blueprint or a guideline for designing and implementing specific IoT systems.
- There are different approaches to define a reference architecture for IoT, depending on the scope, the objectives, the requirements, and the challenges of the IoT domain.
- Some of the common elements or layers that are often found in IoT reference architectures are:
  - Device layer: This layer consists of the physical devices or things that are connected to the internet, such as sensors, actuators, smart objects, etc. This layer is responsible for sensing, actuating, and communicating with the other layers.
  - Network layer: This layer provides the connectivity and the communication protocols between the devices and the other layers. This layer can use different technologies, such as wired, wireless, cellular, satellite, etc.
  - Middleware layer: This layer provides the services and the functionalities that enable the integration, the interoperability, the management, and the security of the devices and the data. This layer can include components such as data processing, data storage, data analytics, device management, service discovery, service orchestration, etc.
  - Application layer: This layer provides the end-user applications and the business logic that use the data and the services from the middleware layer. This layer can include components such as user interfaces, dashboards, decision support systems, etc.
- Some of the examples of IoT reference architectures are:
  - The IoT-A reference architecture: This is a European project that aims to provide a comprehensive and coherent reference architecture for IoT. It defines a set of architectural principles, a reference model, and a reference architecture framework for IoT.
  - The IEEE P2413 reference architecture: This is an ongoing standardization project that aims to provide a common framework and a reference architecture for IoT. It defines a set of architectural building blocks, a reference model, and a reference architecture for IoT.
  - The oneM2M reference architecture: This is a global initiative that aims to provide a common platform and a reference architecture for IoT. It defines a set of functional entities, a reference model, and a reference architecture for IoT.
- The state of the art for IoT is constantly evolving and improving, as new technologies, paradigms, and challenges emerge in the IoT domain .
- Some of the current trends and directions for IoT are :
  - Reactive systems: These are systems that are responsive, resilient, elastic, and message-driven. They can handle the complexity, the uncertainty, and the dynamism of IoT systems. They can also leverage the distributed and parallel computing capabilities of IoT devices.
  - Fog computing: This is a paradigm that extends the cloud computing to the edge of the network, where the IoT devices are located. It enables the processing, the storage, and the analysis of the data closer to the source, reducing the latency, the bandwidth, and the energy consumption. It also enhances the privacy, the security, and the scalability of IoT systems.
  - 6G networks: These are the next generation of wireless networks that will provide ultra-high speed, ultra-low latency, ultra-high reliability, and ultra-high capacity for IoT systems. They will also enable new applications and services, such as holographic communications, immersive virtual reality, and tactile internet.



### Reference Model and Architecture for IoT

- A reference model is a conceptual framework that defines the common terminology, concepts, and principles for designing and implementing IoT systems.
- A reference architecture is a concrete instantiation of a reference model that provides specific guidelines, best practices, and standards for building IoT solutions.
- One of the most widely used reference models for IoT is the IoT World Forum Reference Model, which was developed by the IoT World Forum, a consortium of industry leaders, academia, and government organizations.
- The IoT World Forum Reference Model consists of seven layers, as shown in the following diagram:

IoT World Forum Reference Model

- The seven layers are:

  - **Physical devices and controllers layer**: This layer includes the physical devices, sensors, actuators, and controllers that interact with the physical world and generate data.
  - **Connectivity layer**: This layer provides the communication protocols, standards, and technologies for connecting the devices and controllers to the network.
  - **Edge computing layer**: This layer performs data processing, filtering, aggregation, and analysis at the edge of the network, close to the devices, to reduce latency, bandwidth, and storage requirements.
  - **Data accumulation layer**: This layer collects, stores, and manages the data from the edge computing layer and other sources, such as cloud services, enterprise systems, and external APIs.
  - **Data abstraction layer**: This layer provides data normalization, transformation, and integration services to enable interoperability and data exchange among different applications and systems.
  - **Application layer**: This layer provides the business logic, functionality, and user interface for the IoT solutions, such as monitoring, control, analytics, and visualization.
  - **Collaboration and processes layer**: This layer enables collaboration and coordination among different stakeholders, such as users, devices, systems, and organizations, and supports business processes and workflows for the IoT solutions.

- The IoT World Forum Reference Model is not the only reference model for IoT, but it is a useful starting point for understanding the key components and challenges of IoT systems.
- Other reference models and architectures for IoT include:

  - **IoT-Architectural Reference Model (IoT-ARM)**: This is a comprehensive reference model developed by the IoT-A project, a European research initiative funded by the European Commission. It provides a common vocabulary, a domain model, a functional model, a communication model, a deployment and lifecycle model, and a security and privacy model for IoT systems. 
  - **IBM Cloud IoT Reference Architecture**: This is a reference architecture developed by IBM that leverages the IBM Cloud platform and services to provide a scalable, secure, and reliable IoT solution. It consists of four layers: devices, gateways, cloud, and applications. 
  - **Azure IoT Reference Architecture**: This is a reference architecture developed by Microsoft that leverages the Azure platform and services to provide a customizable and flexible IoT solution. It consists of five components: devices, IoT Hub, IoT Device Provisioning Service, Stream Analytics, and Digital Twins.



### IoT Reference Model

The IoT Reference Model is a framework that defines the main concepts and components of IoT systems and architectures. It provides a common language and understanding for IoT domains and applications. The IoT Reference Model consists of the following sub-models:

- **IoT Domain Model**: This model introduces the basic concepts of IoT, such as devices, IoT services, virtual entities, and their relations. A device is a physical object that can sense, actuate, or communicate. An IoT service is a software component that provides functionality or data to other entities. A virtual entity is a digital representation of a device, a group of devices, or a physical or logical entity that is not a device. A virtual entity can have properties, states, and behaviors that reflect the real-world entity it represents.

- **IoT Functional View**: This model describes the main functions and processes that are performed by IoT systems, such as device management, data processing, service discovery, service composition, and security. The model also defines the functional components that implement these functions, such as gateways, brokers, repositories, and orchestrators. The model shows how these components interact and exchange information through interfaces and protocols.

- **IoT Information View**: This model defines the information and data models that are used by IoT systems, such as device descriptions, service descriptions, virtual entity descriptions, and event models. The model also specifies the syntax and semantics of these models, as well as the methods and standards for data representation and exchange.

- **IoT Deployment and Operational View**: This model describes the physical and logical deployment of IoT systems, such as the network topology, the device location, the communication infrastructure, and the cloud services. The model also covers the operational aspects of IoT systems, such as the configuration, monitoring, maintenance, and troubleshooting of IoT components and services.

- **IoT User View**: This model defines the user roles and interactions with IoT systems, such as the end users, the application developers, the system administrators, and the service providers. The model also describes the user interfaces and applications that enable these interactions, such as web portals, mobile apps, dashboards, and APIs.

The IoT Reference Model is not a prescriptive or normative architecture, but rather a conceptual and descriptive framework that can be used as a basis for designing and developing IoT systems and architectures. The IoT Reference Model can be adapted and extended to suit different IoT domains and applications, such as smart cities, smart homes, smart health, and smart industry. The IoT Reference Model can also be aligned and integrated with other reference models and standards, such as the ISO/IEC 30141 IoT Reference Architecture, the ITU-T Y.2060 IoT Overview, and the IEEE P2413 IoT Architecture Framework.



### IoT Reference Architecture

- IoT reference architecture is a conceptual framework that defines the components, interactions, and principles of an IoT solution.
- IoT reference architecture can help to guide the design, development, and deployment of IoT solutions that are scalable, secure, interoperable, and adaptable to different domains and use cases.
- IoT reference architecture can also facilitate the communication and collaboration among different stakeholders, such as developers, vendors, customers, and regulators, by providing a common vocabulary and understanding of IoT concepts and systems.
- There are different IoT reference architectures proposed by various organizations, such as IBM, Microsoft, and the IoT-A project, which have different levels of abstraction, granularity, and scope.
- However, most IoT reference architectures share some common elements, such as:

  - Things: The physical or virtual entities that generate, consume, or exchange data in an IoT solution. Things can be devices, sensors, actuators, gateways, or software agents.
  - Communication: The protocols, standards, and technologies that enable the data transmission and exchange among things, networks, and platforms in an IoT solution. Communication can be wired or wireless, and can use different technologies, such as MQTT, CoAP, HTTP, Bluetooth, ZigBee, or cellular.
  - Platforms: The software and hardware components that provide the core functionalities and services of an IoT solution, such as data ingestion, processing, storage, analysis, visualization, and management. Platforms can be cloud-based or on-premises, and can use different technologies, such as IBM Watson IoT, Microsoft Azure IoT, or AWS IoT.
  - Applications: The software components that provide the specific business logic and user interface of an IoT solution, such as monitoring, control, automation, or optimization. Applications can be web-based, mobile-based, or desktop-based, and can use different technologies, such as Node.js, Python, or Java.
  - Security: The mechanisms, policies, and practices that ensure the confidentiality, integrity, and availability of the data and resources in an IoT solution. Security can involve different aspects, such as authentication, authorization, encryption, auditing, or anomaly detection.
  - Governance: The rules, standards, and regulations that define the roles, responsibilities, and accountability of the stakeholders in an IoT solution. Governance can involve different aspects, such as data ownership, privacy, quality, compliance, or ethics.

- The following diagram shows an example of an IoT reference architecture based on the IBM Cloud Architecture:

IoT reference architecture diagram

- The diagram illustrates the main components and interactions of an IoT solution, such as:

  - Things: The devices and sensors that generate data and send it to the IoT platform via the communication network.
  - Communication: The network that connects the things to the IoT platform, which can use different protocols and technologies, such as MQTT, HTTP, or cellular.
  - Platforms: The IoT platform that provides the core services and functionalities of the IoT solution, such as data ingestion, processing, storage, analysis, visualization, and management. The IoT platform can also integrate with other cloud services, such as data and AI services, to enhance the capabilities and value of the IoT solution.
  - Applications: The applications that provide the specific business logic and user interface of the IoT solution, such as monitoring, control, automation, or optimization. The applications can access the data and services from the IoT platform via APIs or SDKs, and can also interact with the things via commands or actions.
  - Security: The security mechanisms that ensure the protection and privacy of the data and resources in the IoT solution, such as encryption, authentication, authorization, or auditing.
  - Governance: The governance rules and standards that define the data ownership, quality, compliance, and ethics of the IoT solution, such as GDPR, ISO, or NIST.



### Introduction

- Internet of Things (IoT) is a network of physical objects or things that are embedded with sensors, actuators, and communication devices to interact with each other and exchange data.
- IoT enables various applications such as smart homes, smart cities, smart health, smart agriculture, smart industry, and smart environment.
- IoT architecture is the design of the system that defines how the IoT components interact and communicate with each other and with other systems or services.
- IoT architecture consists of four main layers: perception layer, network layer, middleware layer, and application layer.
- Perception layer is responsible for sensing the physical world and collecting data from the devices or things.
- Network layer is responsible for transmitting the data from the perception layer to the middleware layer or vice versa, using various wired or wireless technologies such as Wi-Fi, Bluetooth, ZigBee, cellular, etc.
- Middleware layer is responsible for processing, storing, and managing the data from the network layer, and providing services such as data analysis, data fusion, data security, data privacy, etc.
- Application layer is responsible for providing the end-user services or applications based on the data from the middleware layer, such as smart home control, smart health monitoring, smart city management, etc.
- IoT reference architecture is a generic or abstract model that describes the common features and functions of IoT systems, and provides a common vocabulary and framework for designing and developing IoT solutions.
- IoT reference architecture can help to address the challenges and requirements of IoT such as interoperability, scalability, security, privacy, reliability, etc.
- IoT reference architecture can also help to identify the best practices, standards, and guidelines for IoT development and deployment.
- There are various IoT reference architectures proposed by different organizations or initiatives, such as ISO/IEC 30141, ITU-T Y.2060, IEEE P2413, IIC, oneM2M, etc.
- Each IoT reference architecture may have different perspectives, scopes, and levels of detail, but they share some common elements and principles.



### Functional View

The functional view of the IoT reference architecture describes the system's runtime functional components, their responsibilities, default functions, interfaces and primary interactions. The functional view follows the modular structure of functional blocks organized into layers, as it was proposed e.g. in SENSEI.

The functional view consists of the following layers:

- **Device Layer**: This layer contains the physical devices that are connected to the IoT system, such as sensors, actuators, gateways, etc. The device layer is responsible for providing data acquisition, data processing, data storage, data transmission and device management functions.
- **Network Layer**: This layer provides the communication infrastructure and protocols for the IoT system, such as wired or wireless networks, routing, addressing, security, etc. The network layer is responsible for enabling data exchange, data aggregation, data filtering, data compression and network management functions.
- **Service Layer**: This layer provides the application logic and services for the IoT system, such as data analysis, data visualization, data fusion, data mining, etc. The service layer is responsible for providing data processing, data presentation, data interpretation and service management functions.
- **Business Layer**: This layer provides the business value and goals for the IoT system, such as business processes, business rules, business models, etc. The business layer is responsible for providing business intelligence, business optimization, business innovation and business governance functions.

The functional view also defines the cross-layer functions that span across multiple layers, such as security, privacy, trust, identity, discovery, etc. These functions are responsible for ensuring the quality, reliability, interoperability and scalability of the IoT system.

The functional view can be represented by the following diagram:

```
+-----------------+
|  Business Layer |
+-----------------+
|  Service Layer  |
+-----------------+
|  Network Layer  |
+-----------------+
|  Device Layer   |
+-----------------+
```



### Information View for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The information view describes the data and information that the system handles, such as the types, formats, sources, destinations, flows, and transformations of data.
- The information view can be used to identify the data requirements, data models, data quality, data security, and data governance of the IoT system.
- The information view can also help to design the data storage, processing, and analytics components of the IoT system, such as databases, data lakes, data warehouses, data pipelines, and data visualization tools.
- The information view can be represented by different diagrams, such as data flow diagrams, entity-relationship diagrams, logical data models, physical data models, and data dictionaries.
- The information view can be aligned with the functional view and the deployment view of the IoT reference architecture, which describe the system's functions and components, and how they are deployed and connected, respectively.
- The information view can vary depending on the use case and application of the IoT system, such as smart home, smart city, smart manufacturing, smart agriculture, etc. Different use cases and applications may have different data sources, data types, data formats, data flows, and data analytics needs.



### Deployment and Operational View

- The deployment and operational view describes the main real world components of the system such as devices, network routers, servers, etc. and how they are deployed and operated .
- The deployment view focuses on the physical layout and distribution of the components, such as the location, connectivity, and configuration of the devices and servers .
- The operational view focuses on the runtime behavior and management of the components, such as the data flow, communication protocols, security mechanisms, and monitoring tools .
- The deployment and operational view can vary depending on the specific domain and use case of the IoT system, but there are some common aspects that are covered in the IoT Reference Architecture, such as:
  - Device layer: The lowest layer that consists of the sensors, actuators, and embedded devices that interact with the physical world and collect data .
  - Communication layer: The layer that provides the network infrastructure and protocols for transmitting data between the devices and the servers .
  - Semantic layer: The layer that provides the data models, ontologies, and standards for representing and interpreting the data from the devices .
  - Application layer: The highest layer that consists of the software applications and services that process, analyze, and visualize the data from the devices and provide value-added functionality to the users .
- The deployment and operational view can also address the non-functional requirements of the IoT system, such as scalability, reliability, availability, performance, security, and privacy .



### Other Relevant Architectural Views for IoT

- Apart from the functional view, which describes the components and interactions of an IoT system, there are other views that can help to understand and design IoT systems from different perspectives.
- Some of the other relevant architectural views for IoT are    :

  - **Device view**: This view focuses on the characteristics and capabilities of the IoT devices, such as sensors, actuators, gateways, and embedded systems. It also considers the device management, security, and communication aspects of the devices.
  - **Data view**: This view deals with the data generated, collected, processed, and stored by the IoT system. It includes the data models, formats, protocols, standards, and analytics techniques used to handle the data. It also addresses the data quality, privacy, and governance issues.
  - **Service view**: This view describes the services offered by the IoT system to the users and other systems. It includes the service discovery, composition, orchestration, and delivery mechanisms, as well as the service level agreements, quality of service, and billing models.
  - **Business view**: This view captures the business goals, value propositions, and stakeholders of the IoT system. It also includes the business processes, models, and rules that govern the operation and evolution of the system.
  - **Security view**: This view covers the security requirements, threats, risks, and countermeasures of the IoT system. It includes the security policies, standards, and best practices, as well as the security architectures, mechanisms, and tools used to protect the system.
  - **User view**: This view represents the user needs, preferences, and expectations of the IoT system. It also includes the user interface, interaction, and experience design, as well as the user feedback and evaluation methods.



### Real-World Design Constraints for IoT Systems

- IoT systems are composed of devices, networks, data, and applications that interact with each other and the physical world.
- IoT systems face various design constraints that affect their functionality, performance, security, and scalability.
- Some of the common design constraints for IoT systems are:

  - **Power consumption**: IoT devices often operate on batteries or harvested energy sources, and need to conserve power as much as possible. This limits the amount of computation, communication, and sensing they can perform, and requires efficient power management techniques .
  - **Hardware capabilities**: IoT devices have limited memory, CPU, and flash storage, which restricts the complexity and size of the software they can run. This also affects the security and update mechanisms they can support .
  - **Network connectivity**: IoT devices have slow, intermittent, and unreliable network connections, which affects the quality and availability of the data they transmit and receive. This also poses challenges for synchronization, coordination, and authentication among devices .
  - **Time accuracy**: IoT devices need to have accurate and consistent time information to perform tasks such as data logging, event detection, and scheduling. However, IoT devices may not have access to reliable time sources or synchronization protocols, and may experience clock drifts due to environmental factors .
  - **Update costs**: IoT devices need to be updated regularly to fix bugs, improve performance, and add new features. However, updating IoT devices can be expensive, risky, and difficult, especially when they are deployed in remote or inaccessible locations. Failed updates can result in device malfunction, data loss, or security breaches .
  - **System complexity**: IoT systems involve multiple layers of hardware, software, and protocols, which increase the complexity and heterogeneity of the system. This makes it harder to design, test, debug, and maintain IoT systems, and requires interoperability and standardization among different components  .



### Introduction

- In this unit, we will learn about the reference architecture for the Internet of Things (IoT), which is a conceptual framework that defines the key components and interactions of an IoT system.
- A reference architecture provides a common vocabulary, a set of principles and best practices, and a logical structure for designing and implementing IoT solutions.
- A reference architecture can also facilitate interoperability, scalability, security, and manageability of IoT systems, as well as enable innovation and evolution of IoT technologies and applications.
- There are different reference architectures proposed by various organizations and standards bodies, such as the IoT-Architecture (IoT-A) project, the IEEE P2413 standard, the Industrial Internet Consortium (IIC), and the OpenFog Consortium.
- In this unit, we will focus on the IoT-A reference architecture, which is one of the most comprehensive and widely adopted reference architectures for IoT.
- The IoT-A reference architecture consists of three main layers: the device layer, the network layer, and the service layer, as shown in the following diagram:

IoT-A reference architecture

- The device layer includes the physical and virtual devices that generate, process, and consume data in an IoT system, such as sensors, actuators, gateways, and smart objects.
- The network layer provides the communication and connectivity infrastructure for the IoT system, such as wired and wireless networks, protocols, and standards.
- The service layer provides the functionality and intelligence for the IoT system, such as data management, analytics, security, and application services.
- The IoT-A reference architecture also defines the functional, information, communication, and trust models for the IoT system, as well as the cross-layer aspects, such as security, privacy, and quality of service.
- In the following sections, we will discuss each of these components and models in more detail.



### Technical Design Constraints for Hardware in IoT

- Hardware design for IoT involves creating embedded systems that can communicate with other devices and networks securely and efficiently.
- Embedded systems are devices that have a microcontroller or microprocessor, memory, input/output interfaces, and software that perform a specific function.
- Embedded systems face several challenges and constraints in IoT applications, such as:

  - Lack of flexibility: Embedded systems have limited resources and capabilities, and may not be able to run complex applications or support multiple protocols. They may also have fixed functionality and cannot be easily updated or modified.
  - Security risks: Embedded systems are vulnerable to physical attacks, tampering, reverse engineering, and cyberattacks. They need to implement encryption, authentication, and integrity mechanisms to protect data and communication. They also need to comply with privacy and regulatory standards.
  - Power consumption: Embedded systems often operate on batteries or harvested energy, and need to minimize power consumption and maximize battery life. They need to use low-power components, optimize software, and implement power management techniques such as sleep modes, duty cycling, and adaptive transmission.
  - Testing and debugging: Embedded systems are difficult to test and debug, as they may have limited or no user interfaces, and may be deployed in remote or inaccessible locations. They need to use simulation tools, debugging hardware, and logging mechanisms to verify and troubleshoot their functionality and performance.
  - Functional safety: Embedded systems may be used in safety-critical applications, such as medical devices, automotive systems, or industrial control systems. They need to ensure that they can perform their functions correctly and reliably, and prevent or mitigate any failures or hazards. They need to follow safety standards and guidelines, and use fault-tolerance and redundancy techniques.
  - Cost and time-to-market: Embedded systems need to be designed and developed within a budget and a deadline, and meet the customer and market requirements. They need to use cost-effective components, modular and reusable design, and agile and iterative development processes.



### Data representation and visualization for IoT

- Data representation and visualization are the processes of transforming raw data from IoT devices into meaningful and useful information for human consumption .
- Data representation and visualization can help IoT users and stakeholders to understand, analyze, and communicate the patterns, trends, and insights derived from the data .
- Data representation and visualization can also enable IoT users and stakeholders to monitor and control the IoT devices and systems in real-time, and to make informed decisions and actions based on the data .
- Data representation and visualization for IoT can be achieved by using various tools and techniques, such as:
  - IoT dashboards: These are web-based applications that collect, process, and display data from IoT devices in the form of charts, graphs, maps, tables, etc. IoT dashboards can be customized to suit different user needs and preferences, and can provide interactive and dynamic features, such as filtering, sorting, zooming, etc. IoT dashboards can also support alerts, notifications, and commands for IoT devices   .
  - IoT data platforms: These are cloud-based services that provide data ingestion, storage, processing, analysis, and visualization capabilities for IoT data. IoT data platforms can handle large volumes and varieties of data from multiple sources, and can provide scalable and reliable performance. IoT data platforms can also integrate with various data analytics and visualization tools, such as Amazon Kinesis Analytics and Amazon QuickSight.
  - IoT data visualization libraries and frameworks: These are software components that provide data visualization functionalities for IoT applications. IoT data visualization libraries and frameworks can support various types of data visualization, such as line charts, bar charts, pie charts, scatter plots, heat maps, etc. IoT data visualization libraries and frameworks can also support various data formats, such as JSON, CSV, XML, etc. Some examples of IoT data visualization libraries and frameworks are D3.js, Chart.js, Highcharts, etc.
- Data representation and visualization for IoT can face some challenges, such as:
  - Data quality and accuracy: IoT data can be noisy, incomplete, inconsistent, or erroneous, which can affect the quality and accuracy of the data representation and visualization. IoT data quality and accuracy can be improved by using data cleaning, validation, and verification techniques, such as outlier detection, missing value imputation, data normalization, etc .
  - Data security and privacy: IoT data can contain sensitive or personal information, which can pose risks of data breaches, leaks, or misuse. IoT data security and privacy can be enhanced by using data encryption, authentication, authorization, and anonymization techniques, such as SSL/TLS, OAuth, JWT, k-anonymity, etc .
  - Data complexity and diversity: IoT data can be complex and diverse, as it can come from various types and sources of IoT devices, and can have different formats, structures, and semantics. IoT data complexity and diversity can be managed by using data integration, transformation, and standardization techniques, such as ETL, MQTT, CoAP, etc .



### Interaction and Remote Control for the Notes of the Unit 2 - Reference Architecture in the Subject of IoT Architecture and Protocols

- Interaction and remote control are essential aspects of IoT systems that enable users, service providers, and product support teams to access, monitor, and configure IoT devices from different locations and platforms.
- Interaction and remote control can be achieved through various methods, such as:
  - Mobile applications and web browsers that provide graphical user interfaces (GUIs) for users to interact with IoT devices and services .
  - Embedded touchscreens and buttons that allow users to control IoT devices locally.
  - Secure shell (SSH) connections that enable remote access to IoT devices through a command-line interface (CLI) .
  - Virtual private network (VPN) connections that create a secure tunnel between remote devices and IoT networks .
  - Proxy connections that route traffic between remote devices and IoT networks through an intermediary server .
  - Remote desktop protocol (RDP) connections that allow remote access to the graphical desktop of IoT devices .
- Interaction and remote control can provide various benefits for IoT systems, such as:
  - Enhancing user experience and convenience by allowing users to access and control IoT devices from anywhere and anytime  .
  - Improving service quality and efficiency by enabling service partners to perform remote diagnostics, maintenance, and updates on IoT devices  .
  - Reducing operational costs and downtime by allowing product support teams to troubleshoot and fix issues on IoT devices remotely  .
  - Increasing security and privacy by encrypting and authenticating remote connections and limiting access to authorized users and devices  .
- Interaction and remote control can also pose some challenges for IoT systems, such as:
  - Managing the complexity and diversity of IoT devices, connections, sensors, data, and platforms  .
  - Ensuring the reliability and availability of remote connections and IoT networks  .
  - Balancing the trade-off between user control and automation in IoT systems .



# Unit 3 - IOT Data Link Layer & Network Layer Protocols

## Data Link Layer Protocols

- The data link layer provides service to the network layer by enabling reliable and efficient communication between devices on the same network segment.
- The data link layer is responsible for framing, error detection, flow control, and medium access control.
- Some of the common data link layer protocols for IoT are:

  - **Bluetooth**: A short-range wireless communication network over a radio frequency. It supports low-power and low-cost devices and enables peer-to-peer and mesh networking. It is widely used for personal area networks (PANs) and wearable devices.
  - **Wi-Fi**: A wireless local area network (WLAN) technology that uses radio waves to provide high-speed internet access and network connectivity. It supports various standards such as 802.11a/b/g/n/ac/ax and offers different security and encryption options. It is widely used for home and office networks and smart devices.
  - **Zigbee**: A low-power and low-data-rate wireless communication network that operates in the industrial, scientific, and medical (ISM) radio bands. It supports mesh networking and self-healing capabilities and is designed for applications such as smart home, smart metering, and industrial automation.
  - **Z-Wave**: A low-power and low-data-rate wireless communication network that operates in the sub-GHz frequency band. It supports mesh networking and interoperability among different vendors and devices. It is designed for applications such as smart home, security, and lighting control.
  - **LoRa**: A long-range and low-power wireless communication network that operates in the sub-GHz frequency band. It supports star and star-of-stars network topologies and offers high immunity to interference and low latency. It is designed for applications such as smart city, smart agriculture, and smart logistics.

## Network Layer Protocols

- The network layer provides service to the transport layer by enabling routing and addressing of data packets across different networks.
- The network layer is responsible for packet forwarding, congestion control, and network security.
- Some of the common network layer protocols for IoT are:

  - **IPv4**: The fourth version of the internet protocol that uses 32-bit addresses to identify devices and networks. It supports various features such as fragmentation, checksum, and options. It is widely used for internet communication and networking.
  - **IPv6**: The sixth version of the internet protocol that uses 128-bit addresses to identify devices and networks. It supports various features such as auto-configuration, mobility, security, and multicast. It is designed to overcome the limitations of IPv4 and enable the growth of IoT.
  - **6LoWPAN**: A network layer protocol that enables the transmission of IPv6 packets over low-power and lossy networks (LLNs) such as Zigbee, Bluetooth, and LoRa. It supports various features such as header compression, fragmentation, and adaptation. It is designed to enable interoperability and scalability of IoT devices and networks.
  - **CoAP**: A network layer protocol that enables the exchange of constrained application protocol (CoAP) messages over UDP. It supports various features such as request/response, observe, discovery, and security. It is designed to enable lightweight and RESTful communication for IoT applications and services.
  - **MQTT**: A network layer protocol that enables the exchange of MQTT messages over TCP. It supports various features such as publish/subscribe, quality of service, and security. It is designed to enable reliable and efficient communication for IoT applications and services.



### PHY/MAC Layer(3GPP MTC

- 3GPP MTC stands for 3rd Generation Partnership Project Machine Type Communication, which is a term used to describe various applications that involve communication between machines or devices without human intervention.
- 3GPP MTC has different requirements and challenges than human-centric communication, such as low power consumption, low cost, low data rate, high reliability, massive connectivity, and diverse traffic patterns.
- 3GPP MTC can be categorized into two types: massive MTC and critical MTC, depending on the number of devices, latency, and reliability requirements.
- 3GPP has developed several technologies and enhancements for MTC in the physical (PHY) and medium access control (MAC) layers, which are the lowest layers of the radio interface protocol architecture.
- The PHY layer is responsible for modulation, coding, multiplexing, and transmission of the data over the radio channel, while the MAC layer is responsible for scheduling, resource allocation, error control, and power control of the data.
- Some of the PHY/MAC layer solutions for MTC in 3GPP are:

  - Narrowband Internet of Things (NB-IoT), which is a new radio access technology that operates in narrowband spectrum and provides low power, low cost, and wide coverage for massive MTC.
  - Enhanced Coverage GSM (EC-GSM), which is an extension of the existing GSM technology that improves the coverage and battery life for MTC devices.
  - LTE-M, which is a subset of LTE that supports low complexity, low power, and low data rate MTC devices.
  - New Radio (NR), which is the 5G radio access technology that supports both massive and critical MTC with flexible numerology, frame structure, and waveform.
  - Device-to-Device (D2D) communication, which is a direct communication between devices without involving the network infrastructure, which can improve the efficiency, reliability, and latency for MTC.
  - Non-Orthogonal Multiple Access (NOMA), which is a technique that allows multiple devices to share the same radio resources by using different power levels or codes, which can increase the spectral efficiency and connectivity for MTC.



### IEEE 802.11

- IEEE 802.11 is a set of standards for wireless local area networks (WLANs) that operate in the 2.4 GHz, 5 GHz, and 60 GHz frequency bands .
- IEEE 802.11 defines the physical layer (PHY) and the medium access control (MAC) layer specifications for WLANs.
- IEEE 802.11 has several amendments that extend or modify the original standard, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11p, and 802.11ad .
- Some of the main features and characteristics of IEEE 802.11 are:

  - It supports data rates from 1 Mbps to 7 Gbps depending on the amendment and the modulation scheme .
  - It uses either frequency-hopping spread spectrum (FHSS), direct-sequence spread spectrum (DSSS), orthogonal frequency-division multiplexing (OFDM), or single-carrier frequency-division multiple access (SC-FDMA) as the modulation techniques .
  - It employs either carrier sense multiple access with collision avoidance (CSMA/CA) or time division multiple access (TDMA) as the MAC protocols .
  - It supports various network architectures, such as infrastructure mode, ad hoc mode, mesh mode, and vehicular mode  .
  - It provides various security mechanisms, such as wired equivalent privacy (WEP), Wi-Fi protected access (WPA), and IEEE 802.11i .
  - It supports various quality of service (QoS) and power management features, such as IEEE 802.11e and IEEE 802.11h .

- IEEE 802.11 is widely used in most home and office networks, as well as in public hotspots, to allow wireless devices to communicate with each other and access the Internet without connecting wires .
- IEEE 802.11 is also a basis for vehicle-based communication networks with IEEE 802.11p, which enables vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) communications in the 5.9 GHz band .
- IEEE 802.11 is constantly evolving to meet the increasing demands and challenges of wireless communications, such as higher data rates, lower latency, better reliability, and wider coverage .



### IEEE 802.15

- IEEE 802.15 is a working group of the Institute of Electrical and Electronics Engineers (IEEE) IEEE 802 standards committee which specifies Wireless Specialty Networks (WSN) standards .
- The working group was formerly known as Working Group for Wireless Personal Area Networks (WPANs) .
- The working group develops standards for low-data-rate, low-power, and low-cost wireless communications among devices .
- The working group has several task groups (TGs) that focus on different aspects of WSNs, such as physical layer (PHY), medium access control (MAC), security, mesh networking, coexistence, and applications .
- Some of the standards developed by the working group are:
  - IEEE 802.15.1: Bluetooth, a short-range wireless technology for personal area networks (PANs) .
  - IEEE 802.15.4: Low-Rate Wireless Networks (LR-WPANs), a standard for low-data-rate, low-power, and low-cost wireless connectivity with fixed, portable, and moving devices  .
  - IEEE 802.15.5: Mesh Networking, a standard for enabling multi-hop communication among devices in a LR-WPAN .
  - IEEE 802.15.6: Body Area Networks (BANs), a standard for wireless communication among devices on, in, or around the human body .
  - IEEE 802.15.7: Visible Light Communication (VLC), a standard for wireless communication using visible light as the medium .
  - IEEE 802.15.8: Peer Aware Communication (PAC), a standard for device-to-device communication in proximity-based services .
  - IEEE 802.15.9: Recommended Practice for Transport of Key Management Protocol (KMP) Datagrams, a standard for secure communication among devices in a WSN .
  - IEEE 802.15.10: Routing Protocol for Low-Power and Lossy Networks (RPL), a standard for routing packets in a WSN .
  - IEEE 802.15.11: Recommended Practice for the Internet of Things (IoT) Scenario and Requirements Analysis, a standard for identifying and analyzing the requirements and challenges of IoT applications .
  - IEEE 802.15.12: Framework for MAC and Upper Layer Protocols for Wireless Networks, a standard for defining the common elements and interfaces of MAC and upper layer protocols for WSNs .



### WirelessHART

- WirelessHART is a wireless communications protocol for process automation applications.
- It is a subset of the HART industrial instrument communication standard as of version 7 .
- It communicates process data over 2.4 GHz radio waves .
- It uses mesh networking technology, which means that each device can act as a router for other devices, creating multiple paths for data transmission .
- It maintains compatibility with existing HART devices, commands, and tools .
- It is designed for robustness and security, using encryption, authentication, and verification mechanisms .
- It requires a gateway device to serve as an interface between the wireless network and a wired network or a host control system .
- It supports up to 250 devices per network and has a typical range of 200 meters per hop .
- It has a data reliability of 99.99% and a latency of less than 2 seconds .
- It is suitable for applications such as monitoring, control, asset management, diagnostics, and safety .



### ZWave

ZWave is a wireless communication protocol designed for smart home and IoT devices. It operates on the low-frequency 800 to 900 MHz band, which avoids interference with the 2.4 GHz band where Wi-Fi and Bluetooth operate. ZWave supports encryption, mesh networking, low power consumption, and interoperability among different vendors. Some of the features and characteristics of ZWave are:

- ZWave was developed by Zensys, a Danish company, in 1999.
- ZWave is a proprietary protocol owned by Sigma Designs, Inc. There is an open source implementation of ZWave protocol stack called open-zwave, but it does not support security layer.
- ZWave uses frequency shift keying (FSK) modulation and Gaussian frequency shift keying (GFSK) for data transmission. The data rate is 9.6 kbps in the US and 40 kbps in Europe.
- ZWave supports up to 232 nodes in a network, and each node can act as a repeater to extend the range and reliability of the network. The maximum distance between two nodes is about 100 meters, depending on the environment .
- ZWave devices are categorized into controllers and slaves. Controllers initiate and manage the communication, while slaves respond to the commands from the controllers. There are different types of controllers, such as primary, secondary, inclusion, portable, and bridge controllers.
- ZWave devices use a common application layer that defines the commands and parameters for different device classes, such as sensors, switches, thermostats, etc. This enables interoperability and compatibility among different vendors and products .
- ZWave devices use a network layer that handles routing, addressing, and error correction. ZWave uses source routing, which means that the controller specifies the entire route for each message. ZWave also supports network-wide inclusion, which allows adding new devices to the network without physically accessing the primary controller.
- ZWave devices use a transport layer that provides security and reliability. ZWave supports AES-128 encryption for secure communication, and uses acknowledgments and retries for error detection and correction .
- ZWave devices use a physical layer that defines the radio frequency, modulation, and power level. ZWave operates on different frequency bands depending on the region, such as 908.42 MHz in the US, 868.42 MHz in Europe, and 921.42 MHz in Australia .
- ZWave is suitable for low-power and low-data rate applications, such as home automation, security, lighting, climate control, etc. ZWave devices can operate on batteries for several years, and can be controlled remotely via smartphones or web browsers .



### Bluetooth Low Energy

- Bluetooth Low Energy (BLE) is a wireless personal area network technology designed and marketed by the Bluetooth Special Interest Group (Bluetooth SIG) aimed at novel applications in the healthcare, fitness, beacons, security, and home entertainment industries.
- BLE is distinct from the previous (often called "classic") Bluetooth Basic Rate/Enhanced Data Rate (BR/EDR) protocol, but the two protocols can both be supported by one device: the Bluetooth 4.0 specification permits devices to implement either or both of the LE and BR/EDR systems.
- BLE has the following advantages over classic Bluetooth:
  - Lower power consumption: BLE devices can operate for months or years on a coin cell battery, while classic Bluetooth devices require frequent recharging.
  - Faster connection time: BLE devices can connect in a few milliseconds, while classic Bluetooth devices may take seconds.
  - Simpler pairing process: BLE devices can use a variety of methods to pair, such as scanning a QR code, tapping a NFC tag, or proximity detection, while classic Bluetooth devices require a PIN code or a confirmation button.
  - Higher scalability: BLE devices can support up to 20 concurrent connections, while classic Bluetooth devices are limited to 7.
- BLE uses two protocols for discovery and communication between devices: the Generic Access Profile (GAP) and the Generic Attribute Profile (GATT).
  - GAP defines how devices advertise themselves and discover other devices. GAP also defines the roles of devices, such as peripheral (device that advertises and provides data) and central (device that scans and consumes data).
  - GATT defines how devices exchange data using services, characteristics, and descriptors. GATT also defines the roles of devices, such as server (device that provides data) and client (device that requests data).
- BLE devices can operate in different modes, such as broadcast, connection, or mesh.
  - Broadcast mode: A device sends data to multiple devices without establishing a connection. This mode is useful for applications such as beacons, where a device broadcasts its location or other information to nearby devices.
  - Connection mode: A device establishes a connection with another device and exchanges data. This mode is useful for applications such as fitness trackers, where a device sends its sensor data to a smartphone or a cloud service.
  - Mesh mode: A device connects with multiple devices and relays data between them. This mode is useful for applications such as smart lighting, where a device can control or monitor other devices in a network.



### Zigbee Smart Energy

- Zigbee Smart Energy (Zigbee SE) is a protocol designed for monitoring and actively managing energy consumption at the end-user level .
- Zigbee SE is based on the Zigbee standard, which is a low-cost and low-power wireless technology that operates in the 2.4 GHz and sub-GHz frequency bands.
- Zigbee SE enables utilities and consumers to reduce waste, energy consumption, and emissions footprint, and to optimize the generation and use of energy, gas, and water .
- Zigbee SE supports various applications, such as smart metering, demand response, load control, pricing, prepayment, home area network, distributed energy resources, and electric vehicle charging.
- Zigbee SE is interoperable with other Zigbee SE certified devices and applications, and can communicate with other Internet Protocol-based networks and systems.
- Zigbee SE is secure, reliable, and scalable, and can support large-scale deployments of smart energy devices and services.



### DASH7

- DASH7 is an open-source wireless sensor and actuator network protocol, which operates in the 433 MHz, 868 MHz and 915 MHz unlicensed ISM band /SRD band.
- DASH7 is based on the ISO 18000-7 standard for active radio frequency identification (RFID) and supports bi-directional, low-power, low-latency communication with long range and high penetration .
- DASH7 is designed for applications that require mobility, security, low cost, and low power consumption, such as asset tracking, building automation, smart metering, and environmental monitoring.
- DASH7 uses a four-layer architecture: physical layer, data link layer, network layer, and application layer. The data link layer defines the frame format, the medium access control (MAC) protocol, and the security mechanisms. The network layer provides routing, addressing, and network management functions. The application layer defines the commands and responses for data exchange and device configuration.
- DASH7 supports different modes of operation, such as beacon, burst, and query, to optimize the trade-off between power consumption and latency. DASH7 also supports different modulation schemes, such as FSK, GFSK, and ASK, to adapt to different channel conditions and data rates.
- DASH7 has several advantages over other wireless technologies, such as Zigbee, Bluetooth, and Wi-Fi, such as longer range, lower power consumption, higher penetration, and lower interference. DASH7 can also coexist with other wireless technologies by using frequency hopping and channel agility .
- DASH7 has many potential applications in various domains, such as automotive, industrial, medical, and consumer. For example, DASH7-based tire pressure monitoring systems (TPMS) can provide more accurate and timely information to drivers, resulting in greater fuel economy, reduced tire wear, and greater safety . DASH7 can also enable smart cities, smart agriculture, smart logistics, and smart homes by providing wireless connectivity and data exchange among sensors, actuators, and devices .



### Network Layer

The network layer is the third layer of the OSI model and the second layer of the TCP/IP model. It is responsible for addressing and routing of data packets across different networks. In the context of IoT, the network layer is part of the infrastructure layer in the IoT reference architecture.

Some of the main functions of the network layer are:

- Encapsulation: The network layer adds a header to the datagram from the transport layer, which contains the source and destination IP addresses, and other information. The header and the datagram together form a data packet.
- Addressing: The network layer assigns a unique IP address to each device in the IoT system, which is used to identify and locate the device on the network. The IP address can be either IPv4 or IPv6, depending on the protocol used.
- Routing: The network layer determines the best path for sending the data packets from the source to the destination, based on factors such as distance, traffic, cost, etc. The network layer uses various routing protocols, such as RIP, OSPF, BGP, etc., to exchange routing information and update routing tables.
- Fragmentation and reassembly: The network layer can divide a large data packet into smaller fragments, if the packet size exceeds the maximum transmission unit (MTU) of the underlying network. The network layer also reassembles the fragments at the destination, based on the information in the header.
- Error control and congestion control: The network layer can detect and correct errors in the data packets, using techniques such as checksum, parity, etc. The network layer can also prevent or reduce congestion on the network, by regulating the flow of data packets, using techniques such as windowing, buffering, etc.

Some of the common network layer protocols used in IoT are:

- Internet Protocol (IP): IP is the most widely used network layer protocol, which provides connectionless and unreliable delivery of data packets. IP can be either IPv4 or IPv6, depending on the version used. IPv4 uses 32-bit addresses, while IPv6 uses 128-bit addresses, which allows for more devices to be connected to the network .
- Internet Control Message Protocol (ICMP): ICMP is a protocol that is used to send error and control messages between devices on the network. ICMP can be used to test the connectivity, troubleshoot the network, or inform the sender about the status of the data packets .
- Internet Protocol Security (IPSec): IPSec is a protocol that provides security and encryption for the data packets at the network layer. IPSec can be used to authenticate the sender and the receiver, protect the data from tampering, and prevent unauthorized access to the network .
- 6LoWPAN: 6LoWPAN is a protocol that enables IPv6 communication over low-power wireless personal area networks (WPANs), such as ZigBee, Bluetooth, etc. 6LoWPAN can compress the IPv6 header, fragment and reassemble the data packets, and support mesh routing, which makes it suitable for IoT devices with limited resources .
- Routing Protocol for Low-Power and Lossy Networks (RPL): RPL is a protocol that provides routing for low-power and lossy networks (LLNs), such as sensor networks, smart grids, etc. RPL can adapt to the dynamic topology, optimize the energy consumption, and support multiple traffic types, such as point-to-point, point-to-multipoint, and multipoint-to-point .



### IPv4

- IPv4 stands for Internet Protocol version 4, which is the fourth version in the development of the Internet Protocol (IP) and the first version of the protocol to be widely deployed.
- IPv4 is a connectionless protocol that operates on the network layer of the OSI model and the internet layer of the TCP/IP model.
- IPv4 uses 32-bit binary numbers to create a single unique address on the network, which can be represented by four decimal numbers separated by dots, also called dotted decimal notation. For example, 192.168.0.1 is a valid IPv4 address.
- The 32-bit address space of IPv4 allows for 2^32 or about 4.3 billion possible addresses, which are not enough to meet the growing demand of the internet. Therefore, techniques such as subnetting, classless inter-domain routing (CIDR), network address translation (NAT), and private addressing are used to conserve and efficiently allocate IPv4 addresses .
- IPv4 addresses are divided into five classes: A, B, C, D, and E, based on the first four bits of the address. Each class has a different range of values and a different purpose. Class A, B, and C are used for unicast communication, class D is used for multicast communication, and class E is reserved for experimental use .
- IPv4 has a header of 20 bytes, which contains 12 fields: version, header length, type of service, total length, identification, flags, fragment offset, time to live, protocol, header checksum, source address, and destination address. Some of these fields can be modified or extended by using options .
- IPv4 supports various types of addressing modes, such as unicast, broadcast, multicast, and anycast. Unicast is a one-to-one communication between a sender and a receiver, broadcast is a one-to-all communication from a sender to all the nodes in a network, multicast is a one-to-many communication from a sender to a group of receivers, and anycast is a one-to-nearest communication from a sender to the nearest node in a group .
- IPv4 is the dominant protocol on the internet, but it has some limitations and challenges, such as address exhaustion, security issues, routing inefficiency, and quality of service. Therefore, a new version of IP, called IPv6, has been developed to overcome these problems and provide more features and benefits.



### IPv6

IPv6 is the next generation Internet Protocol (IP) standard intended to eventually replace IPv4, the protocol many Internet services still use today. IPv6 is designed to solve many of the problems of IPv4, such as address depletion, security, auto-configuration, extensibility, and so on. IPv6 expands the capabilities of the Internet to enable new kinds of applications, including peer-to-peer and mobile applications.

Some of the important features and uses of IPv6 are:

- IPv6 addresses: An IPv6 address uses 128 bits, four times more than the IPv4 address, which uses only 32 bits. This allows for a much larger address space, which can accommodate more devices and networks on the Internet. IPv6 addresses are written using hexadecimal, as opposed to dotted decimal in IPv4. For example, an IPv6 address may look like this: 2001:db8:0:1234:0:567:8:1.
- Network and node addresses: In IPv4, address classes were used to split an address into two components: a network component and a node component. In IPv6, the address is divided into two parts: a 64-bit network prefix and a 64-bit interface identifier. The network prefix identifies the network or subnet to which the device belongs, and the interface identifier identifies the device or interface on that network. The interface identifier can be derived from the MAC address of the device, or randomly generated.
- IPv6 address types and scope: IPv6 defines different types of addresses for different purposes and scopes. Some of the common address types are:

  - Link-local: These addresses are used for communication within a single network segment or link. They are not routable and have a prefix of fe80::/10.
  - Global unicast: These addresses are used for communication across the Internet. They are globally unique and routable and have a prefix of 2000::/3.
  - Unique local: These addresses are used for communication within a local network or site. They are not routable and have a prefix of fc00::/7.
  - Multicast: These addresses are used for sending packets to multiple destinations simultaneously. They have a prefix of ff00::/8.
  - Anycast: These addresses are used for sending packets to the nearest or best destination among a group of devices that share the same address. They have the same format as unicast addresses.

- Using IPv6 addresses in uniform resource locators (URLs): To use an IPv6 address in a URL, the address must be enclosed in square brackets, followed by the port number if needed. For example, http://[2001:db8:0:1234:0:567:8:1]:80/index.html.
- IPv6 loopback: The loopback address is used for testing and communication within the same device. In IPv6, the loopback address is ::1.

Some of the benefits of IPv6 are:

- Enhanced security: IPv6 supports end-to-end encryption and authentication through the use of IPsec, a set of protocols that provide security at the IP layer. IPsec is mandatory in IPv6, whereas it is optional in IPv4.
- Simplified header: IPv6 has a fixed-length header of 40 bytes, which is simpler and more efficient than the variable-length header of IPv4. IPv6 also eliminates some of the fields that are no longer needed, such as checksum and fragmentation.
- Improved performance: IPv6 reduces the need for network address translation (NAT), a technique that allows multiple devices to share a single public IP address. NAT can cause problems for some applications that rely on end-to-end connectivity, such as VoIP and peer-to-peer. IPv6 also supports larger packet sizes, which can improve the throughput and reduce the overhead.
- Enhanced mobility: IPv6 supports seamless mobility for devices that move across different networks, such as laptops and smartphones. IPv6 enables devices to maintain their IP addresses and connections even when they change their point of attachment to the Internet.
- Easier configuration: IPv6 supports stateless address autoconfiguration (SLAAC), a mechanism that allows devices to automatically obtain an IP address without the need for a DHCP server.



### 6LoWPAN

- 6LoWPAN stands for **IPv6 over Low-power Wireless Personal Area Networks** .
- It is an open standard defined by the **Internet Engineering Task Force (IETF)**  that enables low-power devices with limited processing capabilities to participate in the **Internet of Things (IoT)**.
- It allows **IPv6 datagrams** to be transmitted over **IEEE 802.15.4** based networks, which are low-power wireless mesh networks that operate in the 2.4 GHz and sub-GHz frequency bands  .
- It defines mechanisms for **encapsulation**, **header compression**, **neighbor discovery**, **routing**, and **security** that allow IPv6 to operate efficiently over IEEE 802.15.4 networks .
- It supports various applications that require wireless internet connectivity at lower data rates, such as residential and office automation, smart grid, industrial monitoring, healthcare, and environmental sensing .
- It can interoperate with other IPv6 networks through **edge routers**, which may also support IPv6 transition mechanisms to connect 6LoWPAN networks to IPv4 networks, such as **NAT64**.
- It is compatible with other IoT protocols, such as **CoAP**, **MQTT**, and **LwM2M**, which provide application layer services over 6LoWPAN networks.



### 6TiSCH

6TiSCH is a working group at the IETF, which is standardizing how to combine IEEE 802.15.4e time-slotted channel hopping (TSCH) with IPv6. The result is a solution that offers both industrial performance and seamless integration into the Internet and is therefore seen as a key technology for the Industrial Internet of Things (IIoT) .

Some of the main features and benefits of 6TiSCH are:

- It uses 128-bit IPv6 addresses, which allows for a large number of devices to be uniquely identified and connected to the Internet.
- It uses TSCH, which is a link layer protocol that allows the nodes to change their physical channel after each transmission to eliminate interference and improve reliability .
- It uses a Time Division Multiple Access (TDMA) schedule, which assigns a time slot and a channel to each node for each transmission, ensuring deterministic and bounded latency.
- It uses 6top, which is a sublayer that enables distributed and dynamic scheduling of the TSCH slots and channels, allowing the network to adapt to changing traffic patterns and network conditions.
- It uses 6LoWPAN, which is a protocol that compresses and fragments the IPv6 packets to fit the IEEE 802.15.4 frame size, reducing the overhead and increasing the efficiency.
- It uses IP-in-IP encapsulation, which is a technique that wraps an IPv6 packet inside another IPv6 packet, allowing the network to support multiple routing protocols and address spaces.
- It uses RPL, which is a routing protocol that builds a Directed Acyclic Graph (DAG) topology for the network, optimizing the path selection and the energy consumption.

6TiSCH is a promising technology for the IIoT, as it provides a low-power, high-reliability, and scalable network that can support a variety of applications and services. Some of the challenges and open issues of 6TiSCH are:

- How to design and implement efficient and secure mechanisms for network formation, join, and authentication.
- How to balance the trade-offs between centralized and distributed scheduling, and how to coordinate the 6top operations among the nodes.
- How to ensure interoperability and compatibility among different vendors and devices, and how to test and evaluate the performance and functionality of 6TiSCH networks .
- How to integrate 6TiSCH with other protocols and standards, such as CoAP, MQTT, OPC UA, and IEEE 802.1AS.



### ND for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The data link layer provides service to the network layer by enabling reliable and efficient communication between devices on the same network segment.
- The network layer provides service to the transport layer by enabling routing and addressing of data packets across different networks.
- There are various protocols and standards for data link and network layers in IoT, depending on the requirements and characteristics of the IoT application and devices.

#### Data Link Layer Protocols

- Some of the common data link layer protocols in IoT are:

  - **Bluetooth**: A short-range wireless communication network over a radio frequency. It supports low-power and low-cost devices and enables peer-to-peer and mesh networking. It is widely used for personal area networks (PANs) and wearable devices.
  - **Wi-Fi**: A wireless local area network (WLAN) technology that uses radio waves to provide high-speed internet access and network connectivity. It supports high data rates and long-range communication. It is widely used for home and office networks and smart devices.
  - **ZigBee**: A low-power and low-data-rate wireless communication network that operates in the industrial, scientific and medical (ISM) radio bands. It supports mesh networking and self-healing capabilities. It is widely used for sensor networks and smart home applications.
  - **Z-Wave**: A low-power and low-data-rate wireless communication network that operates in the sub-GHz frequency band. It supports mesh networking and interoperability among devices from different vendors. It is widely used for home automation and security applications.
  - **LoRa**: A long-range and low-power wireless communication network that operates in the sub-GHz frequency band. It supports star and star-of-stars topologies and adaptive data rate. It is widely used for smart city and industrial IoT applications.

#### Network Layer Protocols

- Some of the common network layer protocols in IoT are:

  - **IPv4**: The fourth version of the internet protocol that provides logical addressing and routing of data packets over the internet. It supports 32-bit addresses and has a limited address space of about 4.3 billion addresses.
  - **IPv6**: The sixth version of the internet protocol that provides logical addressing and routing of data packets over the internet. It supports 128-bit addresses and has a virtually unlimited address space of about 3.4 x 10^38 addresses. It also supports features such as stateless address autoconfiguration, neighbor discovery, and multicast.
  - **6LoWPAN**: A protocol that enables IPv6 communication over low-power wireless personal area networks (LoWPANs). It compresses and fragments IPv6 packets to fit the small frame size and low bandwidth of LoWPANs. It also supports features such as header compression, mesh routing, and security.
  - **RPL**: A routing protocol for low-power and lossy networks (LLNs) that supports IPv6 communication. It builds a directed acyclic graph (DAG) topology based on the objective function and metrics of the network. It also supports features such as loop avoidance, multipath routing, and security.



### DHCP

- DHCP stands for Dynamic Host Configuration Protocol   .
- It is a network management protocol that automatically provides an Internet Protocol (IP) host with its IP address and other related configuration information such as the subnet mask and default gateway .
- It uses a client-server architecture, where a DHCP server allocates IP addresses and other parameters to DHCP clients that request them  .
- It operates on the application layer of the TCP/IP model.
- It is based on the Bootstrap Protocol (BOOTP), which was designed for diskless workstations .
- It is defined by RFCs 2131 and 2132 as an Internet Engineering Task Force (IETF) standard.
- It reduces the administrative burden and the risk of configuration errors in large networks  .
- It supports static and dynamic IP address allocation, as well as manual and automatic IP address assignment  .
- It uses four basic messages to exchange information between the DHCP server and the DHCP client: DHCPDISCOVER, DHCPOFFER, DHCPREQUEST, and DHCPACK  .
- It can also provide additional information to the DHCP client, such as the domain name, the DNS server, the NTP server, and the proxy server  .
- It can be integrated with other protocols, such as IPv6, DNS, and DHCPv6 .



### ICMP

- ICMP stands for Internet Control Message Protocol  .
- It is a network layer protocol used by network devices to diagnose network communication issues  .
- It is not associated with any transport layer protocol, such as TCP or UDP. It is a connectionless protocol, meaning a device does not need to open a connection with the target device before sending a message.
- It is used to generate error messages to the source IP address when network problems prevent delivery of IP packets. It is also used to determine whether or not data is reaching its intended destination in a timely manner .
- It is a special type of packet used for inter-device communication, carrying everything from redirect instructions to timestamps for synchronization between devices.
- Some common types of ICMP messages are:
  - Echo request and echo reply: used to test the reachability and latency of a destination device  . This is the basis of the ping command.
  - Destination unreachable: used to inform the source device that the destination device or network is unreachable for some reason  .
  - Time exceeded: used to inform the source device that the time to live (TTL) of a packet has expired and the packet has been discarded  .
  - Parameter problem: used to inform the source device that the header of a packet is invalid or incorrect  .
  - Source quench: used to inform the source device that the destination device is congested and cannot process more packets  .
  - Redirect: used to inform the source device that there is a better route to the destination device or network  .
  - Router advertisement and router solicitation: used to discover and advertise the presence of routers on a network  .
- ICMP is important for IOT devices because it helps to monitor and troubleshoot the connectivity and performance of the network . It also helps to optimize the routing of packets and avoid congestion and delays . ICMP can also be used to detect and prevent malicious attacks on the network, such as denial-of-service (DoS) or ping of death .



### RPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for **Routing Protocol for Low-Power and Lossy Networks**.
- It is an **IPv6** routing protocol that is standardized for the **Internet of Things (IoT)** by **Internet-Engineering Task Force (IETF)** .
- It forms a **tree-like topology** which is based on different optimizing process called **Objective Function (OF)** .
- It supports both **many-to-one** and **one-to-one** communication.
- It is designed for **resource-constrained networks** that have low power, low bandwidth, high packet loss, and dynamic topology.
- It uses **Destination Oriented Directed Acyclic Graphs (DODAGs)** as the routing structure, where each node has a **rank** that indicates its position in the graph .
- It defines two types of messages: **DODAG Information Object (DIO)** and **DODAG Information Solicitation (DIS)** .
- DIO messages are used to **advertise** the DODAG and its parameters, such as the rank, the OF, and the prefix .
- DIS messages are used to **request** DIO messages from neighboring nodes .
- RPL also supports **local repair** and **global repair** mechanisms to handle topology changes and network failures .
- RPL has several advantages, such as **scalability**, **adaptability**, **energy efficiency**, and **interoperability** .
- RPL also has some challenges, such as **security**, **mobility**, **overhead**, and **performance** .



# CORPL

- CORPL stands for **Cognitive RPL**, which is a non-standard extension of RPL that is designed for cognitive networks .
- RPL stands for **Routing Protocol for Low-Power and Lossy Networks**, which is a standard protocol for IPv6-based networks that consist of resource-constrained devices.
- Cognitive networks are networks that can adapt to the changing environment and user needs by sensing, learning, and optimizing their parameters and behavior.
- CORPL aims to improve the performance and reliability of RPL by using cognitive radio techniques to select the best frequency channels for data transmission .
- CORPL consists of two main components: **cognitive objective function (COF)** and **cognitive channel selection (CCS)** .
- COF is a metric that evaluates the quality of the links and paths based on the channel conditions, interference, and energy consumption .
- CCS is a mechanism that assigns the optimal channel to each node based on the COF and the availability of the spectrum .
- CORPL can dynamically switch between channels to avoid interference and congestion, and can also cooperate with other nodes to share the spectrum resources .
- CORPL can enhance the network performance in terms of packet delivery ratio, end-to-end delay, throughput, and energy efficiency .
- CORPL can also provide security features such as authentication, encryption, and integrity protection by using cryptographic keys and certificates.



### CARP

- CARP stands for Channel-Aware Routing Protocol.
- It is a distributed routing protocol designed for underwater communication .
- It has lightweight packets so that it can be used for Internet of Things (IoT) .
- It performs two different functionalities: network initialization and data forwarding.
- It does not support previously collected data.
- It keeps track of data communication history to select nodes for data transfer.
- It is a transport layer protocol, not a network layer protocol as mentioned in the topic.



## Unit 4 - Transport & Session Layer Protocols

The transport layer is the fourth layer of the OSI model and the third layer of the TCP/IP model. It provides end-to-end communication services for applications, such as error detection, flow control, congestion control, reliability, and multiplexing. The transport layer protocols lie between user applications and the network, and they offer user-oriented services based on the network characteristics.

Some of the common transport layer protocols are:

- **Transmission Control Protocol (TCP)**: TCP is a connection-oriented, reliable, and full-duplex protocol that establishes a logical connection between two endpoints and ensures that the data is delivered in the same order and without errors. TCP uses a three-way handshake to establish a connection, and a four-way handshake to terminate a connection. TCP also uses a sliding window mechanism to control the flow and congestion of data. TCP is used by many application layer protocols, such as HTTP, FTP, SMTP, and Telnet.

- **User Datagram Protocol (UDP)**: UDP is a connectionless, unreliable, and datagram-based protocol that does not guarantee the delivery, order, or integrity of the data. UDP does not establish or terminate a connection, and it does not use any flow or congestion control mechanisms. UDP is used for applications that require speed, efficiency, or real-time communication, such as DNS, DHCP, RTP, and VoIP.

- **Datagram Congestion Control Protocol (DCCP)**: DCCP is a connection-oriented, unreliable, and datagram-based protocol that provides congestion control for applications that use UDP. DCCP uses a feature negotiation mechanism to allow the endpoints to choose the appropriate congestion control algorithm for their application. DCCP is used for applications that require low latency and high bandwidth, such as streaming media, online gaming, and telephony.

- **Stream Control Transmission Protocol (SCTP)**: SCTP is a connection-oriented, reliable, and message-based protocol that provides multiple streams of data within a single connection. SCTP also provides features such as multihoming, path selection, and partial reliability. SCTP is used for applications that require high availability, fault tolerance, and message orientation, such as signaling, web services, and file transfer.

The session layer is the fifth layer of the OSI model and it is not present in the TCP/IP model. It provides services for establishing, maintaining, and terminating sessions between applications. The session layer protocols manage the synchronization, coordination, and dialog control of the data exchange. The session layer protocols also provide security, authentication, and encryption for the sessions.

Some of the common session layer protocols are:

- **Session Initiation Protocol (SIP)**: SIP is a signaling protocol that is used to create, modify, and terminate multimedia sessions, such as voice and video calls, over the Internet. SIP uses a request-response mechanism to exchange messages between the endpoints, and it supports various features such as call transfer, call hold, call forwarding, and conferencing.

- **Remote Procedure Call (RPC)**: RPC is a protocol that allows a program to execute a procedure or a function on a remote system, as if it were a local system. RPC uses a client-server model to exchange messages between the systems, and it abstracts the details of the network communication. RPC is used for distributed computing, such as in NFS, NIS, and LDAP.

- **Secure Shell (SSH)**: SSH is a protocol that provides secure and encrypted communication between two systems over an insecure network. SSH uses a client-server model to establish a secure channel, and it supports various features such as remote login, remote command execution, file transfer, and port forwarding.

- **AppleTalk Session Protocol (ASP)**: ASP is a protocol that provides session management and communication services for AppleTalk applications. ASP uses a client-server model to establish a session, and it supports various features such as request-response, attention, and write-continue. ASP is used for file sharing, printing, and remote access in AppleTalk networks.



### Transport Layer

- The transport layer is the fourth layer in the OSI model and the TCP/IP model.
- The transport layer is responsible for end-to-end communication between devices or applications in an IoT system.
- The transport layer provides features such as reliability, congestion control, flow control, error detection, and ordering of packets.
- The transport layer can use different protocols depending on the requirements and characteristics of the IoT system, such as bandwidth, latency, power consumption, and security.
- Some of the common transport layer protocols used in IoT are:

  - **TCP (Transmission Control Protocol)**: TCP is a connection-oriented, reliable, and byte-stream protocol that ensures the delivery of packets in the same order as they were sent. TCP is suitable for IoT applications that require high reliability and data integrity, such as remote monitoring, firmware updates, and cloud computing. TCP also provides congestion control and flow control mechanisms to avoid network overload and packet loss. However, TCP has some drawbacks for IoT, such as high overhead, high latency, and high power consumption.
  - **UDP (User Datagram Protocol)**: UDP is a connectionless, unreliable, and datagram protocol that does not guarantee the delivery, order, or integrity of packets. UDP is suitable for IoT applications that require low latency, low overhead, and high scalability, such as real-time streaming, voice over IP, and video surveillance. UDP also supports multicast and broadcast communication, which can be useful for IoT scenarios that involve multiple devices or groups. However, UDP does not provide any reliability or congestion control features, which can lead to packet loss, duplication, or reordering.
  - **CoAP (Constrained Application Protocol)**: CoAP is a specialized protocol designed for constrained devices and networks in IoT. CoAP is based on UDP, but it provides some features of HTTP, such as request-response model, URIs, and methods. CoAP also supports reliability, congestion control, and security features, such as retransmission, exponential back-off, and DTLS. CoAP is suitable for IoT applications that require low power consumption, low bandwidth, and interoperability with web services, such as smart home, smart city, and environmental monitoring.
  - **MQTT (Message Queuing Telemetry Transport)**: MQTT is a publish-subscribe protocol that enables lightweight and asynchronous communication between devices and applications in IoT. MQTT uses TCP as the underlying transport layer protocol, but it reduces the overhead and complexity of TCP by using a simple and binary message format. MQTT also supports quality of service (QoS) levels, which allow the sender and receiver to choose the reliability and delivery guarantee of the messages. MQTT is suitable for IoT applications that require high scalability, low bandwidth, and event-driven communication, such as smart grid, industrial automation, and vehicular networks.



### TCP

TCP stands for Transmission Control Protocol. It is a transport layer protocol that facilitates the transmission of packets from source to destination. It is a connection-oriented protocol that means it establishes the connection prior to the communication that occurs between the computing devices in a network.

Some of the main features and functions of TCP are:

- It provides reliable and ordered delivery of data by using flow and error control mechanisms, such as acknowledgments, retransmissions, sequence numbers, and windowing .
- It supports full-duplex communication, which means that data can be sent and received simultaneously by both ends of the connection.
- It allows multiplexing and demultiplexing of data streams, which means that multiple applications can use the same TCP connection and each data stream can be identified by a port number.
- It performs congestion control and avoidance, which means that it adjusts the rate of data transmission according to the network conditions and avoids sending more data than the network can handle.
- It supports connection management, which means that it handles the establishment, termination, and maintenance of the connection using a three-way handshake and a four-way handshake.

TCP is used by many application protocols, such as HTTP, FTP, SMTP, and SSH, that require reliable and ordered delivery of data .



### MPTCP

- MPTCP stands for Multipath TCP, which is an extension to the original TCP protocol (single-path)   .
- MPTCP enables a transport connection to operate across multiple paths simultaneously, and brings network connection redundancy to user endpoint devices   .
- MPTCP is an ongoing effort of the Internet Engineering Task Force's (IETF) Multipath TCP working group, that aims at allowing a TCP connection to use multiple paths to maximize throughput and increase redundancy .
- MPTCP has several advantages over single-path TCP, such as   :
  - Improved connection stability and resilience to failures, as MPTCP can switch to another path if one path fails or degrades.
  - Increased bandwidth utilization and performance, as MPTCP can aggregate the available bandwidth of multiple paths.
  - Enhanced mobility and seamless handover, as MPTCP can maintain a connection even if the IP address of the device changes due to moving between different networks.
  - Reduced congestion and load balancing, as MPTCP can distribute the traffic across multiple paths and avoid congested links.
- MPTCP works by establishing a regular TCP connection as the initial subflow, and then using additional subflows to utilize other paths between the endpoints   .
- MPTCP uses a set of extensions to regular TCP, such as  :
  - A new TCP option for signaling MPTCP capabilities and exchanging keys for authentication.
  - A new TCP option for advertising and discovering additional addresses for subflow establishment.
  - A new TCP option for managing the subflows and their states.
  - A new TCP option for mapping the data sequence numbers of the subflows to the connection-level sequence numbers.
  - A new TCP option for indicating the data checksum of the subflows to detect data corruption.
  - A new congestion control algorithm that takes into account the characteristics of the subflows and the connection.
- MPTCP is supported by Red Hat Enterprise Linux 8.3 and later versions, and can be configured using the `mptcp` command or the `sysctl` utility   .
- MPTCP is compatible with existing applications and network devices, as it falls back to regular TCP if MPTCP is not supported by either endpoint or any intermediate device   .



### UDP

- UDP stands for User Datagram Protocol. It is a communications protocol that is primarily used to establish low-latency and loss-tolerating connections between applications on the internet .
- UDP speeds up transmissions by enabling the transfer of data before an agreement is provided by the receiving party . This means that UDP does not form a firm connection with the destination before sending the data, and does not guarantee the delivery, order, or integrity of the data .
- UDP is a simple message-oriented transport layer protocol that is documented in RFC 768. It has a header of 8 bytes, which contains the source port, destination port, length, and checksum fields. The payload can be up to 65,507 bytes long.
- UDP is suitable for time-sensitive applications like gaming, streaming media, or DNS lookups, where low latency is more important than the occasional dropped data . UDP can also be used for multicast and broadcast transmissions, where one sender can reach multiple receivers.
- UDP has some disadvantages, such as lack of reliability, congestion control, flow control, and error recovery mechanisms. UDP also does not provide any security features, such as encryption or authentication. Therefore, UDP may not be the best choice for applications that require high reliability, security, or quality of service.



### DCCP

- DCCP stands for **Datagram Congestion Control Protocol**.
- It is a **message-oriented** transport layer protocol.
- It is designed to solve issues present in UDP and TCP, particularly for **real-time and multimedia** (streaming) traffic.
- It implements reliable **connection setup**, **teardown**, **Explicit Congestion Notification (ECN)**, **congestion control**, and **feature negotiation**.
- It divides into a base protocol (RFC 4340) and pluggable **congestion control modules** called CCIDs.
- It allows applications to access congestion control mechanisms without implementing them at the application layer.
- It supports both **unidirectional** and **bidirectional** data transfer.
- It uses a **packet header** that contains a **sequence number**, a **type**, an **acknowledgement number**, and a **checksum**.
- It uses a **three-way handshake** to establish a connection and a **four-way handshake** to close a connection.
- It supports **feature negotiation** to allow endpoints to agree on optional protocol extensions.
- It supports **half-close** and **reset** operations to terminate a connection or a direction of data transfer.
- It supports **server listening**, **active open**, and **passive open** modes to initiate a connection.
- It supports **keepalive** and **ping** mechanisms to maintain a connection or test its liveness.
- It supports **change** and **confirm** options to modify the connection parameters during data transfer.
- It supports **different CCIDs** for different types of traffic, such as TCP-like, TCP-friendly, or multimedia.

: https://en.wikipedia.org/wiki/Datagram_Congestion_Control_Protocol
: https://www.kernel.org/doc/html/latest/networking/dccp.html
: https://www.geeksforgeeks.org/what-is-dccp-datagram-congestion-control-protocol/



### SCTP

- SCTP stands for **Stream Control Transmission Protocol**.
- It is a **transport layer** protocol in the Internet protocol suite.
- It is a **connection-oriented** protocol that supports **multiple streams** of data between two endpoints.
- It ensures **reliable** and **in-sequence** data transmission, so that data units arrive completely and in the right order to the application or user.
- It is designed to transport **Public Switched Telephone Network (PSTN)** signaling messages over IP networks, but is capable of broader applications.
- It places messages and control information into separate **chunks**, each identified by a chunk header.
- The protocol can **fragment** a message into multiple data chunks, but each data chunk contains data from only one user message.
- SCTP **bundles** the chunks into SCTP packets.
- SCTP provides the following features:
  - **Multi-homing**: An SCTP endpoint can have more than one IP address, providing network-level fault tolerance.
  - **Multi-streaming**: An SCTP connection can have multiple streams of data, each with its own sequence number and flow control, allowing independent and concurrent delivery of data.
  - **Congestion control**: SCTP uses a modified version of TCP's congestion control algorithm to avoid network congestion and packet loss.
  - **Selective acknowledgment**: SCTP uses a selective acknowledgment mechanism to acknowledge only the received packets, reducing the number of retransmissions.
  - **Path MTU discovery**: SCTP can discover the maximum transmission unit (MTU) of the path between the endpoints, avoiding fragmentation and improving performance.
  - **Heartbeat**: SCTP can send periodic messages to check the availability of the endpoints and the paths, detecting failures and restoring connectivity.
  - **Cookie mechanism**: SCTP uses a cookie mechanism to prevent denial-of-service attacks and to establish connections in a four-way handshake, avoiding the SYN flooding problem of TCP.

: Stream Control Transmission Protocol - Wikipedia
: Stream Control Transmission Protocol (SCTP) - SearchNetworking
: RFC 4960: Stream Control Transmission Protocol - RFC Editor



### Session Layer for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The session layer is the fifth layer of the OSI model that manages the connection between two endpoints of a network by controlling data between sender and receiver  .
- The session layer protocols are responsible for the actual transmission of data in the IoT ecosystem. That’s why these session layer protocols are called as IoT Messaging Protocols or sometimes referred as IoT Data Protocols .
- The session layer protocols review standards and protocols for message passing. Different standardization organizations introduce the IoT session layer protocols. There are different types of session layer protocol available with different functionality and range.
- Some of the common session layer protocols in IoT are:
  - MQTT (Message Queue Telemetry Transport): A lightweight, publish-subscribe protocol that is designed for constrained devices and low-bandwidth networks. It is widely used for IoT applications that require real-time data delivery, low power consumption, and high reliability  .
  - CoAP (Constrained Application Protocol): A web transfer protocol that is optimized for constrained devices and networks. It is based on the RESTful architecture and uses UDP as the transport layer protocol. It supports features such as multicast, caching, and asynchronous communication  .
  - AMQP (Advanced Message Queuing Protocol): An open standard protocol that provides reliable and secure messaging between applications and devices. It is based on the broker model and uses TCP as the transport layer protocol. It supports features such as message routing, queuing, delivery confirmation, and transactions  .
  - XMPP (Extensible Messaging and Presence Protocol): An open standard protocol that enables instant messaging and presence information exchange between applications and devices. It is based on the client-server model and uses XML as the data format. It supports features such as authentication, encryption, federation, and extensions  .
- The session layer also provides some functions such as:
  - Dialog control: It allows systems to communicate in either half-duplex mode or full-duplex mode.
  - Token management: It prevents two users to simultaneously access or transmit data over the same network.
  - Synchronization: It allows the communication to resume from the point of interruption in case of a failure or disconnection.



### HTTP

HTTP stands for Hypertext Transfer Protocol. It is an application layer protocol in the Internet protocol suite model for distributed, collaborative, hypermedia information systems. It was designed for communication between web browsers and web servers, but it can also be used for other purposes.

Some of the main features of HTTP are:

- It is a request-response protocol, where the client sends a request to the server and the server responds with a status code and optionally a message body.
- It is stateless, meaning that each request is independent and does not depend on the previous or future requests. However, state can be maintained using cookies, sessions, or other mechanisms.
- It is extensible, meaning that new methods, headers, and status codes can be defined and used by applications.
- It supports different types of media, such as text, images, audio, video, etc. The media type is indicated by the Content-Type header in the request or response.
- It supports different types of encoding, such as gzip, deflate, etc. The encoding is indicated by the Content-Encoding header in the request or response.
- It supports different types of transfer, such as chunked, multipart, etc. The transfer type is indicated by the Transfer-Encoding header in the request or response.
- It supports different types of connection, such as keep-alive, close, etc. The connection type is indicated by the Connection header in the request or response.
- It supports different types of caching, such as public, private, no-cache, etc. The caching type is indicated by the Cache-Control header in the request or response.
- It supports different types of authentication, such as basic, digest, etc. The authentication type is indicated by the Authorization header in the request or the WWW-Authenticate header in the response.
- It supports different types of security, such as HTTPS, SSL, TLS, etc. The security type is indicated by the protocol scheme in the request or response URL.

HTTP is based on an underlying and reliable transport layer protocol, such as TCP. However, there are also alternative protocols to HTTP, such as SPDY, HTTP/2, and Gemini, that aim to improve the performance, security, or privacy of HTTP .

HTTP is one of the most widely used protocols on the web and is essential for the functioning of the Internet of Things (IoT) applications. HTTP enables the exchange of data and commands between IoT devices and servers, as well as the integration of IoT devices with web services and applications. HTTP also enables the interoperability of IoT devices from different vendors and platforms, as well as the scalability and flexibility of IoT systems.



### CoAP

CoAP stands for Constrained Application Protocol. It is an application-layer protocol that is intended for use in resource-constrained Internet devices, such as wireless sensor network nodes. CoAP is designed to easily translate to HTTP for simplified integration with the web, while also meeting specialized requirements such as multicast support, very low overhead, and simplicity.

Some of the main features of CoAP are:

- It is based on the RESTful architecture, which means that it supports the standard methods of GET, POST, PUT, and DELETE for accessing and manipulating resources on a server.
- It uses UDP as the underlying transport protocol, which makes it suitable for unreliable and low-power networks. CoAP also provides reliability and congestion control mechanisms to handle packet loss and retransmission.
- It supports asynchronous message exchanges and observe mechanisms, which allow clients to subscribe to resources and receive notifications when they change.
- It supports content negotiation and discovery, which enable clients and servers to exchange information about the available resources and their formats.
- It supports security features such as encryption, authentication, and authorization using Datagram Transport Layer Security (DTLS).

CoAP is one of the most widely used IoT protocols, as it enables simple, constrained devices to join the IoT even through constrained networks with low bandwidth and low availability. CoAP is also interoperable with other IoT protocols, such as MQTT and LWM2M. CoAP is defined in RFC 7252.

: https://dzone.com/articles/coap-protocol-step-by-step-guide
: https://radiocrafts.com/technologies/coap-constrained-application-protocol/
: https://en.wikipedia.org/wiki/Constrained_Application_Protocol
: https://dzone.com/articles/coap-protocol-step-by-step-guide



### XMPP

- XMPP stands for **Extensible Messaging and Presence Protocol** .
- It is an **open communication protocol** designed for **instant messaging (IM)**, **presence information**, and **contact list maintenance** .
- It is based on **XML (Extensible Markup Language)**, which enables the **near-real-time exchange of structured data** between two or more network entities .
- It is a **decentralized protocol**, meaning that anyone can run their own XMPP server and communicate with other servers .
- It is a **living standard**, meaning that engineers actively extend and improve it.
- It supports various features and applications, such as:
  - **IoT (Internet of Things)**: XMPP can be used to connect and control devices, sensors, and actuators.
  - **WebRTC (Web Real-Time Communication)**: XMPP can be used to establish peer-to-peer audio and video calls, as well as data channels.
  - **Online Gaming**: XMPP can be used to create multiplayer games, chat rooms, and social networks.
  - **Realtime Social**: XMPP can be used to create microblogging, activity streams, and social profiles.
- It has a **modular architecture**, meaning that it can be extended with **extensions (XEPs)** that define additional features and functionality .
- Some of the common extensions are:
  - **XEP-0030: Service Discovery**: This extension allows XMPP entities to discover information about other entities, such as their capabilities, identities, and services.
  - **XEP-0045: Multi-User Chat**: This extension allows XMPP entities to create and join chat rooms, where they can communicate with multiple participants.
  - **XEP-0060: Publish-Subscribe**: This extension allows XMPP entities to publish and subscribe to topics, where they can receive notifications about events and data.
  - **XEP-0163: Personal Eventing Protocol**: This extension allows XMPP entities to publish and subscribe to personal events, such as their status, mood, location, and avatar.
  - **XEP-0198: Stream Management**: This extension allows XMPP entities to resume interrupted streams, as well as to acknowledge and request retransmission of lost packets.
  - **XEP-0363: HTTP File Upload**: This extension allows XMPP entities to upload and share files via HTTP, without requiring a direct connection between the sender and the receiver.



### AMQP

- AMQP stands for **Advanced Message Queuing Protocol**.
- It is an **open standard**, **binary** application layer protocol designed for **message-oriented middleware**.
- It enables **encrypted** and **interoperable** messaging between organizations and applications.
- It is used in **client/server messaging** and in **IoT device management**.
- It has **reliable**, **secure**, **open**, and **standard** properties, along with **low overhead** characteristics.
- It has become a good solution for **IoT applications** that require high performance, scalability, and reliability.
- It supports **multiple messaging patterns**, such as **point-to-point**, **publish/subscribe**, and **request/reply**.
- It defines a **common wire format** and a **set of standard behaviors** for **exchanging messages** between **producers**, **brokers**, and **consumers**.
- It uses **TCP** as the underlying transport protocol and supports **TLS** for security.
- It can also use **WebSockets** as an alternative transport layer for **browser-based** or **firewall-friendly** scenarios.
- It supports **claims-based security (CBS)** or **Simple Authentication and Security Layer (SASL)** authentication for connecting to an **IoT hub**.
- It requires the following information for the service client: **IoT hub hostname**, **key name**, and **key value**.
- It allows the client to create **sender** and **receiver** links for **device-to-cloud** and **cloud-to-device** communications.
- It supports **device twins**, **direct methods**, and **file upload** features of **IoT hub**.



### MQTT

MQTT stands for **Message Queuing Telemetry Transport**. It is a **lightweight** and **publish-subscribe** messaging transport protocol that is designed for **machine to machine** communication. It is suitable for connecting remote devices with **resource constraints** or **limited network bandwidth**, such as in the **Internet of Things (IoT)** .

Some of the main features of MQTT are:

- It uses a **broker** and **clients** architecture, where the broker is a server that receives and routes messages from the clients, and the clients are devices that publish or subscribe to topics .
- It supports **three levels of quality of service (QoS)** for message delivery: at most once (QoS 0), at least once (QoS 1), and exactly once (QoS 2).
- It has a **minimal overhead** of 2 bytes per message, which reduces the network traffic and power consumption.
- It supports **persistent sessions** and **last will and testament** messages, which allow clients to resume communication after a network interruption or notify other clients about their disconnection.
- It is based on the **TCP/IP** protocol stack and uses the **port 1883** by default.

Some of the advantages of MQTT are:

- It is **simple** and **easy** to implement and use.
- It is **scalable** and **reliable**, as it can handle millions of concurrent connections and messages.
- It is **interoperable** and **standardized**, as it is an OASIS and ISO standard and supports various platforms and languages.
- It is **secure** and **flexible**, as it can use TLS/SSL encryption and authentication, and support various message formats and payloads.

Some of the applications of MQTT are:

- **Smart home** and **building automation**, such as controlling lights, thermostats, locks, cameras, etc.
- **Industrial IoT** and **Industry 4.0**, such as monitoring sensors, actuators, machines, robots, etc.
- **Healthcare** and **wearables**, such as tracking vital signs, fitness, location, etc.
- **Transportation** and **logistics**, such as tracking vehicles, assets, deliveries, etc.
- **Agriculture** and **environment**, such as monitoring soil, weather, crops, livestock, etc.



## Unit 5 - Service Layer Protocols & Security

- The service layer is a layer in the telecommunication network architecture that provides capability servers owned by a network service provider, accessed through open and secure Application Programming Interfaces (APIs) by application layer servers owned by third-party content providers.
- The service layer also provides an interface to core networks at a lower resource layer.
- Service layer protocols are protocols that operate at the service layer and provide security services to the application layer protocols.
- Security services are services that enhance the security of data processing systems and information transfers of an organization.
- Security services can be classified into five categories: authentication, access control, data confidentiality, data integrity, and non-repudiation.
- Security services can be provided at different layers of the network architecture, such as the application layer, the transport layer, the network layer, or the link layer.
- Some examples of service layer protocols that provide security services are:

  - SSL (Secure Socket Layer): a protocol that provides authentication and confidentiality for data exchanged between a web browser and a web server.
  - TLS (Transport Layer Security): an updated version of SSL that provides authentication, confidentiality, and integrity for data exchanged between any two applications that use TCP as the transport protocol.
  - AT-TLS (Application Transparent Transport Layer Security): a protocol that provides TLS security services to any application that uses TCP, without requiring any changes to the application code.
  - Kerberos: a protocol that provides authentication and access control for distributed systems, based on the concept of tickets and keys.
  - OSPF (Open Shortest Path First): a routing protocol that provides authentication for routing updates exchanged between routers.
  - SNMPv3 (Simple Network Management Protocol version 3): a protocol that provides authentication, confidentiality, and integrity for network management information exchanged between network devices.



### Service Layer for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The service layer is the layer that provides the interface between the IoT devices and the applications or services that use them.
- The service layer is responsible for service discovery, service management, data processing, data storage, data analysis, and data visualization  .
- The service layer can be implemented on different platforms, such as cloud computing, fog computing, edge computing, or peer-to-peer networks .
- The service layer can use different protocols and standards to enable communication and interoperability among IoT devices and services. Some of the common protocols and standards are   :
  - AMQP: Advanced Message Queuing Protocol, an open standard protocol for message-oriented middleware.
  - CoAP: Constrained Application Protocol, a lightweight protocol for resource-constrained devices and networks.
  - DDS: Data Distribution Service, a standard for data-centric publish-subscribe communication.
  - HTTP: Hypertext Transfer Protocol, a widely used protocol for web-based communication and data exchange.
  - MQTT: Message Queuing Telemetry Transport, a lightweight protocol for publish-subscribe communication over low-bandwidth networks.
  - REST: Representational State Transfer, a style of web-based communication that uses HTTP methods and URIs to access resources.
  - SOAP: Simple Object Access Protocol, a protocol for exchanging structured data using XML and HTTP.
  - XMPP: Extensible Messaging and Presence Protocol, an open standard protocol for instant messaging and presence information.
- The service layer also needs to ensure the security and privacy of the IoT devices and data. Some of the challenges and solutions for IoT security are  :
  - Authentication: verifying the identity and legitimacy of the IoT devices and services. Solutions include using certificates, tokens, passwords, biometrics, or blockchain.
  - Authorization: granting or denying access to the IoT devices and data based on predefined policies and rules. Solutions include using access control lists, roles, permissions, or encryption.
  - Confidentiality: protecting the IoT data from unauthorized disclosure or interception. Solutions include using encryption, hashing, or digital signatures.
  - Integrity: ensuring the IoT data is not modified or corrupted during transmission or storage. Solutions include using checksums, hashes, or digital signatures.
  - Availability: ensuring the IoT devices and services are accessible and functional at all times. Solutions include using redundancy, load balancing, fault tolerance, or backup.
  - Non-repudiation: preventing the IoT devices and services from denying their actions or transactions. Solutions include using digital signatures, timestamps, or audit logs.



### oneM2M

- oneM2M is a global partnership project founded in 2012 and constituted by 8 of the world's leading ICT standards development organizations.
- oneM2M aims to develop a common service layer that can be used by various industry IoT verticals, such as smart cities, healthcare, transportation, etc .
- oneM2M service layer consists of a suite of common service functions (CSFs) that provide basic functionalities for IoT applications, such as data management, device management, security, discovery, etc.
- oneM2M service layer is based on a resource-oriented architecture (ROA) that uses RESTful APIs to access and manipulate resources, such as devices, sensors, data, etc.
- oneM2M service layer defines three types of entities: application entity (AE), common service entity (CSE), and network service entity (NSE) .
  - AE is the entity that provides or consumes IoT services, such as a sensor, an actuator, a smartphone app, etc .
  - CSE is the entity that implements the CSFs and acts as a middleware between AEs and NSEs .
  - NSE is the entity that provides network connectivity and interoperability between different CSEs .
- oneM2M service layer supports various communication protocols, such as HTTP, CoAP, MQTT, WebSocket, etc, by using protocol binding and interworking proxies .
- oneM2M service layer provides security mechanisms, such as authentication, authorization, encryption, integrity, etc, by using certificates, tokens, signatures, etc .
- oneM2M service layer is designed to be scalable, flexible, and extensible, by allowing dynamic registration, discovery, and composition of IoT services .



### ETSI M2M

- ETSI M2M stands for European Telecommunications Standards Institute Machine-to-Machine.
- It is a standardization body that develops standards for IoT and M2M technologies.
- It is one of the founding partners of oneM2M, the global standards initiative for IoT and M2M interoperability.
- ETSI M2M defines a high-level architecture for M2M systems, which consists of three main layers: Application Layer, Service Capability Layer (SCL), and Network Layer.
- The Application Layer contains the M2M applications that provide specific services to the end users or devices.
- The Service Capability Layer provides common functions and interfaces for the M2M applications, such as device management, data management, security, discovery, and communication.
- The Network Layer provides the connectivity and transport mechanisms for the M2M data and messages, such as IP, cellular, Wi-Fi, Bluetooth, etc.
- The SCL is the core component of the ETSI M2M architecture, as it enables the interoperability and scalability of the M2M system.
- The SCL is based on a resource-oriented architecture, where each entity and function is represented by a resource with a unique identifier and a set of attributes and operations.
- The SCL defines a common data model and a RESTful API for accessing and manipulating the resources.
- The SCL also supports semantic interoperability by providing a reference ontology and a semantic repository for the M2M data and metadata.
- The ETSI M2M architecture supports various deployment scenarios, such as cloud-based, distributed, or hybrid.
- The ETSI M2M architecture also supports interworking with different M2M area networks, such as ZigBee, Z-Wave, 6LoWPAN, etc., by using gateways or proxies that implement the SCL functions and interfaces.
- The ETSI M2M architecture provides security mechanisms for the M2M system, such as authentication, authorization, encryption, integrity, and privacy.



### OMA for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- OMA stands for Open Mobile Alliance, an organization that develops open standards for the mobile and IoT industry.
- OMA has defined several service layer protocols for IoT, such as OMA Lightweight M2M (LwM2M), OMA Device Management (DM), OMA Smart Objects, and OMA RESTful Network Services (RESTful NS).
- OMA LwM2M is a protocol for device management and service enablement of IoT devices. It is based on CoAP, a lightweight RESTful protocol that runs over UDP or SMS .
- OMA LwM2M defines four interfaces between an LwM2M server and an LwM2M client: Bootstrap, Client Registration, Device Management and Service Enablement, and Information Reporting.
- OMA LwM2M also defines a data model based on reusable and extensible resources, organized in objects and instances. OMA provides a set of standard objects, such as Device, Firmware, Location, Connectivity Monitoring, etc., and allows the creation of custom objects.
- OMA LwM2M supports various security modes, such as NoSec, Pre-Shared Key, Raw Public Key, and Certificate. It also supports DTLS for secure communication and OSCORE for end-to-end security .
- OMA LwM2M is suitable for constrained devices and networks, as it reduces the overhead and complexity of device management and service enablement. It also enables interoperability and scalability of IoT solutions .



### BBF for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- BBF stands for Broadband Forum, an industry organization that develops standards and best practices for broadband networks and services.
- BBF has developed a User Services Platform (USP) that defines a service layer protocol for managing and controlling IoT devices and services.
- USP is based on the Constrained Application Protocol (CoAP), a lightweight and HTTP-friendly protocol that operates on the application layer of the IoT architecture .
- USP supports secure and scalable communication among IoT devices and cloud/edge infrastructures, using features such as encryption, authentication, authorization, trust management, and data privacy .
- USP also supports data modeling, device discovery, event reporting, remote configuration, firmware upgrade, and diagnostics for IoT devices and services.
- USP is compatible with the CPE WAN Management Protocol (CWMP), also known as TR-069, which is a widely used protocol for managing broadband devices and services.
- USP aims to provide a simple migration path from CWMP to USP, using the same data model and data modeling tools.
- USP is one of the several service layer protocols that are designed to address the challenges and requirements of IoT communication and security  .
- Other service layer protocols for IoT include MQTT, AMQP, XMPP, DDS, LWM2M, and OPC UA .
- Each protocol has its own advantages and disadvantages, depending on the use case, device type, network topology, data format, and security level of the IoT application .



### Security in IoT Protocols

- Security is a major challenge for IoT systems, as they involve heterogeneous devices, networks, and applications that exchange large amounts of data and may be vulnerable to various attacks.
- Security protocols are designed to provide security services such as confidentiality, integrity, authentication, authorization, and non-repudiation for IoT communications.
- Some of the security protocols that are commonly used or proposed for IoT are:

  - MQTT (Message Queuing Telemetry Transport): A lightweight publish-subscribe protocol that supports quality of service (QoS) levels and TLS/SSL encryption for secure data transmission .
  - CoAP (Constrained Application Protocol): A web transfer protocol that is optimized for constrained devices and networks, and supports DTLS (Datagram Transport Layer Security) for end-to-end security.
  - LwM2M (Lightweight Machine to Machine): A device management protocol that defines a secure and interoperable way of managing IoT devices, using CoAP as the transport layer.
  - XMPP (Extensible Messaging and Presence Protocol): An open and extensible protocol that enables real-time communication and presence information exchange, and supports TLS and SASL (Simple Authentication and Security Layer) for security.
  - DDS (Data Distribution Service): A middleware standard that enables data-centric publish-subscribe communication for distributed systems, and supports various security mechanisms such as encryption, authentication, access control, and logging.

- Security protocols for IoT have to deal with various challenges and requirements, such as:

  - Resource constraints: IoT devices may have limited memory, processing power, battery life, and bandwidth, which may affect the performance and feasibility of security protocols .
  - Scalability: IoT systems may involve a large number of devices and data, which may pose scalability issues for security protocols, especially in terms of key management, authentication, and authorization .
  - Heterogeneity: IoT systems may consist of diverse devices, networks, and applications, which may have different security standards and specifications, and may require interoperability and compatibility among security protocols .
  - Privacy: IoT systems may collect and process sensitive and personal data, which may raise privacy concerns and require compliance with data protection regulations and policies .
  - Trust: IoT systems may involve multiple stakeholders and entities, which may have different levels of trust and reputation, and may require trust management and verification mechanisms for security protocols .
  - Attacks: IoT systems may be exposed to various types of attacks, such as denial of service, replay, spoofing, man-in-the-middle, eavesdropping, and tampering, which may compromise the security and functionality of security protocols .

- Security protocols for IoT should be designed and evaluated based on the following criteria:

  - Security objectives: The security protocols should meet the security objectives of the IoT system, such as confidentiality, integrity, authentication, authorization, and non-repudiation .
  - Performance: The security protocols should have minimal impact on the performance of the IoT system, such as latency, throughput, overhead, and energy consumption .
  - Usability: The security protocols should be easy to use and configure for the IoT system, such as simplicity, transparency, and user-friendliness .
  - Adaptability: The security protocols should be able to adapt to the dynamic and heterogeneous nature of the IoT system, such as scalability, interoperability, and flexibility .
  - Robustness: The security protocols should be able to resist and recover from various attacks and threats, such as resilience, fault-tolerance, and self-healing .



### MAC 802.15.4

- MAC 802.15.4 is a standard for low-rate wireless personal area networks (LR-WPANs) that defines the physical layer (PHY) and medium access control (MAC) sublayer specifications  .
- MAC 802.15.4 supports low-data-rate wireless connectivity with fixed, portable, and moving devices with no battery or very limited battery consumption requirements .
- MAC 802.15.4 provides the basis of other higher-layer standards, such as ZigBee, WirelessHart, 6LoWPAN and MiWi.
- MAC 802.15.4 supports multiple PHY options, such as frequency-hopping spread spectrum (FHSS), direct-sequence spread spectrum (DSSS), orthogonal frequency-division multiplexing (OFDM), and high-rate pulse ultra-wideband (HRP UWB) .
- MAC 802.15.4 defines two types of devices: full-function devices (FFDs) and reduced-function devices (RFDs). FFDs can operate in any topology and communicate with any other device, while RFDs can only operate in star topology and communicate with FFDs .
- MAC 802.15.4 defines two types of networks: star networks and peer-to-peer networks. In star networks, a single FFD acts as a coordinator and controls the communication with other devices. In peer-to-peer networks, any FFD can act as a coordinator and devices can communicate with each other directly or through intermediate devices .
- MAC 802.15.4 uses a superframe structure to organize the channel access. A superframe consists of an active period and an inactive period. The active period is divided into 16 equally sized slots, which can be allocated for contention-based or contention-free access. The inactive period is used for power saving .
- MAC 802.15.4 supports two types of channel access methods: slotted carrier sense multiple access with collision avoidance (CSMA-CA) and guaranteed time slot (GTS). Slotted CSMA-CA is used for contention-based access, where devices compete for the channel using a random backoff algorithm. GTS is used for contention-free access, where devices request and receive a fixed number of slots from the coordinator .
- MAC 802.15.4 provides security services such as data encryption, data integrity, and data authentication using the advanced encryption standard (AES) algorithm. MAC 802.15.4 also supports key management and device management functions .



### 6LoWPAN

- 6LoWPAN stands for IPv6 over Low-power Wireless Personal Area Networks.
- It is an open standard defined by the Internet Engineering Task Force (IETF) that enables low-power devices with limited processing capabilities to participate in the Internet of Things (IoT) using IPv6.
- It specifies mechanisms for encapsulation, header compression, neighbor discovery, routing, security, and interoperability of IPv6 packets over IEEE 802.15.4 based networks, which are low-rate wireless personal area networks (LR-WPANs) that operate in the 2.4 GHz and sub-GHz frequency bands .
- 6LoWPAN allows devices to communicate with each other or with other IPv6 networks through edge routers, which are devices that can translate between different link-layer technologies and support IPv6 transition mechanisms such as NAT64.
- Some of the benefits of 6LoWPAN are:
  - It provides end-to-end connectivity and addressability for IoT devices, enabling direct communication with other IPv6 nodes without intermediaries or gateways.
  - It reduces the overhead and complexity of IPv6 headers by compressing them to fit the small payload size of IEEE 802.15.4 frames, saving bandwidth and energy.
  - It supports mesh networking and multihop routing, which increases the network coverage and reliability of IoT devices.
  - It leverages the existing IPv6 protocols and standards, such as ICMPv6, UDP, TCP, CoAP, DTLS, etc., which simplifies the development and deployment of IoT applications.
  - It enhances the security and privacy of IoT devices by using IPv6 features such as IPSec, end-to-end encryption, and address randomization.



# RPL for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for Routing Protocol for Low-Power and Lossy Networks (LLNs).
- LLNs are networks that consist of resource-constrained devices (such as sensors, actuators, smart meters, etc.) that communicate over unreliable and low-bandwidth links (such as wireless, power-line, etc.).
- RPL is designed to enable scalable, efficient, and reliable routing in LLNs, which are often used for Internet of Things (IoT) applications.
- RPL is based on the concept of a Destination Oriented Directed Acyclic Graph (DODAG), which is a tree-like structure that defines the routing paths from the nodes to a common destination (such as a gateway or a sink).
- RPL uses a metric called rank to determine the position of a node in the DODAG. The rank is a function of the node's distance to the destination and other parameters (such as energy, hop count, link quality, etc.).
- RPL operates in two modes: storing mode and non-storing mode. In storing mode, each node maintains a routing table that contains the next hop information for all the destinations in the DODAG. In non-storing mode, only the root node maintains a routing table, and the other nodes forward the packets based on the source routing information carried in the packets.
- RPL uses three types of control messages to construct and maintain the DODAG: DODAG Information Object (DIO), Destination Advertisement Object (DAO), and DODAG Information Solicitation (DIS).
- DIO messages are used to advertise the DODAG configuration and the rank of the sender. DAO messages are used to propagate the destination information from the nodes to the root. DIS messages are used to request DIO messages from the neighbors.
- RPL supports multiple DODAGs within the same network, each with a different objective function (OF) that defines how the rank is calculated. RPL also supports multiple instances of the same DODAG with different configurations.
- RPL provides mechanisms for loop detection and avoidance, local repair, global repair, and mobility support.
- RPL faces several security challenges, such as rank attacks, version number (VN) attacks, DAO inconsistency attacks, DIO suppression attacks, sinkhole attacks, wormhole attacks, etc.
- RPL security can be enhanced by using cryptographic techniques (such as digital signatures, message authentication codes, encryption, etc.), trust management schemes, anomaly detection methods, secure routing metrics, etc.



### Application Layer for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The application layer is the interface between the IoT device and the network with which it will communicate.
- It handles data formatting and presentation and serves as the bridge between what the IoT device is doing and the network handoff of the data it produces.
- It also provides services such as data aggregation, data analysis, data visualization, and data management.
- Some of the common application layer protocols in IoT are :
  - MQTT: Message Queuing Telemetry Transport is a lightweight publish-subscribe protocol that is designed for low-bandwidth, high-latency, and unreliable networks. It is widely used for IoT applications that require real-time data delivery, such as smart home, smart grid, and industrial automation.
  - CoAP: Constrained Application Protocol is a web transfer protocol that is optimized for constrained devices and networks. It is based on the RESTful architecture and uses UDP as the transport layer. It supports features such as multicast, caching, and asynchronous communication. It is suitable for IoT applications that involve resource discovery, device management, and sensor networks.
  - HTTP: Hypertext Transfer Protocol is the most common web protocol that is used for data exchange between clients and servers. It is based on the request-response model and uses TCP as the transport layer. It supports features such as authentication, encryption, and compression. It is used for IoT applications that require web-based access, such as cloud services, web applications, and web APIs.
  - AMQP: Advanced Message Queuing Protocol is an open standard for message-oriented middleware that is designed for high-performance, reliable, and secure communication. It is based on the broker model and uses TCP as the transport layer. It supports features such as routing, queuing, transactions, and acknowledgments. It is used for IoT applications that require complex messaging patterns, such as enterprise integration, business process management, and event-driven architectures.

