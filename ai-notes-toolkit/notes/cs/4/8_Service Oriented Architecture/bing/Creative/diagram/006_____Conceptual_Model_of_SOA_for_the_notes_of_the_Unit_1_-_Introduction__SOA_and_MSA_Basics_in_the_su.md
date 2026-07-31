### Conceptual Model of SOA

- Service-oriented architecture (SOA) is a software development model that allows services to communicate across different platforms and languages to form applications.
- A service is a self-contained unit of software designed to complete a specific task.
- SOA is an integration architectural style and an enterprise-wide concept .
- It enables existing applications to be exposed over loosely-coupled interfaces, each corresponding to a business function, that enables applications in one part of an extended enterprise to reuse functionality in other applications .
- The defining concepts of SOA are:
  - The business value is more important than the technical strategy.
  - The strategic goals are more important than benefits related to specific projects.
  - Basic interoperability is more important than custom integration.
  - Shared services are more important than implementations with a specific purpose.
- A conceptual model of SOA can be represented by UML, as shown in the following diagram:

![Conceptual model of SOA](https://www.igi-global.com/viewtitle.aspx?TitleId=72133&imagepath=images/2013/72133/72133.fig.001.jpg)

- The model consists of entities and their relationships:
  - Service: a software component that provides a specific functionality and can be accessed through an interface.
  - Service provider: an entity that owns and manages one or more services.
  - Service consumer: an entity that uses one or more services provided by service providers.
  - Service registry: a repository that stores information about available services and their interfaces.
  - Service broker: an intermediary that facilitates the discovery and invocation of services between service consumers and service providers.
  - Service contract: a specification that defines the terms and conditions of using a service, such as the interface, quality of service, and security requirements.
  - Service composition: a process of combining multiple services to create a new service or application.
  - Service orchestration: a type of service composition that involves a central controller that coordinates the execution of services according to a predefined workflow.
  - Service choreography: a type of service composition that involves a decentralized collaboration of services that interact according to a shared protocol.