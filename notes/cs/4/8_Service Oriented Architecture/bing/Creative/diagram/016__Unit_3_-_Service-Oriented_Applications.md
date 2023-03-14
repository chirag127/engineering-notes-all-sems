## Unit 3 - Service-Oriented Applications

Service-oriented applications are applications that use services to perform business tasks. Services are software components that provide a specific functionality and can communicate with each other across different platforms and languages. Services are reusable, interoperable, and loosely coupled, meaning they can be used by different applications without knowing the details of their implementation. Services are also self-describing, meaning they provide information about their functionality and how to access them.

A service-oriented application typically consists of three layers: the presentation layer, the business layer, and the data layer. The presentation layer is the user interface that interacts with the end users. The business layer contains the business logic and the services that implement it. The data layer manages the data storage and access.

The following diagram illustrates the basic architecture of a service-oriented application using ASCII art:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| Presentation    |      | Business        |      | Data            |
| Layer           |      | Layer           |      | Layer           |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| User Interface  |      | Business Logic  |      | Data Storage    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| Web Browser     |      | Service 1       |      | Database 1      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| Mobile App      |      | Service 2       |      | Database 2      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| Desktop App     |      | Service 3       |      | File System     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|                 |----->| Service 4       |----->| Cloud Storage   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

In this diagram, the presentation layer consists of different user interfaces, such as web browser, mobile app, and desktop app. The business layer consists of different services, such as service 1, service 2, service 3, and service 4. The data layer consists of different data sources, such as database 1, database 2, file system, and cloud storage. The arrows indicate the communication between the layers and the components. For example, the web browser can call service 1, which can access database 1. The mobile app can call service 2, which can access database 2. The desktop app can call service 3, which can access the file system. The presentation layer can also call service 4, which can access the cloud storage. The services can also communicate with each other, for example, service 1 can call service 2, or service 3 can call service 4.

This diagram is only a simplified example of a service-oriented application. In reality, there can be more layers, components, and interactions in a service-oriented application. The main idea is that each service provides a specific functionality that can be used by different applications and other services. This way, the service-oriented application can achieve faster development, easier maintenance, and greater adaptability.