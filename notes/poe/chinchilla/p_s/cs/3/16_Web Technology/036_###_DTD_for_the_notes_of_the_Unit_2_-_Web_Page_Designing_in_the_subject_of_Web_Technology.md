### DTD for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

DTD stands for Document Type Definition. It is a set of rules that define the structure and elements of an XML document. In the context of web page designing, DTD is used to define the structure and elements of an HTML document. In this section, we will learn about the different types of DTDs that are used in web page designing.

#### Types of DTD

There are two types of DTDs that are commonly used in web page designing:

1. Internal DTD: An internal DTD is defined within the HTML document itself. It is enclosed within the <!DOCTYPE> declaration. The syntax for defining an internal DTD is as follows:

   ```
   <!DOCTYPE html
     [
       <!ELEMENT element_name (child_element_name)>
       <!ATTLIST element_name attribute_name attribute_type "default_value">
     ]
   >
   ```

   In the above syntax, <!ELEMENT> is used to define an element and its child elements, and <!ATTLIST> is used to define the attributes of an element.

2. External DTD: An external DTD is defined in a separate file and is linked to the HTML document using the <!DOCTYPE> declaration. The syntax for defining an external DTD is as follows:

   ```
   <!DOCTYPE html SYSTEM "dtd_file_name.dtd">
   ```

   In the above syntax, "dtd_file_name.dtd" is the name of the external DTD file.

#### Advantages of using DTD

1. DTDs help to ensure that the HTML document conforms to a particular structure and set of rules.
2. DTDs make it easier to maintain and update the HTML document as changes can be made to the DTD file.
3. DTDs help to ensure that the HTML document is accessible to all users, including those using assistive technologies such as screen readers.

#### Disadvantages of using DTD

1. DTDs can be complex and may require additional knowledge and expertise to create and maintain.
2. DTDs may limit the flexibility and creativity of the web designer as they must adhere to the structure and rules defined in the DTD.

#### Examples of using DTD

Here are some examples of using DTD in HTML documents:

1. Defining the structure of an HTML document:

   ```
   <!DOCTYPE html
     [
       <!ELEMENT html (head, body)>
       <!ELEMENT head (title)>
       <!ELEMENT title (#PCDATA)>
       <!ELEMENT body (p)>
       <!ELEMENT p (#PCDATA)>
     ]
   >
   <html>
     <head>
       <title>Example Document</title>
     </head>
     <body>
       <p>This is an example HTML document.</p>
     </body>
   </html>
   ```

2. Defining attributes for an HTML element:

   ```
   <!DOCTYPE html
     [
       <!ELEMENT img EMPTY>
       <!ATTLIST img
         src CDATA #REQUIRED
         alt CDATA #IMPLIED
         width CDATA #IMPLIED
         height CDATA #IMPLIED
       >
     ]
   >
   <html>
     <body>
       <img src="example.jpg" alt="Example Image" width="100" height="100">
     </body>
   </html>
   ```

#### Applications of using DTD

1. DTDs are used in web page designing to ensure that the HTML document conforms to a particular structure and set of rules.
2. DTDs are also used in web development to ensure that the XML documents used in web services conform to a particular structure and set of rules.