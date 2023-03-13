CSS stands for Cascading Style Sheets. It is used to format the layout of a webpage, such as the color, font, size, spacing, position, and display of HTML elements . CSS can be applied to HTML elements in three ways: inline, internal, and external.

Inline CSS is when the style attribute is used inside an HTML element. For example:

<p style="color:red;">This is a paragraph with inline CSS.</p>

Internal CSS is when the style element is used inside the head section of an HTML document. For example:

<head>
<style>
p {
  color: blue;
}
</style>
</head>
<body>
<p>This is a paragraph with internal CSS.</p>
</body>

External CSS is when the link element is used to link an external CSS file to an HTML document. For example:

<head>
<link rel="stylesheet" href="style.css">
</head>
<body>
<p>This is a paragraph with external CSS.</p>
</body>

The external CSS file (style.css) would contain the following code:

p {
  color: green;
}

The following diagram illustrates the basic architecture of CSS in web page designing:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   HTML file     |     |   CSS file      |     |   Web browser   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
| <head>          |     | p {             |     |                 |
|   <link rel="   |     |   color: green; |     |                 |
|   stylesheet"   |---->| }               |---->|                 |
|   href="style.  |     |                 |     |                 |
|   css">         |     |                 |     |                 |
| </head>         |     |                 |     |                 |
| <body>          |     |                 |     |                 |
|   <p>This is a  |     |                 |     | This is a       |
|   paragraph     |     |                 |     | paragraph with  |
|   with external |     |                 |     | external CSS.   |
|   CSS.</p>      |     |                 |     |                 |
| </body>         |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```