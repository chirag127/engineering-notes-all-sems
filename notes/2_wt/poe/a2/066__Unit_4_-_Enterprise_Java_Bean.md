 Here is the formal content written in Markdown format without any emojis or external links under the header ## Unit 4 - Enterprise Java Bean:

## Unit 4 - Enterprise Java Bean

1. Enterprise JavaBeans (EJB) is a development architecture for multi-tier enterprise applications.
2. EJB runs on top of an application server and provides services such as transactions, security and scalability.
3. The EJB architecture focuses on reusability of components and a separation between the business logic and the presentation layer.
4. The main advantage of EJB is that it reduces complexity by providing a managed environment for developing enterprise grade applications.
5. The different types of EJBs are:

- Session Beans: Used to encapsulate business logic. Two types: Stateless and Stateful
- Message Driven Beans: Used to provide asynchronous communications via messages
- Entity Beans: Used to map objects to a relational database. Deprecated in EJB 3.1

6. An EJB application typically consists of an EJB container and multiple EJB modules. The EJB container provides services to the EJB modules and manages their lifecycle.
7. EJB implements a client-server architecture. The application client uses the EJB components remotely via interfaces. The EJB components run inside the EJB container.
8. The different EJB interfaces are:

- Remote: Used for remote access. The business methods are accessed remotely via RMI.
- Local: Used for local access. The business methods are accessed locally via direct method calls.
- No-interface: Used since EJB 3.1 to develop POJOs as EJBs. Only local access is possible.

9. EJB supports dependency injection to obtain resource references and can be packaged as deployable units (EJB JAR or WAR file). It provides metadata via XML deployment descriptors or annotations.