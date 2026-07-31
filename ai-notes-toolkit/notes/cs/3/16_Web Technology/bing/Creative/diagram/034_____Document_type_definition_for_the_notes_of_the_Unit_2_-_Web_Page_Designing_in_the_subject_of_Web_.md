### Document type definition for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

- A document type definition (DTD) is a set of rules that defines the structure and the legal elements and attributes of an XML document .
- A DTD can be declared inside an XML document as an internal DTD, or as an external reference in a separate file .
- A DTD helps to ensure the validity and interoperability of XML documents by specifying the allowed syntax and semantics of the markup language .
- A DTD can also be used to declare entities, notations, and processing instructions that can be referenced in the XML document .
- A DTD is not an XML document itself, but a plain text file that follows a specific syntax .
- A DTD can be written in two forms: SGML DTD or XML DTD. The latter is more commonly used and has some restrictions compared to the former .
- A DTD starts with a document type declaration that identifies the root element of the XML document and the location of the DTD (if external) .
- A DTD consists of element declarations, attribute declarations, entity declarations, notation declarations, and comments .
- An element declaration defines the name and the content model of an element, which specifies the possible child elements and their order and occurrence .
- An attribute declaration defines the name, the type, and the default value of an attribute for a given element .
- An entity declaration defines a named replacement text that can be used in the XML document to avoid repetition or to include external content .
- A notation declaration defines a name and an identifier for a non-XML data format that can be referenced by an entity or an attribute .
- A comment is a text that is ignored by the XML parser and can be used to add notes or explanations to the DTD .
- A DTD can be validated by using a DTD validator tool or by using an XML parser that supports DTD validation .

Here is an example of an XML document with an internal DTD:

```xml
<?xml version="1.0"?>
<!DOCTYPE note [
  <!ELEMENT note (to,from,heading,body)>
  <!ELEMENT to (#PCDATA)>
  <!ELEMENT from (#PCDATA)>
  <!ELEMENT heading (#PCDATA)>
  <!ELEMENT body (#PCDATA)>
]>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
```

Here is an example of an XML document with an external DTD:

```xml
<?xml version="1.0"?>
<!DOCTYPE note SYSTEM "note.dtd">
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
```

And here is the content of the note.dtd file:

```xml
<!ELEMENT note (to,from,heading,body)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT body (#PCDATA)>
```