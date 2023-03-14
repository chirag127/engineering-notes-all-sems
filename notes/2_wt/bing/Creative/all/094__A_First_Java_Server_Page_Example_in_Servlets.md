#### A First Java Server Page Example in Servlets

- A Java Server Page (JSP) is a web page that contains small snippets of Java code embedded within HTML tags.
- A JSP can be used to generate dynamic content based on user requests, server logic, or database queries.
- A JSP is processed by a web server that has a JSP engine or a servlet container, such as Apache Tomcat, Jetty, or GlassFish.
- A JSP engine or a servlet container translates the JSP into a Java servlet, which is a Java class that implements the javax.servlet.Servlet interface.
- A servlet is a Java program that runs on the web server and handles HTTP requests and responses.
- A servlet can access various implicit objects that are created by the JSP engine or the servlet container, such as request, response, session, application, out, etc.
- A servlet can also use various directives, such as page, include, or taglib, to control the behavior and structure of the JSP.
- A simple JSP example that displays the current date and a random greeting is shown below:

```html
<html>
<head>
<title>Very Simple JSP Example</title>
</head>
<body bgcolor="white">
<h1>Very Basic JSP</h1>
Current time: <%= new java.util.Date () %>
<br><br>
Reload this page to watch the greeting change.
<br><br><b>
<!-- including lines of Java code in an HTML page -->
<%
int um = (int) ( Math.random () * 5 );
switch ( um )
{
case 0: out.println ("Welcome"); break;
case 1: out.println ("Bienvenidos"); break;
case 2: out.println ("Bienvenue"); break;
case 3: out.println ("Bienvenuti"); break;
case 4: out.println ("Willkommen"); break;
default: out.println ("Huh? " + um);
}
out.println ("<br>");
%>
</b>
</body>
</html>
```

- The JSP expression tag `<%= %>` is used to insert the value of a Java expression into the HTML output.
- The JSP scriptlet tag `<% %>` is used to execute a block of Java code within the JSP.
- The out object is an instance of javax.servlet.jsp.JspWriter that is used to write the HTML output to the response stream.
- The Math.random() method returns a double value between 0.0 and 1.0, which is multiplied by 5 and cast to an int to generate a random number between 0 and 4.
- The switch statement is used to print a different greeting based on the random number.
- The JSP comment tag `<!-- -->` is used to add a comment that is not visible in the HTML output.

- Some possible mnemonics and learning tricks for this JSP example are:

  - JSP stands for Java Server Page, which is a web page with Java code.
  - JSP is translated to servlet, which is a Java program that handles HTTP requests and responses.
  - JSP has implicit objects, such as request, response, session, application, out, etc., that are created by the JSP engine or the servlet container.
  - JSP has directives, such as page, include, or taglib, that control the behavior and structure of the JSP.
  - JSP has tags, such as `<%= %>`, `<% %>`, or `<!-- -->`, that insert Java expressions, execute Java code, or add comments to the JSP.