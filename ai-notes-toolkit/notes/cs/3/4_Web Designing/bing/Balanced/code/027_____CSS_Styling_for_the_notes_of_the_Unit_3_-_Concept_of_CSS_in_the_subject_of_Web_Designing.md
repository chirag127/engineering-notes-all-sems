# CSS Styling

- CSS stands for Cascading Style Sheets. It is a language that describes how HTML elements are displayed on a web page.
- CSS can be used to control the layout, colors, fonts, backgrounds, borders, margins, padding, and other aspects of the presentation of HTML elements.
- CSS can be applied to HTML elements in three ways: inline, internal, and external.
  - Inline CSS: The style attribute is used to add CSS rules directly to an HTML element. For example: `<p style="color: blue;">This is a blue paragraph.</p>`
  - Internal CSS: The `<style>` tag is used to add CSS rules inside the `<head>` section of an HTML document. For example: `<style> p {color: blue;} </style>`
  - External CSS: The `<link>` tag is used to link an external CSS file to an HTML document. For example: `<link rel="stylesheet" href="style.css">`
- CSS rules consist of two parts: a selector and a declaration.
  - A selector is the HTML element that the CSS rule applies to. For example: `p`, `h1`, `div`, etc.
  - A declaration is a pair of property and value that defines how the selector should be styled. For example: `color: blue;`, `font-size: 20px;`, `background-color: yellow;`, etc.
  - A declaration is enclosed in curly braces and separated by a semicolon. For example: `p {color: blue; font-size: 20px;}`
  - A CSS rule can have one or more declarations. For example: `h1 {color: red; text-align: center; font-family: Arial;}`
- CSS rules can be grouped together by using commas. For example: `p, h1, div {color: green;}`
- CSS rules can be nested inside another CSS rule by using a descendant selector. For example: `div p {color: purple;}` means that only the `<p>` elements inside a `<div>` element will be purple.
- CSS rules can be made more specific by using a class or an id selector. For example: `p.intro {font-style: italic;}` means that only the `<p>` elements with the class attribute `intro` will be italic. Similarly, `p#first {font-weight: bold;}` means that only the `<p>` element with the id attribute `first` will be bold.
- CSS rules can be made more dynamic by using a pseudo-class or a pseudo-element selector. For example: `a:hover {color: orange;}` means that the `<a>` elements will change color to orange when the mouse pointer hovers over them. Similarly, `p::first-line {text-decoration: underline;}` means that the first line of the `<p>` elements will be underlined.