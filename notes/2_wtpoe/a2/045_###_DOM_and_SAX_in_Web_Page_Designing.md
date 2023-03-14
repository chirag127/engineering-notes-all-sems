 Here is the content in markdown format:

### DOM and SAX in Web Page Designing

DOM and SAX are two parsing techniques used to read and manipulate XML documents.

**DOM (Document Object Model):**
- DOM parses the entire XML document and loads it into the memory as a tree of objects.
- It provides a logical tree-like model of the XML document, which makes it easy to traverse and manipulate.
- Easy to use but consumes more memory for large documents.
- Some mnemonics to remember:
**D**ata **O**bject **M**odel - treats XML as objects
**T**ree of nodes - logical structure

**SAX (Simple API for XML):**
- SAX does not load the entire XML document into memory, instead it reads the document sequentially and calls handler functions when it encounters things like start/end elements or text.
- Less memory-intensive but more complex to use.
- Some learning tricks:
**S**equential **A**ccess
**X**ML **P**arser
**H**andler functions are called on events

Advantages and Disadvantages:
DOM:
Advantages: Easy to use, can traverse/manipulate tree
Disadvantages: High memory usage for large documents

SAX:
Advantages: Low memory usage, can handle large documents
Disadvantages: More complex to use, can't randomly access data

Applications:
- DOM used for small to medium sized documents that need to be manipulated.
- SAX used for large documents where memory constraints are there.
- Both can be used to parse XML and extract required information.

Detailed diagrams and examples can be included if required. The content can be expanded with more details and points as needed.