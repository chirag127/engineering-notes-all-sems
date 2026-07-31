

# IOT ARCHITECTURE AND PROTOCOLS

- IoT architecture refers to the many ways that IoT devices are structured to meet user needs. Based on complexity, IoT system elements are grouped into 3 to 7 layers, each with its own role.
- IoT protocols are the set of rules that enable communication between IoT devices, gateways, services, and data centers. Different IoT protocols have been designed and optimized for different scenarios and usage.
- The following are some of the common layers and protocols in IoT architecture:

## Device layer
- This layer consists of the physical devices and sensors that collect and transmit data. They can be embedded, wearable, mobile, or stationary.
- Some of the device layer protocols are:
  - Bluetooth: A short-range wireless protocol that enables data exchange between devices within a personal area network (PAN).
  - Zigbee: A low-power, low-data-rate wireless protocol that supports mesh networking and device-to-device communication.
  - Z-Wave: A wireless protocol that operates in the sub-GHz frequency band and is mainly used for home automation and smart appliances.
  - LoRa: A long-range, low-power wireless protocol that uses spread spectrum modulation and supports star and mesh topologies.

## Gateway layer
- This layer acts as a bridge between the device layer and the network layer. It performs data aggregation, filtering, preprocessing, and protocol translation.
- Some of the gateway layer protocols are:
  - MQTT: A lightweight, publish-subscribe protocol that enables bidirectional communication between devices and gateways.
  - CoAP: A web-based protocol that uses HTTP methods and RESTful architecture to enable constrained devices to interact with web services.
  - AMQP: An open, binary protocol that supports reliable, secure, and scalable messaging between devices, gateways, and data centers.

## Network layer
- This layer consists of the network devices and infrastructure that transport data from the gateway layer to the cloud or data center layer. It can use wired or wireless technologies, such as Ethernet, Wi-Fi, cellular, or satellite.
- Some of the network layer protocols are:
  - IPv4: The fourth version of the internet protocol that assigns 32-bit addresses to network devices and supports packet switching and routing.
  - IPv6: The sixth version of the internet protocol that assigns 128-bit addresses to network devices and supports end-to-end connectivity, security, and quality of service.
  - 6LoWPAN: A protocol that enables IPv6 packets to be transmitted over low-power wireless networks, such as Zigbee or Bluetooth.

## Cloud or data center layer
- This layer consists of the servers and databases that store, process, and analyze the data received from the network layer. It can use cloud computing platforms, such as Azure, AWS, or Google Cloud, or on-premise data centers.
- Some of the cloud or data center layer protocols are:
  - HTTP: A widely used protocol that enables data exchange between web browsers and web servers using request-response messages.
  - HTTPS: A secure version of HTTP that encrypts the data using SSL or TLS protocols.
  - WebSocket: A protocol that enables full-duplex, persistent communication between web browsers and web servers over a single TCP connection.

## Application layer
- This layer consists of the software applications and services that provide the user interface and functionality for the IoT system. It can use web, mobile, or desktop applications, or voice or chat assistants.
- Some of the application layer protocols are:
  - REST: A software architectural style that defines a set of constraints and principles for creating web services that are stateless, uniform, and cacheable.
  - SOAP: A protocol that uses XML-based messages to enable communication between web services and clients.
  - GraphQL: A query language and a runtime system that enables clients to specify the data they need from web services and receive it in a structured format.

## Security layer
- This layer consists of the mechanisms and techniques that ensure the confidentiality, integrity, and availability of the data and devices in the IoT system. It can use encryption, authentication, authorization, and auditing methods.
- Some of the security layer protocols are:
  - SSL: A protocol that creates a secure channel between two parties using asymmetric cryptography and digital certificates.
  - TLS



## Unit 1 - IoT-An Architectural Overview

- IoT stands for Internet of Things, which refers to the network of physical objects or devices that can collect, communicate, and exchange data over the internet or other wireless technologies.
- IoT devices can range from simple sensors and actuators to complex smart devices and systems, such as wearable devices, smart home appliances, industrial machines, autonomous vehicles, etc.
- IoT devices can interact with each other, with humans, or with cloud services and applications, depending on the use case and the architecture.
- IoT architecture is the design and structure of the IoT system, which defines the components, functions, interfaces, protocols, and standards involved in the IoT system.
- IoT architecture can vary depending on the requirements, constraints, and objectives of the IoT system, but generally, it can be divided into four main layers: device layer, network layer, service layer, and application layer.

### Device Layer
- The device layer consists of the IoT devices that are the sources and destinations of the data in the IoT system.
- The device layer can include sensors, actuators, embedded systems, microcontrollers, gateways, etc.
- The device layer is responsible for data acquisition, data processing, data storage, data transmission, and data actuation.
- The device layer can use various communication technologies, such as Bluetooth, Wi-Fi, ZigBee, LoRa, etc., to connect to the network layer.

### Network Layer
- The network layer consists of the communication infrastructure that enables the data transfer between the device layer and the service layer.
- The network layer can include wired or wireless networks, such as LAN, WAN, cellular, satellite, etc.
- The network layer is responsible for data routing, data forwarding, data aggregation, data security, and data management.
- The network layer can use various protocols, such as TCP/IP, MQTT, CoAP, HTTP, etc., to ensure the reliability, scalability, and interoperability of the IoT system.

### Service Layer
- The service layer consists of the cloud platforms and services that provide the data processing, data analysis, data storage, and data visualization capabilities for the IoT system.
- The service layer can include cloud computing, edge computing, fog computing, etc.
- The service layer is responsible for data integration, data mining, data analytics, data visualization, and data service provisioning.
- The service layer can use various technologies, such as big data, machine learning, artificial intelligence, etc., to extract insights, knowledge, and value from the IoT data.

### Application Layer
- The application layer consists of the end-user applications and interfaces that enable the interaction and feedback between the IoT system and the users or stakeholders.
- The application layer can include web applications, mobile applications, desktop applications, etc.
- The application layer is responsible for data presentation, data interaction, data feedback, and data control.
- The application layer can use various technologies, such as web development, mobile development, user interface design, etc., to provide a user-friendly and intuitive experience for the IoT system.



Hello, I am Sydney, your AI assistant. I can help you with building an architecture for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS. Here is a possible outline for your notes:

# Unit 1 - IoT-An Architectural Overview

## Introduction
- Define the Internet of Things (IoT) and its characteristics
- Explain the benefits and challenges of IoT
- Describe the main components and layers of an IoT system
- Identify the key stakeholders and roles in an IoT ecosystem

## IoT Architecture Models
- Compare and contrast different IoT architecture models, such as:
  - Three-layer model (perception, network, application)
  - Five-layer model (perception, transport, processing, application, business)
  - Cloud-based model (device, gateway, cloud)
  - Fog-based model (device, fog node, cloud)
  - Edge-based model (device, edge node, cloud)
- Discuss the advantages and disadvantages of each model
- Analyze the suitability of each model for different IoT scenarios and applications

## IoT Protocols and Standards
- Define the concept of protocol and standard in the context of IoT
- Explain the importance and challenges of interoperability and compatibility in IoT
- Classify the main IoT protocols and standards according to their functions and layers, such as:
  - Device discovery and management protocols (e.g., CoAP, MQTT, LWM2M)
  - Data transmission and communication protocols (e.g., HTTP, WebSocket, AMQP)
  - Network and routing protocols (e.g., IPv6, 6LoWPAN, RPL)
  - Security and privacy protocols (e.g., TLS, DTLS, IPSec)
  - Application and service protocols (e.g., REST, SOAP, OMA-DM)
- Compare and contrast the features and performance of different IoT protocols and standards
- Evaluate the trade-offs and design choices of using different IoT protocols and standards

## IoT Security and Privacy
- Define the concepts of security and privacy in the context of IoT
- Explain the challenges and risks of ensuring security and privacy in IoT
- Describe the main security and privacy requirements and objectives for IoT, such as:
  - Confidentiality
  - Integrity
  - Availability
  - Authentication
  - Authorization
  - Accountability
  - Non-repudiation
- Identify the main security and privacy threats and attacks in IoT, such as:
  - Eavesdropping
  - Tampering
  - Spoofing
  - Replay
  - Denial-of-service
  - Malware
  - Data breach
  - Privacy violation
- Discuss the main security and privacy solutions and mechanisms for IoT, such as:
  - Encryption
  - Hashing
  - Digital signature
  - Certificate
  - Key management
  - Access control
  - Firewall
  - Intrusion detection and prevention
  - Anonymization
  - Data minimization



# Main design principles and needed capabilities for the notes of the Unit 1 - IoT-An Architectural Overview

- IoT stands for Internet of Things, which refers to the scenarios where network connectivity and computing capability extends to objects, sensors and everyday items not normally considered computers, allowing these devices to generate, exchange and consume data with minimal human intervention.
- IoT architecture consists of the devices, network structure, and cloud technology that allows IoT devices to communicate with each other. A basic IoT architecture consists of three layers: Perception (the sensors, gadgets, and other devices), Network (the communication protocols, gateways, and cloud services), and Application (the data analysis, visualization, and user interface).
- IoT architecture design should follow some main principles, such as  :
  - Openness: IoT architecture should be open to different devices, platforms, protocols, and standards, and allow interoperability and integration among them.
  - Service-orientation: IoT architecture should provide services to users and applications, and support service discovery, composition, and orchestration.
  - Security: IoT architecture should ensure the confidentiality, integrity, and availability of data and devices, and protect them from unauthorized access, modification, or attack.
  - Trust: IoT architecture should establish trust among users, devices, and services, and provide mechanisms for authentication, authorization, and accountability.
  - Scalability: IoT architecture should be able to handle the increasing number and diversity of devices, data, and services, and support dynamic and flexible adaptation.
  - Modularity: IoT architecture should be modular and layered, and allow for the reuse and replacement of components and functionalities.
  - Performance: IoT architecture should optimize the resource utilization, latency, throughput, and reliability of the system, and balance the trade-offs among them.
- IoT architecture needs some capabilities to support the above principles, such as  :
  - Device management: IoT architecture needs to manage the lifecycle, configuration, and status of devices, and provide remote control and monitoring functions.
  - Data management: IoT architecture needs to collect, store, process, and analyze the data generated by devices, and provide data quality, privacy, and sharing functions.
  - Communication management: IoT architecture needs to support different communication protocols, standards, and technologies, and provide routing, transmission, and synchronization functions.
  - Service management: IoT architecture needs to provide service discovery, registration, composition, and orchestration functions, and enable service-level agreements and quality of service.
  - Event management: IoT architecture needs to detect, filter, and correlate the events generated by devices, data, and services, and provide event notification and subscription functions.
  - User management: IoT architecture needs to identify, authenticate, and authorize the users of the system, and provide user preferences, profiles, and feedback functions.



# An IoT architecture outline for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- IoT architecture is the system of numerous elements that enable IoT devices to communicate with each other and perform various tasks.
- A basic IoT architecture consists of three layers: Perception, Network, and Application.
- Perception layer: This layer comprises the sensors, actuators, and other smart devices that collect data from the physical environment and perform actions on it . Examples of perception devices are temperature sensors, cameras, RFID tags, etc.
- Network layer: This layer comprises the network devices and communications types and protocols that transmit the data from the perception layer to the application layer or vice versa  . Examples of network devices are routers, gateways, switches, etc. Examples of communication types and protocols are 5G, Wi-Fi, Bluetooth, MQTT, CoAP, etc.
- Application layer: This layer comprises the cloud services, platforms, and applications that store, process, and analyze the data from the network layer and provide feedback or commands to the perception layer  . Examples of cloud services are AWS, Azure, Google Cloud, etc. Examples of platforms are IoT Central, ThingWorx, etc. Examples of applications are smart home, smart city, smart agriculture, etc.
- Some IoT architectures may have additional layers or components, such as middleware, edge computing, security, etc., depending on the complexity and requirements of the IoT system  .



# Standards Considerations for the Notes of the Unit 1 - IoT-An Architectural Overview

- The notes should provide a clear and concise introduction to the concept, definition, and characteristics of the Internet of Things (IoT).
- The notes should explain the main components and layers of a basic IoT architecture, such as perception, network, cloud, and application layers .
- The notes should describe the different architectural views and design objectives of IoT, such as functional, information, deployment, operational, and business views .
- The notes should highlight the key challenges and requirements of IoT, such as scalability, interoperability, security, privacy, and trust  .
- The notes should include examples and use cases of IoT applications in various domains, such as smart home, smart city, smart health, smart agriculture, and smart industry .
- The notes should follow a consistent and logical structure, using headings, subheadings, bullet points, diagrams, and tables to organize and present the information.
- The notes should cite the sources of information using numerical references and provide a list of references at the end of the notes.



# M2M and IoT Technology Fundamentals

- M2M stands for Machine to Machine, which is a technology that enables direct communication between devices without human intervention .
- IoT stands for Internet of Things, which is a network of physical devices that can collect, exchange and process data using sensors, software and cloud computing.
- M2M and IoT are related but not the same. M2M is a subset of IoT, as IoT involves communication between machines without human input, making it by definition a form of M2M communication.
- However, IoT expands the power and potential of M2M technology in new ways. The biggest difference between M2M and IoT is that an M2M system uses point-to-point communication, while an IoT system typically situates its devices within a global cloud network that allows larger-scale integration and more sophisticated applications .
- Scalability is another key difference between M2M and IoT. M2M systems are usually limited by the number of devices that can be connected and the bandwidth that can be used. IoT systems, on the other hand, can leverage the cloud infrastructure, software and platform to support millions of devices and massive amounts of data.
- Some examples of M2M applications are smart meters, vending machines, security systems and vehicle tracking. Some examples of IoT applications are smart homes, smart cities, smart agriculture and smart healthcare .
- M2M and IoT technologies have many benefits for various sectors and industries, such as improving efficiency, productivity, safety, quality, customer satisfaction and innovation. They also pose some challenges, such as security, privacy, interoperability, standardization and regulation .



# Devices and gateways for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Devices are the physical objects that are connected to the Internet of Things (IoT) network and can sense, actuate, communicate, and process data. Examples of devices are sensors, actuators, cameras, smart phones, smart watches, etc.
- Gateways are the central hubs that connect devices to the cloud and enable data transfer, protocol translation, data aggregation, security, and device management. Examples of gateways are routers, modems, edge servers, etc.
- The architecture of IoT gateways consists of the following components    :
  - Security: This is one of the most critical factors in an IoT gateway architecture throughout the design phase. It involves encryption, authentication, authorization, and access control of the devices and data.
  - Device layer: This comprises the hardware of an IoT infrastructure, such as IoT sensors, protective circuits, networking modules, and a processor or microcontroller.
  - Data management: This involves the storage, processing, and analysis of the data collected from the devices. It can be done locally on the gateway or remotely on the cloud.
  - Operating system: This is the software that runs the gateway hardware and other programs on the device. It can be a general-purpose OS, such as Linux or Windows, or a specialized OS, such as FreeRTOS or Contiki.
  - Hardware abstraction: This is the layer that provides a common interface for the devices and the gateway, regardless of the hardware specifications and differences. It simplifies the development and integration of the devices and the gateway.
  - Gateway data transfer: This is the layer that handles the communication between the devices and the gateway, as well as between the gateway and the cloud. It can use various protocols, such as MQTT, CoAP, HTTP, etc.
  - Communication protocols: These are the rules and standards that govern the data exchange between the devices and the gateway, as well as between the gateway and the cloud. They can be classified into wired or wireless, and application or transport protocols. Examples of communication protocols are ZigBee, Bluetooth, Wi-Fi, Ethernet, TCP/IP, etc.
  - Cloud connectivity manager: This is the layer that manages the connection between the gateway and the cloud, and ensures the reliability, scalability, and security of the data transfer. It can use various cloud platforms, such as AWS, Azure, Google Cloud, etc.
- The role of IoT gateways in the IoT architecture is to    :
  - Bridge the gap between the physical and digital worlds by connecting the devices and the cloud.
  - Enable data transfer, protocol translation, data aggregation, security, and device management.
  - Enhance the performance, efficiency, and scalability of the IoT system by reducing the network latency, bandwidth, and power consumption.
  - Provide edge computing capabilities by processing and analyzing the data locally on the gateway, and sending only the relevant information to the cloud.
  - Support interoperability and compatibility among different types of devices and protocols.



# Local and Wide Area Networking

- A **local area network (LAN)** is a computer network that interconnects computers within a limited area such as a residence, school, laboratory, university campus or office building .
- A **wide area network (WAN)** is a computer network that covers a larger geographic distance, such as different cities, countries or continents, and generally involves leased telecommunication circuits .
- The main differences between LAN and WAN are:
  - **Size**: LANs are smaller and have a limited number of devices, while WANs are larger and can span across the globe .
  - **Speed**: LANs have higher bandwidth and faster data transmission rates than WANs, due to the shorter distance and lower interference .
  - **Cost**: LANs are cheaper and easier to set up and maintain than WANs, as they use less expensive hardware and software, and do not require leased lines or routers .
  - **Security**: LANs are more secure and reliable than WANs, as they have less exposure to external threats and less dependence on third-party providers .
