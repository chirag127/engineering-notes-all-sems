DOM and SAX are two different ways of processing XML documents. DOM stands for Document Object Model, and SAX stands for Simple API for XML. Here is a detailed ASCII diagram for DOM and SAX in web page designing:

### DOM and SAX in Web Page Designing

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|    XML File    |     |    XML File    |     |    XML File    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |     +----------------+
       |                     |                     |     |                |
       |                     |                     +---->|    SAX API    |
       |                     |                           |                |
       |                     |                           +----------------+
       |                     |                                 |
       |                     |                                 |
       |                     |                                 |
       |                     |                                 |
       |                     |                                 |
       |                     |                                 |
       |                     |                                 |
       |                     |                                 |
       |                     |                                 |
       |                     |                                 |
       |                     |                                 |
       |                     |                                 |
       |                     |                                 |
       |                     |                                 |     +----------------+
       |                     |                                 |     |                |
       |                     |                                 +---->|  Application  |
       |                     |                                       |                |
       |                     |                                       +----------------+
       |                     |
       |                     |
       |                     |
       |                     |
       |                     |
       |                     |
       |                     |
       |                     |
       |                     |
       |                     |
       |                     |
       |                     |
       |                     |
       |                     |
       |                     |     +----------------+
       |                     |     |                |
       |                     +---->|    DOM API    |
       |                           |                |
       |                           +----------------+
       |                                 |
       |                                 |
       |                                 |
       |                                 |
       |                                 |
       |                                 |
       |                                 |
       |                                 |
       |                                 |
       |                                 |
       |                                 |
       |                                 |
       |                                 |
       |                                 |     +----------------+
       |                                 |     |                |
       +---------------------------------+---->|  Application  |
                                               |                |
                                               +----------------+
```

In DOM, the XML file is loaded into memory and parsed into a tree structure that represents the elements and attributes of the document. The DOM API allows the application to access and manipulate the tree structure, as well as read and write the XML file. DOM is useful for small to medium size XML files that may need to be modified and queried in different ways once they have been loaded   .

In SAX, the XML file is read sequentially from top to bottom, and the SAX API generates events for each element, attribute, text, comment, etc. that it encounters. The application can register handlers for these events and process the XML data as it is being read. SAX is useful for large XML files that do not need to be modified or queried, but only need to be processed once    .