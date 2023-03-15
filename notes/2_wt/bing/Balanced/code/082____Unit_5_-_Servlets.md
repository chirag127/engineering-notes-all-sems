## Unit 5 - Servlets

Servlets are a component of the Java Enterprise Edition (JEE) framework used for web development. They provide a platform-independent and component-based method for building web-based applications, without the performance limitations of CGI programs  .

Servlets are Java classes that implement the `javax.servlet.Servlet` interface and run inside a servlet container, such as Tomcat or Jetty. A servlet container is a software component that manages the lifecycle and execution of servlets, as well as providing services such as request handling, session management, security, and concurrency .

A servlet can handle HTTP requests from clients (such as web browsers) and generate dynamic web pages as HTTP responses. A servlet can also access the entire family of Java APIs, including the JDBC API to access enterprise databases .

To create a servlet, we need to:

- Define a Java class that extends `javax.servlet.http.HttpServlet` and overrides the `doGet()` or `doPost()` methods to handle GET or POST requests respectively.
- Annotate the class with `@WebServlet` to specify the URL pattern that the servlet will handle, or define a mapping in the web.xml deployment descriptor file.
- Compile the class and deploy it to the servlet container, along with any web resources (such as HTML, CSS, JS, images, etc.) that the servlet will use.

For example, the following code defines a simple servlet that prints "Hello, world!" to the web browser:

```java
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/hello")
public class HelloServlet extends HttpServlet {

  @Override
  protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
    response.setContentType("text/html");
    PrintWriter out = response.getWriter();
    out.println("<html><body>");
    out.println("<h1>Hello, world!</h1>");
    out.println("</body></html>");
  }
}
```

To learn more about servlets, you can refer to the following resources:

- [Servlets Tutorial - tutorialspoint.com](https://www.tutorialspoint.com/servlets/index.htm)
- [Learn Servlet Tutorial - javatpoint.com](https://www.javatpoint.com/servlet-tutorial)
- [Servlet Tutorial | Java Servlet Tutorial - W3schools](https://www.w3schools.blog/servlet-tutorial)
- [Introduction to Servlets and Servlet Containers | Baeldung](https://www.baeldung.com/java-servlets-containers-intro)