- The main advantages of LAN and WAN are:
  - **LAN**: LANs allow for easy and fast sharing of resources, such as files, printers, scanners, etc., among the connected devices. LANs also enable collaborative work and communication among the users, such as video conferencing, instant messaging, etc. LANs also support centralized management and control of the network, such as backup, security, etc.  .
  - **WAN**: WANs allow for connecting remote locations and users, such as branch offices, customers, suppliers, etc., over long distances. WANs also enable access to global information and services, such as the Internet, cloud computing, etc. WANs also support distributed and decentralized applications and systems, such as e-commerce, online banking, etc.  .
- The main challenges of LAN and WAN are:
  - **LAN**: LANs have limited scalability and performance, as they can only support a certain number of devices and traffic. LANs also have higher risk of congestion and collision, as they use shared media and protocols, such as Ethernet, Wi-Fi, etc. LANs also have higher vulnerability to internal threats and errors, such as unauthorized access, malware, misconfiguration, etc.  .
  - **WAN**: WANs have higher complexity and difficulty, as they involve multiple networks and technologies, such as routers, switches, firewalls, etc. WANs also have higher cost and maintenance, as they require leased lines, service providers, contracts, etc. WANs also have lower security and reliability, as they depend on external factors and parties, such as weather, politics, regulations, etc.  .



# Data management for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Data management is the process of collecting, storing, processing, and analyzing data from various sources, such as sensors, devices, applications, and networks, in the context of the Internet of Things (IoT).
- Data management is essential for IoT because it enables the extraction of valuable insights from the large and diverse data generated by IoT devices and systems, which can improve decision making, optimize operations, enhance customer experience, and create new business opportunities.
- Data management for IoT involves the following steps:
  - Identify what you need from IoT data and how it will benefit your business. Define your goals, use cases, and key performance indicators (KPIs) for IoT data analysis.
  - Ensure that you have the necessary network connectivity and bandwidth to support the data transmission from IoT devices to the cloud or the edge. Choose the appropriate communication protocols and standards for your IoT devices and systems, such as MQTT, CoAP, HTTP, etc.
  - Set up connectivity to the right platform that can handle the data ingestion, storage, processing, and analysis of IoT data. You can use a cloud-based platform, such as AWS IoT, Azure IoT, or Google Cloud IoT, or an edge-based platform, such as AWS Greengrass, Azure IoT Edge, or Google Cloud IoT Edge, depending on your latency, security, and scalability requirements.
  - Assign roles for data collection and analysis, such as data engineers, data scientists, data analysts, and business users. Define the data governance policies and procedures to ensure the data quality, security, privacy, and compliance of IoT data.
  - Analyze data to generate insights that can help you achieve your business goals and KPIs. You can use various data analysis techniques and tools, such as descriptive, diagnostic, predictive, and prescriptive analytics, machine learning, artificial intelligence, data visualization, etc.
  - Review your data management strategy regularly and update it as needed to accommodate the changes in your business needs, data sources, data volume, data velocity, data variety, and data value.

- Data management for IoT also involves some challenges, such as    :
  - Data variety: IoT data can come from different types of devices, sensors, and systems, each with its own data format, structure, and semantics. This makes it difficult to integrate, harmonize, and standardize the data for analysis.
  - Data volume: IoT data can be generated at a very high rate and volume, which can overwhelm the network bandwidth, storage capacity, and processing power of the data management platform. This can also increase the cost and complexity of data management.
  - Data velocity: IoT data can be time-sensitive and require real-time or near-real-time analysis and response. This can pose challenges for data latency, reliability, and availability, especially when the data is transmitted over long distances or unreliable networks.
  - Data veracity: IoT data can be incomplete, inaccurate, inconsistent, or corrupted due to various factors, such as device malfunction, network failure, human error, or malicious attack. This can affect the data quality and trustworthiness, and lead to erroneous or misleading insights.
  - Data value: IoT data can have different levels of value and relevance for different users and purposes. This can make it difficult to prioritize, filter, and aggregate the data for analysis, and to extract the most meaningful and actionable insights from the data.
  - Data security and privacy: IoT data can contain sensitive or personal information that can be vulnerable to unauthorized access, disclosure, modification, or deletion. This can pose risks for data confidentiality, integrity, and availability, and also raise ethical and legal issues for data protection and compliance.



# Business processes in IoT

- A business process is a collection of related events, activities and decisions that involve a number of factors and resources, which collectively lead to an outcome that is of value for the organisation and the customer.
- IoT (Internet of Things) is the network of physical objects embedded with sensors, software and other technologies that enable them to connect and exchange data with other devices and systems over the internet.
- IoT can improve business processes by automating tasks, gathering valuable information, extending business functions, triggering rules, sourcing predictive analytics and big data, among other useful objectives.
- Some examples of business processes that can benefit from IoT are:
  - Inventory management: IoT devices can track the location, quantity and condition of goods in real time, reducing errors, waste and costs.
  - Quality control: IoT devices can monitor and measure the performance and quality of products and processes, detecting defects, anomalies and deviations, and providing feedback and alerts.
  - Asset management: IoT devices can collect and analyse data from machines and equipment, enabling predictive maintenance, remote control and optimisation of operations.
  - Customer service: IoT devices can enhance the customer experience by providing personalised recommendations, support and feedback, as well as enabling self-service and loyalty programs.
- Some recommendations on implementing IoT business processes in your companies are:
  - To define the business process to improve and identify the problem you want to solve.
  - To use an end-to-end approach that covers the entire value chain of the process, from data collection to action execution.
  - To make agile design and start with POC (proof of concept) prototyping, testing and validating the solution before scaling it up.
  - To get on board the right people, better if you keep it low but with the best knowledge, skills and experience in IoT, business and domain.
  - To be persistent but acknowledgeable to failure, learning from mistakes and improving the solution iteratively.
  - To be aware of the potential disruption that IoT can bring to the existing business models, processes and culture, but not to go crazy about it, and to balance innovation and risk.



# Everything as a Service (XaaS) for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Everything as a Service (XaaS) is a general term that describes the delivery of any IT function as a service over the internet, using cloud computing and remote access technologies  .
- XaaS originated from the Software as a Service (SaaS) model, which provides software applications as a service to users, without requiring them to install or maintain them on their own devices .
- XaaS has expanded to include other types of services, such as Infrastructure as a Service (IaaS), which provides computing resources such as servers, storage, and networking as a service; Platform as a Service (PaaS), which provides development and deployment environments as a service; and more functionally-specific models, such as Storage as a Service, Desktop as a Service (DaaS), and Disaster Recovery as a Service (DRaaS)  .
- XaaS enables users to access and consume IT services on demand, without having to invest in or manage the underlying infrastructure or software  . This reduces the cost, complexity, and risk of IT operations, and increases the scalability, flexibility, and agility of IT solutions   .
- XaaS also allows users to pay only for what they use, based on a subscription or consumption-based pricing model, rather than a fixed or upfront fee   . This shifts the IT expenditure from capital expenditure (CAPEX) to operational expenditure (OPEX), and enables users to adjust their IT spending according to their changing needs and preferences   .
- XaaS is closely related to the concept of the service economy, which is the shift from the production and consumption of goods to the provision and consumption of services . XaaS represents the newest addition to the service economy, as it transforms any IT function into a service that can be delivered and consumed over the internet.
- XaaS is also relevant to the Internet of Things (IoT), which is the network of physical objects that are embedded with sensors, software, and connectivity to collect and exchange data over the internet. XaaS can enable IoT devices to access and use IT services without requiring local processing or storage, and can also provide IoT data as a service to users and applications.
- XaaS can offer various benefits to IoT users and providers, such as:
  - Reducing the cost and complexity of deploying and managing IoT devices and applications.
  - Enhancing the security and privacy of IoT data and devices by leveraging the cloud's encryption and authentication mechanisms.
  - Improving the performance and reliability of IoT solutions by using the cloud's scalability and redundancy features.
  - Enabling the integration and interoperability of IoT devices and applications with other cloud services and platforms.
  - Providing new business opportunities and revenue streams for IoT providers and users by offering IoT data and insights as a service.



# M2M and IoT Analytics

- M2M and IoT are both technologies that enable remote communication and data exchange among machines without human intervention.
- M2M stands for Machine-to-Machine, and IoT stands for Internet of Things.
- The main difference between M2M and IoT is that M2M is a more vertical and closed application that meets specific internal demands, while IoT is a more horizontal and open application that has broader and diverse outcomes .
- M2M systems use point-to-point communications between machines, sensors and hardware over cellular or wired networks, while IoT systems rely on IP-based networks to send data collected from IoT-connected devices to gateways, the cloud or middleware platforms.
- M2M and IoT analytics are the processes of collecting, processing, and analyzing the data generated by M2M and IoT devices to gain insights and optimize performance, efficiency, and decision-making .
- M2M and IoT analytics can be applied to various domains, such as smart cities, smart homes, smart manufacturing, smart agriculture, smart healthcare, smart transportation, and smart energy .
- M2M and IoT analytics can benefit from technologies such as artificial intelligence, machine learning, big data, cloud computing, edge computing, and blockchain to enhance the quality, security, and scalability of the data analysis .



# Knowledge Management for the notes of the Unit 1 - IoT-An Architectural Overview

- Knowledge management (KM) is the process of creating, sharing, using and managing the knowledge and information of an organization or a network of connected devices and entities.
- KM can generate intelligence in IoT ecosystems to enable a digital business and society transformation by leveraging the data, information and knowledge generated by IoT devices and applications.
- IoT architecture is the structure enabling internet-connected devices to communicate with other devices, applications and services across edge and cloud environments.
- IoT architecture comprises of several IoT system building blocks connected to ensure that sensor-generated device data is collected, stored, and processed in the big data warehouse and that devices’ actuators perform commands sent via a user application.
- The following diagram reflects a general approach to IoT architecture:

IoT architecture diagram

- The main components or layers of IoT architecture are:

  - **Things layer**: This layer consists of the physical devices, sensors, actuators and gateways that are connected to the internet and can collect, transmit and receive data. This layer is also known as the perception layer or the edge layer.
  - **Transport layer**: This layer is responsible for the communication and networking of the IoT devices and gateways with the cloud or the data center. This layer can use various protocols and technologies such as Wi-Fi, Bluetooth, Zigbee, cellular, satellite, etc. This layer is also known as the network layer or the access layer.
  - **Processing layer**: This layer is where the data collected by the IoT devices is stored, processed and analyzed using various tools and platforms such as databases, data lakes, stream processing, batch processing, etc. This layer can be located in the cloud or on-premises, depending on the latency, security and scalability requirements. This layer is also known as the data layer or the platform layer.
  - **Application layer**: This layer is where the IoT data is transformed into actionable insights and value-added services for the end-users and stakeholders. This layer can use various applications and services such as dashboards, visualization, analytics, machine learning, artificial intelligence, etc. This layer is also known as the service layer or the business layer.

- IoT architecture can vary depending on the use case, domain, scale and complexity of the IoT solution. However, some common architectural challenges and best practices are:

  - **Security**: IoT architecture should ensure the security and privacy of the IoT devices, data and applications from unauthorized access, tampering, theft, etc. This can be achieved by using encryption, authentication, authorization, firewall, etc.
  - **Interoperability**: IoT architecture should enable the seamless integration and communication of the IoT devices and applications with different standards, protocols and platforms. This can be achieved by using common interfaces, APIs, middleware, etc.
  - **Scalability**: IoT architecture should be able to handle the increasing number and variety of IoT devices, data and applications without compromising the performance, reliability and quality of service. This can be achieved by using cloud computing, edge computing, load balancing, etc.
  - **Reliability**: IoT architecture should ensure the availability and functionality of the IoT devices, data and applications in the event of failures, errors, disruptions, etc. This can be achieved by using redundancy, backup, recovery, fault tolerance, etc.
  - **Performance**: IoT architecture should ensure the timely and efficient delivery and processing of the IoT data and commands with minimal latency, jitter, packet loss, etc. This can be achieved by using real-time processing, edge computing, quality of service, etc.



## Unit 2 - Reference Architecture

- A reference architecture is a general and reusable solution to a commonly occurring problem in a specific domain or context.
- It provides a set of principles, guidelines, patterns, standards, and best practices that can be used to design, implement, and evaluate a specific architecture.
- A reference architecture is not a complete and detailed architecture, but rather a template or blueprint that can be customized and adapted to meet the specific needs and requirements of a particular system or organization.
- A reference architecture can help to:
  - Reduce complexity and ambiguity by providing a common vocabulary and understanding of the problem domain and the solution space.
  - Increase quality and consistency by ensuring that the architecture conforms to the established principles, guidelines, patterns, standards, and best practices.
  - Accelerate development and delivery by reusing proven and tested solutions and avoiding reinventing the wheel.
  - Facilitate communication and collaboration by enabling stakeholders to share and exchange knowledge and experience across different projects and teams.
  - Promote innovation and learning by encouraging experimentation and feedback on the reference architecture and its application.
- A reference architecture can be represented in different ways, such as:
  - A conceptual model that describes the key concepts, entities, relationships, and properties of the domain and the solution.
  - A logical model that defines the structure, behavior, and interactions of the components and subsystems of the solution.
  - A physical model that specifies the deployment, configuration, and runtime aspects of the solution.
  - A view or a viewpoint that focuses on a specific set of concerns or interests of a stakeholder or a group of stakeholders.
- A reference architecture can be developed and maintained using different methods and processes, such as:
  - A top-down approach that starts from a high-level vision and goals and decomposes them into more detailed and concrete elements and artifacts.
  - A bottom-up approach that starts from existing or emerging solutions and generalizes them into more abstract and reusable elements and artifacts.
  - An iterative and incremental approach that evolves the reference architecture over time based on feedback and validation from the stakeholders and the users.
  - A collaborative and participatory approach that involves the stakeholders and the users in the creation and evaluation of the reference architecture.



# IoT Architecture-State of the Art

- Internet of Things (IoT) is a paradigm that enables the interconnection and interaction of physical and virtual objects through the Internet.
- IoT architecture is the design and organization of the components and layers that constitute an IoT system, such as devices, networks, platforms, applications, and services.
- A reference model is a model that describes the main conceptual entities and how they are related to each other, while the reference architecture aims at describing the main functional components of a system as well as how the system works, how the system is deployed, what information the system processes, etc.
- There is no single or universal IoT architecture, but rather different architectures proposed by different organizations, such as the International Telecommunication Union (ITU), the European Telecommunications Standards Institute (ETSI), the Internet Engineering Task Force (IETF), the Open Connectivity Foundation (OCF), and the Industrial Internet Consortium (IIC).
- However, most of the IoT architectures share some common features and layers, such as:
  - Device layer: This layer consists of the physical and virtual objects that are equipped with sensors, actuators, identifiers, and communication interfaces to interact with the environment and other devices.
  - Network layer: This layer provides the connectivity and communication protocols for the devices to exchange data with each other and with other systems, such as the Internet, cellular networks, Wi-Fi, Bluetooth, ZigBee, etc.
  - Platform layer: This layer provides the middleware and services for the management, processing, storage, and analysis of the data collected from the devices, such as cloud computing, fog computing, edge computing, etc.
  - Application layer: This layer provides the end-user applications and services that utilize the data and functionalities of the devices, such as smart home, smart city, smart health, smart agriculture, etc.
- IoT architectures also need to address the challenges and requirements of IoT systems, such as scalability, interoperability, security, privacy, reliability, and quality of service.



# Introduction

- The Internet of Things (IoT) is a network of physical objects that can communicate and interact with each other and with other entities over the Internet.
- IoT devices can range from simple sensors and actuators to complex smart devices and systems that can perform various tasks and functions.
- IoT applications can span across different domains and sectors, such as smart homes, smart cities, smart health, smart agriculture, smart industry, etc.
- To enable the IoT vision, various challenges and requirements need to be addressed, such as interoperability, scalability, security, privacy, reliability, etc.
- To cope with these challenges and requirements, different IoT architectures and protocols have been proposed and developed by various organizations and standardization bodies.
- A reference architecture is a generic and abstract framework that defines the main components, functions, interfaces, and interactions of an IoT system.
- A reference architecture can serve as a common basis for designing, developing, and deploying specific IoT solutions and applications.
- A reference architecture can also facilitate the interoperability and integration of different IoT devices, platforms, and services.
- In this unit, we will study some of the most prominent and widely used reference architectures for IoT, such as:

  - The IoT-A reference architecture
  - The IEEE P2413 reference architecture
  - The oneM2M reference architecture
  - The ITU-T Y.2060 reference architecture
  - The ISO/IEC 30141 reference architecture

- We will also compare and contrast these reference architectures in terms of their scope, objectives, features, and limitations.



# State of the Art for the Notes of the Unit 2 - Reference Architecture in the Subject of IoT Architecture and Protocols

