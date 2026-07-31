## Unit 4 - Enterprise Java Bean

Enterprise Java Beans (EJB) is a server-side software component that is used to encapsulate business logic of an application. It provides a modular approach to building enterprise-level applications. Below are some key points to understand EJB:

- EJB is a specification that defines a set of APIs for building distributed enterprise applications in Java.

- EJBs are divided into three types: Session Beans, Entity Beans, and Message-Driven Beans.

- Session Beans are used for implementing business logic and are created and destroyed for each client request.

- Entity Beans represent persistent data and are used to store data in a database. They can be further divided into two types: Container-Managed Persistence (CMP) and Bean-Managed Persistence (BMP).

- Message-Driven Beans are used to process messages asynchronously and are used in messaging systems like Java Messaging Service (JMS).

- EJBs are managed by a container, which provides services such as transaction management, security, and resource pooling.

- EJBs follow the principle of Inversion of Control (IoC), where the container manages the lifecycle of the bean.

- EJBs can be accessed remotely or locally, depending on the deployment architecture.

- EJBs support both synchronous and asynchronous communication.

- EJBs can be tested using tools like Arquillian, which is an integration testing framework for Java EE.

- EJBs can be deployed on a Java EE application server like GlassFish or JBoss.

In conclusion, EJBs provide a powerful framework for building enterprise-level applications. Understanding the different types of EJBs and their usage is crucial for building scalable and maintainable applications.