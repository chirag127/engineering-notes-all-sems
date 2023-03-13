SaaS stands for Software as a Service, which is a delivery model where software applications are hosted and managed by a service provider and accessed by customers over the internet. SaaS applications are typically multi-tenant, meaning that multiple customers share the same instance of the application and the underlying infrastructure, but their data and configurations are isolated from each other.

A basic architecture diagram of a SaaS application could look something like this:

```
+-----------------+        +-----------------+
|                 |        |                 |
|    Customer A   |        |    Customer B   |
|                 |        |                 |
+-----------------+        +-----------------+
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        v                         v
+-----------------+        +-----------------+
|                 |        |                 |
|    Web Browser  |        |    Web Browser  |
|                 |        |                 |
+-----------------+        +-----------------+
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        +-------------------------+
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        v                         v
+-----------------+        +-----------------+
|                 |        |                 |
|    Load Balancer|        |    Load Balancer|
|                 |        |                 |
+-----------------+        +-----------------+
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        +-------------------------+
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        v                         v
+-----------------+        +-----------------+
|                 |        |                 |
|    Web Server   |        |    Web Server   |
|                 |        |                 |
+-----------------+        +-----------------+
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        +-------------------------+
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        v                         v
+-----------------+        +-----------------+
|                 |        |                 |
|    Application  |        |    Application  |
|    Server       |        |    Server       |
|                 |        |                 |
+-----------------+        +-----------------+
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        +-------------------------+
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        v                         v
+-----------------+        +-----------------+
|                 |        |                 |
|    Database     |        |    Database     |
|                 |        |                 |
+-----------------+        +-----------------+
```

In this diagram, each customer accesses the SaaS application through their web browser. The web browser sends requests to a load balancer, which distributes the load among multiple web servers. The web servers handle the requests and communicate with the application servers, which contain the business logic and functionality of the SaaS application. The application servers interact with the database, which stores the data and configurations of each customer in a separate schema or table. The database is also replicated and backed up for high availability and disaster recovery.

This is a simplified diagram that does not show all the details and components of a SaaS architecture, such as security, authentication, monitoring, logging, caching, etc. However, it illustrates the basic concept of how a SaaS application can serve multiple customers with a single instance of the software and the infrastructure.