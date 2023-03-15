### Scripting for the notes of the Unit 5 - Servlets in the subject of Web Technology

- Servlets are server-side programs that run on a web server and process web requests from clients.
- Servlets are written in Java and use the Servlet API, which provides classes and interfaces for handling HTTP requests and responses, accessing web server resources, managing sessions, and generating dynamic web pages.
- Servlets are more efficient, robust, and scalable than CGI scripts, which are external programs that run on a web server and communicate with the web server through a standard protocol.
- Servlets have a life cycle that consists of the following phases:
  - Initialization: The web server loads the servlet class and creates an instance of the servlet. The servlet's `init()` method is invoked to perform any initialization tasks.
  - Request handling: The web server invokes the servlet's `service()` method to process a web request from a client. The `service()` method can delegate the request to different methods depending on the HTTP method, such as `doGet()`, `doPost()`, `doPut()`, etc. The servlet can read request parameters, headers, and body, and write response headers, status, and body.
  - Termination: The web server unloads the servlet and destroys its instance. The servlet's `destroy()` method is invoked to perform any cleanup tasks.
- Servlets can be configured and mapped to specific URL patterns using annotations or deployment descriptors (web.xml files).
- Servlets can use various mechanisms to store and share data across requests, such as:
  - Servlet context: An object that represents the web application and provides access to web server resources and initialization parameters. The servlet context is shared by all the servlets in the same web application.
  - Servlet config: An object that provides access to initialization parameters for a specific servlet. The servlet config is unique for each servlet instance.
  - HTTP session: An object that maintains state information for a client across multiple requests. The session is identified by a unique session ID and can store attributes that are accessible by the servlets in the same web application.
  - Cookies: Small pieces of data that are sent by the web server to the client and stored by the client's browser. The cookies are sent back to the web server with each request and can store information such as user preferences, authentication, etc.
  - Request and response objects: Objects that provide access to the request and response data for a specific web request. The request and response objects can store attributes that are accessible by the servlets and other components that process the same request.