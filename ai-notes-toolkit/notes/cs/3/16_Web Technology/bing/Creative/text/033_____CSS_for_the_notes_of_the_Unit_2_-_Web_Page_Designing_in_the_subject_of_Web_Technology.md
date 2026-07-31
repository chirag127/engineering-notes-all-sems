### CSS

CSS stands for **Cascading Style Sheets**. It is a style sheet language that is used to format the layout and appearance of a web page. With CSS, you can control various aspects of the web page, such as:

- The color, font, and size of text
- The spacing and alignment of elements
- The background images and colors of elements
- The display and positioning of elements
- The responsiveness and adaptability of the web page to different devices and screen sizes

CSS works by applying styles to HTML elements. You can select HTML elements by using **selectors**, such as element names, classes, ids, or attributes. You can then specify the styles for the selected elements by using **properties** and **values**. For example, this CSS code selects all paragraphs (`<p>`) and sets their text color to red:

```css
p {
  color: red;
}
```

You can write CSS code in three different ways:

- **Inline CSS**: You can use the `style` attribute inside an HTML element to apply CSS styles to that element only. For example:

```html
<p style="color: red;">This is a red paragraph.</p>
```

- **Internal CSS**: You can use the `<style>` element inside the `<head>` section of an HTML document to apply CSS styles to the whole document or a specific part of it. For example:

```html
<head>
  <style>
    p {
      color: red;
    }
  </style>
</head>
<body>
  <p>This is a red paragraph.</p>
  <p>This is another red paragraph.</p>
</body>
```

- **External CSS**: You can use the `<link>` element inside the `<head>` section of an HTML document to link to an external CSS file that contains the CSS styles for the document. For example:

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <p>This is a red paragraph.</p>
  <p>This is another red paragraph.</p>
</body>
```

The external CSS file (`style.css`) would look like this:

```css
p {
  color: red;
}
```

Using external CSS files is the most recommended way of writing CSS code, as it allows you to separate the content and presentation of your web page, and reuse the same CSS code for multiple web pages.

CSS has many features and properties that you can use to create beautiful and functional web pages. Some of the topics that you will learn in this unit are:

- CSS syntax and selectors
- CSS colors and backgrounds
- CSS fonts and text
- CSS box model and layout
- CSS flexbox and grid
- CSS media queries and responsive design
- CSS animations and transitions
- CSS frameworks and preprocessors

To learn more about CSS, you can visit the following websites:

- [W3Schools CSS Tutorial](https://www.w3schools.com/Css/)
- [MDN CSS Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [GeeksforGeeks CSS Introduction](https://www.geeksforgeeks.org/css-introduction/)