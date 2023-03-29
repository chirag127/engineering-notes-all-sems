
### Interface Servlet and the Servlet Life Cycle

1. The Servlet interface is the central abstraction of the Java Servlet API and defines the life cycle methods that all servlets must implement.
2. A servlet is a Java class that is used to extend the capabilities of a server.
3. The Servlet interface defines the five life cycle methods: init(), service(), destroy(), getServletConfig() and getServletInfo().
4. The init() method is invoked by the web container to indicate to a servlet that the servlet is being placed into service.
5. The service() method is invoked by the web container to allow the servlet to respond to a request.
6. The destroy() method is invoked by the web container to indicate to a servlet that it is being taken out of service.
7. The getServletConfig() method returns a ServletConfig object, which is used by a servlet to obtain its initialization parameters.
8. The getServletInfo() method returns a string containing information about the servlet, such as its author, version, and copyright.