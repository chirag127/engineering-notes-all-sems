

# IOT ARCHITECTURE AND PROTOCOLS

- IoT architecture refers to the many ways that IoT devices are structured to meet user needs. Based on complexity, IoT system elements are grouped into 3 to 7 layers, each with its own role.
- IoT protocols are the set of rules that enable communication between IoT devices, gateways, services and data centers. Different IoT protocols have been designed and optimized for different scenarios and usage.
- A common IoT architecture consists of the following layers  :
  - Device layer: This layer contains the sensors and actuators that collect data and perform actions in the physical world. They can be embedded, wearable, mobile or stationary devices. They can communicate using wired or wireless connections.
  - Gateway layer: This layer acts as a bridge between the device layer and the network layer. It can perform data aggregation, filtering, preprocessing, encryption and protocol translation. It can also provide local storage, processing and analytics capabilities. Gateways can be hardware or software based, and can be deployed on-premises or on the cloud.
  - Network layer: This layer transports the data from the gateway layer to the cloud layer or vice versa. It can use various communication technologies, such as cellular, Wi-Fi, Bluetooth, Zigbee, LoRaWAN, etc. It can also use different internet protocols, such as TCP/IP, UDP, HTTP, etc.
  - Cloud layer: This layer provides the storage, processing and analytics capabilities for the IoT data. It can also host the IoT applications and services that provide value to the users. It can use various cloud computing models, such as IaaS, PaaS, SaaS, etc. It can also leverage big data, machine learning and artificial intelligence technologies to derive insights and actions from the IoT data.
  - Application layer: This layer serves as the interface between the user and the device within a given IoT protocol. It can provide various functionalities, such as visualization, notification, control, configuration, etc. It can also support different platforms, such as web, mobile, desktop, etc.
- Some of the common IoT protocols are :
  - Message queue telemetry transport (MQTT): This is a lightweight, publish-subscribe protocol that enables efficient data transmission over low-bandwidth and unreliable networks. It is widely used for IoT applications that require real-time, bidirectional and low-latency communication, such as smart home, smart grid, etc.
  - Constrained application protocol (CoAP): This is a web-based protocol that enables RESTful communication between resource-constrained devices. It is designed for IoT applications that require low-power, low-overhead and asynchronous communication, such as smart city, smart agriculture, etc.
  - Advanced message queuing protocol (AMQP): This is a reliable, secure and interoperable protocol that enables message-oriented communication between distributed systems. It is suitable for IoT applications that require high-performance, scalable and flexible communication, such as industrial IoT, smart transportation, etc.
  - Data distribution service (DDS): This is a real-time, peer-to-peer protocol that enables data-centric communication between heterogeneous devices. It is ideal for IoT applications that require high-speed, reliable and deterministic communication, such as autonomous vehicles, robotics, etc.



## Unit 1 - IoT-An Architectural Overview

- IoT stands for Internet of Things, which is a network of physical devices, sensors, actuators, and software that can communicate and exchange data over the internet.
- IoT enables various applications and services that can improve the quality of life, efficiency, productivity, and sustainability of different domains, such as smart cities, smart homes, smart health, smart agriculture, smart industry, etc.
- IoT architecture is the design and organization of the components and layers that constitute an IoT system, such as devices, gateways, networks, platforms, applications, and users.
- IoT architecture can be classified into three main types: centralized, decentralized, and distributed.
  - Centralized IoT architecture relies on a central server or cloud that collects, processes, and stores data from the devices, and provides services and applications to the users. This architecture has the advantages of high scalability, reliability, and security, but also the disadvantages of high latency, bandwidth consumption, and single point of failure.
  - Decentralized IoT architecture distributes the data processing and storage among multiple nodes or servers, such as fog or edge computing, that are closer to the devices and users. This architecture has the advantages of low latency, bandwidth saving, and fault tolerance, but also the disadvantages of low scalability, reliability, and security.
  - Distributed IoT architecture enables the devices to communicate and collaborate directly with each other, without relying on any central or intermediate nodes. This architecture has the advantages of high autonomy, resilience, and privacy, but also the disadvantages of high complexity, overhead, and heterogeneity.
- IoT architecture can also be described by the following five layers: perception, network, middleware, application, and business.
  - Perception layer consists of the devices, sensors, and actuators that collect and generate data from the physical world, and perform actions on it. This layer is responsible for data acquisition, sensing, and actuation.
  - Network layer consists of the communication protocols and technologies that enable the data transmission and exchange among the devices and other layers. This layer is responsible for data transmission, routing, and networking.
  - Middleware layer consists of the platforms and software that provide data processing, storage, management, and analysis services to the devices and applications. This layer is responsible for data processing, storage, management, and analysis.
  - Application layer consists of the applications and services that provide specific functionalities and value to the users and domains. This layer is responsible for data presentation, visualization, and utilization.
  - Business layer consists of the stakeholders, policies, and strategies that govern the IoT system and its operation. This layer is responsible for data governance, security, and monetization.



# Building an architecture for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

The Internet of Things (IoT) is a network of physical objects, devices, sensors, and other items that can communicate and exchange data with each other. IoT architecture is the design of the system that enables IoT devices to interact with each other and with other components, such as cloud services, user applications, and data analytics.

A basic IoT architecture consists of three layers:

- **Perception layer**: This layer includes the sensors, gadgets, and other devices that collect data from the physical environment and send it to the network layer. The perception layer may also include actuators that perform actions based on commands from the network or application layer.
- **Network layer**: This layer provides the connectivity and communication between the perception layer and the application layer. The network layer may use various protocols and technologies, such as Wi-Fi, Bluetooth, cellular, LoRaWAN, MQTT, CoAP, etc. The network layer may also include gateways that aggregate and preprocess the data from the perception layer and forward it to the cloud or edge computing platforms.
- **Application layer**: This layer provides the services and functionalities that use the data from the perception layer and provide value to the users or other systems. The application layer may include cloud computing, data storage, data analytics, machine learning, user interfaces, etc. The application layer may also send commands to the actuators in the perception layer to control the devices.

Depending on the complexity and requirements of the IoT system, there may be additional layers or components in the IoT architecture, such as:

- **Management layer**: This layer provides the functions and tools to monitor, manage, and secure the IoT system, such as device provisioning, configuration, authentication, authorization, encryption, firmware updates, etc.
- **Processing layer**: This layer provides the capabilities to process and analyze the data from the perception layer, either in the cloud or at the edge of the network, to extract insights and generate actions. The processing layer may use various techniques, such as stream processing, batch processing, complex event processing, machine learning, etc.
- **Presentation layer**: This layer provides the interfaces and visualizations to present the data and insights from the processing layer to the users or other systems, such as dashboards, reports, alerts, notifications, etc.

The IoT architecture may vary depending on the application domain, the use case, the scale, the performance, the security, and the cost of the IoT system. There is no single, universal IoT architecture, but rather a set of architectural principles and best practices that can guide the design and development of IoT solutions.

Some of the architectural principles and best practices are:

- **Modularity**: The IoT architecture should be composed of loosely coupled and reusable components that can be easily added, removed, or replaced without affecting the whole system.
- **Interoperability**: The IoT architecture should enable the communication and integration of different devices, platforms, and services, using common standards, protocols, and interfaces.
- **Scalability**: The IoT architecture should be able to handle the increasing number and diversity of devices, data, and users, without compromising the performance, reliability, or security of the system.
- **Reliability**: The IoT architecture should ensure the availability and functionality of the system, even in the presence of failures, errors, or disruptions in the devices, networks, or services.
- **Security**: The IoT architecture should protect the confidentiality, integrity, and availability of the data and the devices, using appropriate mechanisms, such as encryption, authentication, authorization, etc.
- **Privacy**: The IoT architecture should respect the privacy and preferences of the users and the data owners, using techniques such as anonymization, pseudonymization, consent management, etc.



# Main design principles and needed capabilities for the notes of the Unit 1 - IoT-An Architectural Overview

- IoT-An Architectural Overview is a topic that covers the basic concepts, components, and challenges of the Internet of Things (IoT) technology, which enables the interconnection and interaction of physical and digital objects across various domains and applications.
- The main design principles and needed capabilities for the notes of this topic are:

  - **Understand the definition and scope of IoT**: IoT is a broad term that encompasses different scenarios where network connectivity and computing capability extends to objects, sensors, and everyday items not normally considered computers, allowing these devices to generate, exchange, and consume data with minimal human intervention. IoT can be applied to various domains, such as smart homes, smart cities, smart health, smart agriculture, smart industry, etc. The notes should explain the definition, scope, and benefits of IoT, as well as the challenges and risks associated with it, such as security, privacy, interoperability, scalability, etc.
  - **Identify the main components and layers of IoT architecture**: IoT architecture consists of the devices, network structure, and cloud technology that allows IoT devices to communicate with each other and with other systems and services. A basic IoT architecture consists of three layers: Perception (the sensors, gadgets, and other devices that collect and transmit data), Network (the communication protocols, gateways, and infrastructure that enable data transmission and processing), and Application (the cloud platforms, databases, analytics, and user interfaces that provide data storage, processing, and visualization). The notes should describe the main components and functions of each layer, as well as the possible variations and extensions of the architecture, such as edge computing, fog computing, etc.
  - **Analyze the requirements and design choices of IoT solutions**: IoT solutions are designed to meet specific needs and objectives of different application scenarios and stakeholders. Therefore, the notes should discuss the main requirements and design choices of IoT solutions, such as the type and number of devices, the data format and quality, the communication protocols and standards, the security and privacy measures, the data processing and analytics methods, the user interaction and feedback mechanisms, etc. The notes should also provide examples and case studies of existing or potential IoT solutions in different domains and contexts, and compare and contrast their advantages and disadvantages.
  - **Evaluate the impact and challenges of IoT technology**: IoT technology has a significant impact on various aspects of society, economy, and environment, such as improving efficiency, productivity, convenience, safety, sustainability, etc. However, IoT technology also poses various challenges and risks, such as increasing complexity, vulnerability, uncertainty, ethical issues, etc. The notes should assess the impact and challenges of IoT technology from different perspectives and dimensions, such as technical, social, ethical, legal, environmental, etc. The notes should also discuss the possible solutions and best practices to address and mitigate the challenges and risks of IoT technology, such as standardization, regulation, governance, education, awareness, etc.



# An IoT architecture outline for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- IoT architecture is the system of numerous elements that enable IoT devices to communicate with each other and perform various tasks.
- A basic IoT architecture consists of three layers: Perception, Network, and Application.
- Perception layer: This layer comprises the sensors, actuators, and other smart devices that collect data from the physical environment and perform actions on it . Examples of perception devices are temperature sensors, cameras, RFID tags, etc.
- Network layer: This layer comprises the network devices and communications types and protocols that transmit the data from the perception layer to the application layer or vice versa  . Examples of network devices are routers, gateways, switches, etc. Examples of communications types and protocols are 5G, Wi-Fi, Bluetooth, MQTT, CoAP, etc.
- Application layer: This layer comprises the cloud services, platforms, and applications that store, process, and analyze the data from the network layer and provide feedback or commands to the perception layer  . Examples of cloud services are AWS, Azure, Google Cloud, etc. Examples of platforms are IoT Central, ThingWorx, etc. Examples of applications are smart home, smart city, smart agriculture, etc.
- Depending on the complexity and functionality of the IoT system, there can be more layers or components in the IoT architecture, such as the Edge layer, the Analytics layer, the Security layer, etc  .
- Edge layer: This layer comprises the edge devices and servers that perform data processing and filtering at the edge of the network, reducing the latency and bandwidth consumption of the cloud services . Examples of edge devices are Raspberry Pi, Arduino, etc. Examples of edge servers are EdgeX Foundry, AWS Greengrass, etc.
- Analytics layer: This layer comprises the tools and techniques that apply advanced data analytics and machine learning to the data from the network or edge layer, generating insights and predictions for the application layer . Examples of tools and techniques are Spark, TensorFlow, Keras, etc.
- Security layer: This layer comprises the mechanisms and standards that ensure the confidentiality, integrity, and availability of the data and devices in the IoT system, preventing unauthorized access or attacks . Examples of mechanisms and standards are encryption, authentication, authorization, firewall, etc.



# Standards Considerations for the Notes of the Unit 1 - IoT-An Architectural Overview

- The notes should provide a clear and concise introduction to the concept, definition, and characteristics of the Internet of Things (IoT).
- The notes should explain the main components and layers of a basic IoT architecture, such as perception, network, cloud, and application .
- The notes should describe the different architectural views and design objectives of the IoT-A project, which is a reference model for IoT systems.
- The notes should illustrate some examples of IoT applications and use cases in various domains, such as smart home, smart city, smart health, smart agriculture, etc. .
- The notes should highlight the main challenges and opportunities of IoT, such as security, privacy, interoperability, scalability, reliability, etc. .
- The notes should follow a logical and coherent structure, with clear headings, subheadings, bullet points, diagrams, and tables as needed.
- The notes should use proper grammar, spelling, punctuation, and formatting, and cite the sources of information using a consistent referencing style.



# M2M and IoT Technology Fundamentals

## M2M

- M2M stands for **Machine-to-Machine** communication, which refers to the direct exchange of data between devices without human intervention .
- M2M uses **point-to-point** communication, which means that each device has a dedicated connection to another device or a central server.
- M2M is often used for **remote monitoring and control** of equipment, such as vending machines, security cameras, smart meters, etc .
- M2M can also enable **automation** of processes, such as inventory management, fleet management, asset tracking, etc .
- M2M is considered to be the **foundation** of IoT, as it provides the basic functionality of data transmission and device management.

## IoT

- IoT stands for **Internet of Things**, which refers to the network of physical objects that are embedded with sensors, software, and connectivity to collect and exchange data with other devices and systems over the internet.
- IoT expands the power and potential of M2M technology by creating **large cloud networks** of devices that communicate with each other on cloud platforms .
- IoT enables **larger-scale integration** and **more sophisticated applications** of data, such as smart cities, smart homes, smart agriculture, smart healthcare, etc .
- IoT also leverages **advanced data analytics** and **cloud computing** to process and store the massive amount of data generated by the devices and provide insights and solutions for various problems and challenges.
- IoT is considered to be the **future** of M2M, as it provides more flexibility, scalability, interoperability, and intelligence to the devices and systems.



# Devices and gateways

- Devices are the physical objects that are connected to the Internet of Things (IoT) network and can sense, actuate, communicate, and process data. Examples of devices are sensors, cameras, smart meters, smart watches, etc.
- Gateways are the central hubs that connect devices to the cloud and enable data transfer, protocol translation, data aggregation, security, and device management. Examples of gateways are routers, modems, edge servers, etc.
- The architecture of IoT gateways consists of the following components    :
  - Security: This is one of the most critical factors in an IoT gateway architecture throughout the design phase. It involves encryption, authentication, authorization, and firewall mechanisms to protect the data and devices from unauthorized access and cyberattacks.
  - Device layer: This is the hardware of an IoT infrastructure, which includes IoT sensors, protective circuits, networking modules, and a processor or microcontroller. The device layer is responsible for sensing, actuating, and communicating with the gateway and other devices.
  - Data management: This is the software that handles the data collected from the devices and prepares it for transmission to the cloud. It involves data filtering, compression, transformation, and validation to ensure the data quality and integrity.
  - Operating system: This is the software that runs the gateway hardware and other programs on the device. It provides the basic functions and services for the gateway, such as memory management, file system, network stack, device drivers, etc. The operating system can be a general-purpose OS, such as Linux or Windows, or a specialized OS, such as FreeRTOS or Zephyr.
  - Hardware abstraction: This is the software that provides a common interface for the gateway to interact with different types of devices and sensors, regardless of their specific hardware characteristics and communication protocols. It enables the gateway to support a wide range of devices and sensors without modifying the gateway code.
  - Gateway data transfer: This is the software that enables the gateway to send and receive data to and from the cloud and other gateways. It involves the use of communication protocols, such as MQTT, CoAP, HTTP, etc., and data formats, such as JSON, XML, etc. It also involves the use of APIs and SDKs to integrate the gateway with cloud services and platforms.
  - Communication protocols: These are the rules and standards that govern the data exchange between the devices, gateways, and cloud. They define the syntax, semantics, and synchronization of the data messages. They can be classified into two types: device-to-gateway protocols and gateway-to-cloud protocols. Device-to-gateway protocols are used for communication between the devices and the gateway, and they are usually low-power, low-bandwidth, and short-range protocols, such as Zigbee, Bluetooth, LoRaWAN, etc. Gateway-to-cloud protocols are used for communication between the gateway and the cloud, and they are usually high-power, high-bandwidth, and long-range protocols, such as Wi-Fi, Ethernet, Cellular, etc.
  - Cloud connectivity manager: This is the software that manages the connection between the gateway and the cloud. It involves the use of authentication, authorization, and encryption mechanisms to ensure the security and reliability of the connection. It also involves the use of connection management, load balancing, and failover mechanisms to ensure the availability and scalability of the connection.



# Local and Wide Area Networking for IoT

- Local area networks (LAN) and wide area networks (WAN) are two types of networks that can be used to connect IoT devices to the Internet or to each other.
- A LAN is a group of devices that are connected within a short geographic area, typically less than 1000 meters, such as a home, office, or building.
- A WAN is a network that spans a large geographic area, such as a city, country, or the world, and connects multiple LANs or other networks.
- LANs and WANs can use different technologies and protocols to enable IoT communication, depending on the requirements and constraints of the application, such as bandwidth, latency, power consumption, cost, and security.
- Some of the common technologies and protocols for LANs and WANs are:

  - WiFi: A wireless LAN technology that uses radio waves to provide high-speed Internet access and local network connections to devices within a range of about 100 meters. WiFi can be used for applications that run in a local environment, or in a distributed setting if there are multiple access points integrated into a larger network.
  - Bluetooth: A wireless PAN technology that uses short-range radio waves to enable data exchange between devices within a range of about 10 meters. Bluetooth can be used for applications that require low power consumption and simple connectivity, such as wearable devices, smart home appliances, and health monitors.
  - Cellular: A wireless WAN technology that uses the same mobile networks as smartphones to allow IoT devices to communicate over long distances and across different regions. Cellular can be used for applications that require high reliability, security, and mobility, such as smart vehicles, industrial automation, and smart cities.
  - Low Power Wide Area Networks (LPWAN): A wireless WAN technology that uses low-frequency radio waves to provide long-range and low-power connectivity to IoT devices, typically with a range of several kilometers and a battery life of several years. LPWAN can be used for applications that require low data rates and low cost, such as smart agriculture, environmental monitoring, and asset tracking.
  - Mesh Networks: A network topology that consists of nodes that can relay data to each other without relying on a central hub or router. Mesh networks can be used for applications that require scalability, resilience, and self-organization, such as smart lighting, disaster relief, and military operations.



