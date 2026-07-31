### A First Java Server Page Example

1. A Java Server Page (JSP) is a text document that contains two types of text: static data and JSP elements.
2. Static data can be expressed in any text-based format, such as HTML, SVG, or XML.
3. JSP elements are used to construct dynamic content and can be expressed using JSP tags, scriptlets, or expressions.
4. A JSP is compiled into a servlet by the web container, which is responsible for managing the lifecycle of the servlet and handling requests from clients.
5. The following is an example of a simple JSP that displays a message to the user:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title>My First JSP</title>
  </head>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>
```

6. The first line of the JSP is a page directive that specifies the content type, character encoding, and scripting language of the page.
7. The rest of the JSP is standard HTML, with the exception of the `<h1>` element, which contains a JSP expression that outputs the string "Hello, World!".
8. When the JSP is requested by a client, the web container compiles the JSP into a servlet and executes it.
9. The servlet generates the dynamic content of the page by evaluating the JSP expression and inserts it into the static content of the page.
10. The resulting HTML is sent back to the client and displayed by the web browser.