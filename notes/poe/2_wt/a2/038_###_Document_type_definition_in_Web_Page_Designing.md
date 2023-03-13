 Here is the content in markdown format for the topic ### Document type definition in Web Page Designing:

### Document type definition in Web Page Designing

A document type definition (DTD) is a set of markup declarations that define a document type for an SGML-family markup language (SGML, XML, HTML).

A DTD defines the structure and the legal elements and attributes of an XML or HTML document.

It defines the document structure with a list of legal elements and attributes.

A DTD can be declared inline inside an XML/HTML document, or as an external reference.

**Advantages of using a DTD:**

- It defines the structure of the document and makes it valid as per the rules.
- It ensures that the document has a consistent and standardized structure.
- It makes the document portable i.e. usable in other systems/applications as the structure is well-defined.

**Disadvantages of using a DTD:**

- It makes the document rigid as you have to adhere to the structure defined in DTD.
- The DTD code can make the document complex and difficult to understand for humans.

**Examples of DTD declarations:**

```xml
<!DOCTYPE note [
<!ELEMENT note (to,from,heading,body)>
<!ELEMENT to      (#PCDATA)>
<!ELEMENT from    (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT body    (#PCDATA)>
]>

<note>
<to>George</to>
<from>John</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>
```

**Mnemonics to remember:**

- Think DTD as rules for a document (like rules for a game).
- Opening `<!DOCTYPE>` declaration is like a referee blowing a whistle to start the game (document) as per the rules (DTD).
- Elements are like players and attributes are like players' accessories - all have rules to follow.

**When to use?**

- When you want standardized structure for your XML/HTML documents.
- When portability and validation are important.
- When you have a complex document structure with many elements and attributes.