Hello, I am Sydney, your AI assistant. I can help you with data management for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS. Here are some points to consider:

# Data management for the notes of the Unit 1 - IoT-An Architectural Overview

- Data management is the process of collecting, storing, organizing, processing, and analyzing data from various sources, such as sensors, devices, networks, applications, and users, in the context of IoT.
- Data management is essential for IoT because it enables the extraction of meaningful insights, the optimization of performance, the enhancement of security, and the creation of value from the data generated by IoT systems.
- Data management for the notes of the Unit 1 - IoT-An Architectural Overview can be done by following these steps:

  - Identify the data sources and types: The notes should include the different types of data that can be generated by IoT systems, such as structured, unstructured, semi-structured, streaming, batch, static, dynamic, etc. The notes should also identify the data sources, such as sensors, devices, gateways, cloud, fog, edge, etc.
  - Define the data requirements and objectives: The notes should specify the data requirements and objectives for the IoT system, such as the data quality, quantity, frequency, latency, reliability, availability, security, privacy, etc. The notes should also define the data analysis goals, such as the data mining, machine learning, artificial intelligence, etc.
  - Design the data architecture and model: The notes should describe the data architecture and model for the IoT system, such as the data flow, data storage, data processing, data integration, data distribution, data governance, etc. The notes should also illustrate the data model, such as the data schema, data format, data semantics, data ontology, etc.
  - Implement the data management system: The notes should explain the data management system for the IoT system, such as the data collection, data ingestion, data transformation, data cleaning, data validation, data aggregation, data compression, data encryption, data anonymization, data indexing, data querying, data visualization, data analytics, data sharing, data backup, data recovery, etc. The notes should also mention the data management tools, such as the data platforms, data frameworks, data libraries, data APIs, data standards, data protocols, etc.
  - Evaluate the data management system: The notes should evaluate the data management system for the IoT system, such as the data quality, data accuracy, data completeness, data consistency, data timeliness, data relevance, data usability, data scalability, data efficiency, data security, data privacy, data compliance, data value, etc. The notes should also provide the data management metrics, such as the data throughput, data latency, data bandwidth, data storage, data processing, data availability, data reliability, data integrity, data confidentiality, data utility, data ROI, etc.



# Business processes in IoT

Business processes are collections of related events, activities and decisions that involve a number of factors and resources, and that lead to an outcome that is of value for the organisation and the customer. Business processes can be improved with the Internet of Things (IoT), which is the network of physical objects embedded with sensors, software and other technologies that enable data collection and communication.

Some of the benefits of IoT for business processes are:

- Automating process: IoT devices can perform tasks without human intervention, such as controlling temperature, lighting, security, etc. This can reduce errors, costs and risks, and increase efficiency and productivity.
- Gathering valuable information: IoT devices can collect and transmit data about various aspects of the process, such as performance, quality, usage, location, etc. This can provide insights for decision making, optimization, innovation and customer satisfaction.
- Extending business functions: IoT devices can enable new capabilities and services that were not possible before, such as remote monitoring, predictive maintenance, asset tracking, etc. This can create new revenue streams, competitive advantages and customer loyalty.
- Triggering rules: IoT devices can act as triggers for other actions or events in the process, such as sending alerts, notifications, commands, etc. This can enhance coordination, collaboration and responsiveness among different actors and stakeholders in the process.
- Sourcing predictive analytics and big data: IoT devices can generate large amounts of data that can be analysed with advanced techniques such as machine learning, artificial intelligence, etc. This can enable predictive analytics and big data, which can help anticipate future outcomes, trends, behaviours, etc. and provide recommendations, solutions, warnings, etc.

Some of the recommendations for implementing IoT business processes are:

- Define the business process to improve and identify the problem to solve: The first step is to have a clear understanding of the current state of the process, the desired state of the process, and the gap between them. The problem should be specific, measurable, achievable, relevant and time-bound.
- Use an end-to-end approach: The second step is to consider the whole process from the beginning to the end, and not just focus on one part or aspect of it. The IoT solution should be aligned with the overall objectives, requirements and expectations of the process, and should cover all the stages, activities and actors involved.
- Make agile design and start with proof of concept prototyping: The third step is to adopt an agile methodology for designing and developing the IoT solution, which involves iterative, incremental and collaborative processes. The IoT solution should be tested and validated with a proof of concept prototype, which is a small-scale and low-cost version of the solution that demonstrates its feasibility and functionality.
- Get on board the right people, better if you keep it low but with the best knowledge: The fourth step is to involve the right people in the IoT project, such as experts, stakeholders, users, etc. The IoT project team should be small but diverse, with the best knowledge and skills in the relevant domains, such as IoT, business, technology, etc.
- Be persistent but acknowledgeable to failure: The fifth step is to be persistent and resilient in the IoT project, as there might be challenges, risks and uncertainties along the way. The IoT project team should be open to feedback, learning and improvement, and should be able to recognise and address failures and mistakes.
- Disruption could be there, but don’t go crazy about it: The sixth step is to be aware of the potential disruption that IoT can cause to the existing business processes, models and strategies, and to be prepared to adapt and change accordingly. The IoT project team should not be afraid of innovation and experimentation, but should also be realistic and pragmatic about the costs and benefits of IoT.



# Everything as a Service (XaaS) for the notes of the Unit 1 - IoT-An Architectural Overview in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Everything as a Service (XaaS) is a term that describes the delivery of any IT function as a service over the internet, using cloud computing and remote access technologies  .
- XaaS originated from the Software as a Service (SaaS) model, which provides software applications as a service to users, without requiring them to install or maintain them on their own devices.
- XaaS has expanded to include other types of services, such as Infrastructure as a Service (IaaS), which provides computing resources such as servers, storage, and networking as a service; Platform as a Service (PaaS), which provides development and deployment environments as a service; and more functionally-specific models, such as Storage as a Service, Desktop as a Service (DaaS), and Disaster Recovery as a Service (DRaaS)  .
- XaaS enables users to access and consume IT services on demand, without having to invest in or manage the underlying infrastructure or software. Users can pay for what they use, scale up or down as needed, and benefit from the latest features and updates  .
- XaaS also provides benefits to service providers, who can leverage economies of scale, reduce operational costs, increase customer satisfaction, and offer innovative and differentiated services   .
- XaaS is a key component of the service economy, which is characterized by the shift from the production and consumption of goods to the provision and consumption of services. XaaS enables businesses to focus on their core competencies, outsource non-core functions, and create new value propositions and revenue streams .
- XaaS is closely related to the Internet of Things (IoT), which is the network of physical objects that are embedded with sensors, software, and connectivity to exchange data and interact with other devices and systems. IoT enables the creation of new types of services that leverage the data and capabilities of connected devices, such as smart home, smart city, smart health, and smart industry services.
- XaaS and IoT are both driven by the advances in cloud computing, big data, artificial intelligence, and wireless communication technologies, which enable the collection, processing, analysis, and delivery of large amounts of data and services over the internet.
- XaaS and IoT are both transforming the way businesses and consumers access and use IT services, creating new opportunities and challenges for service providers, users, and regulators. Some of the key issues and trends related to XaaS and IoT are security, privacy, interoperability, standardization, regulation, and ethics.



# M2M and IoT Analytics

- M2M and IoT are both technologies that enable remote communication and data exchange among machines without human intervention.
- M2M stands for Machine-to-Machine, and IoT stands for Internet of Things.
- The main difference between M2M and IoT is that M2M is a point-to-point connection of two or more devices over cellular or wired networks, while IoT is a network of devices that connect to the Internet and use IP-based protocols for data transmission and processing.
- M2M is more of a vertical application that meets internal demands, such as monitoring, control, or automation, while IoT is more of a horizontal application that has open-ended capabilities, such as analytics, optimization, or innovation.
- M2M and IoT analytics are the processes of collecting, storing, processing, and visualizing data from M2M and IoT devices, respectively, to generate insights and value for various purposes, such as improving efficiency, reducing costs, enhancing customer experience, or creating new business models.
- M2M and IoT analytics can be performed at different levels, such as the device level, the edge level, the cloud level, or the application level, depending on the data volume, velocity, variety, and veracity, as well as the latency, bandwidth, security, and scalability requirements.
- M2M and IoT analytics can use various techniques, such as descriptive analytics, predictive analytics, prescriptive analytics, or cognitive analytics, to provide different types of information, such as what happened, why it happened, what will happen, what should happen, or how to make it happen.
- M2M and IoT analytics can benefit various domains, such as manufacturing, transportation, healthcare, energy, agriculture, smart cities, or smart homes, by enabling data-driven decision making, optimization, automation, personalization, or innovation.



# Knowledge Management for the Unit 1 - IoT-An Architectural Overview

- Knowledge management (KM) is the process of creating, sharing, using and managing the knowledge and information of an organization or a system.
- KM can generate intelligence in IoT ecosystems to enable a digital business and society transformation by leveraging the data, information and knowledge generated by the interconnected devices, people and processes.
- IoT architecture is the structure enabling internet-connected devices to communicate with other devices, systems and applications.
- IoT architecture comprises of several IoT system building blocks connected to ensure that sensor-generated device data is collected, stored, and processed in the big data warehouse and that devices’ actuators perform commands sent via a user application.
- A standard IoT solution architecture consists of five basic elements:
  - Devices are industrial equipment, sensors, and microcontrollers that connect with the cloud to send and receive data.
  - Provisioning enables devices to take actions and communicate with the cloud.
  - Ingestion is the process of receiving and storing data from devices in the cloud.
  - Analytics is the process of processing, analyzing and visualizing data to generate insights and actions.
  - Presentation is the process of delivering the insights and actions to the users or other systems via dashboards, applications or APIs.
- An IoT architecture can also be divided into different functional layers, such as perception, transport, processing, application and business layers.
  - Perception layer is responsible for sensing the physical environment and collecting data from devices.
  - Transport layer is responsible for transmitting the data from devices to the cloud or edge via wired or wireless networks.
  - Processing layer is responsible for processing the data in the cloud or edge using various techniques such as data cleaning, aggregation, filtering, fusion, mining, etc.
  - Application layer is responsible for providing various IoT services and applications to the users or other systems based on the processed data, such as smart home, smart city, smart health, etc.
  - Business layer is responsible for managing the overall IoT system, such as security, privacy, governance, monetization, etc.
- An IoT architecture can also be classified into different types, such as centralized, decentralized, distributed or hybrid, depending on the location and level of data processing and decision making.
  - Centralized IoT architecture relies on the cloud for data processing and decision making, and has low latency, high scalability and high reliability, but also high cost and bandwidth requirements.
  - Decentralized IoT architecture relies on the edge or fog nodes for data processing and decision making, and has high latency, low scalability and low reliability, but also low cost and bandwidth requirements.
  - Distributed IoT architecture relies on the devices themselves for data processing and decision making, and has very high latency, very low scalability and very low reliability, but also very low cost and bandwidth requirements.
  - Hybrid IoT architecture combines the advantages of the other types and balances the trade-offs between them, and has moderate latency, scalability, reliability, cost and bandwidth requirements.



## Unit 2 - Reference Architecture

- A reference architecture is a **generic** and **abstract** model that defines the structure, behavior, and properties of a system or a domain.
- A reference architecture provides a **common vocabulary**, a **set of guidelines**, and a **base for reuse** of design elements and patterns.
- A reference architecture can be used as a **template** or a **blueprint** for designing and implementing specific architectures or solutions.
- A reference architecture can also be used as a **benchmark** or a **standard** for evaluating and comparing different architectures or solutions.
- A reference architecture typically consists of the following components:
  - A **conceptual model** that defines the key concepts, terms, and relationships in the domain.
  - A **logical model** that defines the functional and non-functional requirements, the architectural principles and patterns, and the high-level design decisions and trade-offs.
  - A **physical model** that defines the implementation details, the technologies and tools, the deployment and configuration, and the operational and maintenance aspects.
- A reference architecture can be developed and maintained by different stakeholders, such as **industry consortia**, **standards bodies**, **research organizations**, **vendors**, or **communities of practice**.
- A reference architecture can be applied and adapted to different contexts, such as **domains**, **sectors**, **scenarios**, or **use cases**.
- A reference architecture can be documented and communicated using different formats, such as **text**, **diagrams**, **models**, or **frameworks**.



# IoT Architecture-State of the Art

- Internet of Things (IoT) is a paradigm that enables the interconnection and interaction of physical and virtual objects through the Internet.
- IoT architecture is the design and organization of the components and layers that constitute an IoT system, such as devices, networks, platforms, applications, and services.
- A reference model is a model that describes the main conceptual entities and how they are related to each other, while the reference architecture aims at describing the main functional components of a system as well as how the system works, how the system is deployed, what information the system processes, etc.
- There is no single or universal IoT architecture, but rather different architectures that suit different scenarios, requirements, and objectives.
- Some of the common elements and challenges of IoT architectures are  :
  - Device management: the process of provisioning, configuring, updating, and monitoring IoT devices, as well as ensuring their security and reliability.
  - Data management: the process of collecting, storing, processing, analyzing, and visualizing data from IoT devices, as well as ensuring their quality, integrity, and privacy.
  - Communication management: the process of establishing, maintaining, and optimizing the connectivity and interoperability of IoT devices, networks, and platforms, as well as ensuring their performance, efficiency, and scalability.
  - Service management: the process of providing, orchestrating, and consuming IoT services, such as data analytics, machine learning, automation, and actuation, as well as ensuring their functionality, usability, and value.
  - Application management: the process of developing, deploying, and running IoT applications, such as smart home, smart city, smart health, and smart industry, as well as ensuring their user experience, innovation, and impact.



# Introduction

- In this unit, we will learn about the reference architecture for the Internet of Things (IoT), which is a conceptual framework that defines the components, interfaces, and protocols for designing and implementing IoT systems.
- A reference architecture provides a common vocabulary, a set of principles and best practices, and a logical structure for integrating the diverse and complex technologies that enable IoT solutions.
- A reference architecture also helps to address the challenges and requirements of IoT, such as scalability, interoperability, security, privacy, and reliability.
- There are different reference architectures proposed by various organizations and standardization bodies, such as the IoT-Architecture (IoT-A) project, the IEEE P2413 standard, the Industrial Internet Consortium (IIC), and the OpenFog Consortium.
- In this unit, we will focus on the IoT-A reference architecture, which is one of the most comprehensive and widely adopted frameworks for IoT.
- The IoT-A reference architecture defines four architectural views: the functional view, the information view, the communication view, and the deployment and operation view.
- The functional view describes the main functions and capabilities of an IoT system, and how they are organized into functional groups and roles.
- The information view defines the data and metadata models, the semantics and ontologies, and the information flows and processing in an IoT system.
- The communication view specifies the communication protocols, the network architectures, and the communication patterns and qualities in an IoT system.
- The deployment and operation view covers the physical devices, the software components, the deployment configurations, and the operational aspects of an IoT system.
- The IoT-A reference architecture also defines a set of architectural principles and guidelines, such as modularity, interoperability, security, privacy, and trust, that should be followed when designing and implementing IoT systems.



# State of the Art for the Notes of the Unit 2 - Reference Architecture in the Subject of IoT Architecture and Protocols

- A reference model is a model that describes the main conceptual entities and how they are related to each other, while the reference architecture aims at describing the main functional components of a system as well as how the system works, how the system is deployed, what information the system processes, etc.
- The principles of Reactive Systems define the state-of-the-art programming models for IoT. Because IoT devices are sensing and actuating physical systems, many of which are critical infrastructure for energy, food, healthcare, and transportation, it is important that they stay responsive, and operate safely and securely.
- IoT architecture is mainly 3-layered: perception layer, network layer and application layer.
  - Perception Layer: The perception layer is all about sensing the physical world and collecting data from various sources, such as sensors, RFID tags, cameras, etc. The perception layer is responsible for data acquisition, processing, filtering and transmission.
  - Network Layer: The network layer is responsible for connecting the perception layer with the application layer, and providing reliable and efficient data transmission. The network layer can use various communication technologies, such as cellular networks, Wi-Fi, Bluetooth, ZigBee, etc. The network layer also provides security, privacy and trust mechanisms for the data.
  - Application Layer: The application layer is responsible for providing various services and applications to the end users, such as smart home, smart city, smart health, smart agriculture, etc. The application layer can use various platforms and technologies, such as cloud computing, fog computing, edge computing, etc. The application layer also provides data analysis, visualization and decision making.
- There are also other IoT architectures proposed in the literature, such as the 5-layer architecture, the service-oriented architecture, the event-driven architecture, the agent-based architecture, etc. These architectures aim at addressing the specific challenges and requirements of different IoT scenarios and applications.



# Reference Model and Architecture for IoT

- A reference model is a conceptual framework that defines the common terminology, concepts, and principles for designing and implementing IoT systems.
- A reference architecture is a concrete instantiation of a reference model that provides specific guidelines, best practices, and standards for developing IoT solutions.
- One of the most widely used reference models for IoT is the IoT World Forum Reference Model, which was proposed by the IoT World Forum, a consortium of industry leaders, academia, and government organizations.
- The IoT World Forum Reference Model consists of seven layers, as shown in the figure below:

IoT World Forum Reference Model

- The seven layers are:

  - **Physical devices and controllers layer**: This layer includes the physical devices, sensors, actuators, and controllers that interact with the physical world and generate data.
  - **Connectivity layer**: This layer provides the communication protocols, standards, and technologies for connecting the devices and controllers to the network.
  - **Edge computing layer**: This layer performs data processing, filtering, aggregation, and analysis at the edge of the network, close to the devices, to reduce latency, bandwidth, and storage requirements.
  - **Data accumulation layer**: This layer stores and manages the data collected from the edge computing layer in various formats and structures, such as databases, data lakes, or data warehouses.
  - **Data abstraction layer**: This layer transforms and normalizes the data from the data accumulation layer into a common format and structure that can be consumed by the upper layers.
  - **Application layer**: This layer provides the business logic, functionality, and user interface for the IoT solutions, such as analytics, visualization, automation, or decision making.
  - **Collaboration and processes layer**: This layer enables the integration and collaboration of the IoT solutions with other systems, processes, and stakeholders, such as cloud services, enterprise applications, or human users.

- The IoT World Forum Reference Model is not the only reference model for IoT, but it is a widely accepted and adopted one that can help to understand the key components and challenges of IoT systems.
- Other reference models for IoT include the IoT Architectural Reference Model (IoT ARM) by the IoT-A project, the IoT Reference Architecture by IBM, and the Azure IoT Reference Architecture by Microsoft.



