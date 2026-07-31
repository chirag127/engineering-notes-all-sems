### Java Server Pages (JSP) in Servlets

Java Server Pages (JSP) is a technology that allows dynamic content injection into static web pages using Java and Java Servlets. JSP pages can be used in combination with servlets that handle the business logic, the model supported by Java servlet template engines .

A JSP page is a text document that contains two types of text: static data, which can be expressed in any text-based format (such as HTML, XML, SVG, WML, and so on), and JSP elements, which construct dynamic content.

The JSP elements are processed by a JSP engine, which is a part of the web server that supports the JSP technology. The JSP engine translates the JSP page into a servlet class, compiles it, and executes it to generate the dynamic content.

The JSP elements include:

- Directives: instructions to the JSP engine that affect the overall structure of the servlet class.
- Scriptlets: fragments of Java code that are executed when the JSP page is requested.
- Expressions: Java expressions that are evaluated and inserted into the output stream.
- Declarations: fragments of Java code that declare variables and methods for the servlet class.
- Actions: XML-style tags that invoke built-in or custom functionality.
- Comments: text that is ignored by the JSP engine.

A simple example of a JSP page that displays the current date and time is:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>JSP Example</title>
</head>
<body>
    <h1>Hello, world!</h1>
    <p>The current date and time is: <%= new java.util.Date() %></p>
</body>
</html>
```

The first line is a directive that specifies the content type, the language, and other attributes of the page. The `<%= %>` is an expression that inserts the result of the Java expression into the output stream. The rest of the text is static HTML that is passed through to the output stream.

To use JSP pages in servlets, you need to configure the web server to support the JSP technology, and place the JSP pages in the appropriate directory. You can also use the `<jsp:include>` action to include the output of a JSP page into another JSP page or a servlet. For example, you can write a servlet that includes the JSP page above as follows:

```java
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class JSPServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<html>");
        out.println("<head>");
        out.println("<title>JSP Servlet Example</title>");
        out.println("</head>");
        out.println("<body>");
        out.println("<h1>This is a servlet that includes a JSP page</h1>");
        out.println("<jsp:include page=\"example.jsp\" />");
        out.println("</body>");
        out.println("</html>");
    }
}
```

The `<jsp:include>` action invokes the JSP page `example.jsp` and includes its output in the servlet's output stream. The JSP page and the servlet must be in the same web application context.

JSP is a powerful and flexible technology that simplifies the development of web applications that generate dynamic content. It is an alternative to Microsoft's Active Server Pages (ASP) technology, and a key component of the Java 2 Enterprise Edition (J2EE) specification.