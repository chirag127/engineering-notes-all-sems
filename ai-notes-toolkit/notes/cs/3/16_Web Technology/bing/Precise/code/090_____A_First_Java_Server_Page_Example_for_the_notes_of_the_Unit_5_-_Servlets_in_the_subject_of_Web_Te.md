### A First Java Server Page Example

1. A Java Server Page (JSP) is a text document that contains two types of text: static data and JSP elements.
2. Static data can be expressed in any text-based format, such as HTML, SVG, or XML.
3. JSP elements are used to construct dynamic content and can be expressed using JSP tags, scriptlets, or expressions.
4. A JSP is compiled into a servlet by the web container, which means that it has all the functionality of a servlet.
5. To create a JSP, you need to have a servlet container, such as Apache Tomcat, installed on your system.
6. A simple JSP example can be created by creating a new file with the `.jsp` extension and placing it in the web application's directory.
7. The JSP file can contain static HTML content, as well as JSP tags and scriptlets to generate dynamic content.
8. When the JSP is accessed by a web browser, the servlet container will compile the JSP into a servlet and execute it to generate the dynamic content.
9. The resulting HTML will be sent back to the web browser for rendering.

Here is an example of a simple JSP that generates dynamic content:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title>A Simple JSP Example</title>
  </head>
  <body>
    <h1>A Simple JSP Example</h1>
    <p>The current time is: <%= new java.util.Date() %></p>
  </body>
</html>
```

This JSP uses a scriptlet to generate the current time and display it on the page. When the JSP is accessed by a web browser, the servlet container will compile the JSP into a servlet, execute it, and send the resulting HTML back to the web browser for rendering. The resulting page will display the current time, which will be updated each time the page is refreshed.