- A reference model is a model that describes the main conceptual entities and how they are related to each other .
- A reference architecture is a description of the main functional components of a system, how the system works, how the system is deployed, what information the system processes, etc .
- A reference architecture can be derived from a reference model by adding more details and specifications.
- A reference architecture can help to guide the design and implementation of IoT systems, as well as to enable interoperability and standardization.
- There are different approaches to define a reference architecture for IoT, depending on the scope, objectives, and requirements of the system.
- Some of the common elements of a reference architecture for IoT are:
  - Devices: The physical objects or things that are connected to the internet, equipped with sensors, actuators, and communication capabilities .
  - Gateways: The intermediate nodes that connect the devices to the network, providing data aggregation, filtering, processing, and security functions .
  - Network: The communication infrastructure that enables data transmission and exchange between the devices, the gateways, and the cloud .
  - Cloud: The centralized platform that provides data storage, analysis, processing, and management services, as well as applications and services for the end-users .
  - Edge: The distributed platform that provides data processing and analysis services closer to the devices, reducing latency, bandwidth, and energy consumption .
- Some of the existing reference architectures for IoT are:
  - The three-layer architecture: A simple and generic architecture that divides the IoT system into three layers: perception, network, and application.
  - The five-layer architecture: An extension of the three-layer architecture that adds two intermediate layers: transport and processing.
  - The IoT-A architecture: A comprehensive and detailed architecture that defines the functional, information, communication, deployment, and trustworthiness views of the IoT system.
  - The RAMI 4.0 architecture: A domain-specific architecture that focuses on the industrial IoT, defining the hierarchy, life cycle, and interoperability levels of the system.
  - The oneM2M architecture: A standard-based architecture that defines the common service layer for IoT, providing a set of functional entities and interfaces for data management, security, discovery, and communication.



# Reference Model and Architecture for IoT

- A reference model is a conceptual framework that defines the common terminology, concepts, and principles for designing and implementing IoT systems.
- A reference architecture is a concrete instantiation of a reference model that provides specific guidelines, best practices, and standards for developing and deploying IoT solutions.
- One of the most widely used reference models for IoT is the IoT World Forum Reference Model, which was proposed by the IoT World Forum, a consortium of industry leaders, academia, and government organizations.
- The IoT World Forum Reference Model consists of seven layers, as shown in the figure below:

IoT World Forum Reference Model

- The seven layers are:

  - **Physical devices and controllers layer**: This layer includes the physical devices, sensors, actuators, and controllers that interact with the physical world and generate data.
  - **Connectivity layer**: This layer provides the communication protocols, standards, and technologies for connecting the devices and controllers to the network and transferring data.
  - **Edge computing layer**: This layer performs data processing, filtering, aggregation, and analysis at the edge of the network, close to the devices, to reduce latency, bandwidth, and storage requirements.
  - **Data accumulation layer**: This layer collects, stores, and manages the data from the edge computing layer and other sources in the cloud or on-premises data centers.
  - **Data abstraction layer**: This layer transforms, normalizes, and enriches the data from the data accumulation layer and exposes it to the upper layers through APIs and services.
  - **Application layer**: This layer provides the business logic, functionality, and user interface for the IoT applications that consume the data and services from the data abstraction layer.
  - **Collaboration and processes layer**: This layer enables the integration, orchestration, and coordination of the IoT applications and services with other systems, processes, and stakeholders.

- The IoT World Forum Reference Model is not the only reference model for IoT, but it is a widely accepted and adopted one that can help to understand the key components and challenges of IoT systems.
- Other reference models for IoT include the IoT Architectural Reference Model (IoT ARM) by the IoT-A project, the IoT Reference Architecture by IBM, and the Azure IoT Reference Architecture by Microsoft.



# IoT Reference Model

The IoT Reference Model is a framework that defines the main concepts and components of IoT systems and architectures. It provides a common language and understanding for IoT systems and enables interoperability and integration among different IoT solutions. The IoT Reference Model consists of the following sub-models:

- **IoT Domain Model**: This sub-model introduces the basic concepts of IoT, such as devices, IoT services, virtual entities, and their relations. A device is a physical object that can sense, actuate, or communicate. An IoT service is a software component that provides functionality or data to other components or users. A virtual entity is a digital representation of a device, a group of devices, or a physical or logical entity that is not a device. A virtual entity can have properties, behaviors, and relationships with other virtual entities.

- **IoT Functional View**: This sub-model defines the main functions and processes that are performed by IoT systems, such as device management, data processing, service discovery, service composition, and security. The functional view also describes the interactions and dependencies among these functions and processes.

- **IoT Information View**: This sub-model specifies the data and information that are exchanged and stored by IoT systems, such as device metadata, sensor data, service descriptions, and context information. The information view also defines the data models, formats, and standards that are used for data representation and communication.

- **IoT Deployment and Operational View**: This sub-model describes the physical and logical deployment of IoT systems, such as the network topology, the communication protocols, the hardware and software platforms, and the cloud and edge computing resources. The deployment and operational view also covers the operational aspects of IoT systems, such as monitoring, maintenance, and scalability.

- **IoT Business View**: This sub-model captures the business aspects of IoT systems, such as the value proposition, the stakeholders, the revenue model, and the governance. The business view also identifies the business requirements, goals, and constraints that drive the design and implementation of IoT systems.

The IoT Reference Model is not a prescriptive or normative architecture, but rather a descriptive and conceptual one. It can be used as a basis for developing specific IoT architectures and solutions that meet the needs and challenges of different IoT domains and applications.



# IoT Reference Architecture

- IoT reference architecture is a conceptual framework that defines the components, interactions, and design principles of IoT solutions.
- IoT reference architecture can help to guide the development, deployment, and management of IoT systems that are scalable, secure, interoperable, and adaptable to different domains and use cases.
- IoT reference architecture can also facilitate the communication and collaboration among different stakeholders, such as developers, vendors, customers, and regulators, by providing a common vocabulary and understanding of IoT concepts and challenges.
- There are different IoT reference architectures proposed by various organizations, such as IBM, Microsoft, and the IoT-A project, which have different scopes, perspectives, and levels of abstraction.
- However, most IoT reference architectures share some common elements, such as:

  - Things: The physical or virtual entities that generate, consume, or exchange data in an IoT system, such as sensors, actuators, devices, gateways, and applications.
  - Connectivity: The communication protocols, networks, and services that enable the data transmission and exchange among things, such as Wi-Fi, Bluetooth, cellular, LoRaWAN, MQTT, and HTTP.
  - Data: The raw or processed information that is generated, collected, stored, analyzed, or consumed by things, such as temperature, humidity, location, speed, and images.
  - Analytics: The processes and techniques that transform data into insights, such as data cleansing, aggregation, filtering, fusion, mining, and machine learning.
  - Actions: The outcomes or responses that are triggered by insights, such as alerts, notifications, commands, and feedback.
  - Security: The mechanisms and policies that ensure the confidentiality, integrity, and availability of data and things, such as encryption, authentication, authorization, and auditing.
  - Management: The functions and tools that enable the monitoring, configuration, and maintenance of things, data, and services, such as device discovery, provisioning, firmware update, and fault detection.

- A possible IoT reference architecture diagram is shown below, based on the Azure IoT reference architecture:

IoT reference architecture diagram

- The diagram illustrates the following components and interactions:

  - Devices: The things that connect to the IoT hub and send or receive data, such as sensors, actuators, cameras, and mobile phones.
  - IoT hub: The cloud service that acts as the central message broker and device management platform for the IoT system, providing secure and reliable communication, device identity and authentication, device twins and direct methods, and device provisioning service.
  - Stream processing: The cloud service that ingests, processes, and analyzes the data streams from the IoT hub, such as Azure Stream Analytics, Azure Functions, or Azure Databricks.
  - Storage: The cloud service that stores the data from the stream processing or the IoT hub, such as Azure Blob Storage, Azure Data Lake Storage, or Azure Cosmos DB.
  - Business applications: The cloud or on-premises applications that consume the data or insights from the storage or the stream processing, such as Power BI, Logic Apps, or custom web apps.
  - User interface: The web or mobile app that allows the users to interact with the IoT system, such as viewing dashboards, sending commands, or receiving notifications.



# Introduction for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- In this unit, we will learn about the reference architecture for the Internet of Things (IoT), which is a conceptual framework that defines the key components, functions, and interfaces of an IoT system.
- A reference architecture provides a common vocabulary, a set of principles and best practices, and a logical structure for designing and implementing IoT solutions.
- A reference architecture can also facilitate interoperability, scalability, security, and manageability of IoT systems across different domains and applications.
- There are various reference architectures proposed by different organizations and standardization bodies for the IoT, such as the IoT-A, the IEEE P2413, the ISO/IEC 30141, and the oneM2M.
- In this unit, we will focus on the oneM2M reference architecture, which is a global standard for machine-to-machine (M2M) and IoT communications.
- The oneM2M reference architecture defines a common service layer that can be embedded in various hardware and software platforms, and that can interact with different network technologies and application domains.
- The oneM2M reference architecture consists of three main entities: the Application Entity (AE), the Common Services Entity (CSE), and the Network Services Entity (NSE).
- The AE represents the application logic and the end-user interface of an IoT system. It can be hosted on devices, gateways, or servers, and it can communicate with other AEs or CSEs using the oneM2M service layer protocols.
- The CSE provides the core functionality of the oneM2M service layer, such as data management, device management, security, discovery, and subscription/notification. It can be hosted on devices, gateways, servers, or cloud platforms, and it can communicate with other CSEs or NSEs using the oneM2M service layer protocols or the underlying network protocols.
- The NSE represents the network infrastructure and the network services that enable the connectivity and the transport of data between CSEs and AEs. It can include various network technologies, such as cellular, Wi-Fi, Bluetooth, Zigbee, or LoRaWAN, and it can communicate with CSEs using the underlying network protocols or the oneM2M service layer protocols.
- The oneM2M reference architecture also defines a set of common service functions (CSFs) that can be implemented by the CSEs or the NSEs, such as registration, access control, group management, location, time series, semantic, and interworking.
- The oneM2M reference architecture supports a variety of deployment scenarios and communication patterns, such as device-to-device, device-to-cloud, device-to-gateway, and gateway-to-cloud.
- The oneM2M reference architecture aims to provide a horizontal and modular approach for developing and integrating IoT systems across different domains and applications, such as smart cities, smart homes, smart health, smart agriculture, and smart industry.



# Functional View for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The functional view of the IoT reference architecture describes the system's runtime functional components, their responsibilities, default functions, interfaces and primary interactions .
- The functional view follows the modular structure of functional blocks organized into layers, as it was proposed e.g. in SENSEI.
- The functional view is use-case- and application-independent and is therefore not compatible to the concept of views and viewpoints one-by-one.
- The functional view consists of four main layers: Device Layer, Network Layer, Service Layer and Application Layer .
- The Device Layer contains the physical devices that are connected to the IoT system, such as sensors, actuators, gateways, etc. The Device Layer is responsible for data acquisition, device management, device discovery and device configuration.
- The Network Layer provides the communication infrastructure and protocols for data transmission between devices and services. The Network Layer is responsible for network management, network discovery, network security and network optimization.
- The Service Layer provides the core functionalities and services of the IoT system, such as data processing, data storage, data analysis, data visualization, etc. The Service Layer is responsible for service management, service discovery, service composition and service orchestration.
- The Application Layer contains the specific applications and use cases that utilize the IoT system, such as smart home, smart city, smart health, etc. The Application Layer is responsible for application management, application discovery, application integration and application customization.
- The functional view also defines the cross-layer functionalities that span across multiple layers, such as security, privacy, trust, identity, etc. These functionalities are responsible for ensuring the reliability, safety, and quality of the IoT system.
- The functional view can be represented by a diagram that shows the functional components, their interfaces, and their interactions. An example of such a diagram is shown below :

```
+-----------------+      +-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |      |                 |
|  Application    |      |   Service       |      |   Network       |      |   Device        |
|    Layer        |      |    Layer        |      |    Layer        |      |    Layer        |
|                 |      |                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |      |                 |
|  Application    |      |   Service       |      |   Network       |      |   Device        |
|  Management     |      |  Management     |      |  Management     |      |  Management     |
|                 |      |                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |      |                 |
|  Application    |      |   Service       |      |   Network       |      |   Device        |
|  Discovery      |      |  Discovery      |      |  Discovery      |      |  Discovery      |
|                 |      |                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |      |                 |
|  Application    |      |   Service       |      |   Network       |      |   Device        |
|  Integration    |      |  Composition    |      |  Security       |      |  Configuration  |
|                 |      |                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |      |                 |
|  Application    |      |   Service       |      |   Network       |      |   Data          |
|  Customization  |      |  Orchestration  |      |  Optimization   |      |  Acquisition    |
|                 |      |                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |

```




# Information View for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The information view describes the data and information that the system handles, such as the data sources, data flows, data formats, data transformations, data storage, and data analysis .
- The information view can be divided into three sub-views: data ingestion, data processing, and data consumption.
- Data ingestion refers to the process of collecting, filtering, validating, and normalizing data from various devices and sources, such as sensors, microcontrollers, industrial equipment, etc. Data ingestion can be done using protocols such as MQTT, HTTP, AMQP, CoAP, etc. Data ingestion can also involve data encryption, compression, and batching .
- Data processing refers to the process of storing, analyzing, and transforming data using various services and technologies, such as databases, data lakes, data warehouses, stream analytics, machine learning, etc. Data processing can be done using platforms such as Azure IoT Hub, Azure IoT Edge, Azure Stream Analytics, Azure Data Lake, Azure Synapse Analytics, etc. Data processing can also involve data quality, data governance, data security, and data privacy  .
- Data consumption refers to the process of delivering, visualizing, and acting on data using various applications and interfaces, such as dashboards, reports, alerts, notifications, commands, etc. Data consumption can be done using services such as Azure IoT Central, Azure Power BI, Azure Logic Apps, Azure Notification Hubs, etc. Data consumption can also involve data integration, data sharing, data feedback, and data monetization  .
- The information view can help to design and implement an IoT solution that meets the functional and non-functional requirements, such as scalability, reliability, performance, security, etc. The information view can also help to identify the data sources, data flows, data formats, data transformations, data storage, and data analysis that are needed for the IoT solution .



# Deployment and Operational View for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The deployment and operational view describes the main real world components of the system such as devices, network routers, servers, etc. and how they are deployed and operated in the IoT environment .
- The deployment view focuses on the physical layout and configuration of the system components, such as the hardware, software, and network resources.
- The operational view focuses on the runtime behavior and management of the system components, such as the communication protocols, data flows, security mechanisms, and monitoring tools.
- The deployment and operational view can vary depending on the specific IoT domain and application, but there are some common aspects that are practically invariant over the IoT domain, such as:
  - The IoT system consists of three main layers: the device layer, the gateway layer, and the cloud layer.
  - The device layer contains the sensors, actuators, and embedded devices that interact with the physical world and generate or consume data.
  - The gateway layer contains the network routers, gateways, and edge devices that connect the device layer to the cloud layer and provide data aggregation, filtering, processing, and security functions.
  - The cloud layer contains the servers, databases, and applications that store, analyze, and visualize the data from the device layer and provide services and feedback to the users and devices.
- The deployment and operational view can also address the following aspects of the IoT system:
  - The scalability, reliability, availability, and performance of the system components and the network connections.
  - The security, privacy, and trust of the data and the system components and the network connections.
  - The interoperability, compatibility, and standardization of the system components and the network connections.
  - The lifecycle, maintenance, and evolution of the system components and the network connections.



# Other Relevant Architectural Views for IoT

- Besides the reference architecture, there are other ways to design and describe IoT systems based on different contexts, perspectives, and goals.
- Some of the other relevant architectural views for IoT are:

## Application-Specific Architecture
- This view focuses on the specific requirements and features of a particular IoT application domain, such as smart home, smart city, smart health, etc.
- It defines the functional components, data flows, communication protocols, and interfaces for the application domain.
- It may also consider the non-functional aspects, such as security, privacy, scalability, reliability, etc.
- An example of an application-specific architecture is the Smart Home Architecture proposed by the European Telecommunications Standards Institute (ETSI) .

## Open Platform Architecture
- This view aims to provide a generic and interoperable framework for IoT systems that can support multiple application domains and devices.
- It defines the common services, platforms, and standards that enable the integration and collaboration of heterogeneous IoT components and systems.
- It may also address the cross-cutting concerns, such as data management, analytics, security, privacy, etc.
- An example of an open platform architecture is the IoT-A Reference Architecture proposed by the IoT-Architecture (IoT-A) project .

## Network as a Service (NaaS) Architecture
- This view focuses on the network infrastructure and connectivity aspects of IoT systems.
- It defines the network services, resources, and capabilities that enable the communication and data exchange among IoT devices and systems.
- It may also consider the network optimization, management, and security issues.
- An example of a NaaS architecture is the Software-Defined Networking (SDN) Architecture proposed by the Open Networking Foundation (ONF) .



# Real-World Design Constraints for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Real-world design constraints are the factors that limit or influence the design and implementation of IoT solutions in various domains and applications.
- Some of the common real-world design constraints are:
  - **Technical constraints**: These are the challenges related to the devices, networks, protocols, standards, interoperability, security, scalability, reliability, and performance of IoT systems. For example, how to select or design devices that are suitable for IoT applications, how to ensure connectivity and communication among heterogeneous devices and networks, how to manage the data and services of IoT systems, how to secure the data and devices from unauthorized access or attacks, how to scale up the IoT systems to handle the increasing number of devices and data, how to ensure the reliability and availability of IoT systems, and how to optimize the performance and efficiency of IoT systems  .
  - **Social constraints**: These are the challenges related to the human aspects, such as user acceptance, user experience, user privacy, user trust, user behavior, user feedback, and user participation in IoT systems. For example, how to design IoT systems that are user-friendly, intuitive, and accessible, how to protect the user privacy and personal data from being exposed or misused, how to build user trust and confidence in IoT systems, how to understand and influence user behavior and preferences, how to collect and utilize user feedback and suggestions, and how to engage and motivate user participation and collaboration in IoT systems .
  - **Economic constraints**: These are the challenges related to the cost, benefit, value, and sustainability of IoT systems. For example, how to estimate and justify the cost and benefit of IoT systems, how to create and capture the value and competitive advantage of IoT systems, how to ensure the sustainability and profitability of IoT systems, and how to deal with the legal, ethical, and regulatory issues of IoT systems  .
