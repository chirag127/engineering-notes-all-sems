### Writing program in XML for creation of DTD, which specifies set of rules for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A DTD (Document Type Declaration) is a way to describe the structure, elements and attributes of an XML document  .
- A DTD can be used to validate the XML document against the grammatical rules of the XML language  .
- A DTD can be declared internally or externally to the XML document .
- An internal DTD is included in the same file as the XML document, inside the `<!DOCTYPE>` declaration .
- An external DTD is stored in a separate file and referenced by the XML document using a `SYSTEM` or `PUBLIC` identifier .
- A DTD defines the following components of an XML document  :
  - Elements: the names and types of the XML elements, their order and occurrence, and their possible content (text, other elements, or empty).
  - Attributes: the names and types of the attributes that can be used in the XML elements, their default or fixed values, and their possible values (enumerated or predefined types).
  - Entities: the names and values of the entities that can be used in the XML document, such as special characters, symbols, or strings.
  - Notations: the names and sources of the notations that can be used in the XML document, such as external applications or media types.
  - Processing instructions: the instructions that can be passed to the application that processes the XML document, such as stylesheets or scripts.
  - Comments: the text that can be added to the XML document for documentation or annotation purposes, without affecting the XML structure or content.
- A DTD uses a specific syntax to declare the components of an XML document  :
  - `<!ELEMENT>`: declares an element, its type, and its content model.
  - `<!ATTLIST>`: declares an attribute, its type, and its default or fixed value.
  - `<!ENTITY>`: declares an entity, its value, and its scope (general or parameter).
  - `<!NOTATION>`: declares a notation, its name, and its source.
  - `<?...?>`: defines a processing instruction, its target, and its data.
  - `<!--...-->`: defines a comment, its content, and its location.
- A DTD example for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab is shown below:

```xml
<?xml version="1.0"?>
<!DOCTYPE notes [
  <!ELEMENT notes (unit+)>
  <!ELEMENT unit (title, content)>
  <!ATTLIST unit number CDATA #REQUIRED>
  <!ELEMENT title (#PCDATA)>
  <!ELEMENT content (section+)>
  <!ELEMENT section (heading, paragraph+)>
  <!ATTLIST section number CDATA #REQUIRED>
  <!ELEMENT heading (#PCDATA)>
  <!ELEMENT paragraph (#PCDATA | code)*>
  <!ELEMENT code (#PCDATA)>
  <!ATTLIST code language (javascript | xml) #REQUIRED>
]>
<notes>
  <unit number="3">
    <title>Design dynamic web pages using Javascript and XML</title>
    <content>
      <section number="1">
        <heading>Introduction to Javascript</heading>
        <paragraph>Javascript is a scripting language that can be embedded in HTML documents to add interactivity and functionality to web pages.</paragraph>
        <paragraph>Some of the features of Javascript are:</paragraph>
        <paragraph>- It is interpreted, not compiled, by the web browser.</paragraph>
        <paragraph>- It is object-based, not object-oriented, meaning that it supports objects, but not classes or inheritance.</paragraph>
        <paragraph>- It is loosely typed, meaning that variables do not have to be declared with a specific data type.</paragraph>
        <paragraph>- It is event-driven, meaning that it can respond to user actions, such as clicks, mouse movements, or keyboard inputs.</paragraph>
        <paragraph>- It can manipulate the HTML document object model (DOM), which is a tree-like representation of the web page elements.</paragraph>
        <paragraph>- It can

```
