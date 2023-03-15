### Types of beans in Enterprise Java Bean

Enterprise Java Beans (EJB) are Java components that can be combined with other resources to create Java applications. They run inside an EJB container, which provides services such as security, transaction management, dependency injection, concurrency, etc.   

There are three types of EJB:

- **Session beans**: These beans contain business logic that can be invoked by local, remote or web service clients. They are non-persistent and do not represent data in a database. There are three subtypes of session beans:   

  - **Stateless session beans**: These beans do not maintain any conversational state with the clients. They are pooled by the container and can be reused by different clients. They are suitable for stateless operations, such as calculations, validations, etc.  

  - **Stateful session beans**: These beans maintain a conversational state with the clients. They are not pooled by the container and are bound to a specific client. They are suitable for stateful operations, such as shopping carts, wizards, etc.  

  - **Singleton session beans**: These beans are instantiated only once per application and are shared by all the clients. They are suitable for application-wide operations, such as caching, logging, configuration, etc.  

- **Message-driven beans**: These beans are asynchronous and event-driven. They receive and process messages from a message queue or a topic. They are suitable for integrating with other systems, such as legacy applications, email servers, etc.   

- **Entity beans**: These beans are deprecated and should not be used. They represent persistent data in a database and provide object-relational mapping. They are replaced by Java Persistence API (JPA) entities.  

A possible mnemonic to remember the types of beans is:

- **S**ession beans are **S**tateless, **S**tateful or **S**ingleton.
- **M**essage-driven beans are **M**essaging and **M**ultithreaded.
- **E**ntity beans are **E**xpired and **E**liminated.

A possible diagram to illustrate the types of beans is:

```
+-----------------+
| Enterprise Java |
|     Beans       |
+-----------------+
       /|\
        |
        |
+-----------------+
|   Session Beans |<-----------------+
+-----------------+                  |
       /|\                          |
        |                           |
        |                           |
+-----------------+                  |
| Stateless Beans |                  |
+-----------------+                  |
                                    |
+-----------------+                  |
| Stateful Beans  |                  |
+-----------------+                  |
                                    |
+-----------------+                  |
| Singleton Beans |                  |
+-----------------+                  |
                                    |
+-----------------+                  |
| Message-Driven  |                  |
|     Beans       |------------------+-----------------+
+-----------------+                  |                 |
                                    |                 |
+-----------------+                  |                 |
|  Entity Beans   |<-----------------+                 |
+-----------------+                                    |
                                                       |
+-----------------+                                    |
|  JPA Entities   |<-----------------------------------+
+-----------------+
```