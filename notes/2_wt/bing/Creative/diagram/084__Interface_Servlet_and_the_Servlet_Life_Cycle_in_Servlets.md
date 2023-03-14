### Interface Servlet and the Servlet Life Cycle in Servlets

The Servlet interface defines methods to initialize a servlet, to service requests, and to destroy a servlet and its resources. These are known as life-cycle methods, and are called in the following order:

- `init()` : This method is invoked only once by the servlet container when the servlet is loaded. It is used to initialize the servlet and its resources, such as database connections, configuration parameters, etc. The servlet container passes a ServletConfig object to this method, which contains information about the servlet's configuration and initialization parameters.
- `service()` : This method is invoked by the servlet container for each request that the servlet receives. It is responsible for processing the request and generating the response. The servlet container passes a ServletRequest object and a ServletResponse object to this method, which contain information about the request and the response respectively. The service() method can delegate the request to different methods based on the HTTP method, such as doGet(), doPost(), doPut(), etc.
- `destroy()` : This method is invoked by the servlet container when the servlet is about to be removed from the service. It is used to release any resources that the servlet has allocated, such as threads, memory, database connections, etc. The servlet container calls this method only once, after all the service() methods have completed or after a timeout period.

The following diagram illustrates the basic architecture of a servlet and its life cycle using ASCII art:

```
+-----------------+            +-----------------+
| Web Browser     |            | Web Server      |
| (Client)        |            | (Servlet        |
|                 |  HTTP      | Container)      |
|                 +----------->|                 |
|                 |            |                 |
|                 |            |  +----------+   |
|                 |            |  | Servlet  |   |
|                 |            |  | Class    |   |
|                 |            |  |          |   |
|                 |            |  | +------+ |   |
|                 |            |  | | init | |   |
|                 |            |  | +------+ |   |
|                 |            |  |    |    |   |
|                 |            |  |    v    |   |
|                 |            |  | +------+ |   |
|                 |            |  | |service| |   |
|                 |            |  | +------+ |   |
|                 |            |  |    |    |   |
|                 |            |  |    v    |   |
|                 |            |  | +------+ |   |
|                 |            |  | |destroy| |   |
|                 |            |  | +------+ |   |
|                 |            |  +----------+   |
|                 |            |                 |
|                 |            |                 |
|                 |            |                 |
|                 |            |                 |
+-----------------+            +-----------------+
```