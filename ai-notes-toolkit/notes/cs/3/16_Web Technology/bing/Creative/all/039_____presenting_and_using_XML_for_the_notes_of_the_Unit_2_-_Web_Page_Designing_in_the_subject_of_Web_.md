# Presenting and using XML for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

## What is XML?

- XML stands for **eXtensible Markup Language**    .
- XML is a markup language similar to HTML, but without predefined tags to use.
- XML allows you to define your own tags designed specifically for your needs.
- XML is a powerful way to store data in a format that can be stored, searched, and shared .

## Why use XML?

- XML stores data in plain text format, which provides a software- and hardware-independent way of storing, transporting, and sharing data.
- XML also makes it easier to expand or upgrade to new operating systems, new applications, or new browsers, without losing data.
- XML can be used to create common data formats and share them across different applications and platforms.
- XML can be used to describe the structure and semantics of data, which can improve the readability and interoperability of data.

## How to use XML?

- XML documents must follow some basic rules to be correct:
  - Document must be **well-formed**, which means it must follow the XML syntax rules.
  - Document must conform to **semantic rules**, which are usually set in an XML schema or a DTD (Document Type Definition).
- XML documents consist of **elements**, which are the basic units of information in XML .
- XML elements are defined by **tags**, which are enclosed in angle brackets (< and >) .
- XML tags have **names**, which are case-sensitive and must start with a letter or underscore .
- XML tags can have **attributes**, which are name-value pairs that provide additional information about the element .
- XML tags can have **content**, which can be text, other elements, or empty .
- XML elements must have a **closing tag**, which has the same name as the opening tag but starts with a slash (/) .
- XML elements can be **nested**, which means they can contain other elements as their content .
- XML documents must have a **root element**, which is the element that contains all other elements .
- XML documents can have an optional **XML declaration**, which specifies the XML version, encoding, and standalone status of the document .

## XML Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
```

- This is an example of a well-formed XML document .
- The XML declaration specifies the XML version, encoding, and standalone status of the document .
- The <note> element is the root element of the document .
- The <to>, <from>, <heading>, and <body> elements are child elements of the <note> element .
- The <to>, <from>, <heading>, and <body> elements have text content .
- The <note> element has a closing tag </note> at the end of the document .

## References

: XML introduction - XML: Extensible Markup Language | MDN - Mozilla
: XML Basics1 1 Introducing XML - City University of New York
: XML Introduction - W3Schools
: XML Tutorial - W3Schools
: XML Tutorial - W3Schools