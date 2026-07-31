# XML Schemes for Web Page Designing

- XML stands for Extensible Markup Language. It is a markup language containing tags to define data.
- XML is used for designing the web pages in an application. It allows the web developers to create their own customized tags and attributes.
- XML Schema is a language which is used for expressing constraint about XML documents. It defines the structure, content, and data types of an XML document .
- XML Schema is also known as XML Schema Definition (XSD). It is based on the XML syntax and uses the XML namespace mechanism.
- The purpose of an XML Schema is to define the legal building blocks of an XML document, such as:
  - the elements and attributes that can appear in a document
  - the number and order of child elements
  - the data types for elements and attributes
  - the default and fixed values for elements and attributes
- An XML Schema is written as an XML document with the xs:schema element as the root element. It contains declarations for elements, attributes, types, and other components.
- An example of an XML Schema for a simple note element is given below:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

  <!-- definition of simple elements -->
  <xs:element name="to" type="xs:string"/>
  <xs:element name="from" type="xs:string"/>
  <xs:element name="heading" type="xs:string"/>
  <xs:element name="body" type="xs:string"/>

  <!-- definition of attributes -->
  <xs:attribute name="date" type="xs:date"/>

  <!-- definition of complex elements -->
  <xs:element name="note">
    <xs:complexType>
      <!-- attributes of the note element -->
      <xs:attribute ref="date" use="required"/>
      <!-- child elements of the note element -->
      <xs:sequence>
        <xs:element ref="to"/>
        <xs:element ref="from"/>
        <xs:element ref="heading"/>
        <xs:element ref="body"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>

</xs:schema>
```

- A visual sitemap is a diagram that shows the structure and hierarchy of a website. It helps the web designers to plan and organize the content, navigation, and layout of the web pages.
- A visual sitemap can be created using various tools, such as Adobe XD, Sketch, or online sitemap generators.
- An example of a visual sitemap for a simple website is given below:

![Visual sitemap example](https://xd.adobe.com/ideas/wp-content/uploads/2020/08/visual-sitemap-example-1.png)

- References:
  - : Why Use XML In Web Design and Development | Go4Expert
  - : XML Schema - javatpoint
  - : XML Schema Tutorial - W3Schools
  - : XML Schema Example - W3Schools
  - : 5 Visual Sitemap Examples for Website Designs | Adobe XD Ideas