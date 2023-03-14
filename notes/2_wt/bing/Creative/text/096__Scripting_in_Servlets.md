#### Scripting in Servlets

- Scripting in servlets refers to the use of Java code embedded in HTML or XML documents to generate dynamic content for web applications.
- Scripting in servlets can be done using three elements: scriptlets, expressions, and declarations.
- Scriptlets are blocks of Java code that are executed when the servlet is invoked. They are enclosed by `<%` and `%>` tags. Scriptlets can access servlet parameters, attributes, and methods, as well as create and manipulate local variables. Scriptlets can also use control structures, such as loops and conditionals, to control the flow of the servlet.
- Expressions are snippets of Java code that are evaluated and inserted into the output stream. They are enclosed by `<%=` and `%>` tags. Expressions can access servlet parameters, attributes, and methods, as well as use operators and functions. Expressions cannot use control structures, such as loops and conditionals, or declare variables. Expressions are equivalent to calling `out.print()` with the expression as the argument.
- Declarations are statements that declare variables or methods that are accessible throughout the servlet. They are enclosed by `<%!` and `%>` tags. Declarations can use any valid Java syntax, such as modifiers, data types, and initializers. Declarations are equivalent to placing the statements outside the service method of the servlet.

- An example of scripting in servlets is:

```html
<html>
<head>
<title>Scripting Example</title>
</head>
<body>
<% // scriptlet
  int x = 10;
  int y = 20;
  int sum = x + y;
%>
<h1>Scripting Example</h1>
<p>The sum of <%= x %> and <%= y %> is <%= sum %>.</p> <!-- expressions -->
<% // scriptlet
  if (sum > 20) {
    out.println("<p>The sum is greater than 20.</p>");
  } else {
    out.println("<p>The sum is less than or equal to 20.</p>");
  }
%>
<%! // declaration
  public void printHello() {
    out.println("<p>Hello from a declared method.</p>");
  }
%>
<% // scriptlet
  printHello();
%>
</body>
</html>
```