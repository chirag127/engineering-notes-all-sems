# XML Schemes in Web Page Designing

- XML stands for **eXtensible Markup Language**. It is a markup language similar to HTML, but without predefined tags to use. Instead, you define your own tags designed specifically for your needs. This is a powerful way to store data in a format that can be stored, searched, and shared.
- XML Schema is an XML-based (and more powerful) alternative to DTD. DTD stands for **Document Type Definition** and is a way to define the structure and content of an XML document. XML Schema supports data types, which makes it easier to describe, validate, and restrict data.
- XML schemas contain numerous design patterns, the most common of which are **Russian Doll**, **Salami Slice**, **Venetian Blind**, and **Garden of Eden**. The patterns vary according to the number of their global elements or types. A global element or type, which is a child of the schema, contains a target namespace.
- The classes in the **System.Xml.Schema** namespace map to the structures defined in the **World Wide Web Consortium (W3C) XML Schema Recommendation** and can be used to build XML schemas in-memory. Building an XML Schema In the code examples that follow, the SOM API is used to build a customer XML schema in-memory.
- XML schemas allow both anonymous and named simple types to be derived by restriction from other simple types (built-in or user-defined) or constructed as a list or union of other simple types. The **XmlSchemaSimpleTypeRestriction** class is used to create a simple type by restricting the built-in **xs:string** type.

: Building XML Schemas | Microsoft Learn
: Introducing Design Patterns in XML Schemas - Oracle
: XML Schema Tutorial - W3Schools
: XML introduction - XML: Extensible Markup Language | MDN - Mozilla
: XML Tutorial - W3Schools