- Real-world design constraints are not fixed or static, but dynamic and evolving, as the IoT technology and applications change and develop over time. Therefore, IoT designers and developers need to constantly monitor, evaluate, and adapt to the real-world design constraints in order to create and implement effective and successful IoT solutions.



# Introduction

- The reference architecture for IoT is a conceptual framework that defines the essential components and interactions of an IoT system.
- The reference architecture for IoT provides a common vocabulary, a set of principles and guidelines, and a set of best practices for designing and implementing IoT solutions.
- The reference architecture for IoT is not a fixed or prescriptive model, but rather a flexible and adaptable one that can accommodate different use cases, domains, and requirements.
- The reference architecture for IoT can help stakeholders to understand the scope, complexity, and challenges of IoT, and to identify the key architectural decisions and trade-offs that need to be made.
- The reference architecture for IoT can also facilitate interoperability, security, and scalability of IoT systems, by promoting the use of standards, protocols, and interfaces.
- The reference architecture for IoT can be divided into four layers: the device layer, the network layer, the service layer, and the application layer. Each layer has a specific role and function in the IoT system, and interacts with the other layers through well-defined interfaces.
- The device layer consists of the physical and virtual devices that generate, process, and exchange data in the IoT system. The devices can be sensors, actuators, gateways, or embedded systems, and can have different capabilities, protocols, and power consumption levels.
- The network layer provides the connectivity and communication between the devices and the service layer. The network layer can use various technologies and protocols, such as wired or wireless, cellular or non-cellular, IP-based or non-IP-based, to transmit data over different distances and speeds.
- The service layer provides the core functionality and intelligence of the IoT system. The service layer can perform data aggregation, analysis, processing, storage, and management, as well as provide services such as device management, security, identity, discovery, and orchestration.
- The application layer provides the user interface and the business logic of the IoT system. The application layer can enable various use cases and scenarios, such as smart home, smart city, smart health, smart agriculture, etc., and can interact with the end users and other applications through different channels and platforms.



# Technical Design Constraints Hardware

Technical design constraints are the limitations or requirements that affect the design of a hardware system, such as an IoT device. Some of the common technical design constraints for IoT hardware are:

- **Power consumption**: IoT devices often need to operate on battery power or harvest energy from the environment, which limits the amount of power they can use for sensing, processing, communication, and security. Power consumption also affects the lifetime, reliability, and maintenance of IoT devices. Designers need to optimize the power efficiency of IoT hardware components and use low-power protocols and techniques to reduce the energy consumption of IoT devices .
- **Security**: IoT devices are exposed to various security threats, such as physical tampering, eavesdropping, spoofing, denial-of-service, and malware attacks. Security is essential to protect the data, privacy, and functionality of IoT devices and networks. Designers need to implement security mechanisms at the hardware level, such as encryption, authentication, secure boot, and tamper detection, to prevent unauthorized access and modification of IoT devices .
- **Flexibility**: IoT devices need to be flexible and adaptable to run different applications and protocols over embedded systems, which may have limited resources and capabilities. Flexibility also enables IoT devices to update and upgrade their software and firmware to cope with changing requirements and standards. Designers need to use modular and scalable hardware architectures and platforms that can support various IoT functionalities and features .
- **Testing**: IoT devices need to be tested and verified for their functionality, performance, reliability, and compatibility before deployment. Testing is challenging for IoT devices due to the complexity, diversity, and heterogeneity of IoT systems and environments. Designers need to use effective testing methods and tools that can simulate and emulate the real-world conditions and scenarios of IoT devices and networks .
- **Cost and time-to-market**: IoT devices need to be cost-effective and competitive in the market, which requires reducing the hardware design and development costs and time. Cost and time-to-market also affect the profitability and sustainability of IoT products and services. Designers need to use standardized and reusable hardware components and platforms that can reduce the design complexity and overhead and accelerate the hardware prototyping and production .



# Data representation and visualization for IoT

- Data representation and visualization are essential for understanding and analyzing the large and complex data generated by IoT devices and applications.
- Data representation refers to the process of transforming raw data into a format that can be easily stored, processed, and communicated. Data representation can involve data compression, encryption, encoding, serialization, and standardization.
- Data visualization refers to the process of presenting data in a graphical or pictorial form that can reveal patterns, trends, correlations, and outliers. Data visualization can involve data aggregation, filtering, transformation, and mapping.
- Data representation and visualization for IoT can have various benefits, such as:
  - Enhancing the user experience and interaction with IoT devices and applications.
  - Providing real-time feedback and insights for decision making and problem solving.
  - Reducing the cognitive load and complexity of data analysis and interpretation.
  - Improving the performance and efficiency of data processing and transmission.
  - Enabling data exploration and discovery for innovation and creativity.
- Data representation and visualization for IoT can also have various challenges, such as:
  - Dealing with the high volume, velocity, variety, and veracity of IoT data.
  - Ensuring the security, privacy, and integrity of IoT data.
  - Choosing the appropriate data representation and visualization techniques and tools for different IoT scenarios and users.
  - Evaluating the effectiveness and accuracy of data representation and visualization outcomes.
- Data representation and visualization for IoT can follow different patterns and best practices, such as:
  - Using data compression and encryption techniques to reduce the size and protect the content of IoT data.
  - Using data encoding and serialization techniques to convert IoT data into a common and interoperable format, such as JSON, XML, or Protobuf.
  - Using data standardization techniques to adhere to the IoT data models and schemas, such as MQTT, CoAP, or LwM2M.
  - Using data aggregation and filtering techniques to reduce the noise and redundancy of IoT data and extract the relevant and meaningful information.
  - Using data transformation and mapping techniques to prepare IoT data for visualization, such as normalization, scaling, or projection.
  - Using data visualization techniques and tools to create interactive and dynamic charts, graphs, maps, or dashboards that can display IoT data in a clear and intuitive way, such as D3.js, Plotly, or QuickSight.
  - Using data evaluation techniques and metrics to measure the quality and impact of data representation and visualization outcomes, such as accuracy, completeness, timeliness, usability, or usefulness.



# Interaction and Remote Control in IoT

- Interaction and remote control are two important aspects of IoT applications that enable users, service providers, and support teams to access, monitor, and manage IoT devices remotely through the internet.
- Interaction refers to the interfaces that allow users to communicate with IoT devices, such as mobile applications, web browsers, embedded touchscreens, voice assistants, etc. Interaction can be used for various purposes, such as:
  - Configuring the settings and preferences of IoT devices
  - Controlling the functions and operations of IoT devices
  - Monitoring the status and performance of IoT devices
  - Receiving feedback and alerts from IoT devices
- Remote control refers to the ability to access and manipulate IoT devices from a distance, without physical contact. Remote control can be used for various purposes, such as:
  - Updating the firmware and software of IoT devices
  - Troubleshooting and debugging IoT devices
  - Performing maintenance and repairs of IoT devices
  - Collecting and analyzing data from IoT devices
- Interaction and remote control in IoT require secure and reliable communication protocols, such as MQTT, CoAP, HTTP, etc. These protocols enable data exchange between IoT devices and cloud platforms, as well as between IoT devices and users.
- Interaction and remote control in IoT also require authentication and authorization mechanisms, such as passwords, tokens, certificates, etc. These mechanisms ensure that only authorized parties can access and control IoT devices, and prevent unauthorized access and attacks.



# Unit 3 - IOT Data Link Layer & Network Layer Protocols

## Data Link Layer Protocols

- The data link layer provides service to the network layer and is responsible for reliable transmission of data frames between nodes on the same network.
- There are various protocols and standard technologies specified by different organizations for data link protocols in IoT.
- Some of the common data link layer protocols in IoT are:

  - **Bluetooth**: A short-range wireless communication network over a radio frequency. It allows devices to form a personal area network (PAN) and exchange data and voice. It supports low-power and low-cost devices and has different versions such as Bluetooth Low Energy (BLE) and Bluetooth Mesh.
  - **Ethernet**: A wired LAN technology that uses twisted pair or coaxial cables to connect devices. It provides data transfer rates as high as 100 Mbps and supports multiple topologies such as bus, star, and ring. It is widely used for industrial and enterprise IoT applications that require high reliability and security.
  - **Wi-Fi**: A wireless LAN technology that uses radio waves to provide internet access to devices. It supports various standards such as IEEE 802.11a/b/g/n/ac/ax and offers high data rates, range, and bandwidth. It is suitable for home and office IoT applications that require internet connectivity and interoperability.
  - **WiMAX**: A wireless broadband technology that provides high-speed internet access over long distances. It uses microwave frequencies and supports various standards such as IEEE 802.16d/e/m. It is designed for metropolitan area networks (MANs) and rural IoT applications that require wide coverage and mobility.
  - **Low-rate WPAN**: A wireless personal area network that operates at low data rates, low power, and short range. It uses various technologies such as Zigbee, Z-Wave, 6LoWPAN, and Thread. It is ideal for smart home and building IoT applications that require low-cost, low-complexity, and mesh networking.

## Network Layer Protocols

- The network layer is responsible for addressing and routing of data packets between nodes on different networks. It provides service to the transport layer and uses the data link layer for physical transmission.
- There are various protocols and standard technologies specified by different organizations for network layer protocols in IoT.
- Some of the common network layer protocols in IoT are:

  - **IPv4**: The most widely used internet protocol that assigns 32-bit addresses to devices and uses various routing protocols such as RIP, OSPF, and BGP. It supports various features such as fragmentation, checksum, and options. It suffers from address exhaustion and security issues in IoT.
  - **IPv6**: The next generation internet protocol that assigns 128-bit addresses to devices and uses various routing protocols such as RIPng, OSPFv3, and BGP4+. It supports various features such as auto-configuration, mobility, and security. It is designed to overcome the limitations of IPv4 and enable IoT scalability and interoperability.
  - **ICMP**: The internet control message protocol that is used to send error and control messages between devices. It supports various types of messages such as echo, destination unreachable, time exceeded, and parameter problem. It is used for diagnostic and troubleshooting purposes in IoT.
  - **CoAP**: The constrained application protocol that is a lightweight version of HTTP for resource-constrained devices. It uses UDP as the transport protocol and supports various features such as caching, discovery, and observation. It is used for RESTful web services and machine-to-machine communication in IoT.
  - **MQTT**: The message queuing telemetry transport protocol that is a publish-subscribe messaging protocol for IoT. It uses TCP as the transport protocol and supports various features such as quality of service, retain, and last will. It is used for data collection and distribution in IoT.



# PHY/MAC Layer(3GPP MTC)

- PHY (Physical) layer is the lowest layer of the 3GPP radio interface protocol stack that handles the transmission and reception of data over the wireless channel.
- MAC (Medium Access Control) layer is the sub-layer of the 3GPP Layer 2 that controls the access to the shared radio resources and multiplexes the data from different logical channels onto the transport channels.
- 3GPP MTC (Machine Type Communication) is a term used to describe the communications of devices that generate or consume small and infrequent data traffic, such as sensors, smart meters, and wearable devices.
- 3GPP has developed several technologies and enhancements for the PHY and MAC layers to support the MTC requirements, such as low cost, low power consumption, high reliability, and massive connectivity.
- Some of the PHY and MAC layer solutions for MTC are:

  - Narrowband IoT (NB-IoT): A new radio access technology that operates in narrowband spectrum and provides low data rate, wide area coverage, and deep indoor penetration for MTC devices.
  - LTE-M: A set of features that enable LTE to support MTC devices with low complexity, low power consumption, and extended coverage.
  - Enhanced Coverage GSM IoT (EC-GSM-IoT): A set of enhancements to GSM that improve the coverage, capacity, and power efficiency of MTC devices using GSM spectrum.
  - Power Saving Mode (PSM) and Extended Discontinuous Reception (eDRX): Two mechanisms that allow MTC devices to enter a low power state and reduce the frequency of signaling and paging, thus extending the battery life.
  - Single Cell Point to Multipoint (SC-PTM): A transmission mode that enables a single cell to broadcast data to multiple MTC devices simultaneously, thus improving the spectral efficiency and reducing the signaling overhead.
  - Random Access Enhancements: A set of modifications to the random access procedure that reduce the collision probability and the access delay for MTC devices, such as preamble repetition, early data transmission, and access class barring.
  - Small Data Transmission (SDT): A set of procedures that enable MTC devices to transmit or receive small data packets without establishing a dedicated radio bearer, thus reducing the signaling overhead and the latency.



# IEEE 802.11

- IEEE 802.11 is a set of standards for wireless local area networks (WLANs) developed by the IEEE 802.11 Working Group .
- IEEE 802.11 defines the physical layer (PHY) and the medium access control (MAC) layer of WLANs, as well as various amendments and extensions to enhance the performance, security, and functionality of WLANs  .
- IEEE 802.11 is used in most home and office networks to allow laptops, printers, smartphones, and other devices to communicate with each other and access the Internet without connecting wires.
- IEEE 802.11 is also a basis for vehicle-based communication networks with IEEE 802.11p, which is part of the dedicated short-range communications (DSRC) standard for intelligent transportation systems (ITS).
- IEEE 802.11 has several variants, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, which differ in terms of frequency band, modulation scheme, data rate, channel width, and range.
- IEEE 802.11 also has some amendments that define new physical layers for WLANs, such as 802.11ad, which operates in the 60 GHz millimeter wave spectrum, and 802.11ah, which operates in the sub-1 GHz spectrum.
- IEEE 802.11 is a dynamic and evolving standard that is constantly updated and revised to meet the changing needs and demands of WLAN users and applications.



# IEEE 802.15

- IEEE 802.15 is a working group of the Institute of Electrical and Electronics Engineers (IEEE) IEEE 802 standards committee which specifies Wireless Specialty Networks (WSN) standards .
- The working group was formerly known as Working Group for Wireless Personal Area Networks (WPANs) .
- The working group has developed several standards and amendments for low-rate wireless connectivity, such as IEEE 802.15.1 (Bluetooth), IEEE 802.15.4 (ZigBee), IEEE 802.15.4a (Ultra-wideband), IEEE 802.15.5 (Mesh networking), IEEE 802.15.6 (Body area network), and IEEE 802.15.7 (Visible light communication) .
- The IEEE 802.15 standards are suitable for IoT applications that require low power consumption, low data rate, short range, and low cost .
- The IEEE 802.15 standards use different frequency bands, modulation schemes, and channel access methods to achieve different trade-offs between performance, reliability, and complexity .
- The IEEE 802.15 standards are compatible with the IEEE 802.2 logical link control (LLC) layer, which provides a common interface to the network layer protocols .
- The IEEE 802.15 standards are also interoperable with other IEEE 802 standards, such as IEEE 802.11 (Wi-Fi), IEEE 802.16 (WiMAX), and IEEE 802.3 (Ethernet) .



# WirelessHART

- WirelessHART is a wireless communications protocol for process automation applications. It adds wireless capabilities to HART technology while maintaining compatibility with existing HART devices, commands, and tools.
- WirelessHART is based on the Highway Addressable Remote Transducer Protocol (HART), which is an open and interoperable standard for communication between field devices and control systems.
- WirelessHART uses 2.4 GHz radio waves to transmit process data from individual instruments to a common gateway device, which serves as an interface between the wireless network and a wired network or a host control system.
- WirelessHART employs mesh networking technology, which means that each device can act as a router and relay messages from other devices. This enhances the reliability and security of the network, as well as the flexibility and scalability of the topology.
- WirelessHART supports self-organizing and self-healing networks, which means that the devices can automatically discover the best routes and adjust to changes in the environment or the network configuration.
- WirelessHART uses time division multiple access (TDMA) and channel hopping to avoid interference and ensure data integrity. Each device is assigned a 10 ms time slot for communication, and the network uses 15 channels that are randomly selected for each transmission.
- WirelessHART provides several security features, such as encryption, authentication, verification, and key management, to protect the network from unauthorized access or malicious attacks.
- WirelessHART offers several benefits for process automation, such as reduced wiring costs, increased availability of data, improved asset management, and enhanced safety and environmental compliance.



# ZWave

ZWave is a wireless communication protocol designed for smart home and IoT devices. It operates on the low-frequency 800 to 900 MHz band, which avoids interference with the 2.4 GHz band where Wi-Fi and Bluetooth operate. ZWave uses a mesh network topology, where each device can relay messages to other devices within range, increasing the network coverage and reliability. ZWave supports encryption and security features to protect the data and devices from unauthorized access. ZWave is a proprietary protocol developed by Sigma Designs, Inc., but there is also an open source implementation called open-zwave.

