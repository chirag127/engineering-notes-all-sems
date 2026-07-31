Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of Text Format for the Unit 3 - Concept of CSS in the subject of Web Designing. Here is the content in markdown format:

# Text Format

- Text format refers to the appearance and style of text elements on a web page, such as font, color, size, alignment, etc.
- Text format can be controlled by using CSS (Cascading Style Sheets), which is a language that defines how HTML elements are displayed on the screen.
- CSS can be applied to text elements in three ways: inline, internal, and external.

## Inline CSS

- Inline CSS is the method of applying CSS rules directly to an HTML element using the `style` attribute.
- Inline CSS has the highest specificity, which means it overrides any other CSS rules that apply to the same element.
- Inline CSS is useful for applying quick and simple styles to a single element, but it is not recommended for large or complex web pages, as it makes the HTML code messy and hard to maintain.
- Example of inline CSS:

```html
<p style="color: red; font-size: 20px;">This is a paragraph with inline CSS.</p>
```

## Internal CSS

- Internal CSS is the method of applying CSS rules to an entire HTML document using the `<style>` tag, which is placed inside the `<head>` section of the HTML document.
- Internal CSS has a lower specificity than inline CSS, which means it can be overridden by inline CSS rules that apply to the same element.
- Internal CSS is useful for applying consistent styles to a single web page, but it is not recommended for multiple web pages, as it requires repeating the same CSS code in each HTML document.
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

- External CSS is the method of applying CSS rules to multiple HTML documents using a separate CSS file, which is linked to the HTML documents using the `<link>` tag, which is placed inside the `<head>` section of the HTML document.
- External CSS has the lowest specificity, which means it can be overridden by inline or internal CSS rules that apply to the same element.
- External CSS is the most recommended and efficient way of applying styles to web pages, as it allows reusing the same CSS code for multiple HTML documents, and makes the HTML code cleaner and easier to maintain.
- Example of external CSS:

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <p>This is a paragraph with external CSS.</p>
</body>
```

```css
/* style.css file */
p {
  color: green;
  font-size: 16px;
}
```