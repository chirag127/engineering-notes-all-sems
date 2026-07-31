### A First Java Server Page Example

Java Server Pages (JSP) is a technology that allows the creation of dynamic web pages using Java. JSPs can be thought of as HTML pages with Java code snippets embedded in them. In this section, we will discuss a first Java Server Page example.

Here are the steps to create a simple JSP example:

1. Create a new JSP file with the extension `.jsp`. For example, `hello.jsp`.
2. Open the file in a text editor and add the following code: 

```html
<!DOCTYPE html>
<html>
<head>
	<title>Hello JSP Example</title>
</head>
<body>
	<h1>Hello World!</h1>
	<p>The time on the server is <%= new java.util.Date() %></p>
</body>
</html>
```

3. Save the file and deploy it to a web server that supports JSPs.
4. Open a web browser and navigate to the URL of the JSP file. For example, `http://localhost:8080/hello.jsp`.

Let's break down the code:

- The `<!DOCTYPE html>` line specifies the document type as HTML5.
- The `<html>` and `<head>` tags define the structure of the HTML document and provide metadata about it.
- The `<title>` tag sets the title of the web page to "Hello JSP Example".
- The `<body>` tag contains the content of the web page.
- The `<h1>` tag displays the text "Hello World!" as a heading.
- The `<p>` tag displays the current date and time using Java code embedded in the JSP with the `<%= %>` syntax.

Note that the JSP code is executed on the server and the resulting HTML is sent to the client's web browser. This allows for dynamic web pages that can change based on user input or other factors.

In summary, this simple JSP example demonstrates the basic syntax and structure of a Java Server Page. With JSPs, it is possible to create dynamic web pages using Java code embedded in HTML.