Some of the main features and advantages of ZWave are:

- Low power consumption: ZWave devices can run on batteries for years, making them suitable for sensors and controllers that do not need constant power supply.
- Scalability: ZWave networks can support up to 232 devices, which can be added or removed easily without affecting the network performance.
- Interoperability: ZWave devices from different manufacturers can work together, as long as they comply with the ZWave certification standards and use the same frequency band.
- Compatibility: ZWave devices can integrate with other smart home and IoT platforms, such as Amazon Alexa, Google Home, Samsung SmartThings, etc., through hubs or gateways that support ZWave protocol.
- Simplicity: ZWave devices are easy to install and configure, as they use a simple pairing process and do not require complex settings or passwords.



# Bluetooth Low Energy

- Bluetooth Low Energy (BLE) is a wireless personal area network technology designed and marketed by the Bluetooth Special Interest Group (Bluetooth SIG) aimed at novel applications in the healthcare, fitness, beacons, security, and home entertainment industries.
- BLE is distinct from the previous (often called "classic") Bluetooth Basic Rate/Enhanced Data Rate (BR/EDR) protocol, but the two protocols can both be supported by one device: the Bluetooth 4.0 specification permits devices to implement either or both of the LE and BR/EDR systems.
- BLE has the following advantages over classic Bluetooth:
  - Lower power consumption: BLE devices can operate for months or years on a coin cell battery, while classic Bluetooth devices require frequent recharging.
  - Faster connection time: BLE devices can connect in a few milliseconds, while classic Bluetooth devices may take several seconds.
  - Simpler pairing process: BLE devices can use a variety of methods to pair, such as scanning a QR code, tapping a NFC tag, or using a proximity-based trigger, while classic Bluetooth devices require a PIN code or a confirmation button.
  - Higher scalability: BLE devices can support up to 20 concurrent connections, while classic Bluetooth devices are limited to 7.
- BLE uses two protocols for discovery and communication between devices: the Generic Access Profile (GAP) and the Generic Attribute Profile (GATT).
  - GAP defines how devices advertise themselves and discover other devices in the vicinity. GAP also defines the roles and modes of devices, such as peripheral (device that advertises data) and central (device that scans for data), broadcaster (device that sends data without connection) and observer (device that receives data without connection), and bonded (device that has a trusted relationship with another device) and non-bonded (device that has no trusted relationship with another device).
  - GATT defines how devices exchange data using a client-server model. GATT also defines the structure and format of data, such as services (collections of related data), characteristics (individual data elements), and descriptors (metadata about characteristics). GATT also defines the operations that can be performed on data, such as read, write, notify, and indicate.



# Zigbee Smart Energy

Zigbee Smart Energy is a wireless protocol that enables smart devices to monitor, control, inform and automate the delivery and use of energy, gas and water. It is designed to help utilities and consumers reduce waste, optimize consumption, and improve efficiency and sustainability. Some of the features and benefits of Zigbee Smart Energy are:

- It is based on the Zigbee standard, which is a low-cost, low-power, and secure mesh network technology that operates in the 2.4 GHz and sub-GHz frequency bands.
- It supports interoperability and certification of devices from different vendors, ensuring compatibility and reliability.
- It allows bidirectional communication between smart meters, smart appliances, smart thermostats, smart plugs, and other smart devices, enabling demand response, load control, time-of-use pricing, and prepayment services.
- It integrates with Internet Protocol (IP) networks, allowing access and control of smart devices from smartphones, tablets, computers, and cloud services.
- It supports advanced security features, such as encryption, authentication, and key management, to protect data and devices from unauthorized access and tampering.
- It supports over-the-air firmware updates, allowing devices to receive new features and bug fixes without requiring physical intervention.



# DASH7

- DASH7 is an open-source wireless sensor and actuator network protocol, which operates in the 433 MHz, 868 MHz and 915 MHz unlicensed ISM band /SRD band.
- DASH7 is based on the ISO 18000-7 standard for active radio frequency identification (RFID).
- DASH7 supports bi-directional, low-power, low-latency, and long-range communication for sensor and actuator applications.
- DASH7 has several advantages over other wireless protocols, such as:
  - It can penetrate walls, water, and metal, and has a range of up to 2 km in urban environments and 40 km in rural areas.
  - It can operate on a single coin cell battery for up to 10 years, and has a low duty cycle of less than 0.1%.
  - It can support up to 250 kbps data rate, and has a low latency of less than 1 second.
  - It can support up to 1.5 million nodes per network, and has a flexible addressing scheme that allows for multicast, broadcast, and unicast communication.
  - It can support security features such as encryption, authentication, and anti-cloning.
- DASH7 has several applications, such as:
  - Tire pressure monitoring systems (TPMS) for vehicles, which can provide more accurate readings and improve fuel economy, safety, and tire wear .
  - Supply chain visibility and asset tracking, which can reduce inventory costs, theft, and loss .
  - Smart metering and energy management, which can enable remote monitoring and control of electricity, gas, and water consumption.
  - Environmental monitoring and agriculture, which can measure soil moisture, temperature, humidity, and other parameters.
  - Healthcare and wellness, which can monitor vital signs, medication adherence, and activity levels of patients and elderly people.
  - Industrial automation and control, which can optimize production processes, quality, and safety.



# Network Layer

The network layer is the third layer of the OSI model and the second layer of the TCP/IP model. It is responsible for addressing and routing of data packets in a network. It also performs functions such as fragmentation, reassembly, congestion control, and error detection.

## Network Layer in IoT

In the context of IoT, the network layer is part of the infrastructure layer in the IoT reference architecture. It enables communication and connectivity between devices in the IoT system, as well as with the wider internet. The network layer in IoT is mainly divided into two parts:

- The routing layer, which sends packets from origin to destination using various routing protocols and algorithms.
- The encapsulation layer, which creates packets by adding headers and trailers to the datagrams from the transport layer. The headers contain information such as source and destination IP addresses, packet length, and checksum.

## Network Layer Protocols in IoT

There are various protocols that can be used at the network layer in IoT, depending on the requirements and constraints of the application and the network. Some of the common network layer protocols in IoT are :

- IPv4 and IPv6, which are the standard protocols for internet communication. IPv4 uses 32-bit addresses, while IPv6 uses 128-bit addresses, which allows for more scalability and security. IPv6 also supports features such as stateless address autoconfiguration, neighbor discovery, and multicast.
- 6LoWPAN, which stands for IPv6 over Low-Power Wireless Personal Area Networks. It is a protocol that adapts IPv6 to work over low-power and low-bandwidth networks, such as ZigBee, Bluetooth Low Energy, and IEEE 802.15.4. It uses header compression, fragmentation, and reassembly techniques to reduce the overhead of IPv6 packets.
- RPL, which stands for Routing Protocol for Low-Power and Lossy Networks. It is a protocol that provides efficient and reliable routing for IoT networks that have limited resources and high packet loss. It uses a Directed Acyclic Graph (DAG) structure to organize the network topology and supports multiple routing metrics and objectives.
- CoAP, which stands for Constrained Application Protocol. It is a protocol that provides a lightweight and RESTful application layer interface for IoT devices. It uses UDP as the transport protocol and supports features such as caching, discovery, observation, and multicast.



# IPv4

- IPv4 stands for Internet Protocol version 4, which is the fourth version in the development of the Internet Protocol (IP) and the first version of the protocol to be widely deployed .
- IPv4 is a numeric address that consists of 32 bits, which are divided into four octets (bytes) separated by dots. Each octet can have a value between 0 and 255 in decimal notation . For example, 192.168.0.1 is a valid IPv4 address.
- IPv4 has 12 header fields, each of which has a fixed length of 20 bytes. The header fields contain information such as the source and destination addresses, the protocol type, the packet length, the time to live (TTL), and the checksum .
- IPv4 supports different types of addresses, such as unicast, broadcast, and multicast. Unicast addresses are used to identify a single host on the network, broadcast addresses are used to send a packet to all hosts on the network, and multicast addresses are used to send a packet to a group of hosts on the network .
- IPv4 also supports variable length subnet masking (VLSM), which allows the network administrator to divide the network into subnets of different sizes, depending on the number of hosts and the traffic requirements .
- IPv4 has a limited address space of 2^32, which is about 4.3 billion addresses. Due to the rapid growth of the Internet, IPv4 addresses are running out and a new version of IP, called IPv6, has been developed to overcome this limitation .



# IPv6

IPv6 is the next generation Internet Protocol (IP) standard intended to eventually replace IPv4, the protocol many Internet services still use today. IPv6 is designed to solve many of the problems of IPv4, such as address depletion, security, auto-configuration, extensibility, and so on. IPv6 expands the capabilities of the Internet to enable new kinds of applications, including peer-to-peer and mobile applications.

Some of the important features and uses of IPv6 are:

- IPv6 addresses: An IPv6 address uses 128 bits, four times more than the IPv4 address, which uses only 32 bits. This allows for a much larger address space, which can accommodate more devices and networks on the Internet. IPv6 addresses are written using hexadecimal, as opposed to dotted decimal in IPv4. For example, an IPv6 address may look like this: 2001:db8:0:1234:0:567:8:1.
- Network and node addresses: In IPv4, address classes were used to split an address into two components: a network component and a node component. In IPv6, the address is divided into two parts: a 64-bit network prefix and a 64-bit interface identifier. The network prefix identifies the network to which the device belongs, and the interface identifier identifies the device on that network. The interface identifier can be derived from the MAC address of the device, or randomly generated.
- IPv6 address types and scope: IPv6 defines different types of addresses for different purposes and scopes. Some of the common address types are:

  - Link-local: These addresses are used for communication within a single network segment, such as a LAN. They are not routable on the Internet, and start with fe80::/10.
  - Global unicast: These addresses are used for communication on the global Internet, and are unique and routable. They start with 2000::/3.
  - Unique local: These addresses are used for communication within a private network, such as a VPN or a corporate network. They are not routable on the Internet, and are similar to IPv4 private addresses. They start with fc00::/7.
  - Multicast: These addresses are used for sending data to multiple recipients at the same time, such as video streaming or online gaming. They start with ff00::/8.
  - Anycast: These addresses are used for sending data to the nearest or best available node that provides a certain service, such as DNS or CDN. They are assigned from the global unicast address space, and are shared by multiple nodes.
  - Loopback: This address is used for testing the connectivity of the device to itself. It is equivalent to the IPv4 address 127.0.0.1, and is represented by ::1 in IPv6.

- Using IPv6 addresses in uniform resource locators (URLs): To use an IPv6 address in a URL, the address must be enclosed in square brackets, followed by the port number if needed. For example, http://[2001:db8:0:1234:0:567:8:1]:80/index.html.
- IPv6 loopback: The IPv6 loopback is a special address that is used for testing the connectivity of the device to itself. It is equivalent to the IPv4 address 127.0.0.1, and is represented by ::1 in IPv6. For example, to ping the loopback address, one can use the command ping ::1.



# 6LoWPAN

- 6LoWPAN stands for IPv6 over Low-power Wireless Personal Area Networks.
- It is an open standard defined by the Internet Engineering Task Force (IETF) that enables low-power devices with limited processing capabilities to participate in the Internet of Things (IoT) by using IPv6 over IEEE 802.15.4 based networks .
- 6LoWPAN defines mechanisms for:
  - Encapsulation: how to fragment and reassemble IPv6 datagrams over the IEEE 802.15.4 frame size limit of 127 bytes.
  - Header compression: how to reduce the size of IPv6 and UDP headers to fit in the IEEE 802.15.4 frame payload.
  - Neighbor discovery: how to discover and register IPv6 addresses and prefixes of other nodes in the network.
  - Routing: how to forward IPv6 datagrams over multiple hops using either mesh-under or route-over approaches.
- 6LoWPAN networks can be connected to other IPv6 networks through edge routers that perform translation and adaptation functions.
- 6LoWPAN networks can also support IPv6 transition mechanisms to connect to IPv4 networks, such as NAT64, without requiring the 6LoWPAN nodes to implement IPv4.
- 6LoWPAN networks can support various applications that require wireless internet connectivity at lower data rates, such as residential and office automation, smart grid, industrial monitoring, etc.



# 6TiSCH

- 6TiSCH stands for IPv6 over the Time Slotted Channel Hopping (TSCH) mode of IEEE 802.15.4e.
- It is a protocol suite that enables reliable and delay-bounded communication in multi-hop and scalable Industrial Internet of Things (IIoT) networks.
- It combines the benefits of TSCH, which provides deterministic medium access and frequency diversity, with IPv6, which enables seamless integration with the Internet and end-to-end addressability.
- It consists of several components, such as:
  - The 6TiSCH Operation Sublayer (6top), which defines the interface between the TSCH MAC layer and the IPv6 adaptation layer (6LoWPAN).
  - The 6top Protocol (6P), which enables distributed and dynamic scheduling of TSCH cells among neighboring nodes.
  - The 6TiSCH Minimal Scheduling Function (MSF), which is a default algorithm for 6P to allocate and deallocate cells based on traffic demand and link quality.
  - The 6TiSCH Minimal Security Framework (MSF), which defines the minimal security mechanisms for joining and operating in a 6TiSCH network.
  - The 6TiSCH Minimal Configuration (6MC), which specifies the default values and parameters for 6TiSCH nodes.
  - The 6TiSCH Architecture, which describes the overall structure and functionality of a 6TiSCH network, including the roles of nodes, the routing protocol (RPL), and the IP-in-IP encapsulation for interconnecting different 6TiSCH domains.
- 6TiSCH is a working group at the Internet Engineering Task Force (IETF), which is standardizing the protocols and specifications for 6TiSCH networks.



# Unit 3 - IOT Data Link Layer & Network Layer Protocols

## Data Link Layer Protocols

- The data link layer provides service to the network layer and is responsible for reliable and efficient transmission of data frames between nodes on the same network.
- There are various protocols and standard technologies specified by different organizations for data link protocols in IoT.
- Some of the common data link layer protocols in IoT are:

  - **Bluetooth**: A short-range wireless communication network over a radio frequency. It allows devices to connect and exchange data with low power consumption and high security. Bluetooth supports different profiles for different applications, such as audio, health, smart home, etc. Bluetooth Low Energy (BLE) is a variant of Bluetooth that is optimized for IoT devices with low data rates and long battery life.
  - **Wi-Fi**: A wireless LAN technology that uses radio waves to provide high-speed internet access and network connectivity. Wi-Fi is widely used for home and office networks, as well as public hotspots. Wi-Fi supports various standards, such as 802.11a/b/g/n/ac/ax, that differ in frequency, bandwidth, range, and data rates. Wi-Fi is suitable for IoT applications that require high data throughput and low latency, such as video streaming, smart appliances, etc.
  - **Zigbee**: A low-power wireless mesh network protocol that operates in the 2.4 GHz frequency band. Zigbee is based on the IEEE 802.15.4 standard and supports various network topologies, such as star, tree, and mesh. Zigbee is designed for IoT applications that require low data rates, long battery life, and large network size, such as smart lighting, security, and environmental monitoring.
  - **Z-Wave**: A low-power wireless network protocol that operates in the sub-GHz frequency band. Z-Wave is based on the ITU-T G.9959 standard and supports a mesh network topology. Z-Wave is designed for IoT applications that require low data rates, long battery life, and interoperability, such as smart home, energy management, and healthcare.
  - **LoRa**: A long-range wireless network protocol that operates in the sub-GHz frequency band. LoRa is based on the LoRaWAN specification and supports a star-of-stars network topology. LoRa is designed for IoT applications that require low data rates, long range, and low power consumption, such as smart agriculture, smart city, and asset tracking.

## Network Layer Protocols

- The network layer provides service to the transport layer and is responsible for addressing and routing of data packets between nodes on different networks.
- There are various protocols and standard technologies specified by different organizations for network layer protocols in IoT.
- Some of the common network layer protocols in IoT are:

  - **IPv4**: The fourth version of the Internet Protocol that uses 32-bit addresses to identify nodes on a network. IPv4 is the most widely used network protocol on the internet and supports various features, such as fragmentation, checksum, and quality of service. IPv4 is suitable for IoT applications that require high reliability and compatibility, such as web services, cloud computing, and multimedia.
  - **IPv6**: The sixth version of the Internet Protocol that uses 128-bit addresses to identify nodes on a network. IPv6 is the successor of IPv4 and supports various features, such as auto-configuration, security, and mobility. IPv6 is suitable for IoT applications that require large address space and scalability, such as smart grid, smart transportation, and smart city.
  - **6LoWPAN**: A network protocol that enables IPv6 packets to be transmitted over low-power wireless personal area networks (LoWPANs), such as IEEE 802.15.4, Bluetooth, and Zigbee. 6LoWPAN is based on the RFC 4944 standard and supports various features, such as header compression, fragmentation, and adaptation. 6LoWPAN is suitable for IoT applications that require low power consumption and interoperability, such as sensor networks, smart home, and industrial automation.
  - **RPL**: A routing protocol that enables data packets to be routed over low-power and lossy networks (LLNs), such as IEEE 802.15.4, Bluetooth, and Zigbee. RPL is based on the RFC 6550 standard and supports various features, such as loop avoidance, multipath routing, and objective function. RPL is suitable for IoT applications that require low power consumption and robustness, such as sensor networks, smart home, and industrial automation.
  - **CoAP**: A network protocol that enables constrained devices to communicate with



