## Unit 2 - Elements of HTML

HTML stands for HyperText Markup Language. It is the standard language for creating web pages and web applications. HTML consists of elements that define the structure and content of a web page.

- An HTML element is a piece of code that starts with a **start tag** and ends with an **end tag**. For example, `<p>` is the start tag and `</p>` is the end tag for a paragraph element. Some elements do not have an end tag, such as `<img>` for an image element. These are called **self-closing elements**.
- An HTML element can have **attributes** that provide additional information about the element. Attributes are written inside the start tag, after the element name, and consist of a name and a value. For example, `<img src="logo.png" alt="Logo">` is an image element with two attributes: `src` and `alt`. The `src` attribute specifies the source of the image, and the `alt` attribute specifies the alternative text for the image.
- An HTML element can contain **text** or **other elements** as its content. For example, `<p>This is a paragraph.</p>` is a paragraph element with text as its content, and `<div><h1>Title</h1><p>Paragraph</p></div>` is a division element with two other elements as its content: a heading element and a paragraph element. The content of an element is written between the start tag and the end tag, unless the element is self-closing.
- HTML elements are organized in a **hierarchical** and **nested** structure, forming a **tree** of elements. The root element of the tree is the `<html>` element, which contains two child elements: the `<head>` element and the `<body>` element. The `<head>` element contains information about the web page, such as the title, the character encoding, and the links to external resources. The `<body>` element contains the visible content of the web page, such as headings, paragraphs, images, links, forms, etc. Each element can have zero or more child elements, forming a branch of the tree. An element can only have one parent element, except for the root element, which has no parent. The parent and child elements are also called **ancestor** and **descendant** elements, respectively. An element that has the same parent as another element is called a **sibling** element. For example, in the following HTML code, the `<h1>` element is the child of the `<body>` element, the ancestor of the `<span>` element, and the sibling of the `<p>` element.

```html
<html>
<head>
  <title>Example</title>
</head>
<body>
  <h1>This is a <span>heading</span></h1>
  <p>This is a paragraph.</p>
</body>
</html>
```

- HTML elements can be classified into different categories based on their function and appearance. Some of the common categories are:

  - **Metadata elements**: These elements provide information about the web page, such as the title, the character encoding, the links to external resources, the keywords, the description, etc. They are usually placed inside the `<head>` element. Some examples of metadata elements are `<title>`, `<meta>`, `<link>`, `<style>`, `<script>`, etc.
  - **Sectioning elements**: These elements define the logical sections or regions of the web page, such as the header, the footer, the main content, the navigation, the sidebar, the article, the section, etc. They are usually placed inside the `<body>` element. Some examples of sectioning elements are `<header>`, `<footer>`, `<main>`, `<nav>`, `<aside>`, `<article>`, `<section>`, etc.
  - **Heading elements**: These elements define the titles or headings of the sections or regions of the web page. They are usually placed inside the sectioning elements. There are six levels of heading elements, from `<h1>` to `<h6>`, with `<h1>` being the most important and `<h6>` being the least important. For example, `<h1>Example</h1>` defines the main title of the web page, and `<h2>Subsection</h2>` defines the title of a subsection.
  - **Text elements**: These elements define the text content of the web page, such as paragraphs, lists, tables, quotations, etc. They are usually placed inside the sectioning elements or the heading elements. Some examples of text elements are `<p>`, `<ul>`, `<ol>`, `<li>