Custom tag libraries are a way of creating reusable components in JSP pages. They allow you to define custom actions that can be used in JSP pages, similar to HTML tags. Custom tag libraries are defined in a tag library descriptor (TLD) file, which specifies the name, attributes, and implementation class of each custom tag. Custom tag libraries can be used in JSP pages by declaring the taglib directive with the URI of the TLD file.

A possible ASCII diagram for custom tag libraries in servlets is:

```
+-----------------+    +-----------------+    +-----------------+
|  JSP Page       |    |  TLD File       |    |  Tag Handler    |
|                 |    |                 |    |  Class          |
|  <%@ taglib     |    |  <taglib>       |    |                 |
|  uri="my-lib.tld"%>  |    <tag>        |    |  public class   |
|                 |    |      <name>     |    |  MyTag extends  |
|  <my:tag        |    |        my:tag   |    |  TagSupport {   |
|  attr="value" /> |    |      </name>    |    |    // tag logic |
|                 |    |      <tag-class>|    |  }              |
+-----------------+    |        MyTag    |    +-----------------+
    |                 |      </tag-class>|
    |                 |    </tag>        |
    |                 |  </taglib>       |
    +-----------------+-----------------+
```