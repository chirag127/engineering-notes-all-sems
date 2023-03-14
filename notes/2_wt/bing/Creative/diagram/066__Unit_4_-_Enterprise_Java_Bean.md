## Unit 4 - Enterprise Java Bean

Enterprise Java Bean (EJB) is a server-side component architecture for developing and deploying distributed, transactional, secure and portable applications based on Java technology. EJB is conceptually based on the Java RMI (Remote Method Invocation) specification. 

There are three types of EJBs: session beans, message-driven beans and entity beans. Session beans encapsulate business logic that can be invoked programmatically by a client. Message-driven beans are similar to session beans, but they are invoked asynchronously by messages from a message queue. Entity beans represent persistent data in a database and provide an object-relational mapping facility.

The following diagram illustrates the basic architecture of an EJB application:

```
+-----------------+       +-----------------+       +-----------------+
|     Client      |       |     Web Tier    |       |    EJB Tier     |
|                 |       |                 |       |                 |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | Application | |       | | Servlets/JSP | |       | | Session    | |
| |  or Web     | |       | |    or JSF    | |       | | Beans      | |
| |  Browser    | |       | +-------------+ |       | +-------------+ |
| +-------------+ |       |                 |       |                 |
|       |         |       | +-------------+ |       | +-------------+ |
|       |         |       | | Web Service | |       | | Message-   | |
|       |         |       | | Client      | |       | | Driven     | |
|       |         |       | +-------------+ |       | | Beans      | |
|       |         |       |                 |       | +-------------+ |
|       |         |       | +-------------+ |       |                 |
|       |         |       | | EJB Client | |       | +-------------+ |
|       |         |       | +-------------+ |       | | Entity     | |
|       |         |       |                 |       | | Beans      | |
|       |         |       +-----------------+       | +-------------+ |
|       |         |               |                 |                 |
|       |         |               |                 +-----------------+
|       |         |               |                           |
|       |         |               |                           |
|       |         |               |                           |
|       |         +---------------+---------------------------+
|       |                         |                           |
|       |                         |                           |
|       |                         |                           |
|       |                         |                           |
|       +-------------------------+---------------------------+
|                                 |                           |
|                                 |                           |
|                                 |                           |
|                                 |                           |
+---------------------------------+---------------------------+
                                  |                           |
                                  |                           |
                                  |                           |
                                  |                           |
+-----------------+       +-----------------+       +-----------------+
|    Database     |       |    JMS Queue    |       |    Web Service  |
|                 |       |                 |       |                 |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | Tables      | |       | | Messages    | |       | | Operations  | |
| +-------------+ |       | +-------------+ |       | +-------------+ |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

: Enterprise JavaBeans Technology - Oracle
: EJB Architecture Java - javatpoint