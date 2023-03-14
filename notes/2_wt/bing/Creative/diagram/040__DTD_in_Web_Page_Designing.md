A DTD (Document Type Definition) is a set of rules that defines the structure and the legal elements and attributes of an XML document. A DTD can be declared inside the XML document or in an external file. A DTD helps to ensure that the XML document is well-formed and valid, and that it can be parsed the same way by different web browsers.

### DTD in Web Page Designing

A web page can use a DTD to specify the version of HTML that it is written in. The DOCTYPE declaration is an instruction to the web browser that contains a reference to the DTD. For example, the following DOCTYPE declaration indicates that the web page is using HTML 4.01 Transitional:

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
```

The DOCTYPE declaration must be the first line of the web page, before the `<html>` tag. The DOCTYPE declaration can refer to different types of DTDs, such as Strict, Transitional, or Frameset, depending on the features and elements that the web page uses.

The following diagram illustrates the basic architecture of a DTD in web page designing:

```
+----------------+      +-----------------+
|                |      |                 |
|  Web Browser   |      |  Web Server     |
|                |      |                 |
+----------------+      +-----------------+
       |                       |
       |                       |
       |  Request web page     |
       |---------------------->|
       |                       |
       |                       |
       |  Send web page        |
       |<----------------------|
       |                       |
       |                       |
       |  Parse DOCTYPE        |
       |  declaration          |
       |                       |
       |                       |
       |  Request DTD file     |
       |---------------------->|
       |                       |
       |                       |
       |  Send DTD file        |
       |<----------------------|
       |                       |
       |                       |
       |  Validate XML         |
       |  document against     |
       |  DTD                  |
       |                       |
       |                       |
       |  Display web page     |
       |                       |
       |                       |
       V                       V
```