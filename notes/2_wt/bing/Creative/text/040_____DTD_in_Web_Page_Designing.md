### DTD in Web Page Designing

- DTD stands for Document Type Definition.
- A DTD defines the structure and the legal elements and attributes of an XML document .
- A DTD can be declared inside an XML document as inline or as an external recommendation.
- A DTD helps to verify that XML data is valid and conforms to the rules of a DTD .
- A DTD also helps independent groups of people to agree on a standard DTD for interchanging data.
- A DTD affects the display of the web page by defining the type of document and the specific version of the HTML spec you intended to target.
- A DTD can be used for HTML-, XHTML-, or HTML5-based pages.
- A DTD consists of two parts: definition and declaration.
- The definition matches the DTD type to the type of code used in the document.
- The declaration specifies the URL of a web-accessible document that contains the DTD rules.
- An example of a DTD declaration for an HTML5 document is:

```html
<!DOCTYPE html>
```

- An example of a DTD declaration for an XML document that uses an external DTD file is:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE note SYSTEM "Note.dtd">
<note>
  <to>Tove</to>
  <from>Jani</from>
</note>
```