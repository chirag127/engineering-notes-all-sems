# XML Schemes for Web Page Designing

- XML stands for Extensible Markup Language. It is a markup language containing tags to define data.
- XML is used for designing the web pages in an application. It allows the web developers to create their own customized tags and attributes.
- XML Schema is a language which is used for expressing constraint about XML documents. It defines the legal building blocks of an XML document, such as the elements, attributes, data types, order, and values .
- XML Schema is also known as XML Schema Definition (XSD). It is written in XML syntax and has a .xsd file extension.
- An example of an XML Schema is shown below:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

  <xs:element name="note">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="to" type="xs:string"/>
        <xs:element name="from" type="xs:string"/>
        <xs:element name="heading" type="xs:string"/>
        <xs:element name="body" type="xs:string"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>

</xs:schema>
```

- This schema defines a note element with four child elements: to, from, heading, and body. Each child element has a string data type.
- A valid XML document that conforms to this schema is shown below:

```xml
<?xml version="1.0" encoding="UTF-8" ?>

<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
```

- A visual sitemap is a diagram that shows the structure and hierarchy of a website. It helps the web designers to plan and organize the content, navigation, and layout of the website.
- A visual sitemap can be created using various tools, such as Adobe XD, Sketch, or online sitemap generators.
- An example of a visual sitemap is shown below:

![Visual sitemap example](https://xd.adobe.com/ideas/wp-content/uploads/2020/10/visual-sitemap-example-1.png)

- This sitemap shows the main pages of a website, such as Home, About, Services, Portfolio, and Contact. It also shows the subpages and links between them.