### DOM and SAX in Web Page Designing

- DOM stands for **Document Object Model**, which is a standard way of representing and manipulating XML documents as a tree of nodes in memory .
- SAX stands for **Simple API for XML**, which is a low-level interface for parsing XML documents in a sequential manner, without loading the whole document into memory .
- Some of the differences between DOM and SAX are   :

| DOM | SAX |
| --- | --- |
| It reads and writes XML documents. | It only reads XML documents. |
| It loads the entire document into memory and creates a tree structure. | It does not load the document into memory, but processes it as a stream of events. |
| It allows random access and manipulation of any part of the document. | It only allows forward traversal of the document, without any modification. |
| It is easier to use and understand, but consumes more memory and CPU time. | It is more efficient and faster, but requires more coding and logic. |
| It is suitable for small to medium size XML documents that need to be queried or modified in different ways. | It is suitable for large XML documents that need to be processed quickly and linearly. |

- A possible mnemonic to remember the difference between DOM and SAX is: **DOM is a tree, SAX is a stream**.