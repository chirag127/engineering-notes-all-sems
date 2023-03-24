## Unit 1 - Develop static web pages using HTML

HTML (Hypertext Markup Language) is the basic building block of the World Wide Web. It is the language used to create web pages and provides structure and content to the web pages. In this unit, you will learn how to develop static web pages using HTML.

### Learning Objectives

By the end of this unit, you will be able to:

- Explain the basic structure of an HTML document
- Create a web page using HTML
- Use HTML tags to add structure and content to a web page
- Create links to other pages and external resources
- Add images and multimedia to a web page
- Use CSS to style and format a web page

### Basic Structure of an HTML Document

An HTML document consists of the following elements:

- The `<!DOCTYPE>` declaration that defines the document type and version
- The `<html>` element that contains the entire document
- The `<head>` element that contains information about the document, such as the title and metadata
- The `<body>` element that contains the content of the document

### Creating a Web Page Using HTML

To create a web page using HTML, follow these steps:

1. Open a text editor such as Notepad or Sublime Text.
2. Type the basic structure of an HTML document as described above.
3. Add content to the `<body>` element using HTML tags.
4. Save the file with a `.html` extension.

### Using HTML Tags

HTML tags are used to add structure and content to a web page. Some of the commonly used tags include:

- `<h1>` to `<h6>` for headings
- `<p>` for paragraphs
- `<a>` for links
- `<img>` for images
- `<ul>` and `<li>` for unordered lists
- `<ol>` and `<li>` for ordered lists

### Creating Links

To create a link to another page or external resource, use the `<a>` tag with the `href` attribute. For example:

```
<a href="https://www.example.com">Visit Example.com</a>
```

### Adding Images and Multimedia

To add images to a web page, use the `<img>` tag with the `src` attribute. For example:

```
<img src="image.jpg" alt="Description of the image">
```

To add multimedia such as videos or audio, use the appropriate tags such as `<video>` or `<audio>`.

### Using CSS

CSS (Cascading Style Sheets) is used to style and format a web page. CSS is typically saved in a separate file with a `.css` extension and linked to the HTML document using the `<link>` tag. For example:

```
<head>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
```

In the CSS file, you can use selectors and properties to style elements on the web page. For example:

```
h1 {
  color: red;
  font-size: 24px;
}
```

### Conclusion

In this unit, you learned how to develop static web pages using HTML. You now have the basic knowledge and skills required to create simple web pages. In the next unit, you will learn how to enhance these web pages using CSS.