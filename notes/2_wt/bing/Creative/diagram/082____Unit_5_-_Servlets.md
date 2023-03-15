## Unit 5 - Servlets

A servlet is a Java program that runs on a web server or an application server and handles HTTP requests and responses. A servlet can process GET, POST, PUT, DELETE and other types of requests from a web browser, a web service client, or another servlet, and generate dynamic content as a response.

A servlet container is a component of a web server or an application server that provides the environment for servlets to run. A servlet container manages the servlet lifecycle, handles the communication between the servlet and the web server, and provides services such as security, concurrency, and session management.

The following diagram shows a simplified architecture of a servlet container and how it interacts with a web server and a servlet:

```
+----------------+        +-----------------+        +----------------+
|                |        |                 |        |                |
|   Web Server   | <----> | Servlet Container | <----> |   Servlet      |
|                |        |                 |        |                |
+----------------+        +-----------------+        +----------------+
     |  ^                         |  ^                      |  ^
     |  |                         |  |                      |  |
     v  |                         v  |                      v  |
+----------------+        +-----------------+        +----------------+
|                |        |                 |        |                |
|   Web Browser  | <----> | Web Service Client | <----> | Other Servlet  |
|                |        |                 |        |                |
+----------------+        +-----------------+        +----------------+
```

The servlet lifecycle consists of the following phases:

- Initialization: The servlet container loads the servlet class and creates an instance of the servlet. Then, it invokes the init() method of the servlet to perform any initialization tasks. The init() method is called only once during the servlet lifetime.
- Request processing: The servlet container passes an HttpServletRequest object and an HttpServletResponse object to the service() method of the servlet. The service() method determines the type of the request (GET, POST, etc.) and calls the corresponding doXXX() method (doGet(), doPost(), etc.) to process the request. The servlet can access the request parameters, headers, cookies, and other information from the HttpServletRequest object, and write the response content, status, headers, cookies, and other information to the HttpServletResponse object. The service() method can be called multiple times during the servlet lifetime, depending on the number of requests received by the servlet container.
- Termination: The servlet container invokes the destroy() method of the servlet to perform any cleanup tasks before removing the servlet instance from memory. The destroy() method is called only once during the servlet lifetime.