### HTML

HTML stands for HyperText Markup Language. It is the code that is used to structure a web page and its content. HTML consists of a series of elements, which you use to enclose, or wrap, different parts of the content to make it appear a certain way, or act a certain way.

Some of the basic concepts of HTML are:

- HTML elements are the building blocks of HTML pages. They are represented by tags, which are written in angle brackets, such as `<p>` for paragraph, `<h1>` for heading, `<img>` for image, etc. Some elements have opening and closing tags, such as `<p>...</p>`, while some are self-closing, such as `<img />`.
- HTML attributes are additional information that can be added to an element to modify its behavior or appearance. They are written inside the opening tag, after the element name, and consist of a name and a value, separated by an equal sign, such as `<p class="intro">...</p>`. The class attribute is one of the most common attributes, which can be used to apply CSS styles to an element.
- HTML documents have a basic structure that consists of a `<!DOCTYPE>` declaration, a `<html>` element, a `<head>` element, and a `<body>` element. The `<!DOCTYPE>` declaration tells the browser what version of HTML the document is using. The `<html>` element contains the whole document. The `<head>` element contains information about the document, such as its title, metadata, links to external resources, etc. The `<body>` element contains the actual content of the document, such as text, images, links, etc.
- HTML comments are used to add notes or explanations to the HTML code, which are ignored by the browser. They are written between `<!--` and `-->`, such as `<!-- This is a comment -->`.

Here is an example of a simple HTML document:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My first HTML page</title>
</head>
<body>
  <h1>Hello, world!</h1>
  <p>This is a paragraph.</p>
  <img src="image.jpg" alt="A picture" />
  <!-- This is a comment -->
</body>
</html>
```