## Unit 5 - Technologies for SOA

- Service-Oriented Architecture (SOA) is a software development model that allows services to communicate across different platforms and languages to form applications.
- A service is a self-contained unit of software designed to complete a specific task.
- SOA benefits organizations by creating interoperability between apps and services, ensuring existing applications can be easily scaled, and reducing costs related to the development of business service solutions.
- SOA is independent of vendors and technologies, and can be implemented with various protocols and standards .
- Some standard protocols to implement SOA include the following:
  - Simple Object Access Protocol (SOAP): A messaging protocol that uses XML to exchange information between services.
  - RESTful HTTP: A style of web service that uses HTTP methods (GET, POST, PUT, DELETE) to perform operations on resources identified by URIs.
  - Apache Thrift: A framework that supports cross-language service development by using an interface definition language (IDL) and a code generator.
  - Apache ActiveMQ: A message broker that enables asynchronous communication between services using a publish-subscribe or point-to-point model.
  - Java Message Service (JMS): A Java API that allows applications to create, send, receive, and read messages using a message-oriented middleware (MOM).
- SOA also requires some supporting technologies to provide security, governance, and discovery for the services, such as :
  - Web Services Description Language (WSDL): A standard XML format to describe the interface, functionality, and location of a web service.
  - Universal Description, Discovery & Integration (UDDI): A registry that enables service providers to publish their services and service consumers to find and bind to them.
  - Enterprise Service Bus (ESB): An architectural pattern that provides a centralized software component to perform integrations between services using various protocols and formats.
  - Service Registry: A repository that stores information about the services, such as their metadata, policies, and contracts.
  - Service Repository: A repository that stores the artifacts related to the services, such as their source code, configuration files, and documentation.