# XML

XML stands for **eXtensible Markup Language**. It is a markup language similar to HTML, but without predefined tags to use. Instead, you define your own tags designed specifically for your needs. This is a powerful way to store data in a format that can be stored, searched, and shared.

Some of the features and benefits of XML are:

- XML stores data in plain text format. This provides a software- and hardware-independent way of storing, transporting, and sharing data.
- XML also makes it easier to expand or upgrade to new operating systems, new applications, or new browsers, without losing data.
- XML was designed to be both human- and machine-readable. This means that you can easily read and understand the structure and content of an XML document.
- XML can be used to create common data formats and share them across different applications, platforms, and organizations. For example, XML can be used to exchange data between web services, databases, and mobile devices.
- XML can be validated against a set of rules, which are usually set in an XML schema or a DTD (Document Type Definition). This ensures that the XML document is well-formed and conforms to the expected structure and semantics .

An example of an XML document is:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
```

This XML document has the following components:

- An XML declaration that specifies the version, encoding, and standalone attributes of the document.
- A root element named `<note>` that contains all the other elements in the document.
- Four child elements named `<to>`, `<from>`, `<heading>`, and `<body>` that contain the data of the note.
- Each element has a start tag and an end tag that mark the beginning and the end of the element.
- The text between the start and end tags is called the element content.
- The elements are nested within each other according to the hierarchy of the document.

To learn more about XML, you can visit the following websites:

- [XML introduction - XML: Extensible Markup Language | MDN - Mozilla](https://developer.mozilla.org/en-US/docs/Web/XML/XML_introduction)
- [XML Tutorial - W3Schools](https://www.w3schools.com/xml/)
- [XML Basics1 1 Introducing XML - City University of New York](http://www.sci.brooklyn.cuny.edu/~jniu/teaching/csc31800/notes/0510-XML.pdf)