### DOM and SAX

- DOM stands for **Document Object Model**. It is a programming interface for web documents that represents the page as a tree of nodes and objects.
- SAX stands for **Simple API for XML**. It is an event-based parser that reads XML documents from top to bottom and triggers callbacks for each element.
- Some differences between DOM and SAX are  :
  - DOM reads and writes the entire document into memory, while SAX only reads the document sequentially.
  - DOM allows random access and manipulation of any part of the document, while SAX only allows forward traversal and does not modify the document.
  - DOM is useful for small to medium size XML files that need complex processing, while SAX is useful for large XML files that need fast and simple processing.
  - DOM consumes more memory and CPU time, while SAX consumes less memory and CPU time.
  - DOM provides a tree-like structure that contains more information about the document, while SAX provides a stream-like structure that contains less information about the document.