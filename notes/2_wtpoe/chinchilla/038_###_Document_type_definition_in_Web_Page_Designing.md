### Document Type Definition in Web Page Designing

Document Type Definition (DTD) is a markup language used to define the structure and rules for creating valid markup documents. It is an important aspect of web page designing as it helps in the creation of error-free, well-structured web pages. DTD defines the elements, attributes, and entities that can be used in a web page, along with their relationships and hierarchy.

#### Syntax

A DTD is defined using a set of rules that specify the syntax and structure of elements and attributes in a document. The basic syntax for defining a DTD is as follows:

```
<!DOCTYPE root_element SYSTEM "dtd_file.dtd">
```

Here, `root_element` is the main element of the document, and `dtd_file.dtd` is the file containing the DTD definition.

#### Types of DTDs

There are two types of DTDs: Internal and External.

##### Internal DTD

An internal DTD is defined within the web page document itself. It is enclosed within the `<!DOCTYPE>` tag and is defined between square brackets `[]`. 

```
<!DOCTYPE html [
  <!ELEMENT html (head, body)>
  <!ELEMENT head (title)>
  <!ELEMENT title (#PCDATA)>
  <!ELEMENT body (#PCDATA)>
]>
```

##### External DTD

An external DTD is defined in a separate file and is referenced in the web page document using the `<!DOCTYPE>` tag, with the `SYSTEM` attribute pointing to the location of the external DTD file.

```
<!DOCTYPE html SYSTEM "dtd_file.dtd">
```

#### Advantages of DTD

- DTD helps in creating well-structured, error-free web pages.
- It facilitates the creation of valid markup documents by specifying the rules for elements, attributes, and entities.
- DTD defines the hierarchy and relationships between elements, making it easier to understand the structure of the web page.

#### Disadvantages of DTD

- DTDs can be complex and difficult to understand, especially for beginners.
- Changes to the DTD can affect the validity of existing web pages, requiring updates to the code.

#### Mnemonics and Learning Tricks

One possible mnemonic for remembering DTD is "Don't Type Errors". This emphasizes the importance of using DTD to create well-structured, error-free web pages. Another possible learning trick is to practice creating web pages using DTD and testing them for validity using online tools such as the W3C Markup Validation Service.