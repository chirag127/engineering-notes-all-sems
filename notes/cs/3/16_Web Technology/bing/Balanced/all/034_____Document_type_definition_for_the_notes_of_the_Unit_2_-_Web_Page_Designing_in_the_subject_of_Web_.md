# Document type definition for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

- A document type definition (DTD) is a set of rules that defines the structure and the legal elements and attributes of an XML document.
- A DTD can be declared inside an XML document as an internal DTD or as an external reference to a DTD file.
- A DTD helps to ensure the validity and interoperability of XML documents by specifying the allowed syntax and semantics of the markup language.
- A DTD can also be used to declare entities, notations, and processing instructions that can be referenced in the XML document.
- A DTD can be written in two syntaxes: SGML or XML. The XML syntax is more concise and compatible with XML parsers.
- A DTD starts with the keyword `<!DOCTYPE` followed by the name of the root element of the XML document and the reference to the DTD source.
- An example of an internal DTD declaration for a simple XML document is:

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
  <to>John</to>
  <from>Jane</from>
  <heading>Reminder</heading>
  <body>Don't forget the meeting tomorrow.</body>
</note>
```

- An example of an external DTD declaration for the same XML document is:

```xml
<?xml version="1.0"?>
<!DOCTYPE note SYSTEM "note.dtd">
<note>
  <to>John</to>
  <from>Jane</from>
  <heading>Reminder</heading>
  <body>Don't forget the meeting tomorrow.</body>
</note>
```

- The external DTD file `note.dtd` contains the same rules as the internal DTD:

```xml
<!ELEMENT note (to,from,heading,body)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT body (#PCDATA)>
```

- A DTD can also use the keyword `PUBLIC` instead of `SYSTEM` to refer to a public DTD that is registered in a catalog and can be accessed by a URI.
- A DTD can also include parameter entities, general entities, notations, and processing instructions that can be used to simplify the DTD syntax or to include external data in the XML document.
- A parameter entity is a named fragment of DTD syntax that can be referenced by a `%` sign in the DTD. For example:

```xml
<!ENTITY % name "(#PCDATA)">
<!ELEMENT to %name;>
<!ELEMENT from %name;>
```

- A general entity is a named fragment of XML syntax that can be referenced by a `&` sign in the XML document. For example:

```xml
<!ENTITY company "GeeksforGeeks">
<note>
  <to>John</to>
  <from>&company;</from>
  <heading>Reminder</heading>
  <body>Don't forget the meeting tomorrow.</body>
</note>
```

- A notation is a way to identify the format or encoding of external data that is referenced by an entity or an attribute. For example:

```xml
<!NOTATION gif SYSTEM "image/gif">
<!ENTITY logo SYSTEM "logo.gif" NDATA gif>
<note>
  <to>John</to>
  <from>Jane</from>
  <heading>Reminder</heading>
  <body>Don't forget the meeting tomorrow.</body>
  <logo>&logo;</logo>
</note>
```

- A processing instruction is a way to provide instructions to the XML processor or application that handles the XML document. For example:

```xml
<?xml-stylesheet type="text/css" href="style.css"?>
<note>
  <to>John</to>
  <from>Jane</from>
  <heading>Reminder</heading>
  <body>Don't forget the meeting tomorrow.</body>
</note>
```

- A DTD can also define the attributes of the elements, their types, and their default values. For example:

```xml
<!ELEMENT note (to,from,