# IoT Reference Model

The IoT Reference Model is a framework that defines the main concepts and components of IoT systems and architectures. It aims to establish a common grounding and a common language for IoT systems. It consists of the following sub-models:

- **IoT Domain Model**: This model introduces the main concepts of the Internet of Things, such as Devices, IoT Services, and Virtual Entities (VEs). It also defines the relations between these concepts, such as ownership, association, and composition. A Device is a physical object that can communicate with other devices or services. An IoT Service is a software component that provides functionality or data to other services or applications. A VE is a digital representation of a physical or logical entity, such as a person, a location, or a process.
- **IoT Functional View**: This model describes the main functions and capabilities of IoT systems, such as sensing, actuating, processing, communication, and management. It also defines the interfaces and interactions between these functions, such as data flow, control flow, and event flow. The IoT Functional View can be used to identify the functional requirements and design choices of IoT systems.
- **IoT Information View**: This model specifies the information and data models of IoT systems, such as the syntax, semantics, and structure of the data exchanged between IoT components. It also defines the metadata and annotations that describe the data, such as the provenance, quality, and context. The IoT Information View can be used to ensure the interoperability and consistency of data across IoT systems.
- **IoT Deployment and Operational View**: This model describes the deployment and operational aspects of IoT systems, such as the physical and logical topology, the configuration, the security, and the lifecycle management. It also defines the policies and rules that govern the operation and behavior of IoT systems, such as the access control, the privacy, and the governance. The IoT Deployment and Operational View can be used to plan and monitor the deployment and operation of IoT systems.

The IoT Reference Model provides the concepts and definitions on which IoT architectures can be built. It also provides a common vocabulary and a common understanding for IoT stakeholders, such as developers, users, and regulators. The IoT Reference Model is not a prescriptive or normative model, but rather a descriptive and conceptual model that can be adapted and extended to suit different IoT scenarios and domains.



# IoT Reference Architecture

- IoT reference architecture is a conceptual framework that defines the components, interactions, and principles of an IoT solution.
- IoT reference architecture can help to guide the design, development, deployment, and operation of IoT systems that are scalable, secure, interoperable, and adaptable.
- IoT reference architecture can also facilitate the communication and collaboration among different stakeholders, such as developers, vendors, customers, and regulators, by providing a common vocabulary and understanding of IoT concepts and challenges.
- There are different IoT reference architectures proposed by various organizations, such as IBM, Microsoft, and the IoT-A project, but they share some common elements and layers, such as:

  - **Things layer**: This layer consists of the physical or virtual devices that generate, collect, process, and transmit data in an IoT system. Examples of things include sensors, actuators, cameras, smartphones, wearables, etc.
  - **Communication layer**: This layer provides the connectivity and networking protocols that enable the data exchange between things and other components of the IoT system. Examples of communication technologies include Wi-Fi, Bluetooth, ZigBee, cellular, LoRaWAN, etc.
  - **Data layer**: This layer handles the storage, management, and analysis of the data generated by the things layer. Examples of data technologies include databases, data lakes, data warehouses, stream processing, batch processing, etc.
  - **Application layer**: This layer provides the business logic and functionality that deliver value to the end users of the IoT system. Examples of applications include dashboards, alerts, notifications, reports, recommendations, etc.
  - **Security layer**: This layer provides the mechanisms and policies that ensure the confidentiality, integrity, and availability of the data and devices in the IoT system. Examples of security technologies include encryption, authentication, authorization, firewall, etc.
  - **Integration layer**: This layer enables the interoperability and integration of the IoT system with other systems and services, such as cloud, edge, enterprise, social, etc. Examples of integration technologies include APIs, web services, message brokers, etc.

- The following diagram illustrates a generic IoT reference architecture based on the above layers:

IoT reference architecture diagram

- The following table summarizes some of the benefits and challenges of using IoT reference architecture:

| Benefits | Challenges |
| -------- | ---------- |
| - Provides a common understanding and language for IoT systems | - May not cover all the specific requirements and scenarios of a particular IoT system |
| - Supports the reuse and standardization of IoT components and technologies | - May introduce complexity and overhead in the design and implementation of IoT systems |
| - Enables the scalability, security, interoperability, and adaptability of IoT systems | - May require constant updating and evolution to keep up with the fast-changing IoT landscape |
| - Facilitates the communication and collaboration among different stakeholders of IoT systems | - May not be universally accepted or adopted by all the IoT players and communities |



# Introduction for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- In this unit, we will learn about the reference architecture for the Internet of Things (IoT), which is a conceptual framework that defines the components, interfaces, and interactions of an IoT system.
- A reference architecture provides a common vocabulary, a set of principles and best practices, and a logical structure for designing and implementing IoT solutions.
- A reference architecture can also facilitate interoperability, scalability, security, and manageability of IoT systems, as well as support innovation and evolution of IoT technologies and applications.
- There are different reference architectures proposed by various organizations and standardization bodies for the IoT, such as the IoT-Architecture (IoT-A) project, the IEEE P2413 standard, the Industrial Internet Consortium (IIC) reference architecture, and the oneM2M architecture.
- In this unit, we will focus on the IoT-A reference architecture, which is one of the most comprehensive and widely adopted reference architectures for the IoT. It was developed by the IoT-A project, a European research initiative that involved 40 partners from academia, industry, and government.
- The IoT-A reference architecture defines the following key concepts and components of an IoT system:

  - IoT device: A physical object that is capable of sensing, actuating, or interacting with the physical world, and that can communicate with other IoT devices or services.
  - IoT resource: A logical representation of an IoT device or a part of it, such as a sensor, an actuator, or a data stream, that can be accessed and controlled via a standardized interface.
  - Virtual entity: A digital representation of a real-world entity, such as a person, a place, or a thing, that can be associated with one or more IoT resources and that can provide a high-level abstraction of the entity's state and behavior.
  - IoT service: A software component that provides a specific functionality or value to the IoT system or its users, such as data processing, analytics, visualization, or orchestration.
  - Service composition: A process of combining multiple IoT services to create a complex functionality or application that meets the user's needs and goals.
  - IoT domain: A logical grouping of IoT devices, resources, services, and users that share a common context, purpose, or interest, such as smart home, smart city, or smart health.
  - IoT architecture: A description of the structure and behavior of an IoT system, including its components, interfaces, interactions, and constraints.

- The IoT-A reference architecture also defines a layered model that organizes the IoT system into four layers: device layer, network layer, service layer, and application layer. Each layer has a specific role and responsibility in the IoT system, and each layer can be further divided into sub-layers or functional groups.

  - Device layer: This layer consists of the IoT devices and their associated IoT resources. It is responsible for sensing, actuating, and interacting with the physical world, and for providing the data and capabilities of the IoT devices to the upper layers.
  - Network layer: This layer consists of the communication and networking technologies and protocols that enable the data exchange and connectivity among the IoT devices, resources, services, and applications. It is responsible for addressing, routing, transporting, and securing the data in the IoT system.
  - Service layer: This layer consists of the IoT services and their associated virtual entities. It is responsible for providing the functionality and value of the IoT system to the upper layer, and for managing and orchestrating the IoT resources and services in the lower layers.
  - Application layer: This layer consists of the IoT applications and their associated users. It is responsible for providing the user interface and the user experience of the IoT system, and for enabling the user interaction and feedback with the IoT system.

- The IoT-A reference architecture also defines a set of cross-cutting functionalities that span across the four layers and that provide common and essential capabilities for the IoT system, such as security, privacy, trust, identity, discovery, and management.

- The IoT-A reference architecture is not a prescriptive or definitive architecture, but rather a flexible and extensible architecture that can be adapted and customized to different IoT scenarios and requirements. It provides a set of architectural viewpoints, models, patterns, and guidelines that can help the IoT stakeholders to design and implement their own IoT solutions.



# Functional View for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The functional view of the IoT reference architecture describes the system's runtime functional components, their responsibilities, default functions, interfaces and primary interactions .
- The functional view is use-case- and application-independent and is therefore not compatible to the concept of views and viewpoints one-by-one.
- The functional view follows the modular structure of functional blocks organized into layers, as it was proposed e.g. in SENSEI.
- The functional view consists of four layers: Device Layer, Network Layer, Service Layer and Application Layer .
- The Device Layer contains the physical devices that are connected to the IoT system, such as sensors, actuators, RFID tags, etc. The Device Layer is responsible for device management, data acquisition, data processing and data communication.
- The Network Layer provides the connectivity and routing functions for the IoT system, such as network discovery, addressing, security, QoS, etc. The Network Layer is responsible for network management, data transmission, data aggregation and data filtering.
- The Service Layer provides the common services and functionalities for the IoT system, such as service discovery, service composition, service orchestration, service mediation, etc. The Service Layer is responsible for service management, data analysis, data storage and data access.
- The Application Layer contains the specific applications and use cases that utilize the IoT system, such as smart home, smart city, smart health, etc. The Application Layer is responsible for application management, data presentation, data visualization and data interaction.
- The functional view also defines the cross-layer functions that span across multiple layers, such as security, privacy, trust, identity, etc. These functions are responsible for ensuring the reliability, safety and usability of the IoT system.



# Information View for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The information view describes the data and information that the system handles, such as the types, formats, sources, destinations, flows, and transformations of data .
- The information view can be used to identify the data requirements, data models, data quality, data security, data governance, and data analytics of the IoT system .
- The information view can also help to design the data storage, data processing, data integration, data communication, and data visualization components of the IoT system .
- The information view can be represented by different diagrams, such as data flow diagrams, entity-relationship diagrams, class diagrams, or logical data models .
- The information view can be aligned with the functional view and the deployment view of the IoT reference architecture to ensure consistency and completeness of the system design .



# Deployment and Operational View

- The deployment and operational view describes the main real world components of the system such as devices, network routers, servers, etc. and how they are deployed and operated in the IoT environment .
- The deployment view focuses on the physical layout and configuration of the system components, such as the hardware, software, and network resources that are needed to run the system .
- The operational view focuses on the management and monitoring of the system components, such as the processes, policies, and procedures that are needed to ensure the system's availability, reliability, security, and performance .
- The deployment and operational view can vary depending on the specific IoT domain, application, and scenario, but there are some common aspects that are covered in the IoT reference architecture, such as:
  - The device layer, which consists of the IoT devices that sense, actuate, and communicate with the system, such as sensors, actuators, cameras, RFID tags, etc.
  - The network layer, which consists of the network infrastructure that connects the IoT devices to the system, such as routers, gateways, switches, firewalls, etc.
  - The service layer, which consists of the cloud services that provide the core functionality and intelligence of the system, such as data storage, processing, analytics, visualization, etc.
  - The application layer, which consists of the end-user applications that consume and interact with the system, such as web, mobile, desktop, etc.
  - The security layer, which consists of the security mechanisms that protect the system from unauthorized access, modification, or disruption, such as encryption, authentication, authorization, etc.
  - The management layer, which consists of the management tools and processes that enable the administration and maintenance of the system, such as configuration, deployment, monitoring, troubleshooting, etc.



# Other Relevant Architectural Views for IoT

- Besides the reference architecture, there are other ways to design and describe IoT systems based on different perspectives and goals.
- Some of the other relevant architectural views for IoT are:

## Application-Specific Architecture
- This view focuses on the specific requirements and features of a particular IoT application domain, such as smart home, smart city, smart health, etc.
- It defines the functional components, data flows, interfaces, and protocols that are relevant for the application scenario.
- It may also consider the non-functional aspects, such as security, privacy, reliability, scalability, etc.
- It may use existing standards or frameworks, such as ZigBee, Z-Wave, MQTT, CoAP, etc., or develop new ones to meet the application needs.
- An example of an application-specific architecture is the one proposed by the Open Connectivity Foundation (OCF) for smart home devices.

## Open Platform Architecture
- This view focuses on the interoperability and integration of different IoT devices, platforms, and services across various application domains and verticals.
- It defines the common layers, components, interfaces, and protocols that enable the communication and collaboration of heterogeneous IoT entities.
- It may also consider the cross-cutting aspects, such as security, privacy, governance, management, etc.
- It may use existing standards or frameworks, such as IEEE P2413, oneM2M, FIWARE, etc., or develop new ones to achieve the open platform vision.
- An example of an open platform architecture is the one proposed by the IoT-A project for the European IoT ecosystem.

## Network as a Service (NaaS) Architecture
- This view focuses on the provisioning and consumption of network resources and capabilities as a service for IoT applications and devices.
- It defines the abstraction, virtualization, orchestration, and management of network functions and services that support the IoT connectivity and functionality.
- It may also consider the optimization and adaptation aspects, such as quality of service, network slicing, edge computing, etc.
- It may use existing standards or frameworks, such as 5G, SDN, NFV, etc., or develop new ones to enable the NaaS model.
- An example of a NaaS architecture is the one proposed by the 5G-PPP project for the next generation mobile network for IoT.



# Real-World Design Constraints for IoT

- IoT is an emerging technology that aims to connect various devices and networks to enable data collection, analysis, and automation for various applications and domains.
- However, IoT also faces certain design constraints that limit its potential and pose challenges for its development and deployment.
- Some of the common design constraints for IoT are:

  - **Technical challenges**: These include the heterogeneity of devices, protocols, standards, and platforms; the scalability and interoperability of IoT systems; the security and privacy of data and devices; the reliability and availability of IoT services; the energy efficiency and battery life of IoT devices; and the quality of service and user experience of IoT applications  .
  - **Social challenges**: These include the ethical, legal, and social implications of IoT; the trust and acceptance of IoT by users and stakeholders; the regulation and governance of IoT; the impact of IoT on human behavior, health, and well-being; and the social responsibility and sustainability of IoT  .
  - **Compromising privacy**: This refers to the trade-off between the benefits of IoT and the risks of exposing personal or sensitive information to unauthorized parties or malicious attacks. IoT devices and networks collect, store, and transmit large amounts of data, some of which may be personal, confidential, or critical. Therefore, IoT must ensure the protection of data and devices from unauthorized access, modification, or disclosure; the compliance with data protection laws and regulations; and the respect for user preferences and consent  .
  - **Performance trade-offs**: This refers to the trade-off between the functionality and efficiency of IoT and the cost and complexity of IoT. IoT devices and networks must balance the requirements of different applications and domains, such as latency, bandwidth, accuracy, reliability, and security. However, these requirements may conflict with each other or with the constraints of IoT devices and networks, such as power, memory, processing, and communication. Therefore, IoT must optimize the performance of IoT systems while minimizing the cost and complexity of IoT devices and networks  .

- These design constraints must be considered and addressed in the development and deployment of IoT systems, as they affect the feasibility, usability, and value of IoT for various applications and domains.
- Reference architecture is a conceptual model that defines the structure, behavior, and interfaces of IoT systems, and provides a common vocabulary, principles, and guidelines for IoT design and implementation.
- Reference architecture can help overcome some of the design constraints for IoT by providing a standardized and modular approach to IoT system design, enabling interoperability and integration of IoT devices and networks, facilitating security and privacy of IoT data and devices, and supporting performance optimization and quality of service of IoT applications.



# Introduction for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- In this unit, we will learn about the reference architecture for the Internet of Things (IoT), which is a conceptual framework that defines the components, interfaces, and interactions of an IoT system.
- A reference architecture provides a common vocabulary, a set of principles and best practices, and a logical structure for designing and implementing IoT solutions.
- A reference architecture can also facilitate interoperability, scalability, security, and manageability of IoT systems, as well as enable innovation and evolution of IoT technologies and applications.
- There are different reference architectures proposed by various organizations and standardization bodies for the IoT, such as the IoT-Architecture (IoT-A) project, the IEEE P2413 standard, the Industrial Internet Consortium (IIC) reference architecture, and the OpenFog reference architecture.
- In this unit, we will focus on the IoT-A reference architecture, which is one of the most comprehensive and widely adopted reference architectures for the IoT.
- The IoT-A reference architecture defines the following key elements of an IoT system:
  - IoT devices: the physical objects that are connected to the network and can sense, actuate, or communicate data.
  - IoT resources: the logical entities that represent the capabilities and functionalities of IoT devices, such as sensors, actuators, services, or applications.
  - IoT communication: the protocols and mechanisms that enable data exchange and interaction among IoT devices and resources, as well as with external systems and users.
  - IoT middleware: the software layer that provides common services and functions for IoT applications, such as data management, device management, security, discovery, orchestration, and analytics.
  - IoT applications: the software programs that use IoT resources and middleware to provide specific functionalities and value for users and stakeholders.
- The IoT-A reference architecture also defines the following key concepts and models for describing and analyzing IoT systems:
  - IoT domain: a logical grouping of IoT devices and resources that share a common context, purpose, or functionality, such as smart home, smart city, or smart factory.
  - IoT domain model: a representation of the structure, behavior, and properties of an IoT domain, including its devices, resources, communication, middleware, and applications.
  - IoT reference model: a generic and abstract representation of the IoT system that defines the functional layers, components, and interfaces of an IoT architecture, as well as the cross-cutting aspects, such as security, privacy, and trust.
  - IoT information model: a representation of the data and information that are exchanged and processed in an IoT system, including the syntax, semantics, and quality of the data.
  - IoT functional model: a representation of the functionalities and services that are provided and consumed in an IoT system, including the inputs, outputs, and parameters of the services.
  - IoT deployment model: a representation of the physical and logical deployment of an IoT system, including the location, configuration, and connectivity of the devices, resources, middleware, and applications.
- The IoT-A reference architecture provides a methodology and a set of tools for designing and developing IoT solutions based on the above elements, concepts, and models. The methodology consists of the following steps:
  - Requirements analysis: identifying and specifying the functional and non-functional requirements of the IoT solution, such as the use cases, scenarios, goals, and constraints.
  - Architecture design: selecting and composing the appropriate components, interfaces, and interactions of the IoT solution based on the IoT reference model and the IoT domain model.
  - Implementation: developing and deploying the IoT solution based on the IoT deployment model and the IoT functional model, using the IoT middleware and the IoT information model.
  - Evaluation: testing and validating the IoT solution based on the requirements and the quality of service metrics, using the IoT information model and the IoT functional model.
