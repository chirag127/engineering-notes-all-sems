### A First Java Server Page Example

- JavaServer Pages (JSP) is a technology that allows web developers to create dynamic web pages using Java code embedded in HTML or XML documents.
- JSP files are compiled into servlets by the web container and executed on the server side.
- JSP files have the extension `.jsp` and can contain HTML tags, JSP directives, JSP scriptlets, JSP expressions, JSP declarations, and JSP actions.
- A simple JSP example that displays the current date is shown below:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>A First JSP Example</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>The current date and time is: <%= new java.util.Date() %></p>
</body>
</html>
```

- The first line of the JSP file is a page directive that specifies the content type, the language, and other attributes of the page.
- The `<%= %>` syntax is a JSP expression that evaluates the Java code inside and inserts the result into the output stream.
- The rest of the file is plain HTML that defines the structure and appearance of the web page.
- To run this JSP file, it needs to be placed in the web application directory of the web container and accessed through a URL that maps to the file name. For example, if the file is named `first.jsp` and located in the `WEB-INF` folder of the web application, the URL could be `http://localhost:8080/WEB-INF/first.jsp`.
- The web container will compile the JSP file into a servlet class and execute it on the server side. The servlet will generate the HTML output and send it back to the browser. The browser will render the web page and display the current date and time.