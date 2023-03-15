 Here is the content in Markdown format without any emojis or external links, written in a formal tone with points:

#### A First Java Server Page Example in Servlets

1. A Java Server Page (JSP) is a text-based document that contains two types of elements: static elements and dynamic elements.
2. Static elements are the regular HTML tags and text that display static content to the user.
3. Dynamic elements are JSP tags such as <% %>, <%= %>, and <%! %> that are processed by the JSP engine to generate dynamic content.
4. A JSP is translated into a servlet by the JSP engine, compiled, and executed on the server to generate dynamic web pages.
5. The following is a basic JSP example that displays "Hello World":

<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<html>
<body>
    <h2>Hello World!</h2>
</body>
</html>

6. The JSP page begins with a page directive that specifies the scripting language as Java, and the character encoding. The remaining lines contain regular HTML that displays a heading.
7. When the JSP is translated into a servlet, the JSP engine inserts appropriate Java code that results in the text "Hello World!" being displayed in the web page.