- The tools provided by the IoT-A reference architecture include the following:
  - IoT-Architecture Reference Model (IoT-ARM): a graphical notation and a formal language for describing and analyzing IoT systems based on the IoT reference model, the IoT domain model, and the IoT functional model.
  - IoT-Architecture Modelling Language (IoT-AML): a graphical notation and a formal language for describing and analyzing IoT information based on the IoT information model.
  - IoT-Architecture Design Toolkit (IoT-ADT): a software tool that supports the architecture design and implementation of IoT solutions based on the IoT-ARM and the IoT-AML.
  - IoT-Architecture Evaluation Toolkit (IoT-AET): a software tool that supports the evaluation and validation of IoT solutions based on the IoT-ARM and the IoT-AML.



Hello, I am Sydney, your AI assistant. I will help you with your notes on the topic of technical design constraints for hardware in IoT architecture and protocols. Here is the content in markdown format:

# Technical Design Constraints for Hardware in IoT Architecture and Protocols

- Hardware is the physical layer of an IoT system that consists of devices, sensors, actuators, gateways, and communication modules.
- Hardware design constraints are the limitations or trade-offs that affect the performance, functionality, cost, and reliability of the hardware components.
- Some of the common hardware design constraints for IoT are:

  - **Power consumption**: IoT devices often operate on batteries or harvested energy sources, so they need to minimize their power consumption and maximize their battery life. Power consumption depends on factors such as device type, sensor type, communication protocol, data rate, duty cycle, and sleep mode.
  - **Size and weight**: IoT devices need to be small and lightweight to fit in different environments and applications, such as wearable devices, smart home devices, or industrial sensors. Size and weight depend on factors such as device shape, material, packaging, and integration level.
  - **Cost**: IoT devices need to be low-cost to enable large-scale deployment and adoption, especially for consumer or mass-market applications. Cost depends on factors such as device complexity, component quality, manufacturing process, and economies of scale.
  - **Reliability**: IoT devices need to be reliable and robust to withstand harsh environmental conditions, such as temperature, humidity, vibration, or interference. Reliability depends on factors such as device design, component selection, testing, and maintenance.
  - **Security**: IoT devices need to be secure and protect the data and privacy of the users and the system. Security depends on factors such as device authentication, encryption, firmware update, and attack prevention.

- Hardware design constraints are interrelated and often conflicting, so hardware designers need to balance and optimize them according to the specific requirements and objectives of each IoT application.



# Data representation and visualization for the notes of the Unit 2 - Reference Architecture in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Data representation and visualization are important aspects of IoT systems, as they enable users to understand and interact with the data collected and processed by various smart devices and sensors.
- Data representation refers to the way data is stored, transmitted, and encoded in IoT systems. Data representation can affect the performance, scalability, security, and interoperability of IoT systems. Some of the common data representation formats used in IoT are JSON, XML, CBOR, EXI, and SenML.
- Data visualization refers to the way data is presented and displayed to users in IoT systems. Data visualization can help users to gain insights, identify patterns and trends, and make informed decisions based on the data. Some of the common data visualization techniques used in IoT are charts, graphs, maps, dashboards, and widgets.
- Data analysis and data visualization play a huge role in an IoT dashboard, which is a web-based application that collects data from different smart devices in real-time and converts it into human-readable information.
- Data visualization shows great efficiency when it comes to large series of data, as it can reduce the cognitive load and enhance the perception of the users.
- Data visualization in IoT can also support various use cases and scenarios, such as monitoring, control, prediction, optimization, and anomaly detection.
- Data visualization in IoT faces some challenges, such as the heterogeneity, volume, velocity, and veracity of the data, the diversity of the users and their needs, the security and privacy of the data, and the usability and accessibility of the visualization tools.
- Data visualization in IoT requires some best practices, such as choosing the right data representation format, selecting the appropriate visualization technique, designing the visualization for the target audience, ensuring the quality and reliability of the data, and evaluating the effectiveness and usefulness of the visualization.



# Interaction and Remote Control for the Notes of the Unit 2 - Reference Architecture in the Subject of IoT Architecture and Protocols

- Interaction and remote control are two important aspects of IoT systems that enable users and applications to access and manipulate IoT devices and data.
- Interaction refers to the process of exchanging information between IoT devices and users or applications, such as sending commands, receiving notifications, querying data, or subscribing to events.
- Remote control refers to the ability to monitor and manage IoT devices from a distance, such as configuring settings, updating firmware, or performing diagnostics.
- Interaction and remote control can be achieved through various components and technologies in the IoT reference architecture, which is a generic framework that describes the main elements and relationships of an IoT system.
- The IoT reference architecture can be divided into four layers: device, communication, semantic, and application.
- The device layer consists of the physical or virtual devices that generate, process, or consume data in the IoT system. These devices can have different capabilities, such as sensing, actuating, computing, or networking.
- The communication layer provides the means for data transmission and exchange between devices and other components in the IoT system. This layer can use various protocols, such as MQTT, CoAP, HTTP, or AMQP, depending on the requirements and constraints of the IoT scenario.
- The semantic layer provides the means for data representation and interpretation in the IoT system. This layer can use various standards, such as JSON, XML, RDF, or OWL, to define the syntax and semantics of the data and enable interoperability and integration among different devices and applications.
- The application layer consists of the software applications that provide the functionality and value for the IoT system. These applications can use various services, such as cloud computing, data analytics, or artificial intelligence, to process, store, visualize, or act upon the data from the IoT devices.
- Interaction and remote control can be implemented in different ways depending on the layer and the component involved. For example, interaction can be done through APIs, web services, or message brokers, while remote control can be done through device management platforms, configuration tools, or command-line interfaces.
- Interaction and remote control can also be influenced by various factors, such as security, privacy, scalability, reliability, or performance, that need to be considered and addressed in the design and implementation of the IoT system.



# Unit 3 - IOT Data Link Layer & Network Layer Protocols

The data link layer and the network layer are two important layers in the IoT technology stack. They are responsible for providing reliable and efficient communication between IoT devices and other networks.

## Data Link Layer Protocols

The data link layer provides service to the network layer. It is responsible for framing, error detection, medium access control, and link management. There are various protocols and standard technologies specified by different organizations for data link protocols. Some of the common data link layer protocols in IoT are:

- **Bluetooth**: Bluetooth is a short-range wireless communication network over a radio frequency. It is widely used for connecting IoT devices such as smartphones, wearables, speakers, keyboards, etc. Bluetooth supports low power consumption, low cost, and easy pairing. There are different versions of Bluetooth, such as Bluetooth Classic, Bluetooth Low Energy (BLE), and Bluetooth Mesh.
- **Wi-Fi**: Wi-Fi is a wireless LAN technology that uses radio waves to provide high-speed internet access and network connectivity. Wi-Fi is one of the most popular and ubiquitous data link layer protocols in IoT. It supports high data rates, long range, and interoperability. Wi-Fi can be used for connecting IoT devices such as laptops, cameras, smart TVs, etc. There are different standards of Wi-Fi, such as IEEE 802.11a/b/g/n/ac/ax.
- **Zigbee**: Zigbee is a low-power, low-data-rate, and low-cost wireless mesh network protocol. It is based on the IEEE 802.15.4 standard and operates in the 2.4 GHz frequency band. Zigbee is designed for applications that require long battery life, network scalability, and self-healing. Zigbee can be used for connecting IoT devices such as sensors, actuators, smart meters, etc.
- **Z-Wave**: Z-Wave is another low-power, low-data-rate, and low-cost wireless mesh network protocol. It operates in the sub-GHz frequency band and supports up to 232 nodes per network. Z-Wave is optimized for home automation and security applications. Z-Wave can be used for connecting IoT devices such as lights, locks, thermostats, etc.
- **LoRa**: LoRa is a long-range, low-power, and low-data-rate wireless network protocol. It uses a spread spectrum modulation technique and operates in the sub-GHz frequency band. LoRa is suitable for applications that require wide area coverage, low bandwidth, and low cost. LoRa can be used for connecting IoT devices such as smart agriculture, smart city, smart parking, etc.

## Network Layer Protocols

The network layer provides service to the transport layer. It is responsible for addressing, routing, and forwarding of data packets. There are various protocols and standard technologies specified by different organizations for network layer protocols. Some of the common network layer protocols in IoT are:

- **IPv4**: IPv4 is the fourth version of the Internet Protocol (IP). It is the most widely used network layer protocol in the internet and IoT. It supports a 32-bit address space, which can accommodate up to 4.3 billion devices. IPv4 uses a hierarchical addressing scheme and supports various routing protocols, such as RIP, OSPF, BGP, etc.
- **IPv6**: IPv6 is the sixth version of the Internet Protocol (IP). It is the successor of IPv4 and aims to overcome its limitations, such as address exhaustion, security, and scalability. It supports a 128-bit address space, which can accommodate up to 3.4 x 10^38 devices. IPv6 uses a flat addressing scheme and supports various routing protocols, such as RIPng, OSPFv3, BGP4+, etc.
- **6LoWPAN**: 6LoWPAN is an adaptation layer that enables the transmission of IPv6 packets over low-power wireless personal area networks (LoWPANs), such as IEEE 802.15.4. It provides header compression, fragmentation, and reassembly of IPv6 packets to fit the constraints of LoWPANs. 6LoWPAN enables the integration of IoT devices with the IPv6 internet.
- **CoAP**: CoAP is an application layer protocol that provides a RESTful web service for constrained IoT devices and networks. It is based on the HTTP protocol and uses the UDP transport protocol. It supports various features, such as caching, discovery, observation, multicast, etc. CoAP enables the communication between IoT devices and web servers.
- **MQTT**: MQTT is an application layer protocol that provides a publish/subscribe messaging pattern for IoT devices



# PHY/MAC Layer(3GPP MTC

- PHY (Physical) layer is the lowest layer of the 3GPP radio interface protocol stack that handles the transmission and reception of data over the air interface.
- MAC (Medium Access Control) layer is the sub-layer of the 3GPP Layer 2 that controls the access to the shared radio resources and multiplexes the data from different logical channels onto transport channels.
- 3GPP MTC (Machine Type Communication) is a term used to describe the communication of devices that generate or consume small and infrequent data traffic, such as sensors, smart meters, and wearable devices.
- 3GPP has developed several technologies and enhancements for the PHY and MAC layers to support the MTC use cases and requirements, such as low power consumption, low device cost, high network capacity, and wide coverage.
- Some of the key PHY and MAC layer solutions for MTC are:

  - Narrowband IoT (NB-IoT): A new radio access technology that operates in narrowband spectrum and provides improved coverage, reduced device complexity, and extended battery life for MTC devices.
  - LTE-M: A set of features that enable LTE to support MTC devices with low power consumption, low data rate, and low mobility.
  - Enhanced Coverage GSM (EC-GSM): A set of enhancements that improve the coverage and battery life of GSM devices for MTC applications.
  - Power Saving Mode (PSM) and Extended Discontinuous Reception (eDRX): Two mechanisms that allow MTC devices to enter a low power state and reduce the frequency of signaling and data transmission, thus saving battery power and network resources.
  - Single Cell Point to Multipoint (SC-PTM): A transmission mode that enables a single cell to broadcast data to multiple MTC devices simultaneously, thus increasing the network efficiency and reducing the signaling overhead.
  - Small Data Transmission (SDT): A set of procedures that enable MTC devices to transmit or receive small amounts of data without establishing a dedicated radio bearer, thus reducing the latency and signaling overhead.
  - Random Access Channel (RACH) Enhancements: A set of enhancements that improve the performance and reliability of the RACH procedure for MTC devices, such as preamble repetition, early data transmission, and contention resolution diversity.
  - Device Triggering: A mechanism that allows the network to initiate a data transmission from a MTC device that is in idle mode, thus enabling the network to request data from the device on demand.



# IEEE 802.11

- IEEE 802.11 is a set of standards for wireless local area networks (WLANs) that operate in the 2.4 GHz, 5 GHz, and 60 GHz frequency bands .
- IEEE 802.11 defines the physical layer (PHY) and the medium access control (MAC) layer specifications for WLANs.
- IEEE 802.11 has several amendments that extend or modify the original standard, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11p, and 802.11ad .
- IEEE 802.11 is also known as Wi-Fi, which is a trademark of the Wi-Fi Alliance, an industry association that certifies the interoperability of WLAN products.
- IEEE 802.11 is widely used in home and office networks, as well as in public hotspots, to allow wireless devices to communicate with each other and access the Internet without wires.
- IEEE 802.11 is also a basis for vehicle-based communication networks with IEEE 802.11p, which is designed for intelligent transportation systems and vehicular ad hoc networks.
- IEEE 802.11 is a part of the IEEE 802 family of standards, which cover local and metropolitan area networks (LANs and MANs) with various technologies and architectures.



# IEEE 802.15

- IEEE 802.15 is a working group of the Institute of Electrical and Electronics Engineers (IEEE) IEEE 802 standards committee which specifies Wireless Specialty Networks (WSN) standards .
- The working group was formerly known as Working Group for Wireless Personal Area Networks (WPANs) .
- The working group has developed several standards and amendments for different types of WSNs, such as low-rate, high-rate, ultra-wideband, mesh, and body area networks .
- Some of the most widely used standards and amendments are:

  - IEEE 802.15.1: This is the first standard developed by the working group, which is based on the Bluetooth specification for short-range wireless communication.
  - IEEE 802.15.4: This is the most popular standard for low-rate wireless personal area networks (LR-WPANs), which are suitable for low-power, low-cost, and low-data-rate applications, such as sensor networks, smart home, and industrial automation .
  - IEEE 802.15.4a: This is an amendment to IEEE 802.15.4, which specifies additional physical layers (PHYs) to the original standard, such as chirp spread spectrum (CSS) and ultra-wideband (UWB), which enable higher data rates, longer ranges, and more precise ranging and localization .
  - IEEE 802.15.6: This is a standard for wireless body area networks (WBANs), which are designed for medical and non-medical applications, such as health monitoring, wearable devices, and implantable devices.
  - IEEE 802.15.7: This is a standard for visible light communication (VLC), which uses light-emitting diodes (LEDs) to transmit data over short distances, such as indoor lighting, vehicle communication, and signage.
  - IEEE 802.15.8: This is a standard for peer-aware communication (PAC), which enables direct device-to-device communication without the need for a central coordinator, such as in social networking, gaming, and emergency scenarios.
  - IEEE 802.15.9: This is a recommended practice for key management in IEEE 802.15.4 networks, which provides guidelines for securing the network layer, the application layer, and the management plane.
  - IEEE 802.15.10: This is a standard for routing protocol for low-power and lossy networks (RPL), which is a distance vector routing protocol that supports multipoint-to-point, point-to-multipoint, and point-to-point traffic flows, as well as mobility and multicast.
  - IEEE 802.15.11: This is a standard for wireless network management (WNM), which defines the network management functions and interfaces for IEEE 802.15 networks, such as configuration, fault, performance, and security management.
  - IEEE 802.15.12: This is a standard for wireless medium access control (MAC) and physical layer (PHY) specifications for long range low power wide area network (LRLPWAN), which is a new type of WSN that aims to provide long-range, low-power, and low-cost connectivity for massive numbers of devices, such as in Internet of Things (IoT) applications.



# WirelessHART

- WirelessHART is a wireless communications protocol for process automation applications.
- It is a subset of the HART industrial instrument communication standard as of version 7, communicating process data over 2.4 GHz radio waves .
- It adds wireless capabilities to HART technology while maintaining compatibility with existing HART devices, commands, and tools.
- It is based on the IEEE 802.15.4 standard for low-power, low-data-rate wireless personal area networks (WPANs).
- It uses mesh networking technology, which means that each device can act as a router and relay messages from other devices.
- It supports self-organization, self-healing, and channel hopping to ensure reliable and secure data transmission.
- It uses 128-bit AES encryption and a join key to authenticate devices and protect data integrity.
- It has a network manager that coordinates the network operation and assigns time slots and channels to each device.
- It has a gateway that serves as an interface between the wireless network and a wired network or a host control system .
- It supports up to 250 devices per network and a maximum hop count of 15.
- It has a typical update rate of 1 second and a latency of less than 2 seconds.
- It is designed for low-power consumption and long battery life, with an estimated 5 to 10 years of operation.
- It is a multi-vendor, interoperable wireless standard, developed by the HART Communication Foundation (now FieldComm Group) and ratified by the International Electrotechnical Commission (IEC) as IEC 62591.



# ZWave

ZWave is a wireless communication protocol designed for smart home and IoT devices. It operates on the low-frequency 800 to 900 MHz band, which avoids interference with the 2.4 GHz band where Wi-Fi and Bluetooth operate. ZWave supports encryption, mesh networking, low power consumption, and interoperability among different vendors.

Some of the features and characteristics of ZWave are:

- It was developed by Zensys, a Danish company, in 1999.
- It is a proprietary protocol owned by Sigma Designs, Inc. An open source implementation of ZWave protocol stack, called open-zwave, is also available but it does not support security layer.
- It uses frequency shift keying (FSK) modulation and Gaussian frequency shift keying (GFSK) for data transmission.
- It supports up to 232 nodes per network and up to four hops between the source and the destination.
- It has a data rate of 9.6 kbps, 40 kbps, or 100 kbps depending on the region and the device class.
- It has a range of up to 100 meters in line of sight and up to 30 meters indoors.
- It supports three types of devices: controllers, slaves, and routing slaves. Controllers initiate and manage the communication, slaves respond to the commands from the controllers, and routing slaves act as repeaters and routers for the messages.
- It uses a source-routed protocol, which means that the controller specifies the route for each message. The route can be updated dynamically based on the network topology and the availability of the nodes.
- It supports two types of network topologies: star and mesh. In star topology, all the devices communicate directly with the controller. In mesh topology, the devices can communicate with each other and relay the messages for other devices.
- It supports encryption based on AES-128 algorithm. The encryption keys are exchanged during the network inclusion process, which is initiated by the controller.
- It supports interoperability among different vendors and devices through the ZWave Alliance, which is a consortium of companies that adhere to the ZWave certification program. The certification ensures that the devices comply with the ZWave protocol and can work together seamlessly  .



# Bluetooth Low Energy

- Bluetooth Low Energy (BLE) is a wireless personal area network technology designed and marketed by the Bluetooth Special Interest Group (Bluetooth SIG) aimed at novel applications in the healthcare, fitness, beacons, security, and home entertainment industries.
- BLE is distinct from the previous (often called "classic") Bluetooth Basic Rate/Enhanced Data Rate (BR/EDR) protocol, but the two protocols can both be supported by one device: the Bluetooth 4.0 specification permits devices to implement either or both of the LE and BR/EDR systems.
- BLE has the following advantages over classic Bluetooth:
  - Lower power consumption: BLE devices can operate for months or years on a coin cell battery, while classic Bluetooth devices require frequent recharging.
  - Faster connection time: BLE devices can connect in a few milliseconds, while classic Bluetooth devices may take seconds.
  - Simpler pairing process: BLE devices can use a variety of methods to pair, such as scanning a QR code, tapping a NFC tag, or using a proximity-based technique, while classic Bluetooth devices require a PIN code or a confirmation button.
  - Higher scalability: BLE devices can support up to 20 connections simultaneously, while classic Bluetooth devices are limited to 7.
  - More flexibility: BLE devices can use a variety of profiles and services to communicate, while classic Bluetooth devices are restricted to predefined profiles.
