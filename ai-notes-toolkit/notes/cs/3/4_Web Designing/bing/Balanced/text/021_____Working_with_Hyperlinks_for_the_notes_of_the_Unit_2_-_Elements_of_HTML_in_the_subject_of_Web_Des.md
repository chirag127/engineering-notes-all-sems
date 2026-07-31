### Working with Hyperlinks

- Hyperlinks are the essential feature of the web that allow users to navigate from one document to another.
- Hyperlinks are created using the `<a>` element, which stands for anchor.
- The `<a>` element has an attribute called `href`, which specifies the URL of the destination document.
- The content of the `<a>` element is the text or image that the user can click on to follow the link.
- Example: `<a href="https://www.example.com">Visit Example.com</a>`
- Hyperlinks can also link to other parts of the same document, using the `id` attribute of the target element and the `#` symbol in the `href` attribute.
- Example: `<a href="#section1">Go to Section 1</a>`
- Hyperlinks can also link to other types of resources, such as email addresses, phone numbers, files, etc., using different schemes in the `href` attribute.
- Example: `<a href="mailto:info@example.com">Send an email to info@example.com</a>`
- Hyperlinks can also have other attributes, such as `target`, `title`, `rel`, etc., to modify their behavior and provide additional information.
- Example: `<a href="https://www.example.com" target="_blank" title="Opens in a new tab" rel="noopener noreferrer">Visit Example.com</a>`
- Hyperlinks are styled by default with blue color and underline, but these can be changed using CSS properties, such as `color`, `text-decoration`, `hover`, etc.
- Example: `a { color: red; text-decoration: none; } a:hover { color: green; text-decoration: underline; }`