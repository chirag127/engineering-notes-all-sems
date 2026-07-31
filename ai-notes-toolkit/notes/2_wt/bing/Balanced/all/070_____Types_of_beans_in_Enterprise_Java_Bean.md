### Types of beans in Enterprise Java Bean

Enterprise Java Beans (EJB) are server-side components that encapsulate the business logic of an application. They can be combined with other resources to create Java applications. There are three types of enterprise beans:

- **Session beans**: These beans contain business logic that can be invoked by local, remote or web service clients. They are transient and do not persist across server restarts. There are two types of session beans:
  - **Stateful session beans**: These beans maintain the conversational state of a client across multiple method calls. They can be associated with a specific client and can store the client's data in their instance variables. They are typically used for complex and long-running interactions that require multiple requests and responses.
  - **Stateless session beans**: These beans do not maintain any conversational state of a client. They can be shared by multiple clients and do not store any client-specific data. They are typically used for simple and short-lived interactions that require a single request and response.
- **Entity beans**: These beans represent persistent data objects that can be stored in a database or other data sources. They provide an object-oriented view of the data and encapsulate the logic for accessing and manipulating the data. They are deprecated since EJB 3.0 and replaced by Java Persistence API (JPA) entities.
- **Message-driven beans**: These beans are asynchronous components that process messages from a message queue or a topic. They act as message consumers and listeners and can respond to messages from any client. They are typically used for integrating applications with other systems using the Java Message Service (JMS) API.

A possible mnemonic to remember the types of beans is:

**S**ession beans are **S**hort-lived and **S**tateful or **S**tateless.

**E**ntity beans are **E**nduring and **E**xpired.

**M**essage-driven beans are **M**essaging and **M**odular.