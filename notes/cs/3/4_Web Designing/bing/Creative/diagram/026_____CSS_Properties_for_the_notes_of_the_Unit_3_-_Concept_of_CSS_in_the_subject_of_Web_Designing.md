Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Designing. Here are some notes on the topic of CSS Properties for Unit 3 - Concept of CSS.

# CSS Properties

CSS properties are the attributes that define how HTML elements are styled and displayed on a web page. CSS properties are specified in a style sheet, either internally in the `<style>` tag or externally in a separate file. CSS properties are written as key-value pairs, separated by a colon and followed by a semicolon. For example:

```css
h1 {
  color: blue;
  font-size: 36px;
}
```

In this example, `color` and `font-size` are CSS properties, and `blue` and `36px` are their values. The `h1` selector indicates that the properties apply to all `<h1>` elements on the page.

## Types of CSS Properties

There are many types of CSS properties that can be used to style and layout HTML elements. Some of the most common ones are:

- **Color properties**: These properties control the color of the text, background, border, and other elements. Some examples are `color`, `background-color`, `border-color`, `opacity`, etc.
- **Font properties**: These properties control the font family, size, weight, style, and other aspects of the text. Some examples are `font-family`, `font-size`, `font-weight`, `font-style`, etc.
- **Text properties**: These properties control the alignment, spacing, decoration, and other aspects of the text. Some examples are `text-align`, `text-indent`, `text-decoration`, `line-height`, etc.
- **Box model properties**: These properties control the dimensions, margins, padding, and borders of the elements. The box model is a concept that describes how each element is represented as a rectangular box with four layers: content, padding, border, and margin. Some examples are `width`, `height`, `margin`, `padding`, `border`, etc.
- **Layout properties**: These properties control the position, display, and arrangement of the elements. Some examples are `position`, `display`, `float`, `clear`, `flex`, `grid`, etc.
- **Transform properties**: These properties control the transformation of the elements, such as scaling, rotating, skewing, and translating. Some examples are `transform`, `transform-origin`, `transform-style`, etc.
- **Transition properties**: These properties control the animation of the elements when they change their state, such as hover, focus, or click. Some examples are `transition`, `transition-property`, `transition-duration`, `transition-timing-function`, etc.
- **Media query properties**: These properties control the responsiveness of the web page, which means how it adapts to different screen sizes and devices. Media queries are conditional statements that apply different style rules based on certain criteria, such as width, height, orientation, resolution, etc. Some examples are `@media`, `min-width`, `max-width`, `min-height`, `max-height`, etc.

## How to Use CSS Properties

To use CSS properties, you need to follow these steps:

1. Select the HTML element(s) that you want to style using a selector. A selector can be an element name, a class name, an id name, an attribute, a pseudo-class, a pseudo-element, or a combination of them. For example:

```css
/* Select all <p> elements */
p {
  /* CSS properties */
}

/* Select elements with class="intro" */
.intro {
  /* CSS properties */
}

/* Select elements with id="main" */
#main {
  /* CSS properties */
}

/* Select elements with href attribute */
[href] {
  /* CSS properties */
}

/* Select elements that are the first child of their parent */
:first-child {
  /* CSS properties */
}

/* Select elements that are before or after another element */
::before {
  /* CSS properties */
}

::after {
  /* CSS properties */
}
```

2. Specify the CSS properties and their values that you want to apply to the selected element(s). You can use different units, keywords, colors, functions, or variables to define the values. For example:

```css
/* Use pixels as the unit */
p {
  font-size: 16px;
}

/* Use percentages as the unit */
div {
  width: 50%;
}

/* Use keywords as the values */
h1 {
  text-align: center;
}

/* Use colors as the values */
body {
  background-color: white;
}

/* Use functions as the values */
div {
  transform: rotate(45deg);
}

/* Use variables as the values */
:root {
  --main-color: blue;
}

p

```
