## Unit 1 - Develop static web pages using HTML

- HTML stands for HyperText Markup Language. It is the standard language for creating web pages and web applications.
- HTML consists of elements that define the structure and content of a web page. Elements are enclosed by tags, which are written in angle brackets (< and >).
- HTML elements can have attributes, which provide additional information or functionality to the elements. Attributes are written inside the start tag of an element, after the element name, and consist of a name and a value separated by an equal sign (=).
- HTML elements can be nested, which means that one element can contain another element inside it. The inner element is called the child element, and the outer element is called the parent element. The child element inherits some properties from the parent element, such as font size and color.
- HTML elements can be classified into two types: block-level elements and inline elements. Block-level elements create a new line on the web page and occupy the full width of the parent element. Inline elements do not create a new line and only occupy the space needed for their content. Examples of block-level elements are <div>, <p>, <h1>, <ul>, etc. Examples of inline elements are <span>, <a>, <img>, <em>, etc.
- HTML also has some special elements that do not have a closing tag, such as <br>, <hr>, <img>, <input>, etc. These elements are called self-closing or void elements.
- HTML supports comments, which are used to add notes or explanations to the code. Comments are written inside <!-- and --> and are ignored by the browser.
- HTML also supports entities, which are used to display special characters that are not part of the standard keyboard, such as ©, €, √, etc. Entities are written as an ampersand (&) followed by a name or a number and a semicolon (;). For example, &copy; displays ©, and &#8730; displays √.
- HTML documents have a basic structure that consists of the following elements:

```html
<!DOCTYPE html> <!-- defines the document type -->
<html> <!-- the root element of the document -->
<head> <!-- contains metadata and information about the document -->
  <title> <!-- defines the title of the document -->
    Document Title
  </title>
</head>
<body> <!-- contains the visible content of the document -->
  <!-- write your HTML code here -->
</body>
</html>
```