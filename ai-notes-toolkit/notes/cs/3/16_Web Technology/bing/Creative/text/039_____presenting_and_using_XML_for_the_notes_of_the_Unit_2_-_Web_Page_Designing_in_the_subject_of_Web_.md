### Presenting and using XML for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

- XML stands for **eXtensible Markup Language**   .
- XML is a markup language similar to HTML, but without predefined tags to use.
- Instead, you define your own tags designed specifically for your needs.
- This is a powerful way to store data in a format that can be stored, searched, and shared .
- XML also makes it easier to expand or upgrade to new operating systems, new applications, or new browsers, without losing data.
- XML was designed to store and transport data .
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

- The XML document above consists of the following parts :
  - XML declaration: `<?xml version="1.0" encoding="UTF-8"?>`
  - Root element: `<note>`
  - Child elements: `<to>`, `<from>`, `<heading>`, and `<body>`
  - Element content: `Tove`, `Jani`, `Reminder`, and `Don't forget me this weekend!`
  - End tags: `</to>`, `</from>`, `</heading>`, and `</body>`
  - Closing root element: `</note>`
- XML documents can also have attributes, comments, processing instructions, and other components .
- XML documents can be validated against an XML schema or a DTD to ensure they follow the semantic rules.
- XML documents can be displayed on web pages using CSS or XSLT .
- XML documents can be manipulated and processed by various XML technologies, such as XPath, XQuery, XLink, XPointer, DOM, SAX, and others .
- XML documents can be exchanged and communicated between different systems and applications using web services, such as SOAP, REST, and WSDL .