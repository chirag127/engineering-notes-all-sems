Enterprise Java Beans (EJB) is a server-side component architecture for building modular, scalable, and secure enterprise applications. There are three types of beans in EJB: Session Beans, Entity Beans, and Message-Driven Beans.

### Types of beans in Enterprise Java Bean
```
+---------------------+
| Enterprise Java Bean|
+---------------------+
|                     |
| +----------------+  |
| | Session Beans  |  |
| +----------------+  |
|                     |
| +----------------+  |
| | Entity Beans   |  |
| +----------------+  |
|                     |
| +----------------+  |
| | Message Beans  |  |
| +----------------+  |
|                     |
+---------------------+
```
Session Beans are used to manage the interactions between the client and the server. They can be stateful, stateless, or singleton.

Entity Beans are used to represent data in a database. They can be container-managed or bean-managed.

Message-Driven Beans are used to process messages asynchronously. They act as a listener for a particular messaging type, such as JMS.
