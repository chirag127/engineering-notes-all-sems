 Here is the content in Markdown format without any emojis or external links:

### A First Java Server Page Example

- A Java Server Page (JSP) is a text-based document that contains two types of content: static data (which can be expressed in any text-based format such as HTML, XML, etc.) and JSP elements.
- JSP elements are used to insert Java code into the page. The Java code is executed on the server and its output is sent to the client as part of the response.
- A JSP is translated into a servlet. The translation occurs the first time the JSP is requested. The servlet is then reused to handle subsequent requests for the JSP.
- The advantages of using JSP are:
-- It separates the presentation of data from the Java code that processes the data.
-- It makes it easy to change the look and feel of a Web application.
-- It uses the familiar HTML-like format which makes it easy to learn and understand.

- Here is a simple JSP example:
<html>
<body>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<h2>Hello World!</h2>
<%
    java.util.Date today = new java.util.Date();
%>
<p>The time is: <%= today %></p>
</body>
</html>

- This JSP will output a web page that displays "Hello World!" and the current time.
- The JSP elements <%@ page ... %> and <% ... %> are used to embed Java code in the page.
- The <%= ... %> element is used to output the value that results from evaluating the expression inside it. In this case, it outputs the value of the today variable.