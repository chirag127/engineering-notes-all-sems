### A First Java Server Page Example

- A Java Server Page (JSP) is a web page that contains Java code embedded in HTML or XML.
- The Java code is executed on the server side and the output is sent to the client as plain HTML or XML.
- JSPs are useful for creating dynamic web pages that can interact with databases, web services, and other server-side components.
- To create a JSP, you need to have a web server that supports JSP, such as Apache Tomcat, and a Java Development Kit (JDK) installed on your machine.
- A JSP file has the extension .jsp and can be placed in any directory under the web server's root directory.
- A JSP file consists of two types of elements: directives and scriptlets.
- Directives are instructions to the JSP engine that control how the JSP is processed. They start with <%@ and end with %> and are placed at the top of the JSP file. For example, the page directive sets the language, content type, and encoding of the JSP file.
- Scriptlets are blocks of Java code that are executed on the server side. They start with <% and end with %> and can be placed anywhere in the JSP file. For example, the out object is a predefined variable that can be used to write output to the client.
- A simple JSP example that displays the current date and time is shown below:

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" %>
<html>
<head>
<title>A First JSP Example</title>
</head>
<body>
<h1>A First JSP Example</h1>
<p>The current date and time is: <% out.println(new java.util.Date()); %></p>
</body>
</html>
```

- To run this JSP, you need to save it as a file named first.jsp in a directory under the web server's root directory, such as C:\Tomcat\webapps\examples\jsp.
- Then, you need to start the web server and open a web browser and enter the URL http://localhost:8080/examples/jsp/first.jsp.
- You should see a web page that looks like this:

![A First JSP Example](https://i.imgur.com/0fQ0f7v.png)

- This is how the JSP engine processes the JSP file:

  - It reads the page directive and sets the language, content type, and encoding of the JSP file.
  - It converts the JSP file into a Java servlet class and compiles it into a bytecode file.
  - It executes the servlet class and invokes the out.println(new java.util.Date()) method to write the current date and time to the output stream.
  - It sends the output stream as plain HTML to the client.