# DHCP

- DHCP stands for Dynamic Host Configuration Protocol  .
- It is a network management protocol that automatically provides an Internet Protocol (IP) host with its IP address and other related configuration information such as the subnet mask and default gateway .
- It uses a client-server architecture, where a DHCP server allocates IP addresses and other parameters to DHCP clients that request them  .
- It is based on the Bootstrap Protocol (BOOTP), which was designed for diskless systems to obtain configuration information from a network server .
- It is defined by RFCs 2131 and 2132, and is an Internet Engineering Task Force (IETF) standard.
- It operates on the application layer of the TCP/IP model, and uses UDP port 67 for server and UDP port 68 for client communication .
- It supports four types of messages: DHCPDISCOVER, DHCPOFFER, DHCPREQUEST, and DHCPACK .
- It follows a four-step process to assign an IP address to a client: discover, offer, request, and acknowledge .
- It can assign IP addresses in three ways: manual, automatic, and dynamic .
- It can also provide other options, such as DNS servers, NTP servers, domain name, etc. to the clients .
- It can be used for various purposes, such as simplifying network administration, reducing configuration errors, supporting mobile users, etc. .



# ICMP

- ICMP stands for Internet Control Message Protocol  .
- It is a network layer protocol used by network devices to diagnose network communication issues  .
- It is not associated with any transport layer protocol, such as TCP or UDP .
- It is a connectionless protocol, meaning a device does not need to open a connection with the target device before sending a message.
- It is used to generate error messages to the source IP address when network problems prevent delivery of IP packets.
- It is also used to determine whether or not data is reaching its intended destination in a timely manner .
- It is also used for inter-device communication, carrying everything from redirect instructions to timestamps for synchronization between devices.
- Some common types of ICMP messages are:
  - Echo request and echo reply: used to test the reachability and latency of a destination device.
  - Destination unreachable: used to inform the source device that the destination device or network is unreachable.
  - Time exceeded: used to inform the source device that the time to live (TTL) of a packet has expired.
  - Parameter problem: used to inform the source device that a packet has an invalid or missing header field.
  - Source quench: used to inform the source device that the destination device is congested and cannot process more packets.
  - Redirect: used to inform the source device that there is a better route to the destination device or network.
- ICMP is important for IOT devices because it helps to monitor and troubleshoot the network connectivity and performance of the devices .
- ICMP can also be used for malicious purposes, such as denial-of-service (DoS) attacks, by flooding a target device with ICMP packets and overwhelming its resources .
- ICMP can also be used for reconnaissance, by scanning a network for active devices and their characteristics using ICMP packets .



# RPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for Routing Protocol for Low-Power and Lossy Networks.
- It is an IPv6 routing protocol that is standardized for the Internet of Things (IoT) by Internet-Engineering Task Force (IETF) .
- It is designed to operate in resource-constrained networks, such as wireless sensor networks, smart grid networks, home automation networks, etc. .
- It forms a tree-like topology, which is based on different optimizing processes called Objective Functions (OFs) .
- OFs define the metrics and constraints for selecting the best paths in the network, such as hop count, energy consumption, link quality, etc. .
- RPL supports both many-to-one and one-to-one communication, as well as multicast and anycast .
- RPL uses two types of messages: control messages and data messages .
- Control messages are used to build and maintain the network topology, such as DODAG Information Object (DIO), Destination Advertisement Object (DAO), DODAG Information Solicitation (DIS), etc. .
- Data messages are used to carry the application data, such as ICMPv6, UDP, TCP, etc. .
- RPL has several advantages, such as scalability, adaptability, interoperability, security, etc. .
- RPL also has some challenges, such as loop detection, mobility support, network dynamics, etc. .



# CORPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- CORPL stands for **C**ontrol **O**bjective **R**outing **P**rotocol for **L**ow-Power and Lossy Networks.
- It is a network layer protocol that is designed for IoT applications that require reliable and energy-efficient data delivery.
- It is based on the RPL protocol, which is the standard routing protocol for low-power and lossy networks (LLNs) defined by the IETF .
- CORPL differs from RPL in the following aspects:
  - It uses a **control objective function (COF)** to select the best routes based on multiple metrics, such as hop count, link quality, energy consumption, and delay.
  - It employs a **dynamic parent set (DPS)** mechanism to maintain multiple backup parents for each node, which increases the network resilience and load balancing.
  - It adopts a **cross-layer feedback (CLF)** scheme to monitor the link quality and energy status of each node, which enables the COF to adapt to the network dynamics and optimize the routing performance.
- CORPL has been shown to outperform RPL in terms of packet delivery ratio, end-to-end delay, energy consumption, and network lifetime in various simulation scenarios.



# CARP

- CARP stands for Channel-Aware Routing Protocol  .
- It is a transport layer protocol developed for underwater networks.
- It is suitable for IoT implementations as header size in this protocol is very small.
- The protocol keeps track of data communication history to select nodes for data transfer.
- It is a distributed routing protocol that does not require any central coordination .
- It uses a probabilistic approach to forward packets based on the channel quality and the distance to the destination .
- It aims to reduce the end-to-end delay and increase the packet delivery ratio .
- It can adapt to the dynamic and harsh underwater environment .



## Unit 4 - Transport & Session Layer Protocols

The transport layer and the session layer are two of the seven layers of the Open Systems Interconnection (OSI) model. They are responsible for providing reliable and efficient communication between applications on different devices.

- The transport layer (layer 4) is the lowest layer that deals with end-to-end communication. It provides services such as error detection, flow control, congestion control, and segmentation of data. It also ensures that data is delivered in the correct order and without duplication. The transport layer can be either connection-oriented or connectionless, depending on the protocol used. The most common transport layer protocols are:

  - Transmission Control Protocol (TCP): A connection-oriented protocol that establishes a virtual circuit between two endpoints and guarantees reliable and ordered delivery of data. TCP uses a three-way handshake to establish a connection, and a four-way handshake to terminate it. TCP also uses acknowledgments, sequence numbers, and sliding window mechanism to ensure reliability and flow control. TCP is suitable for applications that require high reliability and data integrity, such as web browsing, email, and file transfer.

  - User Datagram Protocol (UDP): A connectionless protocol that sends datagrams without establishing a connection or ensuring reliability. UDP does not use acknowledgments, sequence numbers, or flow control. UDP is suitable for applications that require low latency and high speed, such as voice over IP, video streaming, and online gaming.

  - Stream Control Transmission Protocol (SCTP): A connection-oriented protocol that supports multiple streams of data within a single connection. SCTP provides reliable and ordered delivery of data, as well as congestion control and error detection. SCTP also supports multihoming, which allows a device to have multiple IP addresses and switch between them in case of failure. SCTP is suitable for applications that require high availability and flexibility, such as telephony and signaling.

  - Datagram Congestion Control Protocol (DCCP): A connection-oriented protocol that provides congestion control for unreliable datagrams. DCCP does not guarantee reliable or ordered delivery of data, but it allows applications to choose the level of reliability they need. DCCP also supports features such as multipath, encryption, and authentication. DCCP is suitable for applications that require congestion control and adaptability, such as multimedia and interactive applications.

- The session layer (layer 5) is the layer that manages the sessions between applications. It provides services such as session establishment, maintenance, and termination, as well as synchronization, dialog control, and security. The session layer can use different protocols depending on the application and the transport layer protocol. Some of the session layer protocols are:

  - Session Initiation Protocol (SIP): A protocol that initiates, modifies, and terminates multimedia sessions over the Internet. SIP uses a request-response model and supports features such as caller ID, call forwarding, call transfer, and conferencing. SIP can use TCP, UDP, or SCTP as the transport layer protocol.

  - Remote Procedure Call (RPC): A protocol that allows a program to execute a procedure on a remote device. RPC uses a client-server model and supports features such as authentication, encryption, and compression. RPC can use TCP or UDP as the transport layer protocol.

  - Network File System (NFS): A protocol that allows a device to access files on a remote device. NFS uses a client-server model and supports features such as caching, locking, and permission control. NFS can use TCP or UDP as the transport layer protocol.

  - Simple Network Management Protocol (SNMP): A protocol that allows a device to monitor and manage other devices on a network. SNMP uses a manager-agent model and supports features such as polling, traps, and configuration. SNMP can use TCP or UDP as the transport layer protocol.



# Transport Layer for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The transport layer is the fourth layer in the OSI model and the TCP/IP model. It is responsible for end-to-end communication and data transmission between devices in an IoT system.
- The transport layer provides features such as reliability, congestion control, flow control, error detection, and ordering of packets. It also enables multiplexing and demultiplexing of data streams from different applications or processes.
- The transport layer can use different protocols depending on the requirements and characteristics of the IoT application and network. Some of the common transport layer protocols in IoT are:

  - **Transmission Control Protocol (TCP)**: TCP is a connection-oriented and reliable protocol that ensures the delivery of data without errors, duplication, or loss. TCP uses a three-way handshake to establish a connection, and a four-way handshake to terminate it. TCP also uses acknowledgments, sequence numbers, and timers to detect and recover from errors, and window-based mechanisms to control the flow and congestion of data. TCP is suitable for IoT applications that require high reliability and data integrity, such as remote monitoring, control, and firmware updates. However, TCP also has some drawbacks, such as high overhead, latency, and energy consumption, which may limit its performance and scalability in resource-constrained IoT devices and networks.
  - **User Datagram Protocol (UDP)**: UDP is a connectionless and unreliable protocol that does not guarantee the delivery of data. UDP does not use any handshaking, acknowledgment, or error recovery mechanisms, and does not impose any flow or congestion control. UDP is suitable for IoT applications that require low latency, high throughput, and real-time communication, such as video streaming, voice over IP, and gaming. However, UDP also has some drawbacks, such as lack of reliability, security, and quality of service, which may affect the performance and user experience of IoT applications.
  - **Constrained Application Protocol (CoAP)**: CoAP is a specialized protocol designed for constrained IoT devices and networks. CoAP is based on the RESTful architecture and uses UDP as the underlying transport protocol. CoAP provides features such as lightweight messaging, asynchronous communication, resource discovery, caching, and observe. CoAP also supports security, reliability, and congestion control through optional mechanisms. CoAP is suitable for IoT applications that require low power consumption, interoperability, and scalability, such as smart home, smart city, and smart agriculture.
  - **Message Queue Telemetry Transport (MQTT)**: MQTT is a publish-subscribe protocol that enables efficient and reliable data exchange between IoT devices and applications. MQTT uses TCP as the underlying transport protocol and provides features such as quality of service, retain, and last will and testament. MQTT also supports security through Transport Layer Security (TLS) and authentication mechanisms. MQTT is suitable for IoT applications that require low bandwidth, high scalability, and loose coupling, such as industrial automation, smart grid, and healthcare.



# TCP

TCP stands for Transmission Control Protocol. It is a transport layer protocol that facilitates the transmission of packets from source to destination. It is a connection-oriented protocol that means it establishes the connection prior to the communication that occurs between the computing devices in a network.

Some of the main features and functions of TCP are:

- TCP is reliable as it follows the flow and error control mechanism. It also supports the acknowledgment mechanism, which checks the state and sound arrival of the data.
- TCP provides ordered and error-free delivery of data by using sequence numbers and checksums.
- TCP uses a sliding window protocol to control the amount of data that can be sent at a time. It also implements congestion control and avoidance algorithms to prevent network overload.
- TCP uses a three-way handshake to establish a connection between the sender and the receiver. It also uses a four-way handshake to terminate the connection gracefully.
- TCP is used by application protocols like HTTP and FTP that require reliable and ordered delivery of data.

: https://www.javatpoint.com/tcp
: https://www.geeksforgeeks.org/tcp-and-udp-in-transport-layer/
: https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:the-internet/xcae6f4a7ff015e7d:transporting-packets/a/transmission-control-protocol--tcp



# MPTCP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- MPTCP stands for Multipath TCP, which is an extension of TCP for simultaneous transmission over several paths .
- MPTCP can improve the throughput, reliability, and security of data transmission in IoT networks, especially when the IoT devices are equipped with multiple network access interfaces .
- MPTCP has several working modes, such as backup mode, which uses one path as the primary path and the others as backups, and load balancing mode, which distributes the traffic among all available paths .
- MPTCP has been implemented and evaluated on various platforms, such as Linux, Android, and Apple iOS, but there are no official MPTCP kernels for IoT devices yet.
- MPTCP can be combined with opportunistic routing, which is a routing technique that exploits the broadcast nature of wireless networks and selects the best next hop based on the current network conditions.
- MPTCP and opportunistic routing can enhance the performance and resilience of IoT networks, especially in scenarios where the network topology is dynamic and the link quality is variable.



# UDP

UDP stands for User Datagram Protocol. It is one of the core communication protocols of the Internet protocol suite used to send messages (transported as datagrams in packets) to other hosts on an Internet Protocol (IP) network.

Some of the main features and characteristics of UDP are:

- UDP is a simple message-oriented transport layer protocol that is documented in RFC 768.
- UDP provides integrity verification (via checksum) of the header and payload, but it provides no guarantees to the upper layer protocol for message delivery and the UDP layer retains no state of UDP messages once sent.
- UDP is a connectionless protocol, which means that there is no need to establish a connection prior to data transfer.
- UDP is suitable for applications that require low-latency and loss-tolerating connections, such as streaming media, online gaming, voice over IP, etc.
- UDP provides a mechanism to detect corrupt data in packets, but it does not attempt to solve other problems that arise with packets, such as lost or out of order packets.
- UDP has a fixed header size of 8 bytes, which consists of four fields: source port, destination port, length, and checksum.
- UDP does not provide any flow control, congestion control, or error recovery mechanisms, which are left to the application layer to handle.
- UDP can support both one-to-one and one-to-many communication modes, such as unicast, multicast, and broadcast.



# DCCP

DCCP stands for Datagram Congestion Control Protocol. It is a message-oriented transport layer protocol that provides bidirectional unicast connections of congestion-controlled unreliable datagrams . DCCP is suitable for applications that transfer fairly large amounts of data, but can benefit from control over the tradeoff between timeliness and reliability. Some examples of such applications are streaming media, online games, and voice over IP.

Some of the main features of DCCP are:

- It implements reliable connection setup and teardown, using a three-way handshake and a four-way handshake respectively .
- It supports Explicit Congestion Notification (ECN), which allows routers to mark packets as experiencing congestion instead of dropping them .
- It allows the sender and the receiver to negotiate and select a specific congestion control mechanism, such as TCP-like, TCP-friendly, or TCP-low priority .
- It provides a feature negotiation mechanism, which allows the endpoints to enable or disable optional features, such as acknowledgments, checksums, or encryption .
- It uses a 48-bit sequence number and a 24-bit acknowledgment number to identify and acknowledge packets, which reduces the risk of sequence number wraparound and duplicate packets .
- It uses a generic header and a variable-length options field to encode different types of packets, such as data, acknowledgment, request, response, close, or reset .
- It supports half-closed connections, which allow one endpoint to stop sending data while the other endpoint can continue to send data .

DCCP is designed to be a flexible and extensible protocol that can accommodate different application requirements and network conditions. It is also intended to be compatible with existing network infrastructure and protocols, such as IP, UDP, and ICMP . DCCP is defined in RFC 4340, which was published by the IETF as a proposed standard in March 2006.



# SCTP

SCTP stands for Stream Control Transmission Protocol. It is a transport layer protocol in the Internet protocol suite that provides reliable and in-sequence data transmission over a connectionless packet network such as IP. It is designed to transport Public Switched Telephone Network (PSTN) signaling messages over IP networks, but is capable of broader applications. It supports multiple streams of data simultaneously between two endpoints that have established a connection.

Some of the features of SCTP are:

- It uses chunks to encapsulate messages and control information. Each chunk has a chunk header that identifies the type, length and flags of the chunk. There are two types of chunks: data chunks and control chunks. Data chunks carry user data from one application to another. Control chunks carry information for the management of the SCTP association, such as initiation, termination, acknowledgment, etc.
- It can fragment a message into multiple data chunks, but each data chunk contains data from only one user message. SCTP bundles the chunks into SCTP packets, which are then transmitted over the network. Each SCTP packet has a common header that contains the source and destination port numbers, a verification tag and a checksum.
- It supports multiple streams of data within a single SCTP association. A stream is a logical sequence of data chunks that belong to the same message. Streams are identified by stream identifiers and stream sequence numbers. Streams allow the application to send multiple messages concurrently without blocking or head-of-line blocking. Streams also provide partial reliability and unordered delivery options for the application.
- It provides congestion control and flow control mechanisms to avoid network congestion and ensure fair bandwidth allocation among different SCTP associations. It uses a window-based scheme similar to TCP, but with some enhancements, such as fast retransmit, fast recovery, selective acknowledgment, etc.
- It supports multihoming, which means that an endpoint can have more than one IP address. Multihoming provides network redundancy and fault tolerance for the SCTP association. If one of the IP addresses becomes unreachable, SCTP can switch to another IP address without disrupting the data transmission. SCTP also performs path management and path selection to monitor the availability and quality of the network paths between the endpoints.



