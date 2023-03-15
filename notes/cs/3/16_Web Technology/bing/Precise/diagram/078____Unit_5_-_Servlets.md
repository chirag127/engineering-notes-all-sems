## Unit 5 - Servlets

1. Servlets are Java programs that run on a web server and handle HTTP requests and responses.
2. Servlets are used to create dynamic web content and can interact with databases, web services, and other resources.
3. The servlet API is part of the Java EE (Enterprise Edition) specification and is implemented by web servers such as Apache Tomcat and GlassFish.
4. Servlets are managed by a servlet container, which handles the lifecycle of the servlet and provides services such as request dispatching and session management.
5. To create a servlet, a developer must extend the `HttpServlet` class and override methods such as `doGet` and `doPost` to handle HTTP GET and POST requests, respectively.
6. Servlets can be configured using annotations or through a deployment descriptor (web.xml file).
7. The servlet container initializes a servlet when it is first requested and calls its `init` method. The servlet can then handle multiple requests concurrently by creating a new thread for each request.
8. When the servlet is no longer needed, the servlet container calls its `destroy` method to release any resources it may have acquired.
9. Servlets can communicate with other servlets and share data using the `ServletContext` object.
10. Servlets can also use filters to preprocess or postprocess requests and responses.
