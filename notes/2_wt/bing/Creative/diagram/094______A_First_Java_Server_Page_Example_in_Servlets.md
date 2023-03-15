Hello, I am Sydney, your AI assistant. I can help you with your query. A Java Server Page (JSP) is a web page that contains small snippets of Java code that are executed on the server side by a Java servlet . A servlet is a Java class that extends the functionality of a web server and handles requests and responses from clients . A simple example of a JSP that displays the current date is shown below:

```jsp
<html>
<head>
<title>Current Date</title>
</head>
<body>
<h1>The current date is:</h1>
<%= new java.util.Date() %>
</body>
</html>
```

The diagram below shows how a JSP works in servlets:

```
+--------+        +----------+        +---------+        +---------+
| Client | <----> | Web      | <----> | Servlet | <----> | JSP     |
|        |        | Server   |        | Engine  |        | Engine  |
|        |        | (Tomcat) |        |         |        |         |
+--------+        +----------+        +---------+        +---------+
```

The client sends a request to the web server, which forwards it to the servlet engine. The servlet engine invokes the appropriate servlet based on the request URL. The servlet then calls the JSP engine to process the JSP file and generate the HTML output. The servlet engine sends the response back to the web server, which delivers it to the client. This way, the JSP can dynamically generate the web page content based on the server-side logic and data  .