# Session Layer for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The session layer manages the connection between two endpoints of a network by controlling the data exchange between the sender and the receiver  .
- The session layer protocols are responsible for the actual transmission of data in the IoT ecosystem. That's why they are also called as IoT messaging protocols or IoT data protocols  .
- The session layer protocols provide various functions such as:
  - Establishing, maintaining and terminating sessions between devices.
  - Synchronizing data transfer and ensuring data integrity.
  - Managing the dialog control and the communication mode (half-duplex or full-duplex).
  - Handling token management and preventing simultaneous access or collision.
  - Providing security and encryption mechanisms.
- The session layer protocols are reviewed and standardized by different organizations such as IEEE, IETF, OASIS, etc.
- Some of the common session layer protocols in IoT are:
  - MQTT (Message Queuing Telemetry Transport): A lightweight and publish-subscribe based protocol that works well with low-power and low-bandwidth devices  .
  - CoAP (Constrained Application Protocol): A web transfer protocol that is designed for constrained devices and networks. It supports RESTful services and uses UDP as the transport layer protocol  .
  - AMQP (Advanced Message Queuing Protocol): An open and interoperable protocol that supports reliable and secure messaging between applications and devices  .
  - XMPP (Extensible Messaging and Presence Protocol): An XML-based protocol that enables real-time communication and presence information exchange between devices and applications  .
  - DDS (Data Distribution Service): A standard that defines a data-centric and publish-subscribe based communication model for distributed systems. It supports high-performance and real-time data exchange  .
  - STOMP (Simple Text Oriented Messaging Protocol): A simple and text-based protocol that allows interoperability among different message brokers. It uses a frame-based format and supports various transport layer protocols  .



# HTTP

HTTP stands for Hypertext Transfer Protocol. It is an application-layer protocol for transmitting hypermedia documents, such as HTML. It was designed for communication between web browsers and web servers, but it can also be used for other purposes.

Some basic concepts of HTTP are:

- HTTP is a client-server protocol: requests are sent by one entity, the user-agent (or a proxy on behalf of it). Most of the time the user-agent is a web browser, but it can be anything, for example, a robot that crawls the web to populate and maintain a search engine index.
- HTTP is a stateless protocol: each request and response pair is independent of each other, and the server does not keep any information about the previous or future requests from the same client.
- HTTP is an extensible protocol: it relies on concepts like resources and Uniform Resource Identifiers (URIs), simple message structure, and client-server communication flow. On top of these basic concepts, numerous extensions have been developed over the years that add updated functionality and semantics with new HTTP methods or headers.

Some common features of HTTP are:

- HTTP methods: these are the verbs that indicate the action to be performed on a resource, such as GET, POST, PUT, DELETE, etc.
- HTTP headers: these are the key-value pairs that provide additional information about the request or the response, such as Content-Type, Content-Length, Accept, Cookie, etc.
- HTTP status codes: these are the numerical codes that indicate the outcome of the request, such as 200 OK, 404 Not Found, 500 Internal Server Error, etc.
- HTTP messages: these are the actual data that are exchanged between the client and the server, consisting of a start-line, zero or more headers, an empty line, and an optional message body.
- HTTP cookies: these are small pieces of data that are stored by the user-agent and sent back to the server with each request, to enable stateful sessions and personalization.
- HTTP authentication: this is the mechanism by which the user-agent can provide credentials to the server to access protected resources, using schemes such as Basic, Digest, or Bearer.
- HTTP proxy and tunneling: these are the techniques by which the user-agent can communicate with the server through an intermediary, to bypass network restrictions or enhance security.



# CoAP Protocol

- CoAP stands for **Constrained Application Protocol** and it is defined in **RFC 7252** .
- CoAP is an **application-layer protocol** that is intended for use in **resource-constrained Internet devices**, such as wireless sensor network nodes.
- CoAP is designed to easily translate to **HTTP** for simplified integration with the web, while also meeting specialized requirements such as **multicast support**, **very low overhead**, and **simplicity**.
- CoAP is a **client-server protocol** that enables clients to make requests for web transfers as per the need of the hour and servers to respond to arriving requests.
- CoAP is based on the **REST** (Representational State Transfer) architectural style, which means that it follows a **stateless** and **uniform** interface for accessing resources.
- CoAP uses **UDP** (User Datagram Protocol) as the underlying transport layer protocol, which makes it suitable for unreliable and low-power networks.
- CoAP supports four types of **methods**: **GET**, **POST**, **PUT**, and **DELETE**, which correspond to the HTTP methods for retrieving, creating, updating, and deleting resources, respectively.
- CoAP also supports four types of **messages**: **Confirmable**, **Non-confirmable**, **Acknowledgement**, and **Reset**, which are used to ensure reliable and asynchronous communication.
- CoAP uses a simple binary format for encoding messages, which consists of a fixed **header** (4 bytes), a variable-length **token** (0-8 bytes), optional **options**, and an optional **payload**.
- CoAP defines a number of **options** that can be used to specify various parameters of the request or response, such as **Content-Type**, **Content-Format**, **URI-Path**, **URI-Query**, **Observe**, **Block**, etc.
- CoAP supports two types of **responses**: **Piggybacked** and **Separate**, which differ in the way they are delivered to the client. Piggybacked responses are sent within the acknowledgement message, while separate responses are sent as a new confirmable message.
- CoAP supports two types of **resource discovery** mechanisms: **.well-known/core** and **.well-known/linkformat**, which allow clients to query the server for the available resources and their attributes.
- CoAP supports two types of **security** mechanisms: **DTLS** (Datagram Transport Layer Security) and **OSCORE** (Object Security for Constrained RESTful Environments), which provide encryption, authentication, and integrity protection for CoAP messages.
- CoAP is an **IoT protocol** that has interesting features specifically designed for constrained devices. There are other IoT protocols useful to build IoT solutions, such as **MQTT**, **AMQP**, **DDS**, etc.



# XMPP

- XMPP stands for **Extensible Messaging and Presence Protocol** .
- It is an **open communication protocol** designed for **instant messaging (IM)**, **presence information**, and **contact list maintenance** .
- It is based on **XML (Extensible Markup Language)**, which enables the **near-real-time exchange of structured data** between two or more network entities.
- It is a **decentralized protocol**, meaning that anyone can run their own XMPP server and communicate with other servers.
- It is a **living standard**, meaning that engineers actively extend and improve it.
- It supports various features and applications, such as:
  - **IoT (Internet of Things)**: XMPP can be used to connect and control devices and sensors over the internet.
  - **WebRTC (Web Real-Time Communication)**: XMPP can be used to establish peer-to-peer audio and video calls in the browser.
  - **Online Gaming**: XMPP can be used to create multiplayer games and chat rooms.
  - **Realtime Social**: XMPP can be used to create social networks and microblogging platforms.
- It uses a **client-server architecture**, where clients connect to servers using TCP or WebSocket connections.
- It uses a **stream-oriented protocol**, where XML elements are sent and received as **stanzas**.
- It uses a **Jabber ID (JID)** to identify users and resources, which has the format **user@domain/resource**.
- It uses a **service discovery mechanism (XEP-0030)** to query the capabilities and features of other entities.
- It uses a **presence mechanism (XEP-0163)** to broadcast and receive the availability and status of other entities.
- It uses a **message mechanism (XEP-0079)** to send and receive text, media, and other data.
- It uses a **roster mechanism (XEP-0162)** to manage the contact list of users.
- It uses a **pubsub mechanism (XEP-0060)** to publish and subscribe to events and notifications.
- It uses various **extensions (XEPs)** to add more functionality and features to the core protocol .

: XMPP - Wikipedia
: XMPP | The universal messaging standard



# AMQP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- AMQP stands for Advanced Message Queuing Protocol. It is an open standard, binary application layer protocol designed for message-oriented middleware.
- AMQP enables encrypted and interoperable messaging between organizations and applications. The protocol is used in client/server messaging and in IoT device management.
- AMQP has a reliable, secure, interoperable, open, and standard properties, along with its low overhead characteristics, making it a good solution for IoT applications.
- AMQP protocol standardizes messaging using Producers, Brokers and Consumers. Producers send messages to a broker, which stores them in queues until they are consumed by consumers.
- AMQP supports two types of messaging patterns: point-to-point and publish-subscribe. Point-to-point messaging involves one producer and one consumer, while publish-subscribe messaging involves one producer and multiple consumers.
- AMQP supports two types of authentication mechanisms: claims-based security (CBS) and Simple Authentication and Security Layer (SASL). CBS uses tokens to grant access to resources, while SASL uses username and password or shared access signature (SAS) to authenticate clients.
- AMQP supports two types of transport protocols: TCP and WebSockets. TCP is the default transport protocol for AMQP, which provides reliable and ordered delivery of messages. WebSockets is an alternative transport protocol for AMQP, which enables AMQP to work over HTTP proxies and firewalls.
- AMQP supports two types of message delivery modes: at-most-once and at-least-once. At-most-once delivery mode ensures that a message is delivered to a consumer at most once, but it may be lost in transit. At-least-once delivery mode ensures that a message is delivered to a consumer at least once, but it may be duplicated in transit.
- AMQP supports two types of message acknowledgements: automatic and manual. Automatic acknowledgement means that the broker assumes that the consumer has received the message as soon as it is sent. Manual acknowledgement means that the consumer has to explicitly send an acknowledgement to the broker after receiving the message.
- AMQP supports two types of message properties: standard and application-specific. Standard properties are defined by the AMQP specification and include headers, delivery mode, priority, expiration, etc. Application-specific properties are defined by the application and include any custom information that the application needs to process the message.



# MQTT

MQTT is a lightweight, open, and standards-based messaging protocol for the Internet of Things (IoT). It is designed for connections with remote locations that have devices with resource constraints or limited network bandwidth, such as smart sensors, wearables, and other IoT devices. It employs a publish/subscribe communication pattern, which allows for efficient and reliable message delivery between device to cloud and cloud to device.

Some of the main features and benefits of MQTT are:

- It is simple and easy to implement, with a small code footprint and minimal network overhead.
- It supports Quality of Service (QoS) levels, which enable different delivery guarantees for messages, such as at most once, at least once, or exactly once.
- It supports persistent sessions, which allow clients to resume communication after a network interruption without losing any messages.
- It supports retained messages, which allow clients to receive the last message published on a topic when they subscribe to it.
- It supports wildcard subscriptions, which allow clients to subscribe to multiple topics with a single subscription.
- It supports last will and testament messages, which allow clients to notify other clients about their disconnection or failure.
- It supports secure communication, with optional encryption and authentication mechanisms.

Some of the main components and concepts of MQTT are:

- Broker: A server that handles the communication between clients and manages the topics and subscriptions.
- Client: A device or application that connects to the broker and publishes or subscribes to topics.
- Topic: A hierarchical name that identifies the content of a message. Topics are case-sensitive and can have multiple levels separated by slashes (/).
- Message: A payload of data that is published by a client on a topic and delivered to other clients that subscribe to that topic.
- Publish: The action of sending a message to the broker on a specific topic.
- Subscribe: The action of registering interest in receiving messages on a specific topic or topics from the broker.
- QoS: The level of delivery guarantee for a message, which can be 0 (at most once), 1 (at least once), or 2 (exactly once).
- Retain: A flag that indicates whether a message should be stored by the broker and delivered to new subscribers on a topic.
- Clean session: A flag that indicates whether a client wants to start a new session or resume an existing session with the broker.
- Last will: A message that a client can specify to be published by the broker on its behalf when it disconnects unexpectedly.
- Keep alive: A time interval that a client uses to ping the broker and indicate that it is still alive.



## Unit 5 - Service Layer Protocols & Security

- The service layer is a layer in the telecommunication network architecture that provides capability servers owned by a network service provider, accessed through open and secure Application Programming Interfaces (APIs) by application layer servers owned by third-party content providers.
- The service layer also provides an interface to core networks at a lower resource layer.
- Service layer protocols are protocols that operate at the service layer and provide various security services to the application layer protocols and the users.
- Some examples of service layer protocols are:
  - Secure Socket Layer (SSL) protocol: It is an internet security protocol used for exchanging information between a web browser and a web server in a secure manner. It provides two basic security services like authentication and confidentiality.
  - Transport Layer Security (TLS) protocol: It is an extension of SSL protocol that provides more security features and enhancements. It is located between the application protocol layer and the TCP/IP layer, where it can secure and send application data to the transport layer.
  - Application Transparent Transport Layer Security (AT-TLS) protocol: It is a protocol that enables applications to use TLS without modifying the application code. It intercepts the application data and encrypts or decrypts it using TLS before sending or receiving it over the network.
  - Kerberos protocol: It is a protocol that provides authentication, authorization and encryption services in a distributed network environment. It uses tickets and keys to verify the identity of users and servers and to protect the communication between them.
  - Open Shortest Path First (OSPF) authentication: It is a protocol that provides security for the OSPF routing protocol by using cryptographic keys to authenticate the OSPF packets. It prevents unauthorized routers from joining the OSPF network or modifying the routing information.
  - Simple Network Management Protocol version 3 (SNMPv3) protocol: It is a protocol that provides security for the SNMP network management protocol by using encryption and authentication mechanisms. It protects the SNMP messages from being tampered, spoofed or disclosed.



# Service Layer for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The service layer is the layer that provides the interface between the application layer and the network layer in the IoT architecture.
- The service layer is responsible for discovering, managing, and accessing the IoT devices, services, and resources over the internet or cloud networks.
- The service layer also provides security, privacy, and trust mechanisms to ensure the integrity, confidentiality, and availability of the IoT data and services.
- Some of the main functions of the service layer are:

  - Service discovery: The process of finding and registering the IoT devices, services, and resources on the network or cloud.
  - Service management: The process of monitoring, controlling, and configuring the IoT devices, services, and resources on the network or cloud.
  - Service access: The process of enabling the communication and data exchange between the IoT devices, services, and resources on the network or cloud.
  - Service security: The process of protecting the IoT devices, services, and resources from unauthorized access, modification, or disruption on the network or cloud.

- Some of the main protocols and standards used in the service layer are:

  - AMQP: Advanced Message Queuing Protocol, an open standard protocol for message-oriented middleware that supports reliable, secure, and scalable communication between IoT devices and applications.
  - CoAP: Constrained Application Protocol, a lightweight protocol for resource-constrained IoT devices that supports RESTful web services and interoperability with HTTP.
  - MQTT: Message Queuing Telemetry Transport, a publish-subscribe protocol for low-bandwidth and unreliable IoT networks that supports efficient and reliable data transmission between IoT devices and applications.
  - XMPP: Extensible Messaging and Presence Protocol, an open standard protocol for instant messaging and presence information that supports real-time communication and collaboration between IoT devices and applications.
  - DDS: Data Distribution Service, a standard for data-centric publish-subscribe communication that supports high-performance, scalable, and reliable data exchange between IoT devices and applications.
  - LWM2M: Lightweight Machine-to-Machine, a protocol for device management and service enablement that supports remote monitoring, configuration, and control of IoT devices.



# oneM2M

- oneM2M is a global partnership project founded in 2012 and constituted by 8 of the world's leading ICT standards development organizations.
- oneM2M aims to develop a common service layer that can be readily embedded within various hardware and software, and relied upon to connect the myriad of devices in the field with M2M application servers worldwide.
- oneM2M is similar to a distributed operating system for the Internet of Things. It takes the form of a middleware service layer consisting of a suite of common service functions (CSFs).
- oneM2M common service layer contains set of common service functions which are required by various IoT verticals. Common Service Entity (CSE) is the logical entity that implements the common service functions.
- oneM2M defines three types of CSEs: Infrastructure Node (IN-CSE), Middle Node (MN-CSE) and Application Entity (AE). IN-CSE is the root of the oneM2M system and provides the core functionalities. MN-CSE is an intermediate node that can act as a gateway or a proxy. AE is the application logic that interacts with the oneM2M system.
- oneM2M uses a resource-oriented architecture (ROA) based on RESTful principles. Resources are the basic units of information that can be created, retrieved, updated and deleted through standardized interfaces. Resources are organized in a hierarchical tree structure and can have attributes, sub-resources and subscriptions.
- oneM2M supports various protocols for communication between CSEs and AEs, such as HTTP, CoAP, MQTT and WebSocket. oneM2M also defines a protocol-independent binding layer that abstracts the common features of these protocols and provides a uniform way of exchanging messages.
- oneM2M provides various security mechanisms to ensure the confidentiality, integrity and availability of the oneM2M system and its resources. These include authentication, authorization, access control, encryption, digital signature, certificate management and auditing.



# ETSI M2M

- ETSI M2M stands for European Telecommunications Standards Institute Machine-to-Machine.
- It is a standardization body that develops standards for IoT and M2M technologies.
- It is one of the founding partners of oneM2M, a global standards initiative that covers requirements, architecture, API specifications, security solutions and interoperability for M2M and IoT technologies.
- ETSI M2M defines a high-level architecture for an M2M system, as shown in the figure below.

ETSI M2M high-level architecture

