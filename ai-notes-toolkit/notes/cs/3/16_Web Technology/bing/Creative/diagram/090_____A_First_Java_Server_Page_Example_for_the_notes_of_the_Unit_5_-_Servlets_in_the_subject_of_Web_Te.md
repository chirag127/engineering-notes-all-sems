### A First Java Server Page Example

A Java Server Page (JSP) is a web page that contains small snippets of Java code that are executed on the server side. JSPs are similar to Servlets, but they are easier to create and maintain. JSPs can also use HTML tags and special JSP tags to generate dynamic web content.

To create a JSP, you need to have a web server that supports JSP, such as Apache Tomcat, and a text editor. You can also use an IDE, such as Eclipse, that has JSP support.

A JSP file has the extension `.jsp` and consists of two parts: a directive and a body. The directive is a special tag that starts with `<%@` and ends with `%>`. It provides information to the web server, such as the page language, the content type, and the import statements. The body is the main part of the JSP, where you can write HTML, Java, and JSP tags.

A simple JSP example that displays the current date is shown below:

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" %>
<html>
<head>
<title>A Simple JSP Example</title>
</head>
<body>
<h1>A Simple JSP Example</h1>
<p>The current date is: <%= new java.util.Date() %></p>
</body>
</html>
```

The directive in this example specifies that the page language is Java and the content type is HTML with UTF-8 encoding. The body contains HTML tags for the page title, header, and paragraph. The Java code that generates the current date is enclosed in `<%=` and `%>` tags, which are called expression tags. Expression tags are used to insert the result of a Java expression into the output.

To run this JSP, you need to save it in the webapps folder of your web server, for example, `C:\Tomcat\webapps\example\date.jsp`. Then, you can access it from your browser by typing the URL `http://localhost:8080/example/date.jsp`, assuming that your web server is running on port 8080. You should see something like this:

![A Simple JSP Example](https://www.ibm.com/docs/en/zvse/6.2?topic=fa2ws_eg_simple_java_server_page.html)

Some benefits of using JSP are:

- You can separate the presentation logic (HTML) from the business logic (Java) in your web application.
- You can reuse Java components, such as beans, servlets, and tag libraries, in your JSPs.
- You can use JSP implicit objects, such as request, response, session, and out, to access the web server and the client information.
- You can use JSP standard actions, such as `<jsp:include>`, `<jsp:forward>`, and `<jsp:useBean>`, to perform common tasks in your web application.
- You can use JSP custom tags, such as `<c:out>`, `<c:if>`, and `<c:forEach>`, to simplify your JSP code and enhance its functionality.