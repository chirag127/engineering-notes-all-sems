### Document Type Definition for the Notes of Unit 2 - Web Page Designing in the Subject of Web Technology

In the field of web technology, Document Type Definition (DTD) is an important aspect of web page designing. It is a set of rules that define the structure of an XML or HTML document. DTD helps in verifying that the document is well-formed and conforms to a specific standard. In this set of notes, we will discuss the basics of DTD and its usage in web page designing.

#### What is DTD?

- DTD is an abbreviation for Document Type Definition.
- It is a set of rules that define the structure of an XML or HTML document.
- DTD specifies the elements and attributes that can be used in the document, along with their order and hierarchy.
- It also defines the data types that can be used in the document.

#### Why is DTD important for Web Page Designing?

- DTD is important for web page designing because it helps to ensure that the document is well-formed and conforms to a specific standard.
- It helps in validating the document against a specific DTD to ensure that the document is structured correctly.
- It also helps in ensuring that the document is compatible with different web browsers and devices.

#### Types of DTD:

- There are two types of DTD - Internal and External.

##### Internal DTD:

- An internal DTD is defined within the XML or HTML document.
- It is enclosed within the <!DOCTYPE> tag.
- An internal DTD is useful for small documents that do not require frequent updates.

##### External DTD:

- An external DTD is defined in a separate file and referenced in the XML or HTML document.
- It is useful for large documents that require frequent updates.
- An external DTD can be shared among multiple documents, making it easier to maintain consistency across different documents.

#### DTD Syntax:

- The syntax of DTD is based on SGML (Standard Generalized Markup Language).
- A DTD defines the structure of an XML or HTML document by specifying the elements and attributes that can be used in the document.
- The basic syntax of a DTD is as follows:

```
<!DOCTYPE root_element [
    <!ELEMENT element_name (child_element_name)>
    <!ATTLIST element_name attribute_name attribute_type attribute_value>
]>
```

- The `root_element` is the top-level element in the document.
- The `element_name` specifies the name of the element being defined.
- The `(child_element_name)` specifies the child elements of the element being defined.
- The `attribute_name` specifies the name of the attribute being defined.
- The `attribute_type` specifies the type of the attribute (e.g., CDATA, ID, etc.).
- The `attribute_value` specifies the default value of the attribute.

#### Conclusion:

In conclusion, DTD is an important aspect of web page designing. It helps in defining the structure of an XML or HTML document and ensures that the document is well-formed and conforms to a specific standard. DTD also helps in validating the document and ensuring that it is compatible with different web browsers and devices. By understanding the basics of DTD and its usage in web page designing, web developers can create more structured and consistent documents.