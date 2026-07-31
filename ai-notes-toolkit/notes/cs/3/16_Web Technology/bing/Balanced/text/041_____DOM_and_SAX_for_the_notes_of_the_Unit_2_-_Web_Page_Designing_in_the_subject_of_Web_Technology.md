### DOM and SAX for Web Page Designing

- DOM stands for **Document Object Model**. It is a programming interface for web documents that represents the page as a tree of nodes and objects. It allows a language (such as JavaScript) to manipulate, structure, and style the website .
- SAX stands for **Simple API for XML**. It is an event-based parser for XML documents that reads the document from top to bottom and triggers events when it encounters elements, attributes, text, etc. It does not store the document in memory, so it is faster and more memory-efficient than DOM  .
- Some of the differences between DOM and SAX are:

  - DOM allows reading and writing of XML documents, while SAX only allows reading .
  - DOM creates a tree-like structure in memory that provides the client with ample information, while SAX is state-independent and does not retain information about the elements that came before.
  - DOM is useful for small to medium size XML documents, while SAX is suitable for large and complex XML documents.
  - DOM supports random access and traversal of the document, while SAX only supports sequential access and forward traversal .
  - DOM is easier to use and understand, while SAX requires more coding and logic .