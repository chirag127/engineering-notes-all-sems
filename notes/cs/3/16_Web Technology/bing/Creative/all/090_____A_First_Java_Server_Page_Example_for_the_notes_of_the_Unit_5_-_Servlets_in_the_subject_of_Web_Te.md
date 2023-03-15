# A First Java Server Page Example

- A Java Server Page (JSP) is a web page that contains Java code embedded in HTML or XML.
- The Java code is executed on the server side and the output is sent to the client as plain HTML or XML.
- JSPs are useful for creating dynamic web pages that can interact with databases, web services, or other server-side components.
- To create a JSP, we need to use a special file extension (.jsp) and follow some syntax rules for embedding Java code in HTML or XML.
- A JSP file consists of two types of elements: directives and scriptlets.
- Directives are instructions to the JSP engine that control how the JSP is processed and compiled. They start with <%@ and end with %> and are placed at the top of the JSP file.
- Scriptlets are blocks of Java code that are executed on the server side and can access any Java object or method. They start with <% and end with %> and can be placed anywhere in the JSP file.
- A simple JSP example that displays the current date and time is shown below:

```html
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>A First JSP Example</title>
</head>
<body>
    <h1>A First JSP Example</h1>
    <p>The current date and time is: <%= new java.util.Date() %></p>
</body>
</html>
```

- The first line is a directive that specifies the content type, character encoding, and language of the JSP file.
- The second line is a standard HTML tag that starts the HTML document.
- The third line is a standard HTML tag that defines the title of the web page.
- The fourth line is a standard HTML tag that starts the body of the web page.
- The fifth line is a standard HTML tag that defines a heading with the text "A First JSP Example".
- The sixth line is a standard HTML tag that defines a paragraph with the text "The current date and time is: ".
- The seventh line is a scriptlet that embeds a Java expression that creates a new Date object and displays its value using the default toString() method. The expression is enclosed in <%= and %> to indicate that the output of the expression should be inserted in the HTML output.
- The eighth line is a standard HTML tag that ends the body of the web page.
- The ninth line is a standard HTML tag that ends the HTML document.

- To run this JSP, we need to save it in a web server that supports JSP, such as Apache Tomcat, and access it using a web browser with the URL http://localhost:8080/first.jsp (assuming that the JSP file is named first.jsp and is located in the webapps/ROOT directory of the Tomcat server).
- The web browser will display the web page with the current date and time, as shown below:

![A First JSP Example](https://i.imgur.com/8QZ0w0Q.png)

- This is how a JSP works:

  - The web browser sends a request to the web server for the JSP file.
  - The web server receives the request and forwards it to the JSP engine, which is a component of the web server that handles JSP files.
  - The JSP engine checks if the JSP file has been compiled into a Java servlet, which is a Java class that implements the javax.servlet.Servlet interface and can handle HTTP requests and responses.
  - If the JSP file has not been compiled, the JSP engine compiles it into a Java servlet and stores it in a cache for future use.
  - The JSP engine invokes the Java servlet, which executes the Java code in the JSP file and generates the HTML output.
  - The JSP engine sends the HTML output back to the web server, which sends it to the web browser.
  - The web browser receives the HTML output and displays it to the user.