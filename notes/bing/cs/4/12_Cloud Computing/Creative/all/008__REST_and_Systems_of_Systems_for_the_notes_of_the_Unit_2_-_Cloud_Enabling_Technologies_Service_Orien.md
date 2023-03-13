### REST and Systems of Systems for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

- REST stands for **Representational State Transfer**, a software architecture style for distributed systems, particularly distributed hypermedia systems, such as the World Wide Web .
- REST is based on a set of principles that define how resources are identified, accessed, and manipulated on the web .
- The main principles of REST are :
  - **Uniform Resource Identifiers (URIs)**: Every resource on the web has a unique identifier that can be used to locate and access it. For example, https://example.com/users/123 is a URI that identifies a specific user resource.
  - **Uniform Interface**: The interaction between clients and servers is standardized by using a set of methods (such as GET, POST, PUT, DELETE) and formats (such as JSON, XML, HTML) that are universally understood and supported by web browsers and servers.
  - **Stateless**: The communication between clients and servers is stateless, meaning that each request contains all the information necessary to process it, and the server does not store any information about the client's state or session. This improves scalability, performance, and reliability of the web applications.
  - **Cacheable**: The responses from the server can be cached by the clients or intermediate proxies to reduce the network traffic and improve the responsiveness of the web applications. The server indicates the cacheability of the responses by using HTTP headers, such as Cache-Control, Expires, ETag, etc.
  - **Layered System**: The web applications can be composed of multiple layers of components, such as load balancers, firewalls, caches, proxies, etc., that are transparent to the clients and servers. This allows for modularity, scalability, security, and reliability of the web applications.
  - **Code on Demand (optional)**: The server can optionally send executable code (such as JavaScript, Java applets, etc.) to the clients to extend their functionality or provide a richer user interface.

- REST is a popular and widely used architecture style for web services, which are software components that provide functionality over the web .
- Web services can be classified into two types: **SOAP-based** and **RESTful** .
- SOAP stands for **Simple Object Access Protocol**, a protocol that uses XML to exchange structured and typed messages between web service providers and consumers .
- SOAP-based web services rely on a set of standards, such as WSDL (Web Services Description Language), UDDI (Universal Description, Discovery, and Integration), and WS-* (Web Services Specifications), to describe, discover, and secure the web services .
- RESTful web services, on the other hand, do not use any specific protocol or standard, but follow the REST principles to provide and consume web services .
- RESTful web services are simpler, more flexible, and more efficient than SOAP-based web services, and have become the dominant choice for web service development and integration .

- Systems of Systems (SoS) are large-scale, complex systems that consist of multiple independent and heterogeneous systems that interact and cooperate to achieve a common goal .
- SoS are characterized by the following features :
  - **Operational Independence**: The constituent systems can operate independently and have their own objectives, functions, and stakeholders.
  - **Managerial Independence**: The constituent systems are managed and controlled by different authorities, and have their own policies, standards, and regulations.
  - **Emergent Behavior**: The SoS exhibits behavior and properties that are not present in the constituent systems, and that are difficult to predict and control.
  - **Evolutionary Development**: The SoS evolves over time, as the constituent systems change, adapt, or are replaced by new systems.
  - **Geographic Distribution**: The constituent systems are geographically dispersed and communicate over networks with varying bandwidth, latency, and reliability.
  - **Interoperability**: The constituent systems have different interfaces, protocols, and data formats, and need to interoperate and exchange information with each other.

- SoS are prevalent in many domains, such as transportation, health care, defense, energy, environment, etc., and pose significant challenges and opportunities for engineering and management