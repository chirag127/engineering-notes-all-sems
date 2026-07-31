### A First Java Server Page Example

A Java Server Page (JSP) is a text document that contains two types of text: static data and JSP elements. Static data can be expressed in any text-based format, such as HTML, SVG, or XML. JSP elements are used to construct dynamic content and can be expressed using a variety of JSP tags and expressions.

Here is an example of a simple JSP page that generates a dynamic response:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title>A First JSP Example</title>
  </head>
  <body>
    <h1>A First JSP Example</h1>
    <p>The current time is: <%= new java.util.Date() %></p>
  </body>
</html>
```

This JSP page contains both static data (the HTML code) and a JSP element (the `<%= ... %>` expression). The JSP element is used to generate dynamic content by inserting the current date and time into the response.

When this JSP page is requested by a client, the web server will process the JSP elements and generate a dynamic response. The response will be an HTML page that contains the current date and time.

This is a simple example of how JSP can be used to generate dynamic content in a web application. JSP provides a powerful and flexible way to construct dynamic responses to client requests.