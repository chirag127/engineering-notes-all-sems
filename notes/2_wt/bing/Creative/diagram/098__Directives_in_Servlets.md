Directives in Servlets are instructions that tell the container how to handle certain aspects of the JSP processing. They affect the overall structure of the servlet class that is generated from the JSP page. There are three types of directives in Servlets:

- Page directive: It defines page-dependent attributes, such as scripting language, error page, and buffering requirements. It has the syntax: <%@ page attribute = "value" %>
- Include directive: It includes a file during the translation phase. It has the syntax: <%@ include file = "relative url" %>
- Taglib directive: It declares a tag library, containing custom actions, used in the page. It has the syntax: <%@ taglib uri = "uri" prefix = "prefix" %>

The following diagram illustrates the basic architecture of a Servlet with directives:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  JSP Page       |    |  Servlet Class  |    |  HTML Page      |
|                 |    |                 |    |                 |
|  <%@ page ... %>|    |  extends        |    |                 |
|  <%@ include ...%>|  |  implements     |    |                 |
|  <%@ taglib ... %>|  |  methods        |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      ^
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      v                      |
       +----------------->+-----------------+<-----------------+
                         |                 |
                         |  Servlet Engine |
                         |                 |
                         +-----------------+
```