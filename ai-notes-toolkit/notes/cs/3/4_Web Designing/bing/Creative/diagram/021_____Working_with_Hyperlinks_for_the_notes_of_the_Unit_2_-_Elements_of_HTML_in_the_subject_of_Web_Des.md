Hello, I am Sydney, your AI assistant. I will help you with your notes on the topic of working with hyperlinks for the unit 2 - elements of HTML in the subject of web designing. Here is the content in markdown format:

### Working with Hyperlinks

- Hyperlinks are the essential feature of the web that allow users to navigate from one document to another or to other resources on the web.
- Hyperlinks are created using the `<a>` element, which stands for anchor. The `<a>` element has an attribute called `href`, which stands for hypertext reference. The `href` attribute specifies the URL (uniform resource locator) of the destination document or resource.
- The content of the `<a>` element is the text or image that the user can click on to follow the link. For example:

```html
<a href="https://www.example.com">This is a link to example.com</a>
```

- The URL in the `href` attribute can be absolute or relative. An absolute URL specifies the full address of the destination, including the protocol, domain name, path, and file name. A relative URL specifies the location of the destination relative to the current document, omitting some or all of the components of an absolute URL. For example:

```html
<!-- Absolute URL -->
<a href="https://www.example.com/about.html">About us</a>

<!-- Relative URL -->
<a href="about.html">About us</a>
```

- Relative URLs are useful when linking to documents or resources within the same website, as they are shorter and easier to maintain. However, absolute URLs are necessary when linking to external websites or resources.
- Hyperlinks can also have other attributes, such as `target`, `title`, and `rel`. The `target` attribute specifies where the destination document or resource should open, such as in a new tab or window. The `title` attribute provides additional information about the link, which is usually displayed as a tooltip when the user hovers over the link. The `rel` attribute specifies the relationship between the current document and the destination document or resource, such as `nofollow`, `noopener`, or `noreferrer`.
- Hyperlinks can also be used to link to specific parts of a document, such as headings, paragraphs, or images. This is done by using an `id` attribute on the element that is the target of the link, and using a fragment identifier in the `href` attribute of the link. A fragment identifier is a hash sign (#) followed by the value of the `id` attribute of the target element. For example:

```html
<!-- The target element -->
<h2 id="introduction">Introduction</h2>

<!-- The link to the target element -->
<a href="#introduction">Go to introduction</a>
```