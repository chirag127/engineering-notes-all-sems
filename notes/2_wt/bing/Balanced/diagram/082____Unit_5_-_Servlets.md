## Unit 5 - Servlets

A servlet is a Java program that runs on a web server or an application server and handles requests from clients. A servlet can process requests from different types of clients, such as web browsers, mobile devices, or other servers. A servlet can also generate dynamic content, such as HTML, XML, JSON, or binary data, and send it back to the client as a response.

A servlet is managed by a servlet container, which is a component of the web server or application server that provides the runtime environment and services for the servlet. The servlet container is responsible for loading, initializing, invoking, and destroying the servlets. The servlet container also handles the communication between the servlet and the client, as well as the security, concurrency, and performance aspects of the servlet.

The following diagram shows the basic architecture of a servlet and a servlet container:

```
+-----------------+       +-----------------+
|                 |       |                 |
|    Web Server   |       | Application     |
|                 |       | Server          |
|                 |       |                 |
+-----------------+       +-----------------+
|                 |       |                 |
| Servlet         |       | Servlet         |
| Container       |       | Container       |
|                 |       |                 |
+-----------------+       +-----------------+
|                 |       |                 |
| Servlet         |       | Servlet         |
|                 |       |                 |
+-----------------+       +-----------------+
|                 |       |                 |
| Servlet         |       | Servlet         |
|                 |       |                 |
+-----------------+       +-----------------+
|                 |       |                 |
| Servlet         |       | Servlet         |
|                 |       |                 |
+-----------------+       +-----------------+
```

The servlet container interacts with the web server or the application server using a standard interface, such as the Java Servlet API. The servlet container also provides a set of APIs for the servlets to access the request and response objects, the session and context information, the configuration parameters, and other resources.

The servlet container follows a specific life cycle for each servlet, which consists of the following stages:

- Loading: The servlet container loads the servlet class from the web application archive (WAR) file or the file system and creates an instance of the servlet.
- Initialization: The servlet container invokes the init() method of the servlet, which performs any initialization tasks, such as reading configuration parameters or establishing database connections.
- Request handling: The servlet container invokes the service() method of the servlet, which processes the request from the client and generates the response. The service() method can delegate the request to different methods, such as doGet(), doPost(), doPut(), or doDelete(), depending on the HTTP method of the request.
- Destruction: The servlet container invokes the destroy() method of the servlet, which performs any cleanup tasks, such as closing database connections or releasing resources. The servlet container then removes the servlet instance from memory.

The following diagram shows the life cycle of a servlet:

```
+-----------------+       +-----------------+
|                 |       |                 |
|    Client       |       | Servlet         |
|                 |       | Container       |
|                 |       |                 |
+-----------------+       +-----------------+
|                 |       |                 |
|    Request      |-----> | Load servlet    |
|                 |       |                 |
+-----------------+       +-----------------+
|                 |       |                 |
|                 |       | Init servlet    |
|                 |       |                 |
+-----------------+       +-----------------+
|                 |       |                 |
|                 |       | Service request |
|                 |       |                 |
+-----------------+       +-----------------+
|                 |       |                 |
|    Response     |<----- |                 |
|                 |       |                 |
+-----------------+       +-----------------+
|                 |       |                 |
|                 |       | Destroy servlet |
|                 |       |                 |
+-----------------+       +-----------------+
```

A servlet can also communicate with other servlets or components within the same web application or across different web applications. The servlet container provides a mechanism for servlet collaboration, which involves sharing data and invoking methods among servlets. The servlet container also supports servlet filtering, which allows a servlet to intercept and modify the request and response objects before and after they are processed by another servlet.

The following diagram shows an example of servlet collaboration and filtering:

```
+-----------------+       +-----------------+
|                 |       |                 |
|    Client