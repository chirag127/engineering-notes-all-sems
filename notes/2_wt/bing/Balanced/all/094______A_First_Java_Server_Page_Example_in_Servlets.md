#### A First Java Server Page Example in Servlets

- A Java Server Page (JSP) is a web page that contains small snippets of Java code that are executed on the server side and generate dynamic HTML content for the client side.
- A JSP can be used to display the current date, perform calculations, access databases, or any other server-side logic that can be done by a Java servlet .
- A JSP is compiled into a Java servlet by the web container (such as Tomcat) the first time it is requested, and then the servlet is executed to produce the response.
- A JSP can use special tags (<% and %>) to enclose Java code, or use JSP elements (such as directives, declarations, expressions, scriptlets, and actions) to control the structure and behavior of the page.
- A JSP can also use custom tags or JavaBeans components to reuse existing functionality or encapsulate complex logic.

Here is a simple example of a JSP that displays the current date and time:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>A Simple JSP Example</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>The current date and time is: <%= new java.util.Date() %></p>
</body>
</html>
```

- The first line is a directive that specifies the content type, character encoding, and scripting language of the page.
- The HTML tags are used to define the structure and style of the page, as in any normal HTML page.
- The <%= %> tag is an expression that evaluates the Java code inside it and inserts the result into the output stream.
- The new java.util.Date() expression creates a Date object that represents the current date and time, and invokes its toString() method to display it in a human-readable format.

To run this JSP, we need to:

- Install Java, Eclipse, and Tomcat on our system.
- Create a dynamic web project in Eclipse using File -> New -> Dynamic Web Project.
- Name the project as JSPExample and select the target runtime as Apache Tomcat.
- Create a new JSP file in the WebContent folder of the project using File -> New -> JSP File.
- Name the file as index.jsp and copy the above code into it.
- Run the project on the server using Run -> Run on Server.
- Open a web browser and enter the URL http://localhost:8080/JSPExample/index.jsp.

We should see the following output in the browser:

![JSP output](https://www.baeldung.com/wp-content/uploads/2017/09/jsp-output.png)

- The output shows the current date and time on the server, which may differ from the client's date and time.
- The output may also change every time we refresh the page, as the JSP is executed again and generates a new Date object.

This is a simple example of how a JSP can be used to create dynamic web pages using Java code and HTML tags. There are many more features and possibilities that JSP offers, such as:

- Using JSP directives to include other files, set error pages, or define tag libraries.
- Using JSP declarations to declare variables or methods that can be used in the page.
- Using JSP scriptlets to write Java code that can perform any logic or computation.
- Using JSP actions to invoke other JSPs, servlets, or JavaBeans components.
- Using JSP expressions to evaluate Java expressions and insert the results into the output.
- Using JSP comments to write notes or remarks that are ignored by the JSP compiler.
- Using custom tags or JavaBeans components to reuse existing functionality or encapsulate complex logic.

A mnemonic to remember the JSP elements is:

**D**irectives, **D**eclarations, **S**criptlets, **A**ctions, **E**xpressions, **C**omments

**DDSAEC** or **D**o **D**o **S**ome **A**wesome **E**xercises **C**arefully