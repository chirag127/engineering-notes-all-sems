#### Custom Tag Libraries in Servlets

Custom tag libraries are user-defined tag libraries that can provide reusable functionality and custom behavior in JSP pages. They are defined in a tag library descriptor (.tld) file that specifies the tag names, attributes, and tag classes. A tag class is a Java class that implements the javax.servlet.jsp.tagext.Tag interface or extends one of its subclasses. To use a custom tag library from a JSP page, you need to reference its tag library descriptor with a <%@ taglib %> directive and use the tag prefix and name in the JSP page.

For example, suppose you have a custom tag library called my-lib that provides a tag called hello that prints a greeting message. The tag library descriptor file, my-lib.tld, could look something like this:

```xml
<taglib>
  <tlib-version>1.0</tlib-version>
  <jsp-version>2.0</jsp-version>
  <short-name>my-lib</short-name>
  <uri>http://example.com/my-lib</uri>
  <tag>
    <name>hello</name>
    <tag-class>com.example.HelloTag</tag-class>
    <body-content>empty</body-content>
    <attribute>
      <name>name</name>
      <required>true</required>
      <rtexprvalue>true</rtexprvalue>
    </attribute>
  </tag>
</taglib>
```

The tag class, com.example.HelloTag, could look something like this:

```java
package com.example;

import javax.servlet.jsp.JspException;
import javax.servlet.jsp.JspWriter;
import javax.servlet.jsp.tagext.TagSupport;

public class HelloTag extends TagSupport {

  private String name;

  public void setName(String name) {
    this.name = name;
  }

  public int doStartTag() throws JspException {
    try {
      JspWriter out = pageContext.getOut();
      out.print("Hello, " + name + "!");
    } catch (Exception e) {
      throw new JspException(e);
    }
    return SKIP_BODY;
  }
}
```

To use the hello tag from a JSP page, you need to include the following directive:

```jsp
<%@ taglib uri="http://example.com/my-lib" prefix="my" %>
```

And then you can use the tag like this:

```jsp
<my:hello name="John" />
```

This will print "Hello, John!" in the output. You can also use a JSP expression as the value of the name attribute, such as:

```jsp
<my:hello name="<%= request.getParameter("name") %>" />
```

This will print "Hello, [name]!" where [name] is the value of the name parameter in the request.