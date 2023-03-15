# Unit 5 - Servlets

## Introduction

- Servlets are Java programs that run on a web server and handle HTTP requests and responses.
- Servlets can generate dynamic web content, such as HTML, XML, JSON, etc.
- Servlets can also interact with databases, perform authentication, session management, and other web-related tasks.
- Servlets are portable, scalable, and efficient.

## Servlet Architecture

- A servlet is a Java class that implements the `javax.servlet.Servlet` interface or extends the `javax.servlet.GenericServlet` or `javax.servlet.http.HttpServlet` abstract classes.
- A servlet class must override the `service()` method, which takes a `javax.servlet.ServletRequest` and a `javax.servlet.ServletResponse` as parameters, and performs the business logic of the servlet.
- A servlet can also override the `init()`, `destroy()`, and `getServletConfig()` methods, which are used for initialization, cleanup, and configuration purposes, respectively.
- A servlet runs inside a servlet container, which is a component of a web server that provides the runtime environment and services for servlets, such as request dispatching, security, concurrency, etc.
- A servlet container can host multiple servlets, each identified by a unique name and a URL pattern.
- A servlet container can also support filters, listeners, and other components that can modify or monitor the requests and responses of servlets.

## Servlet Lifecycle

- The servlet lifecycle consists of the following phases:
  - Loading and instantiation: The servlet container loads the servlet class and creates an instance of the servlet. This happens only once for each servlet, unless the servlet is unloaded or the web server is restarted.
  - Initialization: The servlet container calls the `init()` method of the servlet, passing a `javax.servlet.ServletConfig` object that contains the initialization parameters and other information about the servlet. This happens only once for each servlet instance, unless the servlet is reloaded.
  - Request handling: The servlet container calls the `service()` method of the servlet for each HTTP request that matches the servlet's URL pattern. The `service()` method can delegate the request to other methods, such as `doGet()`, `doPost()`, etc., depending on the HTTP method of the request. The `service()` method can also access the request and response objects, which provide methods and attributes for manipulating the HTTP headers, parameters, cookies, sessions, etc.
  - Termination: The servlet container calls the `destroy()` method of the servlet when the servlet is no longer needed, or when the web server is shutting down. The `destroy()` method can perform any cleanup operations, such as closing database connections, releasing resources, etc. This happens only once for each servlet instance.