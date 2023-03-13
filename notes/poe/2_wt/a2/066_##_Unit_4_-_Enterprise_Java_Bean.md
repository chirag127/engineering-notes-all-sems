 Here is the content in markdown format for Unit 4 - Enterprise Java Bean:

## Unit 4 - Enterprise Java Bean

- Enterprise JavaBeans (EJB) is a development architecture for building highly scalable and distributed enterprise-level applications using Java programming language.
- EJBs supports transactions, security, scalability, and other enterprise services.
- The EJB architecture consists of two main components:

### EJB Containers
- EJB Containers provide an environment for executing EJB components.
- It manages the life cycle of the EJB components and provides services such as transactions, security, threading, persistence, remoting, etc. to the EJB components.
- Two types of EJB containers:

#### Application Server Container
- Provided by Application Servers like WebLogic, WebSphere, JBoss, etc.
- Manages the execution of the enterprise beans and provides services to enterprise beans.

#### Embedded Container
- Runs within a Java SE application.
- Useful for testing EJBs.

### Enterprise Beans (EJB Components)
- The EJB components are the business logic components that run within the EJB container.
- There are three types of EJB components:

#### Session Beans
- Used to encapsulate business logic/methods.
- Two types: Stateless session beans and Stateful session beans.
- Stateless beans do not maintain client state. A single bean instance can service multiple clients.
- Stateful beans maintain state for a particular client. A single bean instance is used to service a particular client.

#### Message-Driven Beans (MDB)
- Used to provide asynchronous communication.
- MDBs listen to JMS messages and can perform tasks after receiving messages.

#### Entity Beans
- Used to model data in a database.
- An entity bean represents a row in a database table.

Advantages:
- Distributed and scalable architecture.
- Supports transactions, security, concurrency, etc.
- Separates business logic from the presentation layer.

Disadvantages:
- Complex architecture and development process.
- Heavyweight and resource-intensive.
- Vendor dependence.

Applications:
- Enterprise-level applications that require services like transactions, security, etc.
- Applications that need to be distributed and scalable.

[Detailed diagrams and code samples can be added here if required.]