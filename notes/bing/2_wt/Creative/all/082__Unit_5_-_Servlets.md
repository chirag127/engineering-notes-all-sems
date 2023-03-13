## Unit 5 - Servlets

- Servlets are Java programs that run on a web server and handle HTTP requests and responses.
- Servlets can be used to create dynamic web pages, process user input, interact with databases, and implement web services.
- Servlets are based on the Java Servlet API, which defines a set of interfaces and classes for creating and managing servlets.
- The main interface of the Java Servlet API is `javax.servlet.Servlet`, which defines the lifecycle methods and service methods of a servlet.
- The lifecycle methods are `init()`, `destroy()`, and `getServletConfig()`, which are invoked by the web container when the servlet is loaded, unloaded, and queried for configuration information, respectively.
- The service methods are `service()`, `doGet()`, `doPost()`, `doPut()`, `doDelete()`, `doHead()`, `doOptions()`, and `doTrace()`, which are invoked by the web container when the servlet receives a HTTP request of a corresponding method.
- The service methods take two parameters: `javax.servlet.ServletRequest` and `javax.servlet.ServletResponse`, which represent the request and response objects, respectively.
- The request object provides methods to access the request information, such as headers, parameters, cookies, attributes, and input stream.
- The response object provides methods to set the response information, such as status code, headers, cookies, attributes, and output stream.
- The request and response objects are usually subclasses of `javax.servlet.http.HttpServletRequest` and `javax.servlet.http.HttpServletResponse`, which provide additional methods specific to the HTTP protocol.
- To create a servlet, one can either implement the `Servlet` interface directly, or extend an abstract class that implements the interface, such as `javax.servlet.GenericServlet` or `javax.servlet.http.HttpServlet`.
- The `GenericServlet` class provides a generic implementation of the `Servlet` interface, and the `HttpServlet` class provides a HTTP-specific implementation of the `GenericServlet` class.
- The `HttpServlet` class also provides a default implementation of the `service()` method, which dispatches the request to the appropriate `doXXX()` method based on the request method.
- To use a servlet, one has to configure it in the web.xml file, which is the deployment descriptor of the web application.
- The web.xml file contains a `<servlet>` element, which defines the servlet name, class, and initialization parameters, and a `<servlet-mapping>` element, which defines the URL pattern that maps to the servlet.
- The web.xml file also contains other elements, such as `<filter>`, `<listener>`, `<context-param>`, `<session-config>`, `<welcome-file-list>`, `<error-page>`, etc., which define various aspects of the web application.
- A mnemonic to remember the lifecycle methods of a servlet is **I Do Get Service** (init, destroy, getServletConfig, service).
- A mnemonic to remember the service methods of a servlet is **Get Post Put Delete Head Options Trace** (doGet, doPost, doPut, doDelete, doHead, doOptions, doTrace).
- An example of a simple servlet that prints "Hello, world!" to the response output stream is:

```java
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class HelloServlet extends HttpServlet {
  public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    response.setContentType("text/plain");
    PrintWriter out = response.getWriter();
    out.println("Hello, world!");
    out.close();
  }
}
```

- An example of a web.xml file that configures the HelloServlet is:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://java.sun.com/xml/ns/javaee" version="2.5">
  <servlet>
    <servlet-name>HelloServlet</servlet-name>
    <servlet-class>HelloServlet</servlet-class>
  </servlet>
  <servlet-mapping>
    <servlet-name>HelloServlet</servlet-name>
    <url-pattern>/hello</url-pattern>
  </servlet-mapping>
</web-app>
```

- Some advantages of servlets are:
  - They are platform-independent and can run on any web server that supports the Java Servlet API.
  - They are fast and efficient, as they are compiled and run in memory, and can use multithreading to handle multiple requests concurrently.
  - They are secure, as they inherit the Java security features, such as sandboxing, encryption, and authentication.
  - They are extensible, as they can use the Java class libraries and third-party libraries to perform various tasks.
  - They are reusable, as they can