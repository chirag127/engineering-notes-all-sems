# Using XML Processors

- XML processors are programs that can read and process XML documents .
- XML processors can turn XML files into in-memory structures that the rest of the program can access .
- The most fundamental XML processor is a parser, which reads an XML document and converts it into an internal representation for other programs or subroutines to use .
- There are two types of XML parsers: validating and non-validating .
  - Validating parsers check the XML document against a schema or a DTD (Document Type Definition) to ensure that it conforms to the rules and structure defined by the schema or the DTD .
  - Non-validating parsers do not check the XML document against a schema or a DTD, but only check if it is well-formed, meaning that it follows the basic syntax rules of XML .
- XML processors can also perform other tasks on XML documents, such as:
  - XSLT (Extensible Stylesheet Language Transformations) processing, which transforms an XML document into another format, such as HTML, using a stylesheet .
  - XQuery processing, which queries an XML document using a query language and returns a result set .
  - XProc processing, which defines a pipeline of operations on XML documents, such as validation, transformation, filtering, etc .
- XML processors are important for web page designing, as they can help to:
  - Store and exchange data over the Internet in a structured and standardized way.
  - Separate the content and the presentation of web pages using XML and XSLT.
  - Query and manipulate data from XML sources using XQuery.
  - Automate and simplify complex XML processing tasks using XProc .