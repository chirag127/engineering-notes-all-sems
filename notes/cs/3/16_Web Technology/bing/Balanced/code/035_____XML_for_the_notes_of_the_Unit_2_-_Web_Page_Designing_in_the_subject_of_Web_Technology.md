# XML

XML stands for eXtensible Markup Language. It is a markup language used for storing and transporting data. It is derived from SGML (Standard Generalized Markup Language).

Some of the features and advantages of XML are:

- XML is plain text and human-readable.
- XML is software- and hardware-independent.
- XML can be used to create custom tags and structures.
- XML can be validated using DTD (Document Type Definition) or Schema.
- XML can be transformed and formatted using XSLT (eXtensible Stylesheet Language Transformations) and CSS (Cascading Style Sheets).
- XML can be queried and manipulated using XPath (XML Path Language) and XQuery (XML Query Language).
- XML can be used with AJAX (Asynchronous JavaScript and XML) to exchange data between web browsers and servers.

Some of the basic syntax rules of XML are:

- XML documents must have a root element that contains all other elements.
- XML elements must have a start tag and an end tag, or a self-closing tag.
- XML tags are case-sensitive and must match exactly.
- XML attributes must be quoted and have a name and a value.
- XML comments start with `<!--` and end with `-->`.
- XML prolog is optional and starts with `<?xml` and ends with `?>`.
- XML declaration specifies the version, encoding, and standalone attributes of the document.

An example of a simple XML document is:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>John</to>
  <from>Mary</from>
  <subject>Reminder</subject>
  <body>Don't forget to buy milk.</body>
</note>
```