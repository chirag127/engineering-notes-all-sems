### Basic structure of an HTML document

An HTML document is a text file that contains markup tags that define the structure and content of a web page. The basic structure of an HTML document includes the following elements:

1. **DOCTYPE declaration:** This declaration specifies the version of HTML used in the document and is placed at the very beginning of the HTML file. For example, `<!DOCTYPE html>` specifies that the document is written in HTML5.

2. **HTML element:** The `<html>` element is the root element of an HTML page and encloses all other elements in the document. It has an opening tag `<html>` and a closing tag `</html>`.

3. **Head element:** The `<head>` element contains information about the document, such as the title, meta information, and links to stylesheets and scripts. It has an opening tag `<head>` and a closing tag `</head>`.

4. **Body element:** The `<body>` element contains the main content of the document, such as text, images, and links. It has an opening tag `<body>` and a closing tag `</body>`.

5. **Title element:** The `<title>` element specifies the title of the document, which is displayed in the browser's title bar or tab. It is placed within the `<head>` element and has an opening tag `<title>` and a closing tag `</title>`.

6. **Meta element:** The `<meta>` element provides metadata about the HTML document, such as the character encoding and keywords for search engines. It is placed within the `<head>` element and is a self-closing tag, such as `<meta charset="UTF-8">`.

7. **Link element:** The `<link>` element is used to link to external resources, such as stylesheets. It is placed within the `<head>` element and is a self-closing tag, such as `<link rel="stylesheet" href="styles.css">`.

8. **Script element:** The `<script>` element is used to include JavaScript code or to link to an external JavaScript file. It can be placed within the `<head>` or `<body>` element and has an opening tag `<script>` and a closing tag `</script>`.

Here is an example of a basic HTML document structure:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Web Page</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <h1>Welcome to my web page</h1>
    <p>This is some text on my web page.</p>
    <script src="script.js"></script>
  </body>
</html>
```