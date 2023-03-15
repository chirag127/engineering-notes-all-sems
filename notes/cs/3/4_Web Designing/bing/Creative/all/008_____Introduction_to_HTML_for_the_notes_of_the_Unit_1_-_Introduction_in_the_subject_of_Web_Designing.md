Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content in markdown format on the topic of Introduction to HTML for the notes of the Unit 1 - Introduction in the subject of Web Designing. Here is the content I have generated for you:

# Introduction to HTML

HTML stands for HyperText Markup Language. It is the standard language for creating web pages and web applications. HTML describes the structure and content of a web page using tags and attributes. HTML tags are keywords that define how the browser should display the content. HTML attributes are additional information that modify the behavior or appearance of the tags.

## Basic Structure of an HTML Document

An HTML document consists of two main parts: the head and the body. The head contains information about the document, such as the title, the character encoding, the style sheets, and the scripts. The body contains the actual content of the document, such as text, images, links, and forms. The head and the body are enclosed by the `<html>` tag, which indicates the beginning and the end of the document. The `<html>` tag also specifies the language of the document using the `lang` attribute. The following is an example of a simple HTML document:

```html
<html lang="en">
<head>
  <title>My First Web Page</title>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="style.css">
  <script src="script.js"></script>
</head>
<body>
  <h1>Hello, World!</h1>
  <p>This is my first web page.</p>
  <img src="image.jpg" alt="A picture of me">
  <a href="https://www.example.com">Visit my website</a>
  <form action="submit.php" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">
    <label for="email">Email:</label>
    <input type="email" id="email" name="email">
    <button type="submit">Submit</button>
  </form>
</body>
</html>
```

## Common HTML Tags and Attributes

There are many HTML tags and attributes that can be used to create different types of web pages and web applications. Some of the most common ones are:

- `<h1>` to `<h6>`: These tags are used to create headings of different levels. The `<h1>` tag creates the most important heading, while the `<h6>` tag creates the least important heading. Headings help to organize the content and make it easier to read and navigate.
- `<p>`: This tag is used to create paragraphs of text. Paragraphs are separated by a blank line or by the closing `</p>` tag.
- `<img>`: This tag is used to insert images into the web page. The `src` attribute specifies the URL of the image file, while the `alt` attribute provides a text alternative for the image in case it cannot be displayed or accessed by the user. The `width` and `height` attributes can be used to resize the image, while the `align` attribute can be used to position the image relative to the text.
- `<a>`: This tag is used to create hyperlinks that link to other web pages or web resources. The `href` attribute specifies the URL of the destination, while the `target` attribute specifies how the link should be opened (e.g. in a new tab or window). The content of the `<a>` tag is the text or image that the user can click on to follow the link.
- `<form>`: This tag is used to create a form that collects user input and sends it to a server for processing. The `action` attribute specifies the URL of the server-side script that handles the form data, while the `method` attribute specifies the HTTP method to use (e.g. GET or POST). The `<form>` tag can contain various input elements, such as `<input>`, `<textarea>`, `<select>`, `<option>`, `<button>`, etc. Each input element has a `name` attribute that identifies the data, and a `value` attribute that specifies the data. The `<label>` tag can be used to provide a text label for the input element, while the `id` and `for` attributes can be used to associate the label with the input element.
- `<div>` and `<span>`: These tags are used to create generic containers for grouping and styling other elements. The `<div>` tag creates a block-level container, while the `<span>` tag creates an