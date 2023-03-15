### Writing program in XML for creation of DTD, which specifies set of rules for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A DTD (Document Type Declaration) is a way to describe the structure, elements and attributes of an XML document  .
- A DTD can be used to validate the XML document against the grammatical rules of the XML language .
- A DTD can be declared internally or externally to the XML document .
- An internal DTD is written inside the XML document, within the `<!DOCTYPE>` declaration .
- An external DTD is written in a separate file, and referenced by the XML document using the `SYSTEM` or `PUBLIC` keyword .
- A DTD defines the elements and attributes of an XML document using the following syntax  :

  - `<!ELEMENT element-name category>`: defines an element and its category, such as empty, any, mixed, or children.
  - `<!ATTLIST element-name attribute-name attribute-type attribute-value>`: defines an attribute and its type and value for an element.
  - `<!ENTITY entity-name value>`: defines an entity and its value, which can be a text, a character, or an external file.

- A DTD can also use parameter entities, which are entities that can be used within the DTD itself .
- A DTD can also use conditional sections, which are sections of the DTD that are included or ignored based on some conditions .

- An example of a DTD that specifies the rules for the notes of Unit 3 is:

```xml
<!-- This is an external DTD file named notes.dtd -->
<!ELEMENT notes (unit)+>
<!ELEMENT unit (title, content)>
<!ATTLIST unit number CDATA #REQUIRED>
<!ELEMENT title (#PCDATA)>
<!ELEMENT content (paragraph | list | code)*>
<!ELEMENT paragraph (#PCDATA)>
<!ELEMENT list (item)+>
<!ATTLIST list type (ordered | unordered) #REQUIRED>
<!ELEMENT item (#PCDATA)>
<!ELEMENT code (#CDATA)>
<!ENTITY js "Javascript">
<!ENTITY xml "XML">
<!ENTITY % common "<!ENTITY js 'Javascript'><!ENTITY xml 'XML'>">
%common;
```

- An example of an XML document that uses the above DTD is:

```xml
<?xml version="1.0"?>
<!DOCTYPE notes SYSTEM "notes.dtd">
<notes>
  <unit number="3">
    <title>Design dynamic web pages using &js; and &xml;</title>
    <content>
      <paragraph>This unit covers the following topics:</paragraph>
      <list type="ordered">
        <item>Introduction to &js;</item>
        <item>Variables, data types, operators, and expressions in &js;</item>
        <item>Control structures, functions, and objects in &js;</item>
        <item>DOM manipulation and event handling in &js;</item>
        <item>Introduction to &xml;</item>
        <item>DTD and Schema for &xml; validation</item>
        <item>XPath and XSLT for &xml; transformation</item>
        <item>AJAX for asynchronous communication between &js; and &xml;</item>
      </list>
      <paragraph>The following is an example of a simple &js; program:</paragraph>
      <code><![CDATA[
        // This is a comment
        document.write("Hello, world!"); // This writes a message to the web page
      ]]></code>
    </content>
  </unit>
</notes>
```