- The architecture consists of three main layers: the network layer, the service layer and the application layer.
- The network layer provides connectivity and transport services for M2M devices and gateways.
- The service layer provides common functions and capabilities for M2M applications, such as device management, data management, security, discovery and subscription.
- The service layer is implemented by the Service Capability Layer (SCL), which is a software component that exposes a RESTful API to the application layer and the network layer.
- The application layer provides specific functions and logic for M2M applications, such as smart metering, smart home, smart city, etc.
- The application layer interacts with the service layer through the M2M Application Entity (AE), which is a software component that represents an M2M application and its resources.
- The architecture supports different types of M2M networks, such as M2M area networks, M2M access networks and M2M core networks.
- The architecture also supports interworking with other standards and protocols, such as CoAP, MQTT, ZigBee, etc.

## Service Layer Protocols

- The service layer protocols are the protocols used by the SCL and the AE to communicate with each other and with the network layer.
- The service layer protocols are based on HTTP and CoAP, which are application layer protocols that support RESTful interactions.
- HTTP and CoAP are chosen because they are widely used, lightweight, scalable and interoperable protocols for web services and constrained devices.
- The service layer protocols define a common data model and a common resource structure for M2M resources, such as devices, applications, containers, subscriptions, etc.
- The service layer protocols also define a common set of operations and methods for creating, retrieving, updating and deleting M2M resources, such as POST, GET, PUT and DELETE.
- The service layer protocols use XML and JSON as the data formats for exchanging M2M resources and messages.
- The service layer protocols support different types of interactions, such as request/response, publish/subscribe and notification.

## Security

- Security is a key aspect of the ETSI M2M architecture, as it involves the protection of M2M devices, data, services and applications from unauthorized access, modification and disclosure.
- Security is addressed at different levels of the architecture, such as the network layer, the service layer and the application layer.
- Security is also addressed at different phases of the M2M lifecycle, such as the provisioning, the operation and the decommissioning of M2M devices and services.
- Security is based on a combination of mechanisms and techniques, such as encryption, authentication, authorization, access control, integrity, confidentiality, non-repudiation and auditability.
- Security is supported by different standards and protocols, such as TLS, DTLS, IPSec, OAuth, X.509, etc.
- Security is implemented by different components and entities, such as the M2M Security Entity (SE), the M2M Certificate Authority (CA), the M2M Trust Anchor (TA), etc.



# OMA for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- OMA stands for Open Mobile Alliance, an organization that develops standards and specifications for the mobile and IoT industry.
- OMA LwM2M (Lightweight Machine to Machine) is a protocol from OMA for device management and service enablement in IoT .
- OMA LwM2M is based on IETF CoRE (Constrained RESTful Environments) RFCs and drafts, such as CoAP (Constrained Application Protocol), DTLS (Datagram Transport Layer Security), CBOR (Concise Binary Object Representation), and SenML (Sensor Measurement Lists).
- OMA LwM2M defines the application layer communication protocol between an LwM2M Server and an LwM2M Client, which is located in an IoT device.
- OMA LwM2M supports four main operations: Bootstrap, Register, Manage, and Report.
  - Bootstrap: The LwM2M Client obtains the necessary security credentials and server information from a Bootstrap Server to access other LwM2M Servers.
  - Register: The LwM2M Client registers with one or more LwM2M Servers and provides information about its capabilities and resources.
  - Manage: The LwM2M Server can perform device management and service enablement tasks on the LwM2M Client, such as read, write, execute, observe, create, delete, and discover.
  - Report: The LwM2M Client can report its status and measurements to the LwM2M Server, either periodically or based on events or notifications.
- OMA LwM2M uses a resource model to represent the data and functionality of the IoT device. A resource is a piece of information or an action that can be accessed or performed by the LwM2M Server or the LwM2M Client.
- OMA LwM2M defines a set of standard objects and resources that cover common IoT use cases, such as device, firmware, connectivity, location, security, and software management . OMA LwM2M also allows the definition of custom objects and resources for specific applications .
- OMA LwM2M provides end-to-end security for the IoT communication by using DTLS for the transport layer and OSCORE (Object Security for Constrained RESTful Environments) for the application layer .
  - DTLS provides security features such as confidentiality, integrity, and authentication for the CoAP messages exchanged between the LwM2M Server and the LwM2M Client .
  - OSCORE provides security features such as end-to-end encryption, integrity protection, and replay protection for the CoAP payload and selected options between the LwM2M Server and the LwM2M Client .
  - OSCORE is especially useful for IoT scenarios where there are intermediaries or proxies between the LwM2M Server and the LwM2M Client, such as firewalls, NATs, or gateways . OSCORE ensures that the critical data is not exposed or modified by the intermediaries .
- OMA LwM2M is a lightweight, efficient, and secure protocol for IoT device management and service enablement that can be used in various IoT applications and environments   . OMA LwM2M is compatible with other IoT protocols and standards, such as MQTT, HTTP, and 5G . OMA LwM2M is supported by many IoT platforms and vendors, such as AWS, Google, IBM, Microsoft, Huawei, and Samsung.



# BBF for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The service layer protocols are the application layer protocols that enable the communication and interaction among different IoT devices and services, as well as with cloud/edge infrastructures.
- The security of the service layer protocols is crucial for ensuring the confidentiality, integrity, availability, and privacy of the data and services in the IoT ecosystem.
- Some of the common service layer protocols in IoT are:
  - Constrained Application Protocol (CoAP): A lightweight protocol that is HTTP-friendly and uses two basic message types: request and response. It supports confirmable and non-confirmable messages, as well as multicast and observe options. It also provides security features such as encryption, authentication, and authorization using Datagram Transport Layer Security (DTLS)  .
  - Message Queuing Telemetry Transport (MQTT): A publish-subscribe protocol that uses a broker to facilitate the communication between publishers and subscribers. It is designed for low-bandwidth and unreliable networks, and offers three levels of quality of service (QoS): at most once, at least once, and exactly once. It also supports Transport Layer Security (TLS) for secure communication  .
  - Advanced Message Queuing Protocol (AMQP): A binary protocol that uses a broker to enable the exchange of messages between producers and consumers. It supports different message delivery modes, such as direct, fanout, topic, and header. It also provides security features such as encryption, authentication, and authorization using TLS and Simple Authentication and Security Layer (SASL)  .
  - User Services Platform (USP): A protocol that defines a standard way to manage, monitor, and control IoT devices and services. It is based on the Broadband Forum (BBF) data model and uses CoAP, MQTT, or WebSocket as the underlying transport protocol. It also supports security features such as encryption, authentication, and authorization using DTLS, TLS, or WebSocket Secure (WSS) .
- Some of the security challenges and solutions for the service layer protocols are:
  - Data privacy: The service layer protocols should protect the sensitive data from unauthorized access, modification, or disclosure. This can be achieved by using encryption, hashing, and digital signatures to ensure the confidentiality, integrity, and authenticity of the data. Additionally, the protocols should support data minimization and anonymization techniques to reduce the exposure of personal or identifiable information  .
  - Authentication, authorization, and trust management: The service layer protocols should verify the identity and credentials of the devices and services that communicate with each other, and grant or deny access based on predefined policies and rules. This can be achieved by using certificates, tokens, or passwords to authenticate the parties, and using access control lists (ACLs), roles, or attributes to authorize the actions. Moreover, the protocols should support trust management mechanisms to evaluate the trustworthiness and reputation of the devices and services based on their behavior and feedback  .
  - Security attacks: The service layer protocols should prevent or mitigate the impact of various security attacks that can compromise the functionality or performance of the IoT system. Some of the common attacks are:
    - Denial-of-service (DoS) or distributed denial-of-service (DDoS) attacks: These attacks aim to overwhelm the network or the devices with a large amount of traffic or requests, causing them to crash or slow down. The service layer protocols can counter these attacks by using rate limiting, filtering, or throttling techniques to limit or block the malicious traffic or requests  .
    - Replay attacks: These attacks involve capturing and retransmitting the messages or requests to cause unwanted or repeated actions. The service layer protocols can prevent these attacks by using nonce, timestamp, or sequence number to detect and discard the duplicated or outdated messages or requests  .
    - Man-in-the-middle (MITM) attacks: These attacks involve intercepting and modifying the messages or requests between the devices or services, causing data leakage or tampering. The service layer protocols can thwart these attacks by using encryption, digital signatures, or certificates to ensure the confidentiality, integrity, and authenticity of the messages or requests  .



# Security in IoT Protocols

- Security in IoT protocols is the process of ensuring the confidentiality, integrity, and availability of data and devices in the Internet of Things (IoT) network.
- IoT protocols are the communication standards and rules that enable data exchange and interaction among IoT devices, gateways, servers, and cloud platforms.
- IoT protocols have to deal with various security challenges, such as:
  - Resource constraints of IoT devices, which limit the use of complex encryption and authentication mechanisms.
  - Heterogeneity and diversity of IoT devices, which require interoperability and compatibility among different protocols and platforms.
  - Scalability and dynamism of IoT network, which involve a large number of devices and frequent changes in topology and connectivity.
  - Privacy and trust issues of IoT data, which involve sensitive and regulated information that may be accessed by unauthorized or malicious parties.
- Some of the common security attacks and threats in IoT network are:
  - Eavesdropping, which is the interception and analysis of data in transit by unauthorized parties.
  - Replay, which is the retransmission of captured data to impersonate or deceive legitimate parties.
  - Modification, which is the alteration or tampering of data in transit or in storage by unauthorized parties.
  - Denial of service (DoS), which is the disruption or prevention of normal service or functionality of IoT devices or network by overwhelming them with malicious traffic or requests.
  - Physical attacks, which are the damage or destruction of IoT devices or network components by physical means.
- Some of the common security protocols and mechanisms for IoT network are:
  - MQTT (Message Queuing Telemetry Transport), which is a lightweight and publish-subscribe protocol that supports encryption, authentication, and authorization using TLS/SSL, username/password, and access control lists.
  - CoAP (Constrained Application Protocol), which is a web-based and RESTful protocol that supports encryption, authentication, and authorization using DTLS, pre-shared keys, certificates, and tokens.
  - LwM2M (Lightweight Machine to Machine), which is a device management and service enablement protocol that supports encryption, authentication, and authorization using DTLS, pre-shared keys, certificates, and bootstrap.
  - ZigBee, which is a low-power and mesh-based protocol that supports encryption, authentication, and authorization using AES, network keys, link keys, and trust center.
  - 6LoWPAN, which is a protocol that enables IPv6 communication over low-power and lossy networks, and supports encryption, authentication, and authorization using IPSec, IKEv2, and RPL.



# MAC 802.15.4

- MAC 802.15.4 is a standard for low-rate wireless personal area networks (LR-WPANs) that defines the physical layer (PHY) and medium access control (MAC) sublayer specifications  .
- MAC 802.15.4 supports low-data-rate wireless connectivity with fixed, portable, and moving devices with no battery or very limited battery consumption requirements .
- MAC 802.15.4 provides the basis of other higher-layer standards, such as ZigBee, WirelessHart, 6LoWPAN and MiWi .
- MAC 802.15.4 supports multiple PHY options, such as frequency-hopping spread spectrum (FHSS), direct-sequence spread spectrum (DSSS), orthogonal frequency-division multiplexing (OFDM), and high-rate pulse ultra-wideband (HRP UWB)  .
- MAC 802.15.4 supports two types of devices: full-function devices (FFDs) and reduced-function devices (RFDs). FFDs can operate in any topology and communicate with any other device, while RFDs can only operate in star or peer-to-peer topologies and communicate only with FFDs .
- MAC 802.15.4 supports two types of networks: star and peer-to-peer. In a star network, a single FFD acts as a coordinator and controls the access to the medium for all other devices. In a peer-to-peer network, multiple FFDs can act as coordinators and form a mesh network .
- MAC 802.15.4 supports two types of MAC operations: beacon-enabled and non-beacon-enabled. In a beacon-enabled mode, the coordinator periodically broadcasts beacons to synchronize the devices and define the superframe structure. In a non-beacon-enabled mode, the devices use a carrier sense multiple access with collision avoidance (CSMA-CA) mechanism to access the medium .
- MAC 802.15.4 supports two types of MAC services: data service and management service. The data service provides reliable or unreliable data transfer between devices. The management service provides functions such as device association and disassociation, network formation and maintenance, device discovery, channel access, and security .
- MAC 802.15.4 supports two types of MAC security: symmetric-key and asymmetric-key. The symmetric-key security uses a shared secret key between the devices to provide confidentiality, integrity, and authentication. The asymmetric-key security uses public and private keys to provide digital signatures and certificates .



# 6LoWPAN

- 6LoWPAN stands for IPv6 over Low-power Wireless Personal Area Networks.
- It is an open standard defined by the Internet Engineering Task Force (IETF) that enables low-power devices with limited processing capabilities to participate in the Internet of Things (IoT) by using IPv6 over IEEE 802.15.4 based networks .
- 6LoWPAN defines mechanisms for:
  - Encapsulation: how to fragment and reassemble IPv6 datagrams over the IEEE 802.15.4 frame size limit of 127 bytes.
  - Header compression: how to reduce the size of IPv6 and UDP headers to fit in the IEEE 802.15.4 frame payload.
  - Neighbor discovery: how to discover and register IPv6 addresses and prefixes of other nodes in the network.
  - Routing: how to forward IPv6 datagrams over multiple hops using different routing protocols, such as RPL (Routing Protocol for Low-Power and Lossy Networks).
- 6LoWPAN networks can be connected to other IPv6 networks, such as the Internet, through edge routers that support IPv6 transition mechanisms, such as NAT64, which allows IPv6 nodes to communicate with IPv4 nodes.
- 6LoWPAN networks can support various applications that require wireless internet connectivity at lower data rates, such as residential and office automation, smart grid, industrial monitoring, etc.



# RPL for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for **Routing Protocol for Low-Power and Lossy Networks**  .
- It is an **IPv6** routing protocol that is standardized for the **Internet of Things (IoT)** by **Internet-Engineering Task Force (IETF)** .
- It supports **multipoint-to-point (MP-to-P)**, **point-to-point (P-to-P)** and **point-to-multipoint (P-to-MP)** communications .
- It forms a **tree-like topology** which is based on different optimizing process called **Objective Function (OF)** .
- It assumes two types of nodes in a network: **border router (gateway)** and **ordinary nodes** .
- The gateway has a connection to the **Internet**, hence it connects nodes in an LLN to the Internet .
- RPL uses **Directed Acyclic Graphs (DAGs)** to represent the network topology and routing paths.
- A DAG is a graph that has no cycles, meaning that there is no way to start at a node and traverse the graph back to the same node.
- RPL defines two types of DAGs: **Destination-Oriented DAGs (DODAGs)** and **Multicast DAGs (M-DAGs)**.
- A DODAG is a DAG rooted at a single destination, such as the gateway.
- A M-DAG is a DAG that supports multicast communication among a group of nodes.
- RPL uses **DODAG Information Object (DIO)** messages to advertise DODAGs and **DODAG Information Solicitation (DIS)** messages to request DIOs.
- RPL also uses **Destination Advertisement Object (DAO)** messages to propagate destination information and **Destination Advertisement Object Acknowledgment (DAO-ACK)** messages to acknowledge DAOs.
- RPL supports different modes of operation, such as **storing mode** and **non-storing mode**.
- In storing mode, each node maintains a routing table that stores the next hop information for each destination.
- In non-storing mode, each node does not store any routing information, but instead uses source routing to forward packets.
- RPL provides security mechanisms to protect the routing messages and the network topology.
- RPL uses **cryptographic keys** and **signatures** to authenticate the messages and the senders.
- RPL also uses **secure join** and **secure leave** procedures to ensure that only authorized nodes can join or leave the network.
- RPL is considered the de facto routing protocol for the IoT, but it also has some challenges and limitations, such as **scalability**, **mobility**, **reliability**, **energy efficiency**, and **interoperability**.



# Application Layer for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The application layer is the interface between the IoT device and the network with which it will communicate.
- It handles data formatting and presentation and serves as the bridge between what the IoT device is doing and the network handoff of the data it produces.
- It also provides services such as authentication, encryption, compression, and error detection and correction.
- In IoT architecture, this layer lies above the service discovery layer, which is responsible for finding and connecting to other devices and services.
- There are many application layer protocols in IoT, each with different features and trade-offs. Some of the common ones are :
  - MQTT: Message Queuing Telemetry Transport is a lightweight publish-subscribe protocol that is designed for low-bandwidth, high-latency, and unreliable networks. It is widely used for IoT applications that require real-time data delivery, such as smart home, industrial automation, and healthcare.
  - CoAP: Constrained Application Protocol is a web transfer protocol that is optimized for constrained devices and networks. It is based on the RESTful architecture and uses UDP as the transport layer. It supports features such as multicast, caching, and asynchronous communication. It is suitable for IoT applications that involve resource discovery, device management, and sensor networks.
  - HTTP: Hypertext Transfer Protocol is the most common web protocol that is used for exchanging data between clients and servers. It is based on the request-response model and uses TCP as the transport layer. It supports features such as encryption, compression, and authentication. It is suitable for IoT applications that involve web services, cloud computing, and data analytics.
  - AMQP: Advanced Message Queuing Protocol is a binary wire-level protocol that is designed for reliable and secure messaging. It is based on the broker model and uses TCP as the transport layer. It supports features such as routing, queuing, transactions, and acknowledgments. It is suitable for IoT applications that involve distributed systems, enterprise integration, and business processes.

