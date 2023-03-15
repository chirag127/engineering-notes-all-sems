# Writing program in XML for creation of DTD, which specifies set of rules for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A DTD (Document Type Declaration) is a way to describe the structure and the legal elements and attributes of an XML document  .
- A DTD can be used to validate the XML document against the grammatical rules of the appropriate XML language  .
- A DTD can be declared internally or externally to the XML document .
- An internal DTD is included in the same file as the XML document, while an external DTD is referenced by a URL .
- An internal DTD declaration has the following syntax:

```xml
<!DOCTYPE root-element [
  <!-- Element declarations -->
  <!-- Attribute declarations -->
  <!-- Entity declarations -->
  <!-- Notation declarations -->
]>
```

- An external DTD declaration has the following syntax:

```xml
<!DOCTYPE root-element SYSTEM "URL">
```

- To create a DTD for the notes of the Unit 3, we need to define the elements and attributes that are allowed in the XML document.
- For example, we can define the following elements and attributes:

```xml
<!-- The root element of the document -->
<!ELEMENT notes (unit)+>

<!-- The unit element has a number attribute and contains one or more topics -->
<!ELEMENT unit (topic)+>
<!ATTLIST unit number CDATA #REQUIRED>

<!-- The topic element has a name attribute and contains one or more subtopics -->
<!ELEMENT topic (subtopic)+>
<!ATTLIST topic name CDATA #REQUIRED>

<!-- The subtopic element has a name attribute and contains text -->
<!ELEMENT subtopic (#PCDATA)>
<!ATTLIST subtopic name CDATA #REQUIRED>
```

- The above DTD defines the rules for the notes of the Unit 3, such as:
  - The root element must be `notes` and it must contain one or more `unit` elements.
  - The `unit` element must have a `number` attribute and it must contain one or more `topic` elements.
  - The `topic` element must have a `name` attribute and it must contain one or more `subtopic` elements.
  - The `subtopic` element must have a `name` attribute and it must contain text.
- An example of an XML document that follows the above DTD is:

```xml
<?xml version="1.0"?>
<!DOCTYPE notes [
  <!-- The DTD declarations go here -->
]>
<notes>
  <unit number="3">
    <topic name="Javascript">
      <subtopic name="Introduction">Javascript is a scripting language for the web.</subtopic>
      <subtopic name="Syntax">Javascript has a C-like syntax with curly braces and semicolons.</subtopic>
      <subtopic name="Variables">Javascript has var, let and const keywords for declaring variables.</subtopic>
    </topic>
    <topic name="XML">
      <subtopic name="Introduction">XML is a markup language for storing and exchanging data.</subtopic>
      <subtopic name="Syntax">XML has a tree-like structure with tags and attributes.</subtopic>
      <subtopic name="DTD">XML can be validated by a DTD that defines the rules for the XML document.</subtopic>
    </topic>
  </unit>
</notes>
```