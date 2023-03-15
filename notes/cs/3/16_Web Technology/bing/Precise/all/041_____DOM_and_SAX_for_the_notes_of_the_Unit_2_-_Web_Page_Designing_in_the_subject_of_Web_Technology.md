# DOM and SAX

DOM (Document Object Model) and SAX (Simple API for XML) are two common methods for accessing and manipulating XML documents.

## DOM
- DOM is a tree-based model that represents the structure of an XML document.
- It allows for the creation, deletion, and modification of elements and attributes in the document.
- DOM is memory-intensive, as it requires the entire document to be loaded into memory before it can be accessed.
- It is well-suited for small to medium-sized documents, where the entire document can be easily loaded into memory.

## SAX
- SAX is an event-based model that reads the XML document sequentially.
- It generates events for elements, attributes, and other components of the document as it reads them.
- SAX is more memory-efficient than DOM, as it does not require the entire document to be loaded into memory.
- It is well-suited for large documents, where loading the entire document into memory would be impractical.

In summary, DOM and SAX are two common methods for accessing and manipulating XML documents. DOM is a tree-based model that is well-suited for small to medium-sized documents, while SAX is an event-based model that is well-suited for large documents. Both have their advantages and disadvantages, and the choice between them depends on the specific needs of the application.