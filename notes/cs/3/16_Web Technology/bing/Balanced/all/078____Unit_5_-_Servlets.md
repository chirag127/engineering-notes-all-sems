## Unit 5 - Servlets

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- A servlet can perform various tasks, such as generating dynamic web content, processing user input, interacting with databases, and implementing business logic.
- A servlet is managed by a servlet container, which is a component of a web server that provides the runtime environment and services for servlets.
- A servlet container handles the lifecycle of a servlet, which consists of the following phases:
  - Initialization: The servlet container calls the `init()` method of the servlet to initialize it and pass any configuration parameters.
  - Request handling: The servlet container calls the `service()` method of the servlet to handle each incoming HTTP request and generate an appropriate HTTP response. The `service()` method can delegate the request to different methods depending on the HTTP method, such as `doGet()`, `doPost()`, `doPut()`, etc.
  - Termination: The servlet container calls the `destroy()` method of the servlet to release any resources and perform any cleanup actions before the servlet is removed from memory.
- A servlet can access various objects and information through the `ServletConfig`, `ServletContext`, `HttpServletRequest`, and `HttpServletResponse` interfaces, which are passed as parameters to the servlet methods.
- A servlet can also use annotations or XML configuration files to specify its metadata, such as its name, URL mapping, initialization parameters, etc.
- A servlet can communicate with other servlets or web components using various mechanisms, such as request dispatching, session tracking, cookies, URL rewriting, etc.