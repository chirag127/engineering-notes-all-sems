# Basic structure of an HTML document

- HTML stands for HyperText Markup Language, which is the standard language for creating web pages and web applications.
- HTML documents are composed of elements, which are the building blocks of web pages. Elements are defined by tags, which are enclosed in angle brackets (< and >).
- An HTML document has a basic structure that consists of the following parts:

  - A document type declaration (`<!DOCTYPE html>`) that specifies the version of HTML used in the document. This declaration must be the first line of the document.
  - A root element (`<html>`) that contains all the other elements in the document. This element has two attributes: `lang`, which specifies the language of the document, and `dir`, which specifies the text direction (left-to-right or right-to-left).
  - A head element (`<head>`) that contains metadata about the document, such as the title, the character encoding, the style sheets, and the scripts. The metadata is not displayed on the web page, but is used by browsers and search engines to process the document.
  - A body element (`<body>`) that contains the actual content of the document, such as text, images, links, tables, forms, and multimedia. The content is displayed on the web page and can be interacted with by the user.

- An example of a basic HTML document is shown below:

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8">
  <title>My first web page</title>
</head>
<body>
  <h1>Hello, world!</h1>
  <p>This is my first web page.</p>
</body>
</html>
```

- The basic structure of an HTML document can be summarized by the following diagram:

![Basic structure of an HTML document](https://www.w3schools.com/html/img_html5.png)

- The basic structure of an HTML document is important to follow because it ensures that the document is well-formed, valid, and compatible with different browsers and devices. It also helps the document to be more accessible, searchable, and maintainable.