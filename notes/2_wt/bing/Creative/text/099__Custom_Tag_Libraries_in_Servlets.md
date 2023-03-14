#### Custom Tag Libraries in Servlets

- Custom tag libraries are a way to create reusable components that can be used in JSP pages.
- Custom tag libraries consist of two parts: a tag handler class that implements the logic of the tag, and a tag library descriptor (TLD) file that defines the attributes and usage of the tag.
- Custom tag libraries can be used to encapsulate complex functionality, simplify JSP syntax, or provide a consistent look and feel for a web application.
- Custom tag libraries can be created by implementing one of the interfaces from the javax.servlet.jsp.tagext package: SimpleTag, Tag, BodyTag, or IterationTag. Alternatively, one can extend one of the convenience classes from the same package: SimpleTagSupport, TagSupport, BodyTagSupport, or IterationTagSupport.
- Custom tag libraries can be used in JSP pages by declaring the taglib directive with the URI of the TLD file, and then using the prefix and name of the tag as defined in the TLD file. For example:

```jsp
<%@ taglib uri="http://test.com/test.tld" prefix="my" %>
<my:form action="submit.jsp" focus="name">
  <my:input type="text" name="name" label="Name"/>
  <my:input type="password" name="password" label="Password"/>
  <my:submit value="Login"/>
</my:form>
```

- Custom tag libraries can be distributed as JAR files that contain the tag handler classes and the TLD files. The JAR files can be placed in the WEB-INF/lib directory of the web application, or in a shared library directory of the servlet container. The URI of the TLD file can be mapped to the location of the JAR file in the web.xml file of the web application. For example:

```xml
<taglib>
  <taglib-uri>http://test.com/test.tld</taglib-uri>
  <taglib-location>/WEB-INF/lib/my-lib.jar</taglib-location>
</taglib>
```