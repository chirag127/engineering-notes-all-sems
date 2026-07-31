### Creating an HTML document for the notes of the Unit 1 - Introduction in the subject of Web Designing

- HTML stands for HyperText Markup Language, which is the standard language for creating web pages and web applications.
- HTML uses tags to define the structure and content of a web page, such as headings, paragraphs, images, links, etc.
- HTML tags are enclosed in angle brackets (< and >) and usually come in pairs, such as <p> and </p>.
- The first tag in a pair is called the start tag or opening tag, and the second tag is called the end tag or closing tag.
- The content between the start and end tags is called the element content, and the text between the angle brackets is called the tag name.
- Some HTML tags are self-closing, which means they do not need an end tag. For example, <img> is a self-closing tag that defines an image element.
- An HTML document consists of two main parts: the head and the body.
- The head section contains information about the document, such as the title, meta data, style sheets, scripts, etc. The head section is enclosed by the <head> and </head> tags.
- The body section contains the visible content of the document, such as text, images, tables, forms, etc. The body section is enclosed by the <body> and </body> tags.
- The head and body sections are nested inside the <html> and </html> tags, which define the root element of the document.
- The first line of an HTML document is called the document type declaration, or doctype, which specifies the version and syntax of HTML. The doctype for HTML5 is <!DOCTYPE html>.
- An HTML document should also have a <title> element inside the head section, which defines the title of the document that appears in the browser tab or window.
- An HTML document can also have attributes, which are additional information that modify the behavior or appearance of an element. Attributes are specified inside the start tag of an element, after the tag name, and consist of a name and a value, separated by an equal sign (=). For example, <img src="image.jpg" alt="Image"> has two attributes: src and alt, with the values "image.jpg" and "Image" respectively.
- An HTML document can also have comments, which are notes or explanations that are ignored by the browser. Comments are enclosed by <!-- and -->. For example, <!-- This is a comment -->.

Here is an example of a simple HTML document that contains the notes of the Unit 1 - Introduction in the subject of Web Designing:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Unit 1 - Introduction</title>
</head>
<body>
  <h1>Unit 1 - Introduction</h1>
  <p>This unit covers the following topics:</p>
  <ul>
    <li>What is HTML?</li>
    <li>HTML tags and elements</li>
    <li>HTML document structure</li>
    <li>HTML attributes and comments</li>
  </ul>
  <p>To learn more about HTML, you can visit the following websites:</p>
  <ol>
    <li><a href="https://www.w3schools.com/html/">W3Schools HTML Tutorial</a></li>
    <li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML">MDN Web Docs HTML</a></li>
    <li><a href="https://www.html.com/">HTML.com</a></li>
  </ol>
</body>
</html>
```