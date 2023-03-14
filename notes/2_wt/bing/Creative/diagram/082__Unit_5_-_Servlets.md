## Unit 5 - Servlets

A servlet is a Java program that runs on a web server and handles HTTP requests and responses. Servlets can perform various tasks, such as generating dynamic web content, interacting with databases, implementing business logic, and so on. Servlets are platform-independent, scalable, and secure.

The following ASCII diagram illustrates the basic architecture of a servlet:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|     Client      |       |    Web Server   |       |  Web Container  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Web Browser    |       |  HTTP Server    |       |  Servlet Engine |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  HTTP Request   |------>|  HTTP Request   |------>|  HTTP Request   |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  HTTP Response  |<------|  HTTP Response  |<------|  HTTP Response  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  HTML Form      |       |  web.xml        |       |  Servlet Class  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The diagram shows the following components and steps:

- Client: The client is the entity that sends an HTTP request to the web server. The client can be a web browser, an applet, or a custom HTTP client program.
- Web Server: The web server is the software that manages the access to the web resources hosted on the server. The web server can be a static or a dynamic web server. The web server receives the HTTP request from the client and forwards it to the web container.
- Web Container: The web container is the component that communicates with the servlets. The web container is also known as the servlet engine. The web container performs two main tasks: managing the servlet lifecycle and URL mapping. The web container loads the servlet class, instantiates it, initializes it, invokes the service() method, and destroys it. The web container also maps the URL pattern of the request to the corresponding servlet class, based on the web.xml file.
- Servlet Class: The servlet class is the Java program that implements the servlet interface or extends the GenericServlet or HttpServlet abstract classes. The servlet class overrides the init(), service(), and destroy() methods to process the request and generate the response. The servlet class can also access the implicit HTTP request and response data, such as cookies, media types, headers, etc. The servlet class can also communicate with other resources, such as databases, web services, or other servlets. The servlet class sends the HTTP response back to the web container, which forwards it to the web server, which sends it to the client. The response can be in various formats, such as HTML, XML, binary, etc.