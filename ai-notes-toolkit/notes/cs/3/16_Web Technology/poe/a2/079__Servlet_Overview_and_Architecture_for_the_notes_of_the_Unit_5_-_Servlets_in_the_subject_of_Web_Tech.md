 Here is the formal notes in markdown format without any emojis or external links on the topic of Servlet Overview and Architecture:

### Servlet Overview and Architecture

1. Servlet is a Java programming language class used to extend the capabilities of servers that host applications accessed by means of a request-response programming model.

2. The javax.servlet and javax.servlet.http packages provide interfaces and classes for servlet API. Servlet API provides a mechanism to define HTTP servlet request and response objects.

3. The life cycle of a servlet comprises the following stages:

- Loading: The web container loads the servlet class.
- Instantiation: The web container creates an instance of the servlet class.
- Initialization: The web container calls the init method.
- Request Handling: The web container calls the service method to handle requests.
- Destroy: The web container calls the destroy method before removing the servlet.

4. The Servlet interface defines the three key methods known as lifecycle methods:

- init(ServletConfig config): This method is called by the web container to indicate to a servlet that the servlet is being placed into service.
- service(ServletRequest req, ServletResponse res): This method is called by the web container to allow a servlet to respond to requests.
- destroy(): This method is called by the web container to indicate to a servlet that the servlet is being taken out of service.

5. The architecture of Servlet involves:

- Client: Sends requests to the Web server.
- Web Server: Receives requests and forwards them to servlets.
- Servlet: Executes business logic and generates responses.
- Web Container: Manages the lifecycle of servlets.

This notes covers the overview and architecture of Servlets in a formal tone without any emojis or external links as requested. Please let me know if you would like me to modify or add any other points to the notes.