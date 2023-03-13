#### Directives in Servlets

- Directives are special instructions that provide commands or directions to the servlet container on how to deal with and manage certain JSP processing portions .
- Directives affect the overall structure of the servlet class that results from the JSP page.
- Directives usually have the following form: `<%@ directive attribute = "value" %>`.
- There are three types of directives supported by JSP: page, include and taglib.
- The page directive defines attributes that apply to an entire JSP page, such as the language, content type, error page, buffer size, etc.
- The include directive is used to include a file during the translation phase of the JSP page, such as a header, footer, or common code.
- The taglib directive is used to declare a custom tag library that can be used in the JSP page, such as JSTL.
- A mnemonic to remember the three types of directives is PIT: Page, Include, Taglib.
- An example of using directives in a JSP page is:

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html>
<head>
<title>Example of Directives</title>
</head>
<body>
<h1>Example of Directives</h1>
<c:out value="${message}"/>
</body>
</html>
<%@ include file="footer.jsp" %>
```