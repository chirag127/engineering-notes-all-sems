# DOM and SAX

## DOM

- DOM stands for **Document Object Model**.
- It is a **programming interface** for web documents, such as HTML and XML.
- It represents the document as a **tree of nodes and objects** that can be manipulated by programming languages, such as JavaScript .
- It allows the programmer to **read and write** the document, as well as change its structure, style, and content.
- It is useful for **small to medium size** XML files, as it requires loading the entire document into memory.
- It supports **random access** to any part of the document, as well as **traversing** the document in any direction .

## SAX

- SAX stands for **Simple API for XML**.
- It is an **event-based parser** for XML documents .
- It reads the document **sequentially** from top to bottom, and generates **events** for each element, attribute, text, etc .
- It allows the programmer to **handle** the events using **callback methods** .
- It is useful for **large** XML files, as it does not require loading the entire document into memory.
- It does not support **random access** or **traversing** the document in any direction, as it is state-independent .
- It only supports **reading** the document, not writing it.

: https://www.careerride.com/XML-DOM.aspx
: https://www.geeksforgeeks.org/difference-between-sax-parser-and-dom-parser-in-java/
: https://askanydifference.com/difference-between-sax-and-dom/
: https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction
: https://www.freecodecamp.org/news/whats-the-document-object-model-and-why-you-should-know-how-to-use-it-1a2d0bc5429d/