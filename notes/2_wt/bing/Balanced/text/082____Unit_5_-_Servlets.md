## Unit 5 - Servlets

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- A servlet can perform various tasks, such as generating dynamic web content, processing user input, interacting with databases, and implementing business logic.
- A servlet is managed by a servlet container, which is a component of a web server that provides the runtime environment and services for servlets.
- A servlet container handles the lifecycle of a servlet, which consists of the following phases:
  - Initialization: The servlet container calls the `init()` method of the servlet to initialize it and pass any configuration parameters.
  - Request handling: The servlet container calls the `service()` method of the servlet to process each HTTP request and generate an HTTP response. The `service()` method can delegate the request to different methods based on the HTTP method, such as `doGet()`, `doPost()`, `doPut()`, etc.
  - Termination: The servlet container calls the `destroy()` method of the servlet to release any resources and perform any cleanup actions before the servlet is removed from memory.
- A servlet can access various objects and information related to the HTTP request and response, such as:
  - `HttpServletRequest`: An object that represents the HTTP request and provides methods to access the request parameters, headers, cookies, session, etc.
  - `HttpServletResponse`: An object that represents the HTTP response and provides methods to set the response status, headers, cookies, content type, etc.
  - `ServletConfig`: An object that provides access to the initialization parameters of the servlet, which are specified in the web.xml file or using annotations.
  - `ServletContext`: An object that represents the web application context and provides methods to access the application attributes, resources, configuration, etc.
  - `HttpSession`: An object that represents the session associated with the HTTP request and provides methods to store and retrieve session attributes, invalidate the session, etc.
- A servlet can also use various annotations to specify its metadata, such as:
  - `@WebServlet`: An annotation that declares a servlet and its URL patterns, initialization parameters, load-on-startup order, etc.
  - `@WebInitParam`: An annotation that specifies an initialization parameter for a servlet.
  - `@WebFilter`: An annotation that declares a filter, which is a component that intercepts and modifies the HTTP requests and responses before and after they reach the servlet.
  - `@WebListener`: An annotation that declares a listener, which is a component that listens to and reacts to various events in the web application, such as servlet context initialization, session creation, attribute changes, etc.