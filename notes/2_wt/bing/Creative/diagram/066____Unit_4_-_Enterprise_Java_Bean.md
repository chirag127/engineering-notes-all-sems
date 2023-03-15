## Unit 4 - Enterprise Java Bean

An Enterprise Java Bean (EJB) is a Java class that runs on a server and provides business logic for distributed applications. There are three types of EJBs: session beans, entity beans, and message-driven beans. Each type of EJB has a different lifecycle and interacts with the EJB container and the EJB server in different ways.

The following diagram shows a simplified and unofficial UML representation of the EJB architecture, based on the search results     :

```
+-----------------+     +-----------------+     +-----------------+
|  EJB Container  |     |  EJB Container  |     |  EJB Container  |
+-----------------+     +-----------------+     +-----------------+
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Session Bean| |     | | Entity Bean | |     | | Message-    | |
| +-------------+ |     | +-------------+ |     | | Driven Bean | |
| | +---------+ | |     | | +---------+ | |     | +-------------+ |
| | | Business| | |     | | | Business| | |     | | +---------+ | |
| | | Logic   | | |     | | | Logic   | | |     | | | Business| | |
| | +---------+ | |     | | +---------+ | |     | | | Logic   | | |
| +-------------+ |     | +-------------+ |     | | +---------+ | |
| | +---------+ | |     | | +---------+ | |     | +-------------+ |
| | | EJB     | | |     | | | EJB     | | |     | | +---------+ | |
| | | Context | | |     | | | Context | | |     | | | EJB     | | |
| | +---------+ | |     | | +---------+ | |     | | | Context | | |
| +-------------+ |     | +-------------+ |     | | +---------+ | |
+-----------------+     +-----------------+     | +-------------+ |
| +-------------+ |     | +-------------+ |     +-----------------+
| | EJB Home   | |     | | EJB Home   | |     | +-------------+ |
| +-------------+ |     | +-------------+ |     | | EJB Home   | |
| | +---------+ | |     | | +---------+ | |     | +-------------+ |
| | | Create  | | |     | | | Create  | | |     | | +---------+ | |
| | | Remove  | | |     | | | Remove  | | |     | | | Create  | | |
| | | Find    | | |     | | | Find    | | |     | | | Remove  | | |
| | +---------+ | |     | | +---------+ | |     | | +---------+ | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
+-----------------+     +-----------------+     +-----------------+
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | EJB Object | |     | | EJB Object | |     | | EJB Object | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | +---------+ | |     | | +---------+ | |     | | +---------+ | |
| | | Business| | |     | | | Business| | |     | | | Business| | |
| | | Methods | | |     | | | Methods | | |     | | | Methods | | |
| | +---------+ | |     | | +---------+ | |     | | +---------+ | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
+-----------------+     +-----------------+     +-----------------+
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | EJB Local  | |     | | EJB Local  | |     | | EJB Local  | |
| | Home       | |     | | Home       | |     | | Home       | |
| +-------------+ |     | +-------------+ |