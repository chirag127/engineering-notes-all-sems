
### DOM and SAX

DOM and SAX are two different ways of parsing XML documents. 

**DOM (Document Object Model)** is a tree-structured representation of an XML document. It loads the XML document into memory and builds an in-memory tree representation of the document. It allows the user to traverse the tree and modify the document. It is easy to use, but it requires a lot of memory and can be slow for large documents.

**SAX (Simple API for XML)** is an event-driven API for parsing XML documents. It reads the document sequentially and notifies the user of events such as the start of an element, the end of an element, and the text within the element. It is fast and requires less memory, but it is less flexible than DOM.