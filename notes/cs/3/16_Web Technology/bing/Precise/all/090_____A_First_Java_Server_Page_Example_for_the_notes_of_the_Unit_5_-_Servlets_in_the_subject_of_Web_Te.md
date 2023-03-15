### A First Java Server Page Example

A Java Server Page (JSP) is a server-side technology that allows developers to create dynamic web pages using Java. JSPs are similar to servlets, but they provide a more convenient way to generate HTML and other types of content.

Here is an example of a simple JSP that generates an HTML page:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title>My First JSP</title>
  </head>
  <body>
    <h1>Hello, World!</h1>
    <p>This is my first JSP page.</p>
  </body>
</html>
```

This JSP generates an HTML page with a title, a heading, and a paragraph. The `<%@ page %>` directive at the top of the file specifies the content type, character encoding, and scripting language for the JSP.

To use this JSP, you need to save it to a file with a `.jsp` extension and deploy it to a web server that supports JSPs, such as Apache Tomcat. When you access the JSP through a web browser, the server will execute the JSP and generate the HTML page.

JSPs provide a convenient way to generate dynamic content for web pages. They allow developers to mix HTML and Java code, making it easy to create pages that change based on user input or other conditions. JSPs are a powerful tool for building web applications with Java.