# Using XML Processors

- XML processors are programs that can read and process XML documents .
- XML processors can turn XML files into in-memory structures that the rest of the program can access .
- The most fundamental XML processor is a parser, which reads an XML document and converts it into an internal representation for other programs or subroutines to use .
- There are two types of XML parsers: validating and non-validating .
  - Validating parsers check the XML document against a schema or a DTD (Document Type Definition) to ensure that it conforms to the rules and structure defined by the schema or the DTD .
  - Non-validating parsers do not check the XML document against a schema or a DTD, but only check if it is well-formed, meaning that it follows the basic syntax rules of XML .
- XML processors can also perform other tasks on XML documents, such as:
  - XSLT (Extensible Stylesheet Language Transformations), which transforms XML documents into other formats, such as HTML, PDF, or plain text .
  - XQuery (XML Query Language), which queries XML documents and returns subsets of data or new XML documents .
  - XProc (XML Processing Language), which defines a standard way of composing XML processing pipelines, which are sequences of operations on XML documents .
- XML processors are important for web page designing, as they enable the exchange, manipulation, and presentation of data in XML format over the Internet.