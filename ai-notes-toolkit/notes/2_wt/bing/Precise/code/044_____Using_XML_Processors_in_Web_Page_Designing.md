### Using XML Processors in Web Page Designing

XML processors are used in web page designing to parse and manipulate XML data. Here is an example of how to use an XML processor in JavaScript to parse an XML string and extract information from it:

```javascript
let xmlString = `<?xml version="1.0" encoding="UTF-8"?>
<catalog>
   <book id="bk101">
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications with XML.</description>
   </book>
</catalog>`;

let parser = new DOMParser();
let xmlDoc = parser.parseFromString(xmlString, "text/xml");

let book = xmlDoc.getElementsByTagName("book")[0];
let title = book.getElementsByTagName("title")[0].childNodes[0].nodeValue;

console.log(title); // Output: "XML Developer's Guide"
```

This code uses the `DOMParser` object to parse the XML string and create an XML document object. The `getElementsByTagName` method is then used to access the `book` and `title` elements, and the `nodeValue` property is used to extract the text content of the `title` element. This information can then be used in the web page design to display the desired content to the user.