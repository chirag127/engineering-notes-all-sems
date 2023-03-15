# CSS Styling

## Introduction

- CSS stands for Cascading Style Sheets. It is a language that describes how HTML elements are displayed on a web page.
- CSS can be used to control the layout, colors, fonts, backgrounds, borders, margins, padding, and other aspects of the appearance of a web page.
- CSS can be applied to HTML elements in three ways: inline, internal, and external.

## Inline CSS

- Inline CSS is when the style attribute is used to apply CSS rules directly to an HTML element.
- Inline CSS has the highest specificity, meaning it overrides any other CSS rules that might apply to the same element.
- Inline CSS is useful for applying quick and simple styles to a single element, but it is not recommended for creating consistent and maintainable web pages.
- Example of inline CSS:

```html
<p style="color: red; font-size: 20px;">This is a paragraph with inline CSS.</p>
```

## Internal CSS

- Internal CSS is when the `<style>` tag is used to embed CSS rules inside the `<head>` section of an HTML document.
- Internal CSS has a lower specificity than inline CSS, but a higher specificity than external CSS. It can be overridden by inline CSS, but it can override external CSS.
- Internal CSS is useful for applying styles to a single web page, but it is not recommended for creating consistent and maintainable web pages across multiple pages.
- Example of internal CSS:

```html
<head>
  <style>
    p {
      color: blue;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <p>This is a paragraph with internal CSS.</p>
</body>
```

## External CSS

- External CSS is when the `<link>` tag is used to link an external CSS file to an HTML document.
- External CSS has the lowest specificity, meaning it can be overridden by any other CSS rules that might apply to the same element.
- External CSS is the most recommended way of applying styles to web pages, as it allows for creating consistent and maintainable web pages across multiple pages and sites.
- Example of external CSS:

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <p>This is a paragraph with external CSS.</p>
</body>
```

- The external CSS file (style.css) contains the following CSS rules:

```css
p {
  color: green;
  font-size: 16px;
}
```