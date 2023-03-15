Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content in markdown format on the topic of CSS Styling for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing. Here is the content I have generated for you:

# CSS Styling

CSS stands for Cascading Style Sheets. It is a language that is used to define the presentation of HTML elements on a web page. CSS can control the layout, colors, fonts, backgrounds, borders, animations, transitions, and other aspects of the appearance of a web page.

## Benefits of CSS

- CSS separates the content from the presentation, making the HTML code more readable and maintainable.
- CSS allows the web developer to apply consistent styles across multiple web pages, reducing code duplication and saving bandwidth.
- CSS enables the web developer to create responsive web pages that can adapt to different screen sizes and devices, enhancing the user experience and accessibility.
- CSS offers a variety of selectors, properties, values, and units that can be combined to create complex and dynamic styles.

## How to use CSS

There are three ways to use CSS in a web page:

- Inline style: The style attribute is used to apply CSS rules to a single HTML element. For example:

```html
<p style="color: blue; font-size: 20px;">This is a paragraph with inline style.</p>
```

- Internal style: The `<style>` element is used to define CSS rules for the HTML elements within the same document. The `<style>` element is usually placed inside the `<head>` element. For example:

```html
<head>
  <style>
    p {
      color: red;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <p>This is a paragraph with internal style.</p>
</body>
```

- External style: The `<link>` element is used to link an external CSS file to the HTML document. The external CSS file has a .css extension and contains only CSS rules. The `<link>` element is usually placed inside the `<head>` element. For example:

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <p>This is a paragraph with external style.</p>
</body>
```

The external CSS file (style.css) contains:

```css
p {
  color: green;
  font-size: 16px;
}
```

## CSS Syntax

A CSS rule consists of a selector and a declaration block. The selector specifies which HTML elements the rule applies to. The declaration block contains one or more declarations, each consisting of a property and a value. The property specifies the aspect of the element to be styled, and the value specifies the style to be applied. A declaration is separated by a colon (:), and multiple declarations are separated by semicolons (;). A declaration block is enclosed by curly braces ({}). For example:

```css
selector {
  property: value;
  property: value;
}
```

An example of a CSS rule is:

```css
h1 {
  color: white;
  background-color: black;
}
```

This rule applies to all `<h1>` elements in the document, and sets their text color to white and their background color to black.

## CSS Selectors

CSS selectors are used to select the HTML elements that the CSS rules apply to. There are different types of selectors, such as:

- Element selector: Selects all elements of a specific type. For example, `p` selects all `<p>` elements.
- Class selector: Selects all elements that have a specific class attribute. The class selector is preceded by a dot (.). For example, `.intro` selects all elements with `class="intro"`.
- ID selector: Selects a single element that has a specific id attribute. The ID selector is preceded by a hash (#). For example, `#logo` selects the element with `id="logo"`.
- Attribute selector: Selects all elements that have a specific attribute or attribute value. The attribute selector is enclosed by square brackets ([]). For example, `[href]` selects all elements that have an `href` attribute, and `[href="https://www.example.com"]` selects all elements that have an `href` attribute with the value of `https://www.example.com`.
- Pseudo-class selector: Selects elements based on their state or position. The pseudo-class selector is preceded by a colon (:). For example, `:hover` selects elements when the mouse pointer is over them, and `:first-child` selects elements that are the first child of their parent.