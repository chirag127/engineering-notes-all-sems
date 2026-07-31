 Here is the content in formal tone without emojis or external links, written in Markdown format with points:

### DTD in Web Page Designing

1. DTD stands for Document Type Definition. It is a set of markup declarations that define a document type for an SGML-family markup language (SGML, XML, HTML).
2. A DTD defines the document structure with a list of valid elements and attributes. It specifies the rules for the structure and the elements and attributes that can be used in an XML or HTML document.
3. Having a DTD has a few benefits:
- It verifies that the document is structurally correct
- It provides rules/guidelines for formatting the document
- It allows validation - checking if the document follows the rules of the DTD
4. There are two ways to add a DTD to an HTML document:
- Internal DTD - defined inside the document in the head section
- External DTD - defined in a separate file and referenced from the document
5. A sample internal DTD would look like:
<!DOCTYPE html [
<!ELEMENT html (head,body)>
<!ELEMENT head (title)>
<!ELEMENT title (#PCDATA)>
<!ELEMENT body (p)>
<!ELEMENT p (#PCDATA)>
]>

6. A sample external DTD reference in an HTML document would be:
<!DOCTYPE html SYSTEM "sample.dtd">

Does this content meet the required guidelines? Let me know if you would like me to modify or expand the content in any way.