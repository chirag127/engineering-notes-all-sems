 Here is the content in markdown format for the given topic:

### DOM and SAX for the notes of the Unit 2 - Web Page Designing

**Document Object Model (DOM):**
- DOM is a programming interface for HTML and XML documents.
- It represents the page so that programs can change the document structure, style and content.
- The DOM views the HTML document as a tree of nodes where each element, attribute, and piece of text in the markup is represented by a node in the tree.
- Pros: Easy to understand and simple to use. Supports dynamic changes to the document.
- Cons: Requires loading the whole document into memory which can be memory intensive for large documents.

**Simple API for XML (SAX):**
- SAX is an alternative to DOM that provides an interface for reading data from an XML document sequentially.
- It reports parsing events to the application rather than building an internal representation of the document.
- Cons: More complex interface and does not store the document in memory so does not support random access to different parts of the document.
- Pros: More memory efficient and faster as does not require loading the whole document into memory. Ideal for streaming large documents.

To summarize, choose DOM if frequent random access is needed and memory is not a constraint. Choose SAX if memory efficiency is priority and streaming access to XML document is sufficient. Both have their pros and cons so choice depends on requirements and application.

Examples and diagrams can be added as needed to supplement the notes. codes and other details can also be included for deeper understanding. The content can be modified as required to best suit the needs. Let me know if you would like me to modify or add anything.