- BLE uses two protocols for discovery and communication between devices: the Generic Access Profile (GAP) and the Generic Attribute Profile (GATT).
  - GAP defines how devices advertise themselves and discover other devices. GAP also defines the roles and modes of devices, such as peripheral, central, broadcaster, and observer.
  - GATT defines how devices exchange data using services and characteristics. GATT also defines the procedures and formats for data transmission, such as read, write, notify, and indicate.
- BLE devices can operate in different modes depending on their roles and capabilities:
  - Peripheral mode: A device that advertises itself and provides data or services to other devices. For example, a heart rate monitor, a smartwatch, or a beacon.
  - Central mode: A device that scans for and connects to other devices that provide data or services. For example, a smartphone, a tablet, or a laptop.
  - Broadcaster mode: A device that advertises itself but does not allow connections from other devices. For example, a sensor, a key finder, or a tag.
  - Observer mode: A device that scans for other devices that advertise themselves but does not connect to them. For example, a scanner, a locator, or a tracker.



# Zigbee Smart Energy

Zigbee Smart Energy is a wireless protocol for device monitoring and control that aims to reduce energy consumption and waste, and enable utilities to manage customers' energy use. It is based on the Zigbee standard, which is a low-cost and low-power communication technology for the Internet of Things (IoT).

Some of the features and benefits of Zigbee Smart Energy are:

- It supports interoperability and compatibility among different devices and vendors .
- It operates on the global 2.4 GHz spectrum and regional SubGHz frequencies, which are license-free and offer good range and penetration .
- It uses Internet Protocol (IP) as the network layer, which allows seamless integration with existing IP networks and applications.
- It provides security and privacy mechanisms, such as encryption, authentication, and key management .
- It enables smart metering, demand response, load control, distributed generation, and home automation applications  .
- It facilitates green homes and sustainability by empowering consumers to monitor and optimize their energy usage and reduce their carbon footprint.

Zigbee Smart Energy is suitable for both residential and commercial settings, and can be deployed in various scenarios, such as:

- Smart meters that communicate with utilities and consumers, and provide real-time data and feedback on energy consumption and pricing .
- Smart appliances and devices that can be remotely controlled and programmed to operate at optimal times and modes, and respond to dynamic pricing signals .
- Smart thermostats and HVAC systems that can adjust the temperature and ventilation according to the occupancy and preferences of the users, and participate in demand response programs .
- Smart lighting and sensors that can dim or turn off the lights when not needed, and detect motion, temperature, humidity, and other environmental factors .
- Smart plugs and outlets that can measure and report the power consumption of connected devices, and switch them on or off according to schedules or commands .
- Smart solar panels and batteries that can generate and store renewable energy, and sell or buy excess energy from the grid .

Zigbee Smart Energy is an evolving standard that has two versions: Zigbee Smart Energy 1.0 and Zigbee Smart Energy 2.0. The main difference between them is that Zigbee Smart Energy 1.0 uses Zigbee Cluster Library (ZCL) as the application layer, while Zigbee Smart Energy 2.0 uses IP as the application layer. Zigbee Smart Energy 2.0 is designed to be more scalable, flexible, and interoperable with other IP-based protocols and devices. However, Zigbee Smart Energy 1.0 is still widely used and supported by many products and utilities .

Zigbee Smart Energy is one of the leading protocols for smart energy and IoT applications, and has been adopted by many countries and regions, such as the US, UK, Europe, Australia, Japan, and Korea  . It is also supported by many industry and standard organizations, such as the Zigbee Alliance, the Smart Energy Profile 2.0 Consortium, the Wi-SUN Alliance, and the OpenADR Alliance  . Zigbee Smart Energy is expected to grow and expand in the future, as more devices and applications become connected and smart  .



# DASH7

DASH7 is a wireless sensor and actuator network protocol that operates in the sub-GHz ISM bands, such as 433 MHz, 868 MHz and 915 MHz. It is based on the ISO/IEC 18000-7 standard for active RFID and defines the physical, data link and network layers of the protocol stack. Some of the features and applications of DASH7 are:

- It supports bi-directional communication between nodes, which can be either tags or readers.
- It has a range of up to 2 km in line-of-sight and up to 200 m in non-line-of-sight conditions, depending on the antenna and power settings.
- It has a low power consumption, with an average current of less than 50 µA for a tag and less than 1 mA for a reader.
- It has a low data rate of up to 200 kbps, which is suitable for transmitting small packets of sensor or actuator data.
- It has a low latency of less than 1 second for a round-trip communication between a tag and a reader.
- It has a high scalability, with up to 250 nodes per network and up to 65,536 networks per channel.
- It has a high security, with AES-128 encryption and authentication options.
- It has a high interoperability, with a common air interface and a standardized application layer.
- It can be used for various applications, such as asset tracking, supply chain management, smart metering, building automation, environmental monitoring, industrial control, and automotive safety.



# Network Layer

The network layer is the third layer of the OSI model and the second layer of the TCP/IP model. It is responsible for addressing and routing of data packets in a network. It also provides services such as fragmentation, error detection, congestion control, and security.

## Network Layer Protocols for IoT

The network layer protocols for IoT are designed to meet the specific requirements and challenges of IoT devices, such as low power consumption, limited bandwidth, scalability, mobility, and interoperability. Some of the common network layer protocols for IoT are:

- **IPv6**: IPv6 is the latest version of the Internet Protocol, which provides a larger address space, better security, and more efficient routing than IPv4. IPv6 is essential for IoT, as it can support the massive number of devices and sensors that need to be connected to the internet. IPv6 also enables end-to-end communication, which reduces the need for intermediate devices such as gateways and proxies.
- **6LoWPAN**: 6LoWPAN stands for IPv6 over Low-Power Wireless Personal Area Networks. It is a protocol that adapts IPv6 to the constraints of low-power and low-bandwidth wireless networks, such as ZigBee, Bluetooth Low Energy, and IEEE 802.15.4. 6LoWPAN enables IPv6 packets to be transmitted over these networks by compressing the headers, fragmenting the payloads, and using mesh routing. 6LoWPAN allows IoT devices to communicate directly with the internet, without requiring a gateway or a translation mechanism.
- **RPL**: RPL stands for Routing Protocol for Low-Power and Lossy Networks. It is a protocol that provides efficient and reliable routing for IoT networks that are characterized by high packet loss, low data rates, and dynamic topology. RPL organizes the network into a Destination-Oriented Directed Acyclic Graph (DODAG), where each node has a rank that determines its position and role in the network. RPL supports both upward and downward routing, as well as multicast and anycast communication. RPL also provides mechanisms for loop detection, loop avoidance, and loop repair.
- **CoAP**: CoAP stands for Constrained Application Protocol. It is a protocol that provides a lightweight and RESTful application layer for IoT devices. CoAP is based on the HTTP model, but uses UDP instead of TCP, and employs a binary format instead of text. CoAP supports four methods: GET, PUT, POST, and DELETE, and provides features such as caching, discovery, observation, and block-wise transfer. CoAP enables IoT devices to interact with web services and applications, as well as with each other. CoAP can also be mapped to HTTP, allowing interoperability between the two protocols.

## References

: Network Layer Protocols: IOT Part 8 - Engineers Garage
: IoT Network Layer Protocols - TechVidvan
: Architecture of Internet of Things (IoT) - GeeksforGeeks
: 6 IoT architecture layers and components explained - IoT Agenda
: Trusted Internet of Things (IoT) Device Network-Layer Onboarding and Lifecycle Management - NIST



# IPv4

- IPv4 stands for Internet Protocol version 4. It is the fourth revision of the Internet protocol and a widely used protocol for communication over the Internet or on a local network  .
- IPv4 is a connectionless protocol that uses packet-switching technology to transfer data. It operates at the network layer of the OSI model and the internet layer of the TCP/IP model .
- An IPv4 address is a 32-bit address that identifies a device on a network. It is composed of four octets (groups of 8 bits) separated by dots. Each octet can have a value from 0 to 255. For example, 192.168.1.1 is a valid IPv4 address .
- IPv4 addresses are divided into five classes: A, B, C, D, and E. Each class has a different range of values for the first octet and a different number of bits for the network and host portions of the address. Class A addresses are used for large networks, class B for medium-sized networks, class C for small networks, class D for multicast groups, and class E for experimental purposes .
- IPv4 addresses can be written in different notations, such as decimal, binary, hexadecimal, or dotted decimal. For example, the IPv4 address 192.168.1.1 can be written as C0.A8.01.01 in hexadecimal or 11000000.10101000.00000001.00000001 in binary .
- IPv4 uses a subnet mask to determine which part of the address belongs to the network and which part belongs to the host. A subnet mask is a 32-bit number that has the same format as an IPv4 address. The bits that correspond to the network portion of the address are set to 1, and the bits that correspond to the host portion are set to 0. For example, the subnet mask for a class C address is 255.255.255.0 or 11111111.11111111.11111111.00000000 .
- IPv4 supports both static and dynamic addressing. Static addressing means that the IPv4 address of a device is manually configured and does not change. Dynamic addressing means that the IPv4 address of a device is automatically assigned by a server, such as a DHCP server, and can change over time .
- IPv4 has a limited address space of 2^32 or about 4.3 billion possible addresses. This is not enough to accommodate the growing number of devices connected to the Internet. Therefore, IPv4 uses various techniques to conserve and extend the address space, such as network address translation (NAT), private addressing, and classless inter-domain routing (CIDR) .
- IPv4 is gradually being replaced by IPv6, which is the sixth version of the Internet protocol and has a much larger address space of 2^128 or about 3.4 x 10^38 possible addresses. IPv6 also has other advantages over IPv4, such as improved security, simplified header format, and enhanced support for mobility and multicast .



# IPv6 for IOT

- IPv6 is the most recent version of Internet Protocol (IP), which is the system of assigning unique addresses to devices connected to the internet.
- IPv6 is designed to supply IP addressing and additional security to support the predicted growth of connected devices in IoT, manufacturing, and emerging areas like autonomous driving.
- IPv6 is based on 128-bit addresses and is able to facilitate close to 340 undecillion unique IP identifiers, which is a massive increase in capability compared to IPv4, which is based on 32-bit addresses and can only support about 4.3 billion addresses.
- IPv6 provides improved remote access and management for large fleets of IoT devices, as it allows each device to have a globally unique address that can be reached directly from anywhere on the internet.
- IPv6 also has a highly efficient multicast communication feature, which all but eliminates the need for routine broadcast messaging, which is when a device sends a message to all other devices on the network. This improvement helps in preserving the battery life of IoT devices by reducing the number of packets processed.
- IPv6 is capable of sending large data packets simultaneously to conserve bandwidth, which is the amount of data that can be transmitted in a given time. With the help of fast transmission of data due to IPv6, devices used in IoT will also be able to interact with each other more efficiently.
- IPv6 provides far better security than IPv4, as it provides confidentiality, authenticity, and data integrity as well. Confidentiality means that the data is encrypted and can only be read by the intended recipient. Authenticity means that the sender and receiver can verify each other's identity. Data integrity means that the data is not altered or corrupted during transmission.
- IPv6 also supports features such as stateless address autoconfiguration, which allows devices to automatically configure their own IP addresses without the need for a central server, and neighbor discovery, which allows devices to discover and communicate with other devices on the same network. These features make IPv6 more suitable for dynamic and heterogeneous IoT environments.



# 6LoWPAN

- 6LoWPAN stands for **IPv6 over Low-power Wireless Personal Area Networks** .
- It is an open standard defined by the **Internet Engineering Task Force (IETF)**  that enables low-power devices with limited processing capabilities to participate in the **Internet of Things (IoT)**.
- It allows **IPv6 datagrams** to be transmitted over **IEEE 802.15.4** based networks, which are low-power wireless mesh networks that operate in the 2.4 GHz and sub-GHz frequency bands  .
- It defines mechanisms for **encapsulation**, **header compression**, **neighbor discovery**, **routing**, **security**, and **fragmentation** of IPv6 packets over IEEE 802.15.4 links .
- It supports various **application layer protocols**, such as **CoAP**, **MQTT**, **HTTP**, and **WebSockets**, that can communicate with web servers and cloud services.
- It enables wireless internet connectivity at lower data rates for applications such as **residential and office automation**, **smart grid**, **industrial monitoring**, **healthcare**, and **environmental sensing** .
- It can interoperate with other IPv6 networks through **edge routers** that can translate between 6LoWPAN and IPv4 or IPv6 protocols.



# 6TiSCH

- 6TiSCH stands for IPv6 over the Time Slotted Channel Hopping (TSCH) mode of IEEE 802.15.4e.
- It is a protocol stack that combines the industrial performance of TSCH with the seamless integration of IPv6 for the Industrial Internet of Things (IIoT).
- It enables reliable and delay-bounded communication in multi-hop and scalable networks of low-power and lossy devices.
- It consists of several components, such as:
  - The IEEE 802.15.4e TSCH link layer protocol, which provides time synchronization, channel hopping, and medium access control.
  - The 6TiSCH Operation Sublayer (6top), which provides an interface between the link layer and the network layer, and allows the nodes to dynamically allocate and manage the TSCH schedule.
  - The 6top Protocol (6P), which defines the messages and procedures for the nodes to negotiate the TSCH schedule with their neighbors.
  - The 6LoWPAN adaptation layer, which enables the compression and fragmentation of IPv6 packets over the IEEE 802.15.4 frame format.
  - The IP-in-IP encapsulation, which allows the nodes to tunnel IPv6 packets over the 6LoWPAN network.
  - The Routing Protocol for Low-Power and Lossy Networks (RPL), which provides routing and topology management for the 6TiSCH network.
- 6TiSCH is a working group at the Internet Engineering Task Force (IETF), which is standardizing the architecture and protocols for 6TiSCH networks.
- 6TiSCH is a key technology for the convergence of Operational Technology (OT) and Information Technology (IT), as it offers both industrial performance and seamless integration into the Internet.



# ND for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

## Data Link Layer Protocols
- The data link layer provides service to the network layer and is responsible for reliable transmission of data frames between nodes on the same network.
- There are various protocols and standard technologies specified by different organizations for data link protocols.
- Some of the common data link protocols in IoT are:
  - **Bluetooth**: A short-range wireless communication network over a radio frequency. It supports point-to-point and point-to-multipoint connections and can be used for data exchange, audio streaming, and device control.
  - **Wi-Fi**: A wireless LAN technology that uses radio waves to provide high-speed internet access and network connections. It supports various standards such as 802.11a/b/g/n/ac/ax and can be used for home automation, smart appliances, and cloud services.
  - **ZigBee**: A low-power, low-rate wireless personal area network (WPAN) that operates in the 2.4 GHz frequency band. It supports mesh networking and can be used for sensor networks, smart lighting, and smart metering.
  - **Z-Wave**: A low-power, low-rate wireless home automation network that operates in the sub-GHz frequency band. It supports mesh networking and can be used for security systems, smart locks, and smart thermostats.
  - **LoRa**: A long-range, low-power wireless network that operates in the sub-GHz frequency band. It supports star-of-stars topology and can be used for smart agriculture, smart city, and smart logistics.

## Network Layer Protocols
- The network layer is responsible for addressing and routing of data packets between different networks.
- There are various protocols and standard technologies specified by different organizations for network layer protocols.
- Some of the common network layer protocols in IoT are:
  - **IPv4**: The most widely used internet protocol that provides logical addressing and fragmentation of data packets. It supports 32-bit addresses and can accommodate up to 4.3 billion devices.
  - **IPv6**: The next generation internet protocol that provides logical addressing and fragmentation of data packets. It supports 128-bit addresses and can accommodate up to 3.4 x 10^38 devices. It also supports features such as stateless address autoconfiguration, neighbor discovery, and multicast.
  - **6LoWPAN**: A protocol that enables IPv6 packets to be transmitted over low-power wireless networks such as ZigBee, Z-Wave, and Bluetooth Low Energy (BLE). It compresses the IPv6 header and adapts it to the data link layer frame size.
  - **CoAP**: A protocol that enables constrained devices to communicate with web services using a RESTful architecture. It uses UDP as the transport layer protocol and supports features such as caching, discovery, and observation.
  - **MQTT**: A protocol that enables publish-subscribe messaging between devices and applications. It uses TCP as the transport layer protocol and supports features such as quality of service, retain messages, and last will and testament.



# DHCP

DHCP stands for Dynamic Host Configuration Protocol. It is a network management protocol that automatically provides an Internet Protocol (IP) host with its IP address and other related configuration information such as the subnet mask and default gateway . It is used on Internet Protocol (IP) networks for automatically assigning IP addresses and other communication parameters to devices connected to the network using a client–server architecture .

## Features of DHCP

- DHCP simplifies the management of IP addresses and other network configuration parameters by centralizing them on a server.
- DHCP enables devices to join a network without manual configuration and to leave a network without leaving a trace.
- DHCP supports both static and dynamic allocation of IP addresses. Static allocation means that a device always receives the same IP address from the DHCP server. Dynamic allocation means that a device receives an IP address for a limited period of time, called a lease, and may change its IP address when the lease expires or when it reconnects to the network.
- DHCP supports the reuse of IP addresses that are no longer needed by devices that have left the network or have changed their IP address.
- DHCP supports the discovery of other network services, such as Domain Name System (DNS) servers, Network Time Protocol (NTP) servers, and proxy servers, by providing them as options in the DHCP messages.

## How DHCP works

- DHCP uses a client–server model, where a DHCP server provides configuration information to one or more DHCP clients. A DHCP client is any device that requests an IP address from a DHCP server. A DHCP server is any device that responds to DHCP requests and provides IP addresses and other configuration information to DHCP clients.
- DHCP uses four types of messages to communicate between the client and the server: DHCPDISCOVER, DHCPOFFER, DHCPREQUEST, and DHCPACK. The following steps describe the basic DHCP process:

  1. A DHCP client that does not have an IP address or wants to renew its IP address broadcasts a DHCPDISCOVER message to the network, asking for an IP address and other configuration information.
  2. A DHCP server that receives the DHCPDISCOVER message and has an available IP address for the client responds with a DHCPOFFER message, offering the IP address and other configuration information to the client.
  3. The DHCP client receives one or more DHCPOFFER messages from different DHCP servers and chooses one of them. The client then broadcasts a DHCPREQUEST message to the network, requesting the IP address and other configuration information from the chosen DHCP server and rejecting the other offers.
  4. The DHCP server that receives the DHCPREQUEST message and confirms that the IP address is still available for the client responds with a DHCPACK message, acknowledging the IP address and other configuration information to the client. The DHCP server also updates its database with the IP address and other information of the client.
  5. The DHCP client receives the DHCPACK message and configures its network interface with the IP address and other configuration information. The client also starts a timer for the lease duration of the IP address, which is specified in the DHCPACK message.

