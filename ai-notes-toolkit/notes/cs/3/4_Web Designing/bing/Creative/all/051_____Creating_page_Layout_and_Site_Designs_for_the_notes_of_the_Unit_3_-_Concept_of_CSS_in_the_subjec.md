# Creating page Layout and Site Designs

## Concept of CSS

CSS stands for Cascading Style Sheets. It is a language that describes how HTML elements are displayed on a web page. CSS can control the layout, colors, fonts, backgrounds, borders, margins, padding, and other aspects of the presentation of a web page.

CSS can be applied to HTML elements in three ways:

- Inline style: The style attribute is used to apply CSS rules to a single HTML element. For example: `<p style="color: blue;">This is a blue paragraph.</p>`
- Internal style: The `<style>` element is used to apply CSS rules to a specific HTML document. The `<style>` element is placed inside the `<head>` section of the HTML document. For example:

```
<head>
  <style>
    p {
      color: red;
    }
  </style>
</head>
<body>
  <p>This is a red paragraph.</p>
</body>
```

- External style: The `<link>` element is used to link an external CSS file to an HTML document. The external CSS file has a .css extension and contains the CSS rules for the HTML document. The `<link>` element is placed inside the `<head>` section of the HTML document. For example:

```
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <p>This is a paragraph styled by an external CSS file.</p>
</body>
```

CSS uses selectors to target HTML elements and apply style rules to them. A selector can be an element name, an id, a class, or a combination of them. For example:

- `p` is a selector that targets all `<p>` elements in the HTML document.
- `#intro` is a selector that targets the element with the id attribute of "intro" in the HTML document.
- `.highlight` is a selector that targets all elements with the class attribute of "highlight" in the HTML document.
- `p.highlight` is a selector that targets all `<p>` elements with the class attribute of "highlight" in the HTML document.

CSS rules consist of a selector and a declaration block. The declaration block contains one or more declarations, each of which consists of a property and a value. The property specifies the aspect of the element to be styled, and the value specifies the value of the property. For example:

```
p {
  color: green;
  font-size: 20px;
}
```

This CSS rule applies to all `<p>` elements in the HTML document. The declaration block contains two declarations: one that sets the color property to green, and one that sets the font-size property to 20 pixels.

CSS can create different layouts and designs for web pages by using various properties and values. Some of the common properties and values used for creating layouts and designs are:

- `display`: This property specifies how an element is displayed on the web page. The possible values are: `block`, `inline`, `inline-block`, `none`, `flex`, `grid`, etc. For example: `display: block;` makes an element occupy the entire width of its parent element, while `display: inline;` makes an element occupy only the space needed for its content.
- `position`: This property specifies how an element is positioned on the web page. The possible values are: `static`, `relative`, `absolute`, `fixed`, `sticky`, etc. For example: `position: static;` makes an element stay in its normal position in the document flow, while `position: absolute;` makes an element positioned relative to its nearest positioned ancestor element.
- `float`: This property specifies how an element is floated on the web page. The possible values are: `left`, `right`, `none`, `inherit`, etc. For example: `float: left;` makes an element float to the left of its containing element, while `float: none;` makes an element not float at all.
- `clear`: This property specifies how an element is cleared of the floating elements on the web page. The possible values are: `left`, `right`, `both`, `none`, `inherit`, etc. For example: `clear: both;` makes an element clear both the left and the right floating elements, while `clear: none;` makes an element not clear any floating elements.
- `width` and `height`: These properties specify the width and height of an element on the web page. The values can be specified in pixels, percentages, ems, rems, vw, vh, etc. For example: `width: 50%;` makes an element occupy half of the width of its parent element, while `height: