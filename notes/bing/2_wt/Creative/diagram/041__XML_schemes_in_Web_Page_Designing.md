XML schemas are used to describe and validate the structure and the content of XML data. They define the elements, attributes and data types that can appear in an XML document. XML schemas can also support namespaces, which allow different XML vocabularies to be combined in a single document.

One way to design XML schemas is to use design patterns, which are common solutions to recurring problems. Some of the most common design patterns in XML schemas are:

- Russian Doll: This pattern defines all the elements locally within a single complex type. It is called Russian Doll because the elements are nested inside each other like the Russian matryoshka dolls. This pattern is simple and easy to understand, but it does not allow reuse of types or elements.
- Salami Slice: This pattern defines all the elements globally and then references them in a sequence within a single complex type. It is called Salami Slice because the elements are sliced into separate pieces and then put together in a sequence. This pattern allows reuse of elements, but it does not allow reuse of types or groups of elements.
- Venetian Blind: This pattern defines all the types globally and then references them in a sequence within a single complex type. It is called Venetian Blind because the types are hidden behind the complex type like the slats of a Venetian blind. This pattern allows reuse of types and groups of elements, but it does not allow reuse of elements.
- Garden of Eden: This pattern defines both the elements and the types globally and then references them in a sequence within a single complex type. It is called Garden of Eden because it allows maximum flexibility and reuse of both elements and types.

The following diagram illustrates the basic architecture of a XML schema using the Garden of Eden pattern:

```
+-----------------+    +-----------------+
| XML Schema      |    | XML Document    |
+-----------------+    +-----------------+
|                 |    |                 |
| <xs:schema>     |    | <note>          |
|                 |    |                 |
|   <xs:element   |    |   <to>          |
|     name="note" |    |     Tove        |
|     type="Note" |    |   </to>         |
|   />            |    |                 |
|                 |    |   <from>        |
|   <xs:element   |    |     Jani        |
|     name="to"   |    |   </from>       |
|     type="xs:string" | |                 |
|   />            |    |   <heading>     |
|                 |    |     Reminder    |
|   <xs:element   |    |   </heading>    |
|     name="from" |    |                 |
|     type="xs:string" | |   <body>        |
|   />            |    |     Don't forget|
|                 |    |     me this     |
|   <xs:element   |    |     weekend!    |
|     name="heading" | |   </body>       |
|     type="xs:string" | |                 |
|   />            |    | </note>         |
|                 |    |                 |
|   <xs:element   |    +-----------------+
|     name="body" |
|     type="xs:string" |
|   />            |
|                 |
|   <xs:complexType |
|     name="Note" |
|   >             |
|                 |
|     <xs:sequence |
|     >           |
|                 |
|       <xs:element |
|         ref="to" |
|       />        |
|                 |
|       <xs:element |
|         ref="from" |
|       />        |
|                 |
|       <xs:element |
|         ref="heading" |
|       />        |
|                 |
|       <xs:element |
|         ref="body" |
|       />        |
|                 |
|     </xs:sequence |
|     >           |
|                 |
|   </xs:complexType |
|   >             |
|                 |
| </xs:schema>    |
|                 |
+-----------------+
```