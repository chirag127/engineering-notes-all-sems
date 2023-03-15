
### Interface Servlet and the Servlet Life Cycle in Servlets

* A Servlet is a Java class that implements the `javax.servlet.Servlet` interface. 
* The `Servlet` interface defines the life cycle of a servlet, which includes initialization, service, and destruction.
* The `init()` method is used to initialize a servlet. It is called only once during the servlet's life cycle, and is used to set up resources such as database connections.
* The `service()` method is used to handle requests from the client. It is called each time a request is made to the servlet.
* The `destroy()` method is used to clean up resources such as database connections. It is called when the servlet is destroyed.