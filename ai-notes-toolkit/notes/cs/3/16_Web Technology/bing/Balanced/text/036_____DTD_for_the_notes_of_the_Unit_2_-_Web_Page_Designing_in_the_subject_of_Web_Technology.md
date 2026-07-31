### DTD for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

- DTD stands for Document Type Definition. It is a set of rules that defines the structure and content of an XML or HTML document.
- DTD can be used to validate the syntax and semantics of an XML or HTML document, ensuring that it conforms to the specified rules and standards.
- DTD can be declared either internally or externally. An internal DTD is embedded within the XML or HTML document, while an external DTD is referenced by a URL or a file path.
- DTD consists of elements, attributes, entities, notations, and comments. Elements define the tags and their content model, attributes define the properties and values of the elements, entities define the shortcuts or aliases for frequently used text or symbols, notations define the format and encoding of external data, and comments provide additional information or explanation.
- DTD syntax follows some basic rules, such as:
  - The DTD declaration starts with `<!DOCTYPE>` and ends with `>`.
  - The DTD declaration specifies the root element of the document and the location of the external DTD (if any).
  - The DTD elements, attributes, entities, and notations are declared with `<!ELEMENT>`, `<!ATTLIST>`, `<!ENTITY>`, and `<!NOTATION>` respectively, followed by their names and definitions.
  - The DTD comments start with `<!--` and end with `-->`.
  - The DTD declarations are case-sensitive and must follow a specific order: elements, attributes, entities, notations, and comments.
- DTD examples:

  - An internal DTD for a simple HTML document:

    ```html
    <!DOCTYPE html [
      <!ELEMENT html (head, body)>
      <!ELEMENT head (title)>
      <!ELEMENT title (#PCDATA)>
      <!ELEMENT body (h1, p)>
      <!ELEMENT h1 (#PCDATA)>
      <!ELEMENT p (#PCDATA)>
    ]>
    <html>
      <head>
        <title>My First HTML Page</title>
      </head>
      <body>
        <h1>Hello World!</h1>
        <p>This is a simple HTML page with an internal DTD.</p>
      </body>
    </html>
    ```

  - An external DTD for a simple XML document:

    ```xml
    <?xml version="1.0"?>
    <!DOCTYPE note SYSTEM "note.dtd">
    <note>
      <to>John</to>
      <from>Mary</from>
      <subject>Reminder</subject>
      <body>Don't forget to buy milk.</body>
    </note>
    ```

    The external DTD file (note.dtd) contains:

    ```xml
    <!ELEMENT note (to, from, subject, body)>
    <!ELEMENT to (#PCDATA)>
    <!ELEMENT from (#PCDATA)>
    <!ELEMENT subject (#PCDATA)>
    <!ELEMENT body (#PCDATA)>
    ```