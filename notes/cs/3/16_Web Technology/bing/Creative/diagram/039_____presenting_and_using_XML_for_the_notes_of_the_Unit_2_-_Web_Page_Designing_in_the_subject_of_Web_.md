# Presenting and using XML for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

## What is XML?

- XML stands for **eXtensible Markup Language**    .
- It is a markup language similar to HTML, but without predefined tags to use.
- Instead, you define your own tags designed specifically for your needs.
- This is a powerful way to store data in a format that can be stored, searched, and shared .

## Why use XML?

- XML stores data in plain text format.
- This provides a software- and hardware-independent way of storing, transporting, and sharing data.
- XML also makes it easier to expand or upgrade to new operating systems, new applications, or new browsers, without losing data.
- XML was designed to be both human- and machine-readable .

## How to write XML?

- An XML document consists of elements, attributes, comments, and processing instructions.
- An element is defined by a start tag and an end tag, with some content in between  .
- An attribute is a name-value pair that provides additional information about an element.
- A comment is a text that is ignored by the XML parser.
- A processing instruction is a special instruction for the XML processor.
- An XML document must be well-formed, meaning that it must conform to all XML syntax rules .
- An XML document can also be valid, meaning that it must conform to semantic rules, which are usually set in an XML schema or a DTD (Document Type Definition) .

## XML Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- This is a comment -->
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
```

- The first line is the XML declaration, which specifies the XML version, the encoding, and the standalone attribute  .
- The second line is a comment, which starts with `<!--` and ends with `-->`  .
- The third line is the root element, which is `<note>`  .
- The fourth to seventh lines are child elements, which are `<to>`, `<from>`, `<heading>`, and `<body>`  .
- The eighth line is the end tag of the root element, which is `</note>`  .
- The content of each element is the text between the start tag and the end tag  .
- The elements are nested, meaning that each element can contain other elements  .
- The elements are case-sensitive, meaning that `<note>` and `<Note>` are different  .
- The elements must be properly closed, meaning that each start tag must have a corresponding end tag  .
- The elements must be properly nested, meaning that no element can overlap another element  .

## References

: XML introduction - XML: Extensible Markup Language | MDN - Mozilla
: XML Basics1 1 Introducing XML - City University of New York
: XML Introduction - W3Schools
: XML Tutorial - W3Schools
: XML Tutorial - W3Schools