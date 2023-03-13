## Unit 4 - Enterprise Java Bean

Enterprise Java Bean (EJB) is a server-side component architecture for developing and deploying distributed, transactional, secure and portable applications based on Java technology. EJB is conceptually based on the Java RMI (Remote Method Invocation) specification. In EJB, the beans are run in a container having four-tier architecture .

The following diagram illustrates the basic architecture of a EJB application using ASCII art:

```
+-----------------+       +-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |       |                 |
|  Client Tier    |       |  Web Tier       |       |  Business Tier  |       |  EIS Tier       |
|                 |       |                 |       |                 |       |                 |
|  +-----------+  |       |  +-----------+  |       |  +-----------+  |       |  +-----------+  |
|  |           |  |       |  |           |  |       |  |           |  |       |  |           |  |
|  |  Client   |  |       |  |  Web      |  |       |  |  EJB      |  |       |  |  Database |  |
|  |  Program  |  |       |  |  Server   |  |       |  |  Container|  |       |  |  Server   |  |
|  |           |  |       |  |           |  |       |  |           |  |       |  |           |  |
|  +-----------+  |       |  +-----------+  |       |  +-----------+  |       |  +-----------+  |
|                 |       |                 |       |                 |       |                 |
|                 |       |                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+       +-----------------+
       |                       |                       |                       |
       |                       |                       |                       |
       |                       |                       |                       |
       |                       |                       |                       |
       |                       |                       |                       |
       |                       |                       |                       |
       |                       |                       |                       |
       |                       |                       |                       |
       |                       |                       |                       |
       |                       |                       |                       |
       |                       |                       |                       |
       |                       |                       |                       |
       |                       |                       |                       |
       |                       |                       |                       |
       +---------------------->+---------------------->+---------------------->+
```

The client tier consists of the client program that accesses the EJB components. The client program can be a web browser, a standalone application, or another web server.

The web tier consists of the web server that hosts the web pages and servlets that communicate with the EJB components. The web server can use the Java EE web container to manage the web components.

The business tier consists of the EJB server that hosts the EJB components. The EJB server can use the Java EE EJB container to manage the EJB components. The EJB components provide the business logic and services for the application.

The EIS tier consists of the database server that stores the data and resources for the application. The EJB components can access the database server using the Java EE Connector Architecture (JCA) or the Java Database Connectivity (JDBC) API.