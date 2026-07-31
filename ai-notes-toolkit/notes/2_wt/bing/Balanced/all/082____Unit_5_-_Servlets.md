## Unit 5 - Servlets

- Servlets are a component-based, platform-independent method for building web-based applications, without the performance limitations of CGI programs .
- Servlets have access to the entire family of Java APIs, including the JDBC API to access enterprise databases .
- Servlets are robust and scalable because of Java language.
- Servlets run on the server side and generate dynamic web pages.
- Servlets are managed by a servlet container, which is a part of a web server or an application server .
- A servlet container is responsible for loading, initializing, executing, and destroying servlets.
- A servlet container also provides services such as request dispatching, security, concurrency, and session management.
- A servlet is a Java class that implements the javax.servlet.Servlet interface.
- A servlet can handle HTTP requests and responses using the javax.servlet.http.HttpServlet class, which is a subclass of Servlet.
- A servlet can override the methods of HttpServlet class, such as doGet, doPost, doPut, doDelete, etc., to process different types of HTTP requests.
- A servlet can also use the javax.servlet.http.HttpServletRequest and javax.servlet.http.HttpServletResponse classes, which are subclasses of ServletRequest and ServletResponse, to access the HTTP request and response information.
- A servlet can also use the javax.servlet.http.HttpSession class to maintain the state of a user across multiple requests.
- A servlet can also use the javax.servlet.ServletConfig and javax.servlet.ServletContext classes to access the initialization parameters and the context information of the web application.
- A servlet can also use the javax.servlet.RequestDispatcher class to forward or include the response of another resource (such as another servlet, a JSP page, or a HTML file) in the current response.
- A servlet can also use the javax.servlet.Filter class to intercept and modify the request and response before and after they are processed by a servlet or a resource.

### Example of a servlet

```java
// Import required java libraries
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

// Extend HttpServlet class
public class HelloServlet extends HttpServlet {

  private String message;

  public void init() throws ServletException {
    // Do required initialization
    message = "Hello World";
  }

  public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {

    // Set response content type
    response.setContentType("text/html");

    // Actual logic goes here
    PrintWriter out = response.getWriter();
    out.println("<h1>" + message + "</h1>");
  }

  public void destroy() {
    // do nothing.
  }
}
```

### Advantages of servlets

- Servlets are faster and more efficient than CGI programs, as they run in the same JVM and do not create a new process for each request .
- Servlets are portable across different platforms and web servers, as they are written in Java and follow a standard API .
- Servlets can communicate with other servlets or Java components, such as EJBs, using the RMI or CORBA protocols .
- Servlets can leverage the features of Java, such as multithreading, exception handling, security, and networking .
- Servlets can be easily integrated with other web technologies, such as JSP, JSF, Struts, Spring, etc., to create dynamic and interactive web applications.

### Disadvantages of servlets

- Servlets are more complex and tedious to write than CGI programs, as they require more knowledge of Java and the servlet API .
- Servlets are harder to debug than CGI programs, as they run inside the web server and do not have a standard output or error stream .
- Servlets may suffer from memory leaks or performance issues if they are not properly coded or configured .
- Servlets may not be compatible with some web servers or browsers, as they rely on the HTTP protocol and the servlet container .

### Applications of servlets

- Servlets can be used to create web applications that perform various tasks, such as data processing, form handling, file uploading, authentication, authorization, etc[^3