### Java Server Pages (JSP) in Servlets

Java Server Pages (JSP) is a technology that helps software developers create dynamically generated web pages based on HTML, XML, or other document types. JSP is similar to PHP and ASP, but it uses the Java programming language.

Here is an example of a simple JSP page that displays the current time:

```jsp
<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Current Time</title>
</head>
<body>
<%
    java.util.Date date = new java.util.Date();
    out.println("<h2>Current Time: " + date.toString() + "</h2>");
%>
</body>
</html>
```

This JSP page can be deployed in a servlet container such as Apache Tomcat or Jetty. When a user accesses the page, the JSP code is compiled into a servlet and executed. The resulting HTML is then sent to the user's web browser.
