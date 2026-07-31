### Interface Servlet and the Servlet Life Cycle in Servlets

The Servlet interface is defined in the javax.servlet package and provides the methods to initialize, service, and destroy a servlet. All servlets must implement this interface either directly or by extending a class that implements it, such as HttpServlet  .

The Servlet interface defines the following life cycle methods:

- `init(ServletConfig config)`: This method is invoked by the web container when the servlet is loaded into the container. It is used to initialize the servlet with configuration parameters and resources. The ServletConfig object passed as a parameter contains the initialization parameters and a reference to the ServletContext object     .
- `service(ServletRequest request, ServletResponse response)`: This method is invoked by the web container each time a request for the servlet is received. It is used to process the request and generate a response. The ServletRequest and ServletResponse objects passed as parameters contain the information about the request and the response respectively     .
- `destroy()`: This method is invoked by the web container when the servlet is unloaded from the container. It is used to release any resources and perform any cleanup operations. The web container may call this method when the servlet is idle for a long time or when the container is shutting down     .

The following diagram shows the life cycle of a servlet:

```
+----------------+    +----------------+    +----------------+
| Servlet is     |    | Servlet is     |    | Servlet is     |
| born           |    | initialized    |    | ready to       |
|                |    |                |    | service        |
|                |    |                |    |                |
|                |    |                |    |                |
|                |    |                |    |                |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |<----------------+
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       v                     v                     v                 |
+----------------+    +----------------+    +----------------+    |
| Servlet is     |    | Servlet is     |    | Servlet is     |    |
| destroyed      |    | not ready to   |    | servicing      |    |
|                |    | service        |    |                |    |
|                |    |                |    |                |    |
|                |    |                |    |                |    |
|                |    |                |    |                |    |
|                |    |                |    |                |    |
+----------------+    +----------------+    +----------------+    |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       |                     |                     |                 |
       +---------------------+---------------------+-----------------+
```

: https://www.javaguides.net/2019/02/servlet-life-cycle.html
: https://erainnovator.com/servlet-life-cycle/