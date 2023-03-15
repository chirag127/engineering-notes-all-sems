## Unit 5 - Servlets

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- A servlet can perform various tasks, such as generating dynamic web content, processing user input, interacting with databases, and implementing business logic.
- A servlet is managed by a servlet container, which is a component of a web server that provides the runtime environment and services for servlets.
- A servlet container handles the lifecycle of a servlet, which consists of the following phases:
  - Initialization: The servlet container calls the init() method of the servlet to initialize it and pass any configuration parameters.
  - Request handling: The servlet container calls the service() method of the servlet to process each HTTP request and generate an HTTP response. The service() method can delegate the request to different methods depending on the HTTP method, such as doGet(), doPost(), doPut(), doDelete(), etc.
  - Termination: The servlet container calls the destroy() method of the servlet to release any resources and perform any cleanup actions before removing it from memory.
- A servlet can access various objects and information through the servlet API, which consists of two packages: javax.servlet and javax.servlet.http.
- The javax.servlet package defines the generic servlet interface and classes, such as Servlet, ServletConfig, ServletContext, ServletRequest, ServletResponse, etc.
- The javax.servlet.http package defines the HTTP-specific servlet interface and classes, such as HttpServlet, HttpServletRequest, HttpServletResponse, HttpSession, Cookie, etc.
- A servlet can be configured and mapped to a URL pattern using annotations or deployment descriptors (web.xml files).
- A servlet can communicate with other servlets or web components using various techniques, such as request dispatching, redirecting, filtering, event listening, etc.