- If the DHCP client wants to extend its lease or change its IP address, it can repeat the DHCP process before the lease expires. If the DHCP client wants to release its IP address, it can send a DHCPRELEASE message to the DHCP server, informing the server that the IP address is no longer needed. The DHCP server then updates its database and makes the IP address available for other clients.

## Advantages and disadvantages of DHCP

- Some of the advantages of DHCP are:

  - It reduces the administrative overhead and human errors involved in manually assigning and managing IP addresses and other network configuration parameters.
  - It enables devices to join and leave a network easily and dynamically, without requiring any intervention from the network administrator or the user.
  - It optimizes the utilization of IP addresses and avoids IP address conflicts by reusing IP addresses that are no longer needed by devices that have left the network or have changed their IP address.
  - It facilitates the discovery and configuration of other network services, such as DNS servers, NTP servers, and proxy servers, by providing them as options in the DHCP messages.

- Some of the disadvantages of DHCP are:

  - It introduces a dependency on the availability and reliability of the DHCP server. If the DHCP server fails or becomes unreachable, the DHCP clients may not be able to obtain or renew their IP addresses and other configuration information, resulting in network connectivity problems.
  - It may pose a security risk if the DHCP server is not properly secured and authenticated.



# ICMP

- ICMP stands for Internet Control Message Protocol  .
- It is a network layer protocol used by network devices to diagnose network communication issues  .
- It is not associated with any transport layer protocol, such as TCP or UDP .
- It is a connectionless protocol, meaning a device does not need to open a connection with the target device before sending a message.
- It is used to generate error messages to the source IP address when network problems prevent delivery of IP packets .
- It is also used to determine whether or not data is reaching its intended destination in a timely manner .
- It is also used for inter-device communication, carrying everything from redirect instructions to timestamps for synchronization between devices.
- Some common types of ICMP messages are:
  - Echo request and echo reply: used to test the reachability and latency of a destination device (e.g., ping command).
  - Destination unreachable: used to inform the source device that the destination device or network is unreachable for some reason (e.g., network congestion, routing error, firewall blocking, etc.).
  - Time exceeded: used to inform the source device that the time to live (TTL) value of an IP packet has expired and the packet has been discarded (e.g., traceroute command).
  - Parameter problem: used to inform the source device that an IP header field or option is invalid or missing.
  - Source quench: used to inform the source device that the destination device or network is overloaded and cannot process the incoming packets (e.g., congestion control).
  - Redirect: used to inform the source device that there is a better route to the destination device or network (e.g., routing optimization).



# RPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for **Routing Protocol for Low-Power and Lossy Networks**.
- It is an **IPv6** routing protocol that is standardized for the **Internet of Things (IoT)** by **Internet-Engineering Task Force (IETF)**  .
- It is designed for **resource-constrained** networks that have **heterogeneous traffic**, **low bandwidth**, **high packet loss**, and **dynamic topology**  .
- It forms a **tree-like topology** that is based on different optimizing process called **Objective Function (OF)** .
- It supports both **many-to-one** and **one-to-one** communication, as well as **multicast** and **anycast** .
- It uses **Destination Oriented Directed Acyclic Graphs (DODAGs)** as the routing structure, where each node has a **rank** that indicates its position in the graph  .
- It defines three types of control messages: **DODAG Information Object (DIO)**, **Destination Advertisement Object (DAO)**, and **DODAG Information Solicitation (DIS)**  .
- DIO messages are used to **advertise** the DODAG and its parameters, such as the OF, the rank, and the prefix  .
- DAO messages are used to **inform** the DODAG root or a parent node about the **downward routes** to the destination nodes  .
- DIS messages are used to **request** DIO messages from neighboring nodes  .
- RPL has several advantages, such as **scalability**, **adaptability**, **energy efficiency**, and **interoperability** with other IPv6 protocols  .
- RPL also has some challenges, such as **security**, **reliability**, **mobility**, and **performance**  .



# CORPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- CORPL stands for **C**ontrol **O**bjective **R**outing **P**rotocol for **L**ow power and Lossy Networks.
- It is a network layer protocol that is designed for IoT applications that require reliable and energy-efficient data delivery in constrained environments.
- It is based on the concept of **control objectives**, which are high-level goals that the network should achieve, such as minimizing delay, maximizing throughput, or balancing load.
- CORPL uses a distributed algorithm to compute optimal routes based on the control objectives and the network state, such as link quality, traffic load, and residual energy.
- CORPL is compatible with the IPv6 Routing Protocol for Low-Power and Lossy Networks (RPL), which is the standard routing protocol for IoT networks.
- CORPL can interoperate with RPL nodes and use RPL messages to exchange routing information.
- CORPL has the following advantages over RPL:
  - It can support multiple and dynamic control objectives, while RPL can only support one static objective.
  - It can adapt to network changes faster and more accurately, while RPL may suffer from routing loops, inconsistencies, and suboptimal paths.
  - It can achieve better performance in terms of packet delivery ratio, end-to-end delay, and energy consumption, while RPL may incur more overhead and waste more resources.
- CORPL has the following limitations and challenges:
  - It requires more computation and memory than RPL, which may be an issue for resource-constrained devices.
  - It may not be compatible with some existing RPL features, such as storing mode, non-storing mode, and multicast.
  - It may need to deal with security and privacy issues, such as authentication, authorization, and confidentiality of routing information.



# CARP

CARP stands for Channel-Aware Routing Protocol. It is a network layer protocol that is designed for underwater communication. It has lightweight packets so that it can be used for Internet of Things (IoT)   .

Some of the features of CARP are:

- It is a distributed routing protocol that does not require any centralized control or coordination   .
- It performs two different functionalities: network initialization and data forwarding  .
- It uses a channel-aware metric to select the best relay node for data transmission   .
- It keeps track of the data communication history to avoid loops and redundant transmissions  .
- It adapts to the dynamic changes in the underwater environment and network topology   .
- It reduces the end-to-end delay and energy consumption of the network   .

Some of the advantages of CARP are:

- It is suitable for IoT applications that require low overhead and high scalability    .
- It improves the network performance and reliability in terms of packet delivery ratio, throughput, and latency    .
- It is compatible with existing MAC layer protocols and does not need any modification   .

Some of the challenges of CARP are:

- It may not be able to handle high traffic load and congestion in the network .
- It may not be able to cope with the interference and noise in the underwater channel .
- It may not be able to provide security and privacy for the data transmission .



# Unit 4 - Transport & Session Layer Protocols

The transport layer and the session layer are two of the seven layers of the Open Systems Interconnection (OSI) model. They are responsible for providing reliable and efficient communication between applications and hosts on a network.

## Transport Layer

The transport layer is the fourth layer of the OSI model. It provides end-to-end data transfer services to the upper layers, such as the session, presentation, and application layers. The transport layer can be either connection-oriented or connectionless, depending on the type of protocol used.

- Connection-oriented protocols establish a logical connection between the source and destination hosts before sending any data. They also provide reliable data delivery, error detection and correction, flow control, and congestion control. An example of a connection-oriented protocol is the Transmission Control Protocol (TCP).
- Connectionless protocols do not require a logical connection between the source and destination hosts. They send data as independent packets, without any guarantee of delivery, order, or integrity. An example of a connectionless protocol is the User Datagram Protocol (UDP).

Some of the functions of the transport layer are:

- Multiplexing and demultiplexing: The transport layer can use port numbers to identify different applications or processes on the same host and deliver data to the correct destination.
- Segmentation and reassembly: The transport layer can divide a large message into smaller segments and add headers to each segment. The segments are then reassembled at the destination host by using sequence numbers and acknowledgment messages.
- End-to-end communication: The transport layer can provide end-to-end communication between applications on different hosts, regardless of the underlying network layer protocols or physical media.

Some of the protocols that operate at the transport layer are:

- Transmission Control Protocol (TCP): TCP is a connection-oriented, reliable, and full-duplex protocol that provides reliable data delivery, error detection and correction, flow control, and congestion control. TCP uses a three-way handshake to establish a connection, a sliding window mechanism to regulate the data flow, and a four-way handshake to terminate a connection.
- User Datagram Protocol (UDP): UDP is a connectionless, unreliable, and best-effort protocol that provides fast and efficient data transfer for applications that do not require reliability or order. UDP does not provide any error detection, correction, or flow control. UDP uses a simple header that contains the source and destination port numbers, the length, and the checksum of the data.
- Stream Control Transmission Protocol (SCTP): SCTP is a connection-oriented, reliable, and message-oriented protocol that provides multiple streams of data within a single connection. SCTP also provides features such as multihoming, path selection, and partial reliability. SCTP uses a four-way handshake to establish a connection, a selective acknowledgment mechanism to regulate the data flow, and a shutdown procedure to terminate a connection.
- Datagram Congestion Control Protocol (DCCP): DCCP is a connection-oriented, unreliable, and congestion-controlled protocol that provides efficient data transfer for applications that can tolerate some data loss, such as multimedia streaming or online gaming. DCCP also provides features such as congestion control, acknowledgment feedback, and security. DCCP uses a four-way handshake to establish a connection, a congestion control mechanism to regulate the data flow, and a close procedure to terminate a connection.

## Session Layer

The session layer is the fifth layer of the OSI model. It provides session management and synchronization services to the upper layers, such as the presentation and application layers. The session layer can establish, maintain, and terminate sessions between applications on different hosts. It can also coordinate the exchange of data and synchronize the communication between the applications.

Some of the functions of the session layer are:

- Session establishment: The session layer can initiate a session between two or more applications by using a session identifier, a session token, or a session key. The session layer can also negotiate the parameters and options for the session, such as the protocol, the encryption, or the compression methods.
- Session maintenance: The session layer can monitor and control the session by using checkpoints, timers, or heartbeat messages. The session layer can also handle errors, interruptions, or timeouts that may occur during the session.
- Session termination: The session layer can end a session gracefully by using a session close message or abruptly by using a session abort message. The session layer can also release the resources and data associated with the session.

Some of the protocols that operate at the session layer are:

- Session Initiation Protocol (SIP): SIP is a signaling protocol that is used to establish, maintain, and terminate multimedia sessions, such as voice, video, or instant messaging. SIP uses a



# Transport Layer for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The transport layer is the fourth layer of the OSI model and the TCP/IP model. It is responsible for end-to-end communication and data transfer between applications or devices over a network.
- The transport layer provides features such as reliability, congestion control, flow control, error detection and correction, and ordering of data packets.
- The transport layer protocols can be classified into two categories: connection-oriented and connectionless. Connection-oriented protocols establish a logical connection between the sender and the receiver before exchanging data, while connectionless protocols do not require a connection and send data as independent packets.
- The commonly used transport layer protocols in IoT are:

  - TCP (Transmission Control Protocol): A connection-oriented, reliable, and byte-stream oriented protocol that ensures the delivery of data in the same order and without errors. TCP is widely used for web applications, email, file transfer, and remote access. TCP uses a three-way handshake to establish a connection, a sliding window mechanism to control the flow and congestion of data, and acknowledgments and retransmissions to ensure reliability.
  - UDP (User Datagram Protocol): A connectionless, unreliable, and datagram oriented protocol that does not guarantee the delivery, order, or integrity of data. UDP is faster and more efficient than TCP, but it may lose or duplicate packets, or deliver them out of order. UDP is suitable for real-time applications, such as voice and video streaming, online gaming, and DNS queries. UDP does not use any handshaking, windowing, or acknowledgment mechanisms, and relies on the application layer to handle errors and reordering of data.
  - DCCP (Datagram Congestion Control Protocol): A connection-oriented, unreliable, and datagram oriented protocol that provides congestion control for UDP-like applications. DCCP is designed to support applications that need low latency and high throughput, such as multimedia streaming, telephony, and online games. DCCP uses a four-way handshake to establish a connection, a feedback mechanism to adjust the sending rate according to the network conditions, and a feature negotiation mechanism to allow the sender and the receiver to agree on the congestion control algorithm and other options.
  - SCTP (Stream Control Transmission Protocol): A connection-oriented, reliable, and message oriented protocol that supports multiple streams of data within a single connection. SCTP is designed to overcome some of the limitations of TCP, such as head-of-line blocking, lack of multihoming, and vulnerability to SYN flooding attacks. SCTP uses a four-way handshake to establish a connection, a selective acknowledgment mechanism to improve the performance over lossy networks, and a heartbeat mechanism to monitor the status of the connection and the network paths.
  - RSVP (Resource Reservation Protocol): A connectionless, signaling, and QoS oriented protocol that allows applications to request and reserve network resources for data transmission. RSVP is designed to support applications that have strict requirements on bandwidth, delay, jitter, and packet loss, such as video conferencing, voice over IP, and multimedia streaming. RSVP uses a PATH and RESV message exchange to establish a reservation state along the network path, and a TEAR and ERROR message exchange to modify or delete the reservation state.
  - DTLS (Datagram Transport Layer Security): A connection-oriented, secure, and datagram oriented protocol that provides encryption, authentication, and integrity for UDP-based applications. DTLS is based on TLS, but it adds some modifications to handle the unreliability and fragmentation of datagrams. DTLS uses a handshake protocol to negotiate the cryptographic parameters and exchange the keys, a record protocol to encrypt and authenticate the data, and a alert protocol to signal any errors or warnings.
  - TLS (Transport Layer Security): A connection-oriented, secure, and byte-stream oriented protocol that provides encryption, authentication, and integrity for TCP-based applications. TLS is the successor of SSL, and it is widely used for securing web traffic, email, instant messaging, and VPN. TLS uses a handshake protocol to negotiate the cryptographic parameters and exchange the keys, a record protocol to encrypt and authenticate the data, and a alert protocol to signal any errors or warnings.
  - RPL (Routing Protocol for Low-Power and Lossy Networks): A connectionless, routing, and IPv6 oriented protocol that provides efficient and scalable routing for IoT networks. RPL is designed to handle the challenges of low-power and lossy networks, such as limited resources, dynamic topology, and high packet loss. RPL uses a Destination Oriented Directed Acyclic Graph (DODAG) to organize the network



# TCP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- TCP stands for Transmission Control Protocol .
- It is a transport layer protocol that facilitates the transmission of packets from source to destination .
- It is a connection-oriented protocol that means it establishes the connection prior to the communication that occurs between the computing devices in a network .
- TCP is a reliable protocol as it follows the flow and error control mechanism. It also supports the acknowledgment mechanism, which checks the state and sound arrival of the data .
- TCP is used by application protocols like HTTP and FTP that require reliable and ordered delivery of data .
- TCP has three main steps: establish connection, send packets of data, and close the connection.
  - Establish connection: When two computers want to send data to each other over TCP, they first need to establish a connection using a three-way handshake . The sender initiates the connection by sending a SYN (synchronize) packet to the receiver. The receiver responds with a SYN-ACK (synchronize-acknowledge) packet to acknowledge the request. The sender then sends an ACK (acknowledge) packet to confirm the connection .
  - Send packets of data: When a packet of data is sent over TCP, the recipient must always acknowledge what they received using an ACK packet. If the sender does not receive an ACK packet within a certain time, it assumes that the packet was lost or corrupted and resends it. This ensures that no data is lost or duplicated in the transmission .
  - Close the connection: When the data transmission is complete, the sender and the receiver need to close the connection using a four-way handshake . The sender sends a FIN (finish) packet to indicate that it has no more data to send. The receiver responds with an ACK packet to acknowledge the FIN packet. The receiver then sends its own FIN packet to indicate that it has no more data to receive. The sender responds with an ACK packet to acknowledge the FIN packet. The connection is then terminated .
- TCP has some advantages and disadvantages over other transport layer protocols such as UDP (User Datagram Protocol).
  - Advantages: TCP provides reliable and ordered delivery of data, which is essential for applications that need to ensure the integrity and completeness of the data. TCP also handles congestion control and flow control, which prevent the network from being overloaded or overwhelmed by too much data .
  - Disadvantages: TCP has an additional overhead due to the connection establishment and termination, the acknowledgment mechanism, and the retransmission of lost packets. TCP also has a higher latency and lower throughput than UDP, which can affect the performance of real-time applications such as video streaming or gaming .



# MPTCP

- MPTCP stands for Multipath TCP, which is an extension to the original TCP protocol (single-path)  .
- MPTCP enables a transport connection to operate across multiple paths simultaneously, and brings network connection redundancy to user endpoint devices  .
- MPTCP aims at allowing a TCP connection to use multiple paths to maximize throughput and increase redundancy .
- MPTCP is a set of extensions to regular TCP that enables a single data flow to be separated and carried across multiple connections .
- MPTCP is an ongoing effort of the Internet Engineering Task Force's (IETF) Multipath TCP working group .
- MPTCP has several advantages over single-path TCP, such as:
  - Improved resilience to path failures and network congestion  .
  - Increased bandwidth utilization and efficiency  .
  - Seamless mobility and handover between different network interfaces  .
  - Reduced need for application-layer adaptations  .
- MPTCP has some challenges and limitations, such as:
  - Compatibility with existing network devices and middleboxes  .
  - Security and privacy issues related to exposing multiple addresses  .
  - Congestion control and fairness issues with other flows  .
  - Implementation and deployment complexity  .
- MPTCP is supported by Red Hat Enterprise Linux 8.3 and later versions .
- MPTCP can be configured and managed using the mptcpd daemon and the mptcpctl command-line tool .
- MPTCP can be enabled or disabled on a per-socket basis using the IP_MPTCP socket option .
- MPTCP can be tested using tools such as iperf3, curl, wget, and nc .

: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/getting-started-with-multipath-tcp_configuring-and-managing-networking
: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/getting-started-with-multipath-tcp_configuring-and-managing-networking
: https://en.wikipedia.org/wiki/Multipath_TCP
: https://www.cisco.com/c/en/us/support/docs/ip/transmission-control-protocol-tcp/116519-technote-mptcp-00.html
: https://developers.redhat.com/blog/2020/08/19/multipath-tcp-on-red-hat-enterprise-linux-8-3-from-0-to-1-subflows



