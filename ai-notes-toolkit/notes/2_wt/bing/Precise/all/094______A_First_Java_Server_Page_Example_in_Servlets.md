#### A First Java Server Page Example in Servlets

A Java Server Page (JSP) is a text document that contains two types of text: static data and JSP elements. Static data can be expressed in any text-based format, such as HTML, SVG, WML, and XML, while JSP elements are used to control the dynamic generation of the response.

Here is an example of a simple JSP page that generates a response in HTML:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title>My First JSP</title>
  </head>
  <body>
    <h1>Hello, World!</h1>
    <p>The current time is: <%= new java.util.Date() %></p>
  </body>
</html>
```

This JSP page contains two JSP elements: a page directive and an expression. The page directive sets the content type and the scripting language for the page, while the expression outputs the current date and time.

When this JSP page is requested, the JSP engine translates it into a servlet. The servlet generates the response by executing the JSP elements and outputting the static data. The resulting HTML page is then sent back to the client.

Advantages of using JSP:
- Separation of concerns: JSP allows the separation of dynamic content generation from the presentation logic.
- Reusability: JSP elements can be reused across multiple pages, reducing code duplication.
- Ease of use: JSP is easy to learn and use, even for developers with little or no experience in Java.

Disadvantages of using JSP:
- Performance: JSP pages may have slower performance compared to pure servlets, as they need to be translated into servlets before execution.
- Limited control: JSP provides limited control over the generated response, as it is mainly intended for generating presentation logic.

Mnemonics and learning tricks:
- Remember that JSP stands for Java Server Pages.
- JSP elements start with `<%` and end with `%>`.
- The page directive sets the content type and scripting language for the page.
- Expressions output dynamic content and are enclosed in `<%=` and `%>`.