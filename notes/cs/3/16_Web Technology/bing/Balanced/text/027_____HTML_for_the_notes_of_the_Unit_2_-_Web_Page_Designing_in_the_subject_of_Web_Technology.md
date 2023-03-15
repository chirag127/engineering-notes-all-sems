### HTML for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

- HTML stands for HyperText Markup Language. It is the code that is used to structure a web page and its content. 
- HTML consists of a series of elements, which are used to enclose, or wrap, different parts of the content to make it appear or act a certain way. 
- HTML elements are made up of two tags: an opening tag and a closing tag. The opening tag has the element name and optional attributes, while the closing tag has a forward slash and the element name. The content goes between the tags.  
- For example, `<p>This is a paragraph.</p>` is an HTML element that defines a paragraph. The `<p>` is the opening tag, the `</p>` is the closing tag, and the text between them is the content.  
- Some HTML elements are self-closing, which means they do not need a closing tag. For example, `<img src="image.jpg" alt="An image">` is an HTML element that embeds an image into the web page. The `src` attribute specifies the source of the image, and the `alt` attribute provides an alternative text for the image.  
- HTML elements can be nested inside other elements, which means they can have children or parent elements. For example, `<ul><li>Item 1</li><li>Item 2</li></ul>` is an HTML element that defines an unordered list with two list items. The `<ul>` element is the parent of the `<li>` elements, and the `<li>` elements are the children of the `<ul>` element.  
- HTML elements can have different types and roles, depending on their purpose and function. For example, there are elements for marking up headings, paragraphs, links, images, tables, forms, etc.   
- HTML documents have a basic structure that consists of a `<!DOCTYPE>` declaration, a `<html>` element, a `<head>` element, and a `<body>` element. The `<!DOCTYPE>` declaration tells the browser what version of HTML the document is using. The `<html>` element is the root element that contains all the other elements. The `<head>` element contains information about the document, such as the title, the character encoding, the style sheets, etc. The `<body>` element contains the visible content of the document, such as the text, images, links, etc.  
- For example, a basic HTML document could look like this:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My First HTML Page</title>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Hello, World!</h1>
  <p>This is my first HTML page.</p>
  <img src="image.jpg" alt="An image">
  <a href="https://www.w3schools.com">Learn more about HTML</a>
</body>
</html>
```

- HTML documents can be edited and viewed using any text editor and web browser. To edit an HTML element, you can right-click on it and choose "Inspect" or "Inspect Element" to see what elements are made up of. You can also edit the HTML or CSS on-the-fly in the Elements or Styles panel that opens.  
- HTML is easy to learn and use. It is the standard markup language for web pages. With HTML, you can create your own website and display your content in various ways. 

: HTML basics - Learn web development | MDN - Mozilla
: Introduction to HTML - W3Schools
: HTML Basic - W3Schools
: HTML Tutorial - W3Schools