A composite application is a software system that consists of functionality drawn from several different sources, such as existing applications, web services, or components. A composite application orchestrates these sources to deliver a new solution that none of the previously available applications could deliver on their own.

A composite application programming model is a framework that supports the development, deployment, and execution of composite applications. It defines how the components of a composite application can be specified, assembled, configured, and managed. It also provides mechanisms for communication, coordination, and integration among the components.

One example of a composite application programming model is the Service Component Architecture (SCA) , which is a set of specifications that describe a model for building applications and systems using a service-oriented architecture (SOA). SOA is an architectural style that promotes the design of loosely coupled, reusable, and interoperable services that can be composed to form business solutions.

The following diagram illustrates the basic architecture of a composite application using SCA:

```
+---------------------+     +---------------------+
| Composite Application |     | Composite Application |
+---------------------+     +---------------------+
|                     |     |                     |
| +-----------------+ |     | +-----------------+ |
| | Service        | |     | | Service        | |
| | Component      | |     | | Component      | |
| +-----------------+ |     | +-----------------+ |
| | Implementation | |     | | Implementation | |
| +-----------------+ |     | +-----------------+ |
| | Interface      | |     | | Interface      | |
| +-----------------+ |     | +-----------------+ |
| | Properties     | |     | | Properties     | |
| +-----------------+ |     | +-----------------+ |
| | References     | |     | | References     | |
| +-----------------+ |     | +-----------------+ |
|                     |     |                     |
+---------------------+     +---------------------+
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
+---------------------+     +---------------------+
| Composite           |     | Composite           |
+---------------------+     +---------------------+
|                     |     |                     |
| +-----------------+ |     | +-----------------+ |
| | Service        | |     | | Service        | |
| | Component      | |     | | Component      | |
| +-----------------+ |     | +-----------------+ |
| | Implementation | |     | | Implementation | |
| +-----------------+ |     | +-----------------+ |
| | Interface      | |     | | Interface      | |
| +-----------------+ |     | +-----------------+ |
| | Properties     | |     | | Properties     | |
| +-----------------+ |     | +-----------------+ |
| | References     | |     | | References     | |
| +-----------------+ |     | +-----------------+ |
|                     |     |                     |
+---------------------+     +---------------------+
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
          |                           |
+---------------------+     +---------------------+
| Runtime Environment |     | Runtime Environment |
+---------------------+     +---------------------+
|                     |     |                     |
| +-----------------+ |     | +-----------------+ |
| | Binding        | |     | | Binding        | |
| +-----------------+ |     | +-----------------+ |
| | Protocol       | |     | | Protocol       | |
| +-----------------+ |     | +-----------------+ |
| | Transport      | |     | | Transport      | |
| +-----------------+ |     | +-----------------+ |
| | Security       | |     | | Security       | |
| +-----------------+ |     | +-----------------+ |
| | Quality of     | |     | | Quality of     | |
| | Service (QoS)  | |     | | Service (QoS)  | |
| +-----------------+ |     | +-----------------+ |
|                     |     |                     |
+---------------------+     +---------------------