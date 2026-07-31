### DOM and SAX for Web Page Designing

- DOM stands for **Document Object Model**, which is a programming interface for web documents. It represents the page as a tree of nodes and objects that can be manipulated by languages like JavaScript.
- SAX stands for **Simple API for XML**, which is an event-based parser for XML documents. It reads the document from top to bottom and triggers events when it encounters elements, attributes, text, etc.
- Some of the differences between DOM and SAX are  :
  - DOM reads and writes the entire document into memory, while SAX only reads the document sequentially and does not store it.
  - DOM allows random access and manipulation of any part of the document, while SAX only allows forward access and cannot modify the document.
  - DOM is useful for small to medium size documents that need a lot of processing, while SAX is useful for large documents that need minimal processing.
  - DOM consumes more memory and CPU time, while SAX is more efficient and faster.
  - DOM provides a standard object model for the document, while SAX does not have a standard way of representing the document.