# UDP

- UDP stands for User Datagram Protocol. It is one of the core communication protocols of the Internet protocol suite used to send messages (transported as datagrams in packets) to other hosts on an Internet Protocol (IP) network .
- UDP is a simple message-oriented transport layer protocol that is documented in RFC 768. It provides integrity verification (via checksum) of the header and payload, but it does not provide any guarantees to the upper layer protocol for message delivery and the UDP layer retains no state of UDP messages once sent .
- UDP is a lightweight and fast protocol that works on top of IP. It does not require a connection establishment or termination, and it does not perform any congestion control or flow control. UDP is suitable for applications that need low-latency and loss-tolerating connections, such as real-time audio and video streaming, online gaming, and DNS queries .
- UDP has a simple header format that consists of four fields: source port, destination port, length, and checksum. The source and destination ports identify the endpoints of the communication, the length specifies the size of the UDP datagram in bytes, and the checksum is used to detect errors in the header and payload .
- UDP does not provide any mechanisms to handle the problems that may arise with packets, such as loss, duplication, reordering, or delay. These problems are left to the upper layer protocols or applications to deal with. Some examples of upper layer protocols that use UDP are RTP (Real-time Transport Protocol), RTCP (Real-time Transport Control Protocol), and DHCP (Dynamic Host Configuration Protocol) .



# DCCP

- DCCP stands for **Datagram Congestion Control Protocol** .
- It is a **message-oriented** transport layer protocol that provides **bidirectional unicast** connections of **congestion-controlled unreliable datagrams** .
- It is suitable for applications that transfer fairly large amounts of data, but can benefit from control over the tradeoff between **timeliness and reliability**.
- It implements reliable connection setup, teardown, Explicit Congestion Notification (ECN), congestion control, and feature negotiation .
- It supports different types of congestion control algorithms, such as TCP-like, TCP-friendly, and TFRC .
- It uses a packet header format that is similar to TCP, but with some differences, such as a 48-bit sequence number, a 24-bit acknowledgment number, and a 16-bit service code .
- It uses two types of packets: **DCCP-Request** and **DCCP-Response** for connection initiation, and **DCCP-Data** and **DCCP-Ack** for data transfer and acknowledgment .
- It uses a four-way handshake to establish a connection, and a three-way handshake to close a connection .
- It uses a feature negotiation mechanism to allow the endpoints to agree on the parameters and options of the connection, such as the congestion control algorithm, the ECN capability, and the checksum coverage .
- It uses a state machine to manage the connection states, such as **CLOSED**, **LISTEN**, **REQUEST**, **RESPOND**, **PARTOPEN**, **OPEN**, **CLOSEREQ**, and **TIMEWAIT** .
- It uses a congestion control identifier (CCID) to specify the congestion control algorithm for each direction of the connection .
- It uses a window counter (W) to indicate the number of packets sent or received in each congestion window .
- It uses a reset code (R) to indicate the reason for resetting the connection, such as **Aborted**, **No Connection**, **Packet Error**, **Option Error**, **Mandatory Error**, **Connection Refused**, **Bad Service Code**, **Too Busy**, **Bad Init Cookie**, **Aggression Penalty**, and **Feature Negotiation Failed** .
- It uses a generic header option format that consists of a type field, a length field, and a data field .
- It uses a checksum to detect errors in the packet header and payload .
- It uses a partial checksum coverage option to allow the endpoints to specify the parts of the packet that are covered by the checksum .
- It uses a change option and a confirm option to negotiate the features of the connection .
- It uses a data dropped option to inform the receiver about the packets that are dropped by the sender due to congestion .
- It uses a timestamp option and a timestamp echo option to measure the round-trip time of the connection .
- It uses a sequence window option and an acknowledgment number window option to specify the size of the sequence number space and the acknowledgment number space .
- It uses a padding option to fill the unused space in the packet header .
- It uses a mandatory option to indicate that the option must be understood and processed by the receiver .
- It uses a slow receiver option to indicate that the receiver is experiencing a high packet loss rate or a low processing rate .
- It uses a service code option to specify the service class of the connection, such as **Best Effort**, **Priority**, **Expedited Forwarding**, or **Assured Forwarding** .
- It uses a init cookie option and a cookie option to prevent connection flooding attacks .
- It uses a send acknowledgment option and a acknowledgment vector option to acknowledge the received packets .
- It



# SCTP

SCTP stands for **Stream Control Transmission Protocol**. It is a **transport layer** protocol in the Internet protocol suite that provides reliable and in-sequence data transmission over a connectionless packet network such as IP .

Some of the features and characteristics of SCTP are:

- It supports **multiple streams** of data within a single connection, which allows different types of data to be sent simultaneously without blocking or interleaving .
- It uses **chunks** to encapsulate messages and control information, each with a chunk header that identifies the type, length, and flags of the chunk. A chunk can be either a **data chunk** that contains user data, or a **control chunk** that contains protocol commands or responses.
- It can **fragment** a large message into multiple data chunks, or **bundle** multiple chunks into a single SCTP packet, depending on the network conditions and the maximum transmission unit (MTU) of the underlying network .
- It provides **reliable** data transmission, which means that it ensures that all data chunks are acknowledged by the receiver, and retransmitted if lost or corrupted .
- It provides **ordered** and **unordered** delivery modes, which means that the sender can specify whether the data chunks should be delivered to the receiver in the same order as they were sent, or in any order as long as they belong to the same stream .
- It supports **multihoming**, which means that each endpoint of a connection can have multiple IP addresses, and the protocol can switch between them in case of network failure or congestion .
- It supports **congestion control** and **flow control**, which means that it adjusts the transmission rate and window size according to the network conditions and the receiver's buffer capacity .
- It supports **graceful shutdown**, which means that it allows the endpoints to close the connection in an orderly manner, by exchanging termination chunks and releasing the resources .
- It supports **partial reliability**, which means that it allows the sender to specify a lifetime for each data chunk, and discard the chunk if it is not delivered within the specified time .
- It supports **authentication**, which means that it allows the endpoints to exchange a shared secret key and use it to verify the integrity and origin of the chunks .

SCTP was originally designed to transport **Public Switched Telephone Network (PSTN) signaling messages** over IP networks, but it is capable of broader applications, such as web browsing, streaming media, file transfer, and voice over IP (VoIP)  .



# Session Layer for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The session layer is the fifth layer of the OSI model that manages the connection between two endpoints of a network by controlling data between sender and receiver  .
- The session layer protocols are responsible for actual transmission of data in IoT ecosystem. That’s why these session layer protocols are called as IoT Messaging Protocols or sometimes referred as IoT Data Protocols .
- The session layer protocols review standards and protocols for message passing. Different standardization organizations introduce the IoT session layer protocols. There are different types of session layer protocol available with different functionality and range.
- Some of the common session layer protocols in IoT are:
  - MQTT (Message Queue Telemetry Transport): A lightweight publish-subscribe protocol that works on TCP/IP and supports QoS levels  .
  - CoAP (Constrained Application Protocol): A web transfer protocol that works on UDP and supports RESTful web services  .
  - AMQP (Advanced Message Queuing Protocol): A binary protocol that works on TCP/IP and supports reliable and secure message delivery  .
  - XMPP (Extensible Messaging and Presence Protocol): An XML-based protocol that works on TCP/IP and supports instant messaging and presence information  .
- The session layer also provides some functions such as:
  - Dialog control: It allows systems to communicate in either half-duplex mode or full-duplex mode.
  - Token management: It prevents two users to simultaneously access or transmit data over the network.
  - Synchronization: It allows the addition of checkpoints into a data stream so that the data can be re-synchronized in case of failure or loss.



# HTTP

HTTP stands for **Hypertext Transfer Protocol**. It is an **application layer protocol** in the Internet protocol suite model for distributed, collaborative, hypermedia information systems. It is used for transmitting **hypermedia documents**, such as HTML, between web browsers and web servers.

Some key points about HTTP are:

- HTTP is a **stateless** protocol, which means that each request and response pair is independent and does not remember any previous interaction.
- HTTP uses **TCP** as the underlying and reliable transport layer protocol. TCP establishes a connection between the client and the server, and ensures that the data is delivered in order and without errors.
- HTTP follows a **request-response** model, where the client sends a request message to the server, and the server sends back a response message to the client. The request and response messages have a similar structure, consisting of a **start-line**, **headers**, and an optional **body**.
- HTTP defines a set of **methods** that indicate the action to be performed on the requested resource. Some common methods are **GET**, **POST**, **PUT**, **DELETE**, **HEAD**, and **OPTIONS**.
- HTTP defines a set of **status codes** that indicate the result of the request. Some common status codes are **200 OK**, **404 Not Found**, **301 Moved Permanently**, **500 Internal Server Error**, and **403 Forbidden**.
- HTTP supports **multiple versions**, such as HTTP/1.0, HTTP/1.1, and HTTP/2. Each version introduces new features and improvements, such as persistent connections, pipelining, compression, multiplexing, and encryption.
- HTTP can be extended by adding new **headers**, **methods**, **status codes**, and **media types**. For example, HTTP/1.1 introduced the **Host** header, which allows multiple domains to share the same IP address. HTTP/2 introduced the **:method**, **:path**, and **:authority** pseudo-headers, which replace the start-line of the request message.
- HTTP can be used for other purposes than web browsing, such as **APIs**, **web services**, **webhooks**, and **IoT**. For example, HTTP can be used to send and receive data from sensors, actuators, and other devices connected to the Internet.
- HTTP can be combined with other protocols, such as **HTTPS**, **WebSocket**, and **HTTP/3**. HTTPS is a secure version of HTTP that uses **TLS** to encrypt the communication between the client and the server. WebSocket is a protocol that enables **bidirectional** and **real-time** communication between the client and the server. HTTP/3 is a new version of HTTP that uses **QUIC** as the transport layer protocol, which is faster and more reliable than TCP.



# CoAP

CoAP is an acronym for **Constrained Application Protocol**. It is an application-layer protocol that is intended for use in resource-constrained Internet devices, such as wireless sensor network nodes. CoAP is designed to easily translate to HTTP for simplified integration with the web, while also meeting specialized requirements such as multicast support, very low overhead, and simplicity.

Some of the main features of CoAP are:

- It is based on the RESTful architecture, which means that it supports the standard methods of GET, POST, PUT, and DELETE for resource manipulation.
- It uses UDP as the underlying transport protocol, which makes it suitable for unreliable and low-power networks.
- It employs a simple binary header format that minimizes the message size and the parsing complexity.
- It supports asynchronous message exchanges through a built-in reliability mechanism that allows for retransmission and acknowledgement of messages.
- It enables resource discovery through a well-known URI (/ .well-known/core) that returns a list of available resources and their attributes.
- It supports content negotiation through the use of media types and CoAP-specific options.
- It allows for observation of resources through a subscribe/notify mechanism that enables clients to receive updates from servers when the state of a resource changes.
- It supports caching and proxying of resources through the use of ETags and Max-Age options.
- It provides security through the use of Datagram Transport Layer Security (DTLS), which offers encryption, authentication, and replay protection.

CoAP is one of the most widely used IoT protocols, as it enables efficient and interoperable communication between constrained devices and the web. CoAP can be used for various IoT applications, such as smart home, smart city, smart grid, industrial automation, and environmental monitoring. CoAP is also compatible with other IoT protocols, such as MQTT and LwM2M, which can be used for different purposes and scenarios. CoAP is an open and evolving standard that is defined in RFC 7252 and other related documents.



# XMPP

- XMPP stands for **Extensible Messaging and Presence Protocol** .
- It is an **open communication protocol** designed for **instant messaging (IM)**, **presence information**, and **contact list maintenance** .
- It is based on **XML (Extensible Markup Language)**, which enables the **near-real-time exchange of structured data** between two or more network entities.
- It is a **decentralized protocol**, meaning that anyone can run their own XMPP server and communicate with other servers.
- It is a **living standard**, meaning that engineers actively extend and improve it.
- It supports various features, such as:
  - **End-to-end encryption** for secure communication.
  - **Multi-user chat** for group conversations.
  - **PubSub** for publish-subscribe messaging.
  - **Jingle** for voice and video calls.
  - **IoT** for connecting devices and sensors.
  - **WebRTC** for real-time communication in web browsers.
  - **Online Gaming** for multiplayer games.
  - **Realtime Social** for social networking.
- It is used by many applications and services, such as:
  - **WhatsApp** for instant messaging.
  - **Google Talk** for voice and video calls.
  - **Facebook Messenger** for social networking.
  - **Signal** for secure communication.
  - **Cisco Jabber** for enterprise collaboration.
  - **Mozilla Thunderbird** for email and chat.
  - **Ejabberd** for scalable XMPP server.
  - **Prosody** for lightweight XMPP server.



# AMQP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- AMQP stands for **Advanced Message Queuing Protocol**.
- It is an **open standard**, **binary** application layer protocol designed for **message-oriented middleware**.
- It enables **encrypted** and **interoperable** messaging between organizations and applications.
- It is used in **client/server messaging** and in **IoT device management**.
- It has **reliable**, **secure**, **interoperable**, **open**, and **standard** properties, along with its **low overhead** characteristics, making it a good solution for IoT applications.
- It supports **publish/subscribe**, **point-to-point**, and **request/response** messaging patterns.
- It standardizes messaging using **Producers**, **Brokers** and **Consumers**.
- Producers send messages to a **broker** (a server that routes messages to the appropriate destinations).
- Consumers receive messages from a broker, either by **subscribing** to a **topic** (a logical name for a group of messages) or by **polling** a **queue** (a buffer that stores messages until they are consumed or expire).
- AMQP defines a **wire-level protocol**, which means that the messages are **binary** and can be efficiently parsed by any platform.
- AMQP also defines a **semantic model**, which specifies the **meaning** and **behavior** of the messages and the entities involved in the communication.
- AMQP uses **TCP** as the underlying transport protocol, and optionally **TLS** for encryption.
- AMQP can also use **WebSockets** as a transport layer, which allows it to work over **HTTP**.
- To connect to an IoT hub by using AMQP, a client can use the **claims-based security (CBS)** or **Simple Authentication and Security Layer (SASL)** authentication.
- The client needs to provide the **IoT hub hostname**, the **key name**, and the **key value** for authentication.
- The client can then create a **sender link** or a **receiver link** to send or receive messages to or from the IoT hub.
- AMQP supports **device-to-cloud** and **cloud-to-device** communications, as well as **device twins**, **direct methods**, and **file upload** features of IoT Hub.



# MQTT

MQTT is a lightweight messaging protocol for the Internet of Things (IoT). It is designed as an extremely lightweight publish/subscribe messaging transport that is ideal for connecting remote devices with a small code footprint and minimal network bandwidth.

Some of the features and benefits of MQTT are:

- It allows for messaging between device to cloud and cloud to device. This makes for easy broadcasting messages to groups of things.
- It can scale to connect with millions of IoT devices.
- It provides reliable message delivery with different levels of quality of service (QoS).
- It employs a publish/subscribe communication pattern, which decouples the message sender from the receiver.
- It is an open standard that is widely supported by many platforms and languages.

Some of the concepts and components of MQTT are:

- Broker: A server that receives and distributes messages from publishers to subscribers.
- Client: A device or application that connects to the broker and can either publish or subscribe to messages.
- Topic: A hierarchical string that identifies the subject or category of a message.
- Payload: The actual data or content of a message.
- QoS: A parameter that specifies the delivery guarantee of a message. There are three levels of QoS: 0 (at most once), 1 (at least once), and 2 (exactly once).
- Retain: A flag that indicates whether the broker should store the last message published on a topic and send it to new subscribers.
- Will: A message that a client can specify to be published by the broker in case the client disconnects unexpectedly.

The basic steps of MQTT communication are:

- A client connects to a broker using TCP/IP or a secure variant such as TLS.
- A client can publish a message to a topic by sending it to the broker with a QoS level.
- A client can subscribe to one or more topics by sending a request to the broker.
- The broker forwards the messages published on the topics to the subscribed clients according to the QoS level.
- A client can disconnect from the broker gracefully or ungracefully.



# Unit 5 - Service Layer Protocols & Security

## Service Layer
- The service layer is the layer that provides **capability servers** owned by a telecommunication network service provider, accessed through open and secure **Application Programming Interfaces (APIs)** by application layer servers owned by third-party content providers.
- The service layer also provides an interface to core networks at a lower **resource layer**.
- The service layer can be seen as a bridge between the **application layer** and the **transport layer** in the network architecture.

## Service Layer Protocols
- Service layer protocols are protocols that operate at the service layer and provide various **security services** to the application layer protocols.
- Some examples of service layer protocols are:
  - **SSL (Secure Socket Layer)**: A protocol that provides authentication and confidentiality for data exchanged between a web browser and a web server.
  - **TLS (Transport Layer Security)**: A protocol that is an improved version of SSL and provides more security features and flexibility for data exchanged between various applications.
  - **AT-TLS (Application Transparent Transport Layer Security)**: A protocol that provides transparent security for any TCP-based application without requiring any changes to the application code.
  - **Kerberos**: A protocol that provides authentication, authorization and encryption for distributed systems using secret-key cryptography.
  - **OSPF (Open Shortest Path First)**: A protocol that provides authentication for routing information exchanged between routers using digital signatures or passwords.
  - **SNMPv3 (Simple Network Management Protocol version 3)**: A protocol that provides authentication, encryption and access control for network management information exchanged between agents and managers.

## Security Services
- Security services are services that provide protection for data and communication in a network.
- Some examples of security services are:
  - **Peer entity authentication**: A service that verifies the identity of the communicating parties.
  - **Data origin authentication**: A service that verifies the source of the data.
  - **Access control service**: A service that restricts the access to the data or resources based on the identity or role of the requester.
  - **Confidentiality service**: A service that prevents unauthorized disclosure of the data.
  - **Data integrity service**: A service that prevents unauthorized modification of the data.
  - **Non-repudiation service**: A service that prevents the denial of involvement in the communication or transaction.
  - **Availability service**: A service that ensures the accessibility and usability of the data or resources.



# Service Layer for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

The service layer is the layer that provides the interface between the application layer and the network layer in the IoT architecture. The service layer is responsible for:

- Service discovery or service management: This is the process of finding and registering other devices, services and resources over the internet or the cloud. The service layer enables the IoT devices to communicate with each other and access the required services and resources.
- Data processing and analysis: This is the process of transforming, aggregating, filtering, and extracting meaningful information from the raw data collected by the IoT devices. The service layer can perform data processing and analysis at the edge, the fog, or the cloud, depending on the latency, bandwidth, and security requirements.
- Communication protocols: These are the rules and standards that govern how the IoT devices exchange data and messages with each other and with the cloud. The communication protocols can be classified into two categories: network protocols and data protocols. Network protocols provide methods of connecting IoT devices with other devices or the internet, while data protocols provide methods of information exchange and representation.

