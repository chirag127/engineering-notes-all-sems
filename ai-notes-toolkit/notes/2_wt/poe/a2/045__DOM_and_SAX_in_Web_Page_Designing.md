 Here is the formal content on DOM and SAX in Web Page Designing:

### DOM and SAX in Web Page Designing

1. DOM or Document Object Model:
- DOM is a programming interface for HTML and XML documents.
- It represents the page so that it can be accessed and manipulated by programming languages.
- The DOM views the HTML document as a tree of nodes.
- It creates a full object model of the HTML document which can be used to access and modify the structure and content of the document.
- DOM is easier to use but requires loading the entire document into memory, so it is memory intensive and slower.

2. SAX or Simple API for XML:
- SAX is an event-based sequential access parser API for XML.
- It does not load the entire document into memory at once. Instead, it reports parsing events to the application.
- The application can handle the events to read/write portions of the document as it is needed.
- So, it does not require much memory but the application has to maintain its own state since it only gets fragments of the document.
- SAX is more efficient and faster but more complex to use compared to DOM.

The choice between DOM and SAX depends on the application requirements like speed, memory usage, simplicity, etc. Both have their pros and cons and can be used for parsing XML and HTML documents to access and manipulate their content.