 Here is the content in markdown format for the given topic:

### DTD for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

1. DTD stands for Document Type Definition. It is a set of markup declarations that defines a document type for an SGML-family markup language (GML, SGML, XML).
2. A DTD defines the structure and the legal elements and attributes of an XML document. It defines the document structure with a list of valid elements and attributes.
3. A DTD can be declared inline inside an XML document, or as an external reference. The external DTD is preferred as it can be reused by multiple XML documents.
4. The declaration of an external DTD is done by using a document type declaration, <!DOCTYPE>, followed by the URI that points to the DTD file.
```
<!DOCTYPE note SYSTEM "note.dtd">
```
5. An example of a DTD defining a simple note:
```
<!ELEMENT note (to,from,heading,body)>
<!ELEMENT to      (#PCDATA)>
<!ELEMENT from    (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT body    (#PCDATA)>
```
This DTD defines a note element with to, from, heading and body elements, and states that these elements contain parsed character data.

Advantages:
- Validates the structure of an XML document.
- Prevents invalid documents.
- Serves as documentation for the structure of XML documents.

Disadvantages:
- Can be complex to write.
- Does not allow extension of the vocabulary. New elements and attributes can't be added.
- External DTDs require separate files and more processing.

Applications:
- Defining the structure of XML configuration files.
- Defining the structure of vectors graphics (SVG).
- Defining the structure of RSS feeds.
- Defining the structure of office documents (OpenOffice, LibreOffice).

[Detailed diagrams and code examples can be added here if required.]