Some of the common service layer protocols and standards in IoT are:

- AMQP: Advanced Message Queuing Protocol is an open standard protocol used for message-oriented middleware. It enables reliable and secure communication between applications and devices across different platforms and networks.
- CoAP: Constrained Application Protocol is a lightweight protocol designed for resource-constrained IoT devices. It provides a RESTful web service model for device-to-device or device-to-cloud communication. It supports multicast, asynchronous, and low-power communication.
- MQTT: Message Queuing Telemetry Transport is a publish-subscribe protocol that enables efficient and low-overhead communication between IoT devices and the cloud. It is suitable for unreliable and low-bandwidth networks. It supports quality of service levels and last will and testament messages.
- XMPP: Extensible Messaging and Presence Protocol is an open standard protocol based on XML. It enables real-time and bidirectional communication between IoT devices and the cloud. It supports presence, chat, and pubsub features.
- DDS: Data Distribution Service is a standard for data-centric publish-subscribe communication. It enables high-performance and scalable communication between IoT devices and the cloud. It supports quality of service policies, discovery, and security features.

The service layer also provides security mechanisms to protect the IoT devices, data, and services from unauthorized access, modification, or disruption. Some of the security challenges and solutions in the service layer are:

- Authentication and authorization: This is the process of verifying the identity and access rights of the IoT devices and users. The service layer can use various methods such as passwords, tokens, certificates, biometrics, or blockchain to authenticate and authorize the IoT devices and users.
- Encryption and decryption: This is the process of converting the data into an unreadable form and back to a readable form using a secret key. The service layer can use various algorithms such as AES, RSA, ECC, or quantum cryptography to encrypt and decrypt the data exchanged between the IoT devices and the cloud.
- Integrity and non-repudiation: This is the process of ensuring that the data is not tampered with or altered during transmission or storage. The service layer can use various techniques such as checksums, hashes, digital signatures, or blockchain to verify the integrity and non-repudiation of the data.
- Privacy and anonymity: This is the process of protecting the personal and sensitive information of the IoT devices and users from unauthorized disclosure or tracking. The service layer can use various methods such as anonymization, pseudonymization, differential privacy, or homomorphic encryption to preserve the privacy and anonymity of the data.



# oneM2M

- oneM2M is a global partnership project founded in 2012 and constituted by 8 of the world's leading ICT standards development organizations.
- oneM2M aims to develop a common service layer that can be readily embedded within various hardware and software, and relied upon to connect the myriad of devices in the field with M2M application servers worldwide.
- oneM2M is similar to a distributed operating system for the Internet of Things. It takes the form of a middleware service layer consisting of a suite of common service functions (CSFs).
- oneM2M common service layer contains set of common service functions which are required by various IoT verticals. Common Service Entity (CSE) is the main component of oneM2M common service layer which provides the common service functions.
- oneM2M defines three types of CSEs: Infrastructure Node (IN-CSE), Middle Node (MN-CSE) and Application Entity (AE). IN-CSE is the root of the oneM2M system and provides the core functionalities. MN-CSE is an intermediate node that can act as a gateway or a proxy. AE is an application that uses the oneM2M services.
- oneM2M uses a resource-oriented architecture (ROA) based on RESTful principles. Resources are the basic units of information that can be created, retrieved, updated and deleted through the oneM2M interfaces. Resources are organized in a hierarchical tree structure and have unique identifiers.
- oneM2M defines four types of interfaces: Mca, Mcc, Mcn and Mcc'. Mca is the interface between an AE and a CSE. Mcc is the interface between two CSEs. Mcn is the interface between a CSE and a network service entity (NSE). Mcc' is the interface between a CSE and a non-oneM2M system.
- oneM2M supports various protocols for communication, such as HTTP, CoAP, MQTT and WebSocket. oneM2M also defines a protocol-independent binding mechanism called oneM2M Base Protocol (oB) that allows the mapping of oneM2M messages to different protocols.
- oneM2M provides various common service functions, such as registration, discovery, data management, subscription and notification, group management, access control, security, device management and semantic interoperability.
- oneM2M has released five versions of its technical specifications so far: Release 1 (2015), Release 2 (2016), Release 3 (2018), Release 4 (2019) and Release 5 (2021). Each release adds new features and enhancements to the previous one.



# ETSI M2M

- ETSI M2M stands for European Telecommunications Standards Institute Machine-to-Machine.
- It is a standardization body that develops standards for IoT and M2M technologies.
- It is one of the founding partners of oneM2M, the global standards initiative for IoT and M2M interoperability.
- ETSI M2M defines a high-level architecture for M2M systems, consisting of three main layers: Application Layer, Service Layer, and Network Layer.
- The Service Layer is the core of the ETSI M2M architecture, as it provides common functions and interfaces for M2M applications and devices.
- The Service Layer consists of two main components: Service Capability Layer (SCL) and M2M Area Network (MAN).
- The SCL is a middleware that enables communication and data exchange between M2M applications and devices, regardless of the underlying network technologies.
- The SCL provides a set of common services, such as registration, discovery, security, data management, subscription, notification, and group management.
- The SCL also defines a resource-oriented architecture, based on RESTful principles, where each M2M entity is represented by a resource with a unique identifier and a set of attributes and operations.
- The MAN is a local network of connected devices, sensors, and actuators, also called objects, that communicate with the SCL through a gateway or a proxy.
- The MAN can use various network technologies, such as ZigBee, Bluetooth, Wi-Fi, or cellular, depending on the application requirements and the device capabilities.
- The ETSI M2M architecture also defines security mechanisms for M2M systems, such as authentication, authorization, encryption, and key management.
- The ETSI M2M architecture supports interworking with other standards and protocols, such as CoAP, MQTT, OMA LWM2M, and Semantic Web technologies, through the use of ontologies and mappings.



# OMA for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- OMA stands for Open Mobile Alliance, an organization that develops open standards for the mobile and wireless industry.
- OMA Lightweight M2M (LwM2M) is a protocol from OMA for machine to machine (M2M) or Internet of things (IoT) device management and service enablement.
- LwM2M defines the application layer communication protocol between an LwM2M Server and an LwM2M Client, which is located in an IoT device.
- LwM2M is based on the Constrained Application Protocol (CoAP), which is a RESTful protocol that uses UDP as the transport layer and supports various data formats such as JSON, CBOR, and TLV.
- LwM2M provides four main features for IoT devices:
  - **Bootstrap**: The process of provisioning the device with the necessary information to register and communicate with the LwM2M Server.
  - **Register**: The process of registering the device with the LwM2M Server and providing information about its capabilities and resources.
  - **Manage**: The process of performing device management operations such as configuration, firmware update, reporting, and remote control.
  - **Report**: The process of sending data or notifications from the device to the LwM2M Server or vice versa.
- LwM2M defines a set of standard objects and resources that represent common functionalities and data models for IoT devices, such as device information, connectivity monitoring, location, temperature, humidity, etc.
- LwM2M also allows the definition of custom objects and resources for specific use cases and applications.
- LwM2M supports various security modes and mechanisms, such as pre-shared keys, raw public keys, certificates, and DTLS .
- LwM2M aims to be a simple, low-cost, and efficient protocol for IoT device management and service enablement, especially for constrained devices that have limited memory, power, and bandwidth.
- LwM2M is one of the protocols that can be used in the service layer of the IoT architecture, along with other protocols such as HTTP, MQTT, XMPP, WebSockets, etc.
- LwM2M can be integrated with other IoT platforms and technologies, such as 5G, edge computing, cloud computing, etc.



# BBF for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

## Service Layer Protocols
- Service layer protocols are the protocols that enable the communication and interaction among applications and services running on different IoT devices and on cloud/edge infrastructures.
- Service layer protocols are typically based on the application layer of the TCP/IP model, but they may also operate on other layers, such as the transport or the network layer.
- Some of the common service layer protocols in IoT are:
  - Constrained Application Protocol (CoAP): A lightweight protocol that is HTTP-friendly and uses two basic message types: request and response. It supports confirmable and non-confirmable messages, as well as multicast and observe options. It is designed for constrained devices and networks, and uses UDP as the transport protocol.
  - Message Queuing Telemetry Transport (MQTT): A publish-subscribe protocol that allows devices to publish messages to a broker, which then delivers them to the subscribers. It is suitable for low-power and low-bandwidth devices, and uses TCP as the transport protocol. It supports three levels of quality of service (QoS): at most once, at least once, and exactly once.
  - Advanced Message Queuing Protocol (AMQP): A binary protocol that supports both publish-subscribe and point-to-point communication models. It is designed for high-performance and reliable messaging, and uses TCP as the transport protocol. It supports transactions, acknowledgments, and security features.
  - HyperText Transfer Protocol (HTTP): A widely used protocol that supports request-response and RESTful communication models. It is based on the client-server architecture, and uses TCP as the transport protocol. It supports various methods, such as GET, POST, PUT, and DELETE, and various formats, such as XML, JSON, and HTML.
  - Extensible Messaging and Presence Protocol (XMPP): A protocol that supports instant messaging and presence information. It is based on the XML format, and uses TCP as the transport protocol. It supports various features, such as authentication, encryption, federation, and extensions.

## Security in IoT
- Security in IoT is the protection of the confidentiality, integrity, and availability of the data and devices involved in the IoT system.
- Security in IoT is challenging due to the heterogeneity, scalability, and resource constraints of the IoT devices and networks, as well as the complexity and diversity of the IoT applications and services.
- Security in IoT can be addressed at different layers of the IoT architecture, such as the device layer, the network layer, the service layer, and the application layer.
- Some of the security threats and attacks that can affect the IoT system are:
  - Eavesdropping: The interception and analysis of the data transmitted over the network by an unauthorized party.
  - Replay: The retransmission of a previously captured message by an attacker to impersonate a legitimate sender or receiver.
  - Modification: The alteration of the data or the message header by an attacker to change the content or the destination of the message.
  - Spoofing: The creation and transmission of a fake message by an attacker to impersonate a legitimate sender or receiver.
  - Denial-of-service (DoS): The prevention of the normal functioning of the network or the device by an attacker by flooding them with malicious traffic or requests.
  - Distributed denial-of-service (DDoS): The prevention of the normal functioning of the network or the device by an attacker by coordinating multiple compromised devices to flood them with malicious traffic or requests.
  - Malware: The malicious software that can infect the device or the network and perform harmful actions, such as stealing data, deleting files, or executing commands.
  - Man-in-the-middle (MITM): The interception and modification of the data transmitted between two parties by an attacker who positions himself in the middle of the communication channel.
  - Sybil: The creation and use of multiple fake identities by an attacker to disrupt the network or the service, such as by spreading false information, voting multiple times, or colluding with other attackers.
  - Wormhole: The creation and use of a tunnel between two distant points in the network by an attacker to relay the messages and create a false sense of proximity, such as by attracting traffic, disrupting routing, or launching other attacks.
- Some of the security solutions and mechanisms that can be applied to the IoT system are:
  - Encryption: The transformation of the data into an unreadable form by using a



# Security in IoT Protocols

- Security in IoT protocols is the process of ensuring the confidentiality, integrity, and availability of data and devices in an IoT network.
- Security in IoT protocols is vital as IoT involves pervasive data collection and dissemination, and can affect various critical sectors such as economy, health, and national security .
- Security in IoT protocols faces various challenges such as resource constraints, heterogeneity, scalability, mobility, and privacy .
- Security in IoT protocols can be implemented at different layers of the IoT architecture, such as the perception layer, the network layer, the middleware layer, and the application layer .
- Security in IoT protocols can be achieved by using various mechanisms such as encryption, authentication, authorization, access control, trust management, intrusion detection, and anomaly detection  .
- Security in IoT protocols can be enhanced by using standard and interoperable protocols that are designed for IoT scenarios, such as MQTT, CoAP, DTLS, LWM2M, and IPSec  .
- Security in IoT protocols can be evaluated by using various metrics such as security level, performance, overhead, scalability, and usability .
- Security in IoT protocols can be improved by following best practices such as updating firmware and software, using strong passwords and encryption keys, enabling firewall and antivirus, and monitoring network traffic  .



# MAC 802.15.4

- MAC 802.15.4 is a standard for low-rate wireless personal area networks (LR-WPANs) that defines the physical layer (PHY) and medium access control (MAC) sublayer specifications  .
- MAC 802.15.4 supports low-data-rate wireless connectivity with fixed, portable, and moving devices with no battery or very limited battery consumption requirements .
- MAC 802.15.4 provides the basis of other higher-layer standards, such as ZigBee, WirelessHart, 6LoWPAN and MiWi.
- MAC 802.15.4 supports multiple PHY options, such as frequency-hopping spread spectrum (FHSS), direct-sequence spread spectrum (DSSS), orthogonal frequency-division multiplexing (OFDM), and high-rate pulse ultra-wideband (HRP UWB) .
- MAC 802.15.4 supports two types of devices: full-function devices (FFDs) and reduced-function devices (RFDs). FFDs can operate as coordinators or ordinary devices, while RFDs can only operate as ordinary devices .
- MAC 802.15.4 supports two types of topologies: star and peer-to-peer. In a star topology, a single FFD acts as a central coordinator and communicates with other devices. In a peer-to-peer topology, any FFD can act as a coordinator and form a cluster with other devices .
- MAC 802.15.4 supports two types of MAC operations: beacon-enabled and non-beacon-enabled. In a beacon-enabled mode, the coordinator periodically broadcasts beacons to synchronize the devices and define the superframe structure. In a non-beacon-enabled mode, the devices use a carrier sense multiple access with collision avoidance (CSMA/CA) mechanism to access the channel .
- MAC 802.15.4 supports various MAC services, such as data transfer, association and disassociation, device discovery, channel access, security, and network management .
- MAC 802.15.4 supports various MAC features, such as guaranteed time slots (GTSs), frame acknowledgement, frame retransmission, frame filtering, frame pending, and frame versioning .
- MAC 802.15.4 supports various MAC security features, such as encryption, authentication, key management, and replay protection .



# 6LoWPAN

- 6LoWPAN stands for IPv6 over Low-power Wireless Personal Area Networks.
- It is an open standard defined by the Internet Engineering Task Force (IETF) that enables low-power devices with limited processing capabilities to participate in the Internet of Things (IoT) by using IPv6 over IEEE 802.15.4 based networks .
- 6LoWPAN defines mechanisms for:
  - Encapsulation: how to fragment and reassemble IPv6 datagrams over the IEEE 802.15.4 frame size limit of 127 bytes.
  - Header compression: how to reduce the size of IPv6 and UDP headers to fit in the IEEE 802.15.4 frame payload.
  - Neighbor discovery: how to discover and register IPv6 addresses and prefixes of other nodes in the network.
  - Routing: how to forward IPv6 datagrams over multiple hops using either mesh-under or route-over approaches.
- 6LoWPAN also supports IPv6 transition mechanisms to connect 6LoWPAN networks to IPv4 networks, such as NAT64, which translates IPv6 addresses to IPv4 addresses and vice versa.
- 6LoWPAN is suitable for applications that require wireless internet connectivity at lower data rates, such as residential and office automation, smart grid, industrial monitoring, etc.



# RPL for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for **Routing Protocol for Low-Power and Lossy Networks**  .
- It is an **IPv6** routing protocol that is standardized for the **Internet of Things (IoT)** by **Internet-Engineering Task Force (IETF)** .
- It supports **multipoint-to-point (MP-to-P)**, **point-to-point (P-to-P)** and **point-to-multipoint (P-to-MP)** communications .
- It forms a **tree-like topology** which is based on different optimizing process called **Objective Function (OF)** .
- It assumes two types of nodes in a network: **border router (gateway)** and **ordinary nodes** .
- The gateway has a connection to the **Internet**, hence it connects nodes in an LLN to the Internet .
- It uses **Directed Acyclic Graphs (DAGs)** to represent the network topology and routing paths.
- It defines two types of DAGs: **Destination-Oriented DAG (DODAG)** and **Instance DAG (IDAG)**.
- A DODAG is a subgraph of a DAG that has a single **root node** and a common **objective function**.
- An IDAG is a set of DODAGs that share the same **RPL instance ID** and the same **administrative domain**.
- RPL uses **control messages** to build and maintain the DAGs, such as **DAG Information Object (DIO)**, **DAG Information Solicitation (DIS)**, **Destination Advertisement Object (DAO)**, and **Destination Advertisement Object Acknowledgment (DAO-ACK)**.
- RPL provides **security mechanisms** to protect the control messages and the network topology from **attacks**, such as **replay protection**, **integrity protection**, and **confidentiality protection**.
- RPL also supports **routing metrics** and **constraints** to optimize the routing paths according to the **application requirements** and the **network characteristics**.
- RPL is considered the **de facto routing protocol** for the IoT, but it also has some **challenges** and **limitations**, such as **scalability**, **mobility**, **reliability**, and **interoperability**.



# Application Layer for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The application layer is the interface between the IoT device and the network with which it will communicate .
- It handles data formatting and presentation and serves as the bridge between what the IoT device is doing and the network handoff of the data it produces.
- It is also responsible for providing services such as data storage, processing, analytics, visualization, and security.
- In IoT architecture, the application layer lies above the service discovery layer, which is responsible for finding and connecting to the appropriate services in the network.
- Some of the common application layer protocols in IoT are:

  - MQTT: Message Queuing Telemetry Transport is a lightweight publish-subscribe protocol that is designed for low-bandwidth, high-latency, and unreliable networks. It is widely used for IoT applications that require real-time data exchange, such as smart home, industrial automation, and healthcare .
  - CoAP: Constrained Application Protocol is a web transfer protocol that is optimized for constrained devices and networks. It is based on the RESTful architecture and uses UDP as the transport layer. It supports features such as multicast, caching, asynchronous messaging, and resource discovery .
  - HTTP: Hypertext Transfer Protocol is the standard protocol for web communication. It is based on the client-server model and uses TCP as the transport layer. It supports features such as authentication, encryption, compression, and caching. It is widely used for IoT applications that require web integration, such as smart city, e-commerce, and social media .
  - AMQP: Advanced Message Queuing Protocol is an open standard for message-oriented middleware. It is based on the broker model and uses TCP as the transport layer. It supports features such as reliability, security, routing, and interoperability. It is widely used for IoT applications that require complex messaging, such as smart grid, logistics, and finance .

