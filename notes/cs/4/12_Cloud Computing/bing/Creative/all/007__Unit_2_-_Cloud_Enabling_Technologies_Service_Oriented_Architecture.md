## Unit 2 - Cloud Enabling Technologies Service Oriented Architecture

- Service Oriented Architecture (SOA) is a design paradigm that aims to create loosely coupled, reusable, and interoperable services that can communicate across different platforms and technologies.
- SOA consists of three main components: service providers, service consumers, and service registry.
- Service providers are the entities that offer the functionality of a service, such as a web server or a database server.
- Service consumers are the entities that request and use the functionality of a service, such as a web browser or a mobile app.
- Service registry is the entity that maintains a directory of available services and their metadata, such as service name, description, location, and interface.
- SOA enables the development of distributed and scalable applications that can adapt to changing business needs and requirements.
- SOA follows some key principles, such as abstraction, reusability, modularity, composability, discoverability, and interoperability.

- REST (Representational State Transfer) is an architectural style that defines a set of constraints and best practices for designing web services that are based on the HTTP protocol and the concept of resources.
- RESTful web services expose resources (such as data, documents, or images) through uniform resource identifiers (URIs) and support a set of standard HTTP methods (such as GET, POST, PUT, and DELETE) to manipulate them.
- RESTful web services use a stateless communication model, meaning that each request from a client to a server must contain all the information necessary to understand the request, and that the server does not store any client context between requests.
- RESTful web services use a representation-based interaction model, meaning that the client and the server exchange representations of resources (such as JSON, XML, or HTML) that describe the state of the resource and the possible actions on it.
- RESTful web services aim to achieve high performance, scalability, simplicity, and modifiability.

- Systems of Systems (SoS) are large-scale, complex systems that are composed of multiple independent and heterogeneous subsystems that interact and cooperate to achieve a common goal or functionality.
- SoS have some characteristics that distinguish them from traditional systems, such as operational and managerial independence, evolutionary development, emergent behavior, and geographical distribution.
- SoS can be classified into four types, according to the degree of control and collaboration among the subsystems: directed, acknowledged, collaborative, and virtual.
- Directed SoS are those that have a central authority that controls the subsystems and imposes a common objective and a predefined design. An example of a directed SoS is a military command and control system.
- Acknowledged SoS are those that have a central authority that coordinates the subsystems and establishes a common objective and a general design, but the subsystems retain some operational and managerial independence. An example of an acknowledged SoS is an air traffic management system.
- Collaborative SoS are those that have no central authority, but the subsystems voluntarily collaborate and share resources to achieve a common objective and a consensus-based design. An example of a collaborative SoS is a scientific research network.
- Virtual SoS are those that have no central authority and no common objective, but the subsystems interact opportunistically and dynamically to provide a service or a functionality. An example of a virtual SoS is the Internet.

- Web Services are software components that provide a standardized way of exposing functionality and data over the web, using XML-based protocols and formats.
- Web Services can be classified into two types, according to the level of abstraction and the degree of coupling: SOAP-based and RESTful.
- SOAP-based web services use the Simple Object Access Protocol (SOAP) to exchange structured and typed messages between the service provider and the service consumer, using a predefined interface and contract. SOAP-based web services rely on the Web Services Description Language (WSDL) to describe the service interface and the Universal Description, Discovery, and Integration (UDDI) to register and discover the service.
- RESTful web services use the Representational State Transfer (REST) architectural style to expose resources and support a set of standard HTTP methods to manipulate them, using a flexible and self-descriptive interface. RESTful web services rely on the HyperText Transfer Protocol (HTTP) to describe the service interface and the HyperText Markup Language (HTML) to register and discover the service.
- Web Services enable the integration and interoperability of heterogeneous and distributed applications over the web, using open and platform-independent standards.

- Publish-Subscribe Model is a communication paradigm that decouples the service providers (publishers) and the service consumers (subscribers) by introducing an intermediary entity (broker