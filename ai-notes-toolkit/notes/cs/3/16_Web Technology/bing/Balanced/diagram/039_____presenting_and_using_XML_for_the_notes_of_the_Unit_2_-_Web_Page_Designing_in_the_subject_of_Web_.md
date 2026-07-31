### Presenting and using XML for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

- XML stands for eXtensible Markup Language   .
- XML is a markup language similar to HTML, but without predefined tags to use.
- Instead, you define your own tags designed specifically for your needs.
- This is a powerful way to store data in a format that can be stored, searched, and shared .
- XML also makes it easier to expand or upgrade to new operating systems, new applications, or new browsers, without losing data.
- XML was designed to be both human- and machine-readable .
- For an XML document to be correct, the following conditions must be fulfilled:
  - Document must be well-formed.
  - Document must conform to all XML syntax rules.
  - Document must conform to semantic rules, which are usually set in an XML schema or a DTD (Document Type Definition).
- An example of a simple XML document is :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
```

- The first line is the XML declaration, which specifies the XML version, the encoding, and the stand-alone attribute .
- The second line is the root element, which contains all other elements .
- The next four lines are child elements, which contain the data of the document .
- Each element has a start tag and an end tag, which must match in case and spelling .
- The elements can have attributes, which provide additional information about the element .
- The elements can also have text content, which is the data between the start and end tags .
- The elements can be nested, which means that one element can contain another element as its child .
- The order of the elements is significant, which means that changing the order can change the meaning of the document .
- XML documents can be validated against an XML schema or a DTD, which define the structure and the rules of the document .
- XML documents can be processed by various applications, such as browsers, editors, parsers, validators, transformers, etc .
- XML documents can be displayed using various methods, such as CSS, XSLT, XQuery, etc .
- XML documents can be used for various purposes, such as data exchange, configuration, metadata, web services, etc .