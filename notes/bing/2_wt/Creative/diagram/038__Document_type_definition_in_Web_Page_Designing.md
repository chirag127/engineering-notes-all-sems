A document type definition (DTD) is an instruction that tells the web browser about the version of markup language in which a web page is written . It defines the structure and the legal elements and attributes of an XML document . A DTD can be declared inside an XML document as inline or as an external reference.

The following diagram illustrates the basic architecture of a document type definition in web page designing using ASCII characters:

```
+---------------------+     +---------------------+
|                     |     |                     |
|   Web Page (.html)  |     |   XML Document      |
|                     |     |                     |
|  <!DOCTYPE html>    |     |  <!DOCTYPE note     |
|                     |     |  SYSTEM "note.dtd"> |
|  <html>             |     |                     |
|  ...                |     |  <note>             |
|  </html>            |     |  ...                |
|                     |     |  </note>            |
+---------------------+     +---------------------+
        |                             |
        |                             |
        |                             |
        |                             |
        |                             |
        |                             |
        |                             |
        |                             |
        |                             |
        |                             |
        |                             |
        |                             |
        |                             |
        |                             |
        |                             |
        |                             |
        |                             |
        |                             |
        |                             |
        v                             v
+---------------------+     +---------------------+
|                     |     |                     |
|   Web Browser       |     |   Web Browser       |
|                     |     |                     |
|  Parses the HTML    |     |  Parses the XML     |
|  document according |     |  document according |
|  to the HTML5 DTD   |     |  to the note DTD    |
|                     |     |                     |
|  Renders the web    |     |  Renders the XML    |
|  page on the screen |     |  document on the    |
|                     |     |  screen             |
+---------------------+     +---------------------+
```