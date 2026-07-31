# CSS

CSS stands for Cascading Style Sheets. It is a style sheet language that is used to format the layout and appearance of web pages. CSS can control various aspects of web design, such as:

- The color, font, and size of text
- The spacing and alignment of elements
- The background images and colors of elements
- The display and positioning of elements
- The responsiveness and adaptability of web pages to different devices and screen sizes

CSS can be applied to HTML elements in three ways:

- Inline style: using the `style` attribute inside an HTML tag
- Internal style: using the `<style>` tag inside the `<head>` section of an HTML document
- External style: using the `<link>` tag to link to an external CSS file

CSS uses selectors to target specific HTML elements and apply styles to them. A selector can be an element name, an id, a class, or a combination of them. For example, this CSS selector targets all `<p>` elements and sets their color to red:

```css
p {
  color: red;
}
```

CSS also uses properties and values to define the styles for each selector. A property is a specific aspect of an element that can be styled, such as `color`, `font-size`, `margin`, etc. A value is the choice of style for that property, such as `red`, `16px`, `10px`, etc. For example, this CSS property and value sets the font size of all `<h1>` elements to 32 pixels:

```css
h1 {
  font-size: 32px;
}
```

CSS can also use units to specify the size, length, or position of an element. There are two types of units: absolute and relative. Absolute units are fixed and do not depend on the context, such as `px`, `cm`, `in`, etc. Relative units are flexible and depend on the context, such as `%`, `em`, `rem`, `vw`, etc. For example, this CSS unit sets the width of a `<div>` element to 50% of its parent element:

```css
div {
  width: 50%;
}
```

CSS can also use pseudo-classes and pseudo-elements to style elements based on their state or position. A pseudo-class is a keyword that starts with a colon (`:`) and modifies the selector, such as `:hover`, `:active`, `:first-child`, etc. A pseudo-element is a keyword that starts with two colons (`::`) and creates a virtual element, such as `::before`, `::after`, `::first-line`, etc. For example, this CSS pseudo-class changes the color of a `<button>` element when the user hovers over it:

```css
button:hover {
  color: blue;
}
```

CSS can also use media queries to apply different styles based on the media type, device, or screen size. A media query is a logical expression that starts with the `@media` keyword and contains a media type and one or more media features, such as `screen`, `max-width`, `orientation`, etc. For example, this CSS media query changes the font size of all `<p>` elements to 12 pixels when the screen width is less than or equal to 600 pixels:

```css
@media screen and (max-width: 600px) {
  p {
    font-size: 12px;
  }
}
```

These are some of the basic concepts of CSS. To learn more about CSS, you can refer to the following sources:

- [W3Schools CSS Tutorial](https://www.w3schools.com/Css/)
- [MDN CSS Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [GeeksforGeeks CSS Introduction](https://www.geeksforgeeks.org/css-introduction/)