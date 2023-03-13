## Unit 5 - Servlets

- Servlets are Java classes that run on a web server and handle requests from web clients (such as browsers).
- Servlets can generate dynamic web pages, interact with databases, process forms, manage sessions, and perform other web-related tasks.
- Servlets are managed by a servlet container, which is a component of a web server that provides the runtime environment and services for servlets.
- Servlets follow a request-response model, where the servlet container receives an HTTP request from a client, invokes the appropriate servlet, and sends back an HTTP response to the client.
- Servlets implement the `javax.servlet.Servlet` interface, which defines the lifecycle methods and the service method for handling requests.
- Servlets can be configured using annotations or deployment descriptors (XML files).
- Servlets can access various objects and information from the servlet container, such as the servlet context, the servlet config, the request, the response, the session, and the listeners.
- Servlets can use filters to intercept and modify requests and responses before and after they reach the servlet.
- Servlets can use listeners to monitor and react to events in the servlet context, the session, the request, and the attributes.
- Servlets can use cookies and URL rewriting to track the state of a client across multiple requests.
- Servlets can use JavaServer Pages (JSP) to simplify the creation of dynamic web pages using HTML, XML, and Java code.