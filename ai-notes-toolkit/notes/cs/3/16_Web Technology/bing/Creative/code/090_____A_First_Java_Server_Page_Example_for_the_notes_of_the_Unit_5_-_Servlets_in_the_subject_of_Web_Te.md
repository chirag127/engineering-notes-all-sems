### A First Java Server Page Example

- A Java Server Page (JSP) is a web page that contains Java code embedded in HTML or XML tags.
- The Java code in a JSP is executed on the server side and generates dynamic content for the web page.
- A JSP file has the extension `.jsp` and can be placed in any directory under the web application root.
- A JSP file can include static HTML or XML elements, as well as JSP elements, such as directives, declarations, expressions, scriptlets, and actions.
- A JSP file can also use JavaBeans, custom tags, and other components to modularize and reuse the code.
- A JSP file is compiled into a servlet class by the web container when it is first requested by a client.
- The servlet class is then executed by the web container to generate the response for the client.
- The web container also caches the servlet class and reuses it for subsequent requests, unless the JSP file is modified.

#### Example of a Simple JSP File

- The following JSP file displays the current date and time using the `java.util.Date` class:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>A Simple JSP Example</title>
</head>
<body>
    <h1>A Simple JSP Example</h1>
    <p>The current date and time is: <%= new java.util.Date() %></p>
</body>
</html>
```

- The first line of the JSP file is a directive that specifies the content type, the language, and other attributes of the page.
- The directive starts with `<%@` and ends with `%>`.
- The `<%= %>` tags are used to embed a Java expression that is evaluated and printed as part of the output.
- The expression can be any valid Java expression that returns a value, such as a variable, a method call, or a literal.
- The rest of the JSP file is plain HTML that defines the structure and style of the web page.

#### How to Run the JSP File

- To run the JSP file, you need to have a web container that supports the JSP technology, such as Apache Tomcat, Jetty, or GlassFish.
- You also need to have a web browser that can send HTTP requests and display HTML pages, such as Chrome, Firefox, or Edge.
- To run the JSP file, follow these steps:

  - Copy the JSP file to a directory under the web application root of the web container. For example, if you are using Tomcat, you can copy the JSP file to the `webapps/ROOT` directory.
  - Start the web container and make sure it is listening on a port, such as 8080.
  - Open the web browser and enter the URL of the JSP file, such as `http://localhost:8080/simple.jsp`.
  - The web browser will send a GET request to the web container, which will compile the JSP file into a servlet class and execute it.
  - The servlet class will generate the HTML output and send it back to the web browser, which will display the web page.
  - The web page will show the current date and time, as well as the title and the heading of the JSP file.

#### Output of the JSP File

- The output of the JSP file may look something like this:

![JSP output](https://i.imgur.com/3qZy0xH.png)

- The output may vary depending on the date and time of the request, the web container, and the web browser.