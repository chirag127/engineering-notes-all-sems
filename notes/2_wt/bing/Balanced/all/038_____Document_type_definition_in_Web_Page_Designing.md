### Document type definition in Web Page Designing

- A document type definition (DTD) is an instruction that tells the web browser about the markup language in which the current page is written .
- A DTD defines the structure and the legal elements and attributes of an XML document . It can be declared inside an XML document as internal or as an external reference.
- A DTD is useful for two reasons:
  - It helps web browsers to determine which rendering mode they should use (quirks mode or standards mode).
  - It helps markup validators to check the document against the rules of the DTD and report any errors or warnings.
- The syntax of a DTD declaration is as follows :

```xml
<!DOCTYPE root-element PUBLIC "DTD-name" "DTD-location">
```

- The root-element is the name of the root element of the XML document. The DTD-name is a unique identifier for the DTD. The DTD-location is the URL of the external DTD file. The PUBLIC keyword indicates that the DTD is a public standard .
- An example of a DTD declaration for an HTML document is :

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
```

- This declares that the document is written in HTML 4.01 and follows the strict DTD rules defined by the W3C at the given URL .
- A mnemonic to remember the syntax of a DTD declaration is: **D**o **T**his **D**eclaration for the **root-element** with the **PUBLIC** **DTD-name** and **DTD-location**.
- A learning trick to understand the purpose of a DTD is to think of it as a contract between the web page and the web browser. The web page promises to follow the rules of the DTD, and the web browser promises to render the web page accordingly.