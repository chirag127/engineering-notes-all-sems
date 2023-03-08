 Here is the content in markdown format:

### Writing program in XML for creation of DTD, which specifies set of rules for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab:

1. XML stands for Extensible Markup Language which is a markup language much like HTML. It is used to store and transport data.
2. A DTD or Document Type Definition is a set of markup declarations that defines a document type for an XML document. It declares what elements and attributes are used in the XML document, and what are their relationships.
3. To create a DTD for the notes of Unit 3, first we will define the root element <notes> and inside that the child elements like <title>, <heading>, <description>, etc. For example:
<notes>
    <title>Unit 3 Notes</title>
    <heading>Javascript</heading>
    <description>Javascript is a lightweight, interpreted programming or scripting language that is typically embedded into web pages. It allows web pages to be interactive and more dynamic.</description>
    ...
</notes>

4. Then we will declare the elements and attributes we used along with their data types and relationships using declarations in the DTD. For example:
<!DOCTYPE notes [
    <!ELEMENT notes (title, heading+, description+)>
    <!ELEMENT title (#PCDATA)>
    <!ELEMENT heading (#PCDATA)>
    <!ELEMENT description (#PCDATA)>
]>

5. This DTD specifies that the <notes> element must contain one <title> element followed by one or more <heading> elements and one or more <description> elements. The title, heading and description elements can only contain parsed character data.

6. Such a DTD can then be used to validate the notes XML document and check for any errors. It ensures that the document follows the structure and rules specified in the DTD.

7. Some advantages of using XML and DTD are:
- XML is platform independent and language independent.
- XML documents are easily parsed and processed by XML parsers.
- DTD enables validation of XML documents which ensures correctness and consistency.
- XML and DTD are extensible and make documents self-describing.