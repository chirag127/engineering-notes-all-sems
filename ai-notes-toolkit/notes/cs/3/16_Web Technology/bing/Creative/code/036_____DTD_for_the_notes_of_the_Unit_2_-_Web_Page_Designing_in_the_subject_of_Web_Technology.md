### DTD for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

- DTD stands for Document Type Definition.
- It is a set of markup declarations that define a type of document for the SGML family, such as HTML, XML, etc.
- It is used to define the document structure with a list of legal elements and attributes.
- It can be declared inside an XML document as internal or as an external reference.
- It can be used to validate the XML data and ensure that it conforms to the expected structure.
- It can also be used to facilitate data interchange between different applications or groups.
- Some examples of DTD declarations are:

```xml
<!DOCTYPE note [
<!ELEMENT note (to,from,heading,body)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT body (#PCDATA)>
]>
```

This DTD defines a note element with four child elements: to, from, heading, and body. Each child element can contain only parsed character data (PCDATA).

```xml
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```

This DTD references an external DTD file that defines the XHTML 1.0 Transitional document type. The PUBLIC keyword indicates that the DTD is available to the public, and the URL specifies the location of the DTD file.

- Web page designing is the process of creating web pages using HTML, CSS, JavaScript, and other web technologies.
- Web pages are written for web browsers, which interpret the HTML code and display the content on the screen.
- Web pages can also use XML to store and exchange data, and use XSLT to transform the XML data into HTML or other formats.
- Web pages can have different layouts, styles, interactivity, and functionality depending on the design goals and requirements.
- Some examples of web page design tools are:

  - Text editors, such as Notepad, Sublime Text, Visual Studio Code, etc.
  - Web design software, such as Adobe Dreamweaver, Microsoft Expression Web, etc.
  - Web frameworks, such as Bootstrap, Foundation, etc.
  - Content management systems, such as WordPress, Joomla, Drupal, etc.