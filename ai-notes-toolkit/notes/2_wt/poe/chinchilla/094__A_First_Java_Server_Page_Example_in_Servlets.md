#### A First Java Server Page Example in Servlets

Java Server Pages (JSP) is a technology used to develop web applications in Java. It allows developers to write dynamic web pages using Java code, which is executed on the server-side. Servlets are Java classes used to perform server-side processing in web applications. In this article, we will discuss a simple example of creating a JSP using Servlets.

Here are the steps to create a simple JSP using Servlets:

1. Create a new Java project in your IDE.
2. Add the necessary JAR files for Servlets and JSPs to your project's classpath.
3. Create a new Servlet by extending the HttpServlet class.
4. Implement the doGet() method in the Servlet to handle HTTP GET requests.
5. In the doGet() method, set the content type of the response to "text/html".
6. Create a PrintWriter object to write the HTML code to the response.
7. Use the PrintWriter object to write HTML code to the response, which will be displayed in the browser.
8. Create a new JSP file in your project's "WebContent" folder.
9. In the JSP file, use the <jsp:include> tag to include the Servlet in the JSP.
10. Start the server and run the application.

Here is an example code snippet for a simple JSP using Servlets:

```java
@WebServlet("/hello")
public class HelloServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<html>");
        out.println("<head>");
        out.println("<title>Hello Servlet</title>");
        out.println("</head>");
        out.println("<body>");
        out.println("<h1>Hello World!</h1>");
        out.println("</body>");
        out.println("</html>");
    }
}
```

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Hello JSP</title>
</head>
<body>
<jsp:include page="/hello"/>
</body>
</html>
```

In this example, we have created a simple Servlet named "HelloServlet" that returns an HTML page with the message "Hello World!". We have also created a JSP file named "index.jsp" that includes the "HelloServlet" using the <jsp:include> tag.

In conclusion, creating a JSP using Servlets is a simple process that can be done in a few easy steps. By using Servlets and JSPs, developers can easily create dynamic web pages with Java code.