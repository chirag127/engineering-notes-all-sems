### CSS Id and Class

- CSS id and class are two types of selectors that can be used to apply styles to specific elements in an HTML document.
- A CSS id is a unique identifier that can be assigned to only one element in a document. It is written with a hash (#) symbol followed by the id name, for example: `#header`.
- A CSS class is a group of elements that share the same style. It is written with a dot (.) symbol followed by the class name, for example: `.red`.
- To assign an id or a class to an element, use the `id` or `class` attribute in the HTML tag, for example: `<div id="header" class="red">...</div>`.
- To select an element with a specific id or class, use the id or class selector in the CSS rule, for example: `#header {background-color: blue;}` or `.red {color: red;}`.
- An element can have both an id and a class, or multiple classes, but it cannot have multiple ids. For example: `<div id="header" class="red large">...</div>`.
- An id has a higher specificity than a class, which means that if an element has both an id and a class, the style defined by the id will override the style defined by the class. For example: `#header {background-color: blue;}` and `.red {background-color: red;}` will result in a blue background for the element with id="header" and class="red".
- A class can be reused for multiple elements, but an id should be unique for each element. For example: `<div class="red">...</div>` and `<p class="red">...</p>` will both have red text, but `<div id="header">...</div>` and `<p id="header">...</p>` will cause an error.