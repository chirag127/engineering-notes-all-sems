# Writing program in XML for creation of DTD, which specifies set of rules for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A DTD (Document Type Declaration) is a way to describe the structure and the legal elements and attributes of an XML document  .
- A DTD can be used to validate the XML document against the grammatical rules of the appropriate XML language  .
- A DTD can be declared internally or externally to the XML document .
- An internal DTD is included in the same file as the XML document, inside the `<!DOCTYPE>` declaration .
- An external DTD is referenced by the XML document using a URL or a system identifier, inside the `<!DOCTYPE>` declaration .
- A DTD defines the following components of an XML document  :
  - Elements: the names and the relationships of the XML tags
  - Attributes: the names and the values of the XML attributes
  - Entities: the names and the values of the XML entities
  - Notations: the names and the values of the XML notations
  - Processing instructions: the instructions for the XML processor
  - Comments: the comments for the XML document
- A DTD uses the following syntax to declare the components of an XML document  :
  - `<!ELEMENT>`: to declare an element and its content model
  - `<!ATTLIST>`: to declare an attribute and its type and default value
  - `<!ENTITY>`: to declare an entity and its replacement text
  - `<!NOTATION>`: to declare a notation and its identifier
  - `<?...?>`: to declare a processing instruction
  - `<!--...-->`: to declare a comment
- A DTD can use the following symbols to specify the occurrence of the components of an XML document  :
  - `?`: to indicate that the component is optional (zero or one occurrence)
  - `+`: to indicate that the component is required (one or more occurrences)
  - `*`: to indicate that the component is optional (zero or more occurrences)
  - `|`: to indicate that the component is a choice (one of the alternatives)
  - `,`: to indicate that the component is a sequence (all of the alternatives in order)
  - `()` : to group the components
  - `#PCDATA`: to indicate that the component is parsed character data (text)
  - `#REQUIRED`: to indicate that the attribute is mandatory
  - `#IMPLIED`: to indicate that the attribute is optional
  - `#FIXED`: to indicate that the attribute has a fixed value
- A DTD can use the following data types to specify the values of the components of an XML document  :
  - `CDATA`: to indicate that the value is character data (any text)
  - `ID`: to indicate that the value is a unique identifier (a name that starts with a letter or underscore and contains only letters, digits, underscores, hyphens, and periods)
  - `IDREF`: to indicate that the value is a reference to an ID value
  - `IDREFS`: to indicate that the value is a list of references to ID values
  - `ENTITY`: to indicate that the value is a reference to an entity
  - `ENTITIES`: to indicate that the value is a list of references to entities
  - `NMTOKEN`: to indicate that the value is a name token (a name that contains only letters, digits, underscores, hyphens, and periods)
  - `NMTOKENS`: to indicate that the value is a list of name tokens
  - `NOTATION`: to indicate that the value is a reference to a notation
  - `ENUMERATION`: to indicate that the value is one of the specified values

- An example of a DTD that specifies the set of rules for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab is:

```xml
<!DOCTYPE notes [
  <!ELEMENT