### Document type definition in Web Page Designing

- A document type definition (DTD) is an instruction that tells the web browser about the markup language in which the current page is written .
- A DTD defines the structure and the legal elements and attributes of an XML document .
- A DTD can be declared inside an XML document as internal or as an external reference.
- A DTD helps to ensure the validity and interoperability of XML data.
- A DTD can also be used to specify the default values, entities, notations, and processing instructions for an XML document.

#### Syntax of DTD declaration

- A DTD declaration starts with `<!DOCTYPE` and ends with `>` .
- A DTD declaration can have one of the following forms:

  - `<!DOCTYPE root-element SYSTEM "DTD-file">` : This form declares an external DTD file that is referenced by a URI .
  - `<!DOCTYPE root-element PUBLIC "DTD-name" "DTD-file">` : This form declares an external DTD file that is referenced by a public identifier and a URI .
  - `<!DOCTYPE root-element [ ... ]>` : This form declares an internal DTD that is embedded within the XML document .

- The root-element is the name of the root element of the XML document .
- The DTD-file is the URI of the external DTD file .
- The DTD-name is the public identifier of the external DTD file .
- The ... is the content of the internal DTD that defines the elements, attributes, entities, notations, and processing instructions for the XML document .

#### Example of DTD declaration

- The following example shows an XML document that declares an external DTD file named books.dtd using a public identifier:

  ```xml
  <?xml version="1.0"?>
  <!DOCTYPE books PUBLIC "-//W3C//DTD Books 1.0//EN" "books.dtd">
  <books>
    <book>
      <title>XML: A Beginner's Guide</title>
      <author>Steven Holzner</author>
      <price>29.99</price>
    </book>
    <book>
      <title>Learning XML</title>
      <author>Erik T. Ray</author>
      <price>39.99</price>
    </book>
  </books>
  ```

- The following example shows an XML document that declares an internal DTD that defines the elements and attributes for a simple note:

  ```xml
  <?xml version="1.0"?>
  <!DOCTYPE note [
    <!ELEMENT note (to,from,heading,body)>
    <!ELEMENT to (#PCDATA)>
    <!ELEMENT from (#PCDATA)>
    <!ELEMENT heading (#PCDATA)>
    <!ELEMENT body (#PCDATA)>
    <!ATTLIST note date CDATA #IMPLIED>
  ]>
  <note date="2023-03-13">
    <to>John</to>
    <from>Sydney</from>
    <heading>Reminder</heading>
    <body>Don't forget to study for the exam.</body>
  </note>
  ```

#### Advantages of DTD

- Some of the advantages of using DTD are:

  - It helps to ensure the validity and consistency of XML data by defining the rules and constraints for the document structure .
  - It helps to improve the interoperability and compatibility of XML data by allowing different applications and systems to share a common DTD .
  - It helps to simplify the processing and parsing of XML data by providing default values, entities, notations, and processing instructions .
  - It helps to facilitate the reuse and maintenance of XML data by allowing the separation of the document structure from the document content .

#### Disadvantages of DTD

- Some of the disadvantages of using DTD are:

  - It does not support namespaces, which are a mechanism to avoid name conflicts among elements and attributes from different sources.
  - It does not support data types, which are a way to