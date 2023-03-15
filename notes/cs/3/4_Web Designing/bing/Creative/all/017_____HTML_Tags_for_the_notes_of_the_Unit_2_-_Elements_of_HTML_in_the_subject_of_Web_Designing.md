# HTML Tags

HTML tags are like keywords that define how a web browser will format and display the content of a web page. HTML tags are used to create HTML elements, which are the building blocks of HTML documents. HTML tags consist of three main parts: an opening tag, a closing tag, and the content between them. Some HTML tags are self-closing, which means they do not have a closing tag.

## Examples of HTML Tags

- The `<html>` tag is the root element of an HTML document. It contains the `<head>` and `<body>` elements, which hold the metadata and the visible content of the web page, respectively.
- The `<p>` tag is used to create a paragraph element, which contains text content. The text content is automatically wrapped to fit the width of the web page.
- The `<img>` tag is used to embed an image element, which displays an image from a specified source. The `<img>` tag is a self-closing tag, which means it does not need a closing tag. The `<img>` tag has a required attribute `src`, which specifies the URL of the image file.
- The `<a>` tag is used to create a hyperlink element, which links to another web page or a location within the same web page. The `<a>` tag has a required attribute `href`, which specifies the URL of the destination. The content of the `<a>` tag is the text or image that the user can click on to follow the link.

## Syntax of HTML Tags

The syntax of HTML tags is as follows:

- An opening tag starts with a left angle bracket `<`, followed by the tag name, followed by zero or more attributes, followed by a right angle bracket `>`.
- A closing tag starts with a left angle bracket `<`, followed by a forward slash `/`, followed by the tag name, followed by a right angle bracket `>`.
- A self-closing tag starts with a left angle bracket `<`, followed by the tag name, followed by zero or more attributes, followed by a forward slash `/`, followed by a right angle bracket `>`.
- The content of an HTML tag is the text or HTML elements that are placed between the opening and closing tags, or after the self-closing tag.
- The attributes of an HTML tag are additional information that modify the behavior or appearance of the HTML element. Attributes are specified as name-value pairs, separated by an equal sign `=`. The value of an attribute can be enclosed in single quotes `'` or double quotes `"`, or left unquoted if it does not contain any spaces or special characters.

## Example of HTML Document

The following is an example of a simple HTML document that uses some HTML tags:

```html
<html>
<head>
  <title>My First Web Page</title>
</head>
<body>
  <h1>Hello, World!</h1>
  <p>This is my first web page.</p>
  <img src="image.jpg" alt="A picture of me" />
  <p>You can learn more about HTML <a href="https://www.w3schools.com/html/">here</a>.</p>
</body>
</html>
```

## References

- [HTML Tags - javatpoint](https://www.javatpoint.com/html-tags)
- [What is an HTML Tag? | DigitalOcean](https://www.digitalocean.com/community/tutorials/what-is-an-html-tag)
- [HTML Reference - W3Schools](https://www.w3schools.com/TAGs/)