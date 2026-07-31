 Here is the content in markdown format with formal tone and without any emojis or external links:

#### Directives in Servlets

- `<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>` - This directive specifies the scripting language of the servlet, content type and the encoding format. It is the first line of any servlet and contains all the metadata about the servlet.
- `<%@ include file="common.jsp"%>` - This is an include directive which includes the content of the specified file (common.jsp in this case) at the location of the directive. This is useful to avoid repetition and promote reuse of code.
- `<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>` - This is a taglib directive which declares a tag library with a given URI and prefix. The prefix is then used to use the tags from the library in the JSP page.

The directives are processed by the JSP engine even before the servlet is compiled. They provide important information to the JSP engine to process the page. The directives start with `<%@` and end with `%>`.