### Writing program in XML for creation of DTD, which specifies set of rules for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A DTD (Document Type Declaration) is a way to describe the structure, elements and attributes of an XML document  .
- A DTD can be used to validate the XML document against the grammatical rules of the XML language .
- A DTD can be declared internally or externally to the XML document .
- An internal DTD is declared inside the XML document, within the `<!DOCTYPE>` tag.
- An external DTD is declared in a separate file, with the extension `.dtd`, and referenced by the XML document using the `SYSTEM` or `PUBLIC` keyword .
- A DTD defines the elements and attributes of an XML document using declarations .
- An element declaration specifies the name and content model of an element .
- An attribute declaration specifies the name, type and default value of an attribute .
- A DTD can also define entities, notations and comments .

Here is an example of an XML document with an internal DTD that specifies the rules for the notes of Unit 3:

```xml
<?xml version="1.0"?>
<!DOCTYPE notes [
  <!ELEMENT notes (unit+)>
  <!ELEMENT unit (title, content)>
  <!ELEMENT title (#PCDATA)>
  <!ELEMENT content (section+)>
  <!ELEMENT section (heading, paragraph+)>
  <!ELEMENT heading (#PCDATA)>
  <!ELEMENT paragraph (#PCDATA)>
  <!ATTLIST unit number CDATA #REQUIRED>
  <!ATTLIST section number CDATA #REQUIRED>
]>
<notes>
  <unit number="3">
    <title>Design dynamic web pages using Javascript and XML</title>
    <content>
      <section number="1">
        <heading>Introduction to Javascript</heading>
        <paragraph>Javascript is a scripting language that runs on the web browser.</paragraph>
        <paragraph>It can be used to create dynamic and interactive web pages.</paragraph>
      </section>
      <section number="2">
        <heading>Introduction to XML</heading>
        <paragraph>XML is a markup language that defines a set of rules for encoding data.</paragraph>
        <paragraph>It can be used to store and exchange data between different applications.</paragraph>
      </section>
    </content>
  </unit>
</notes>
```