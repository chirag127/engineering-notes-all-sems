Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content in markdown format on the topic of CSS Properties for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing. Here is the content:

# CSS Properties

CSS properties are the attributes that define how HTML elements are styled and displayed on a web page. CSS properties are specified in the form of property: value pairs, and are applied to HTML elements using selectors. For example, the following CSS rule sets the color of all paragraphs to blue:

```css
p {
  color: blue;
}
```

In this rule, `p` is the selector, `color` is the property, and `blue` is the value.

## Types of CSS Properties

There are many types of CSS properties that can be used to style different aspects of HTML elements, such as:

- **Text properties**: These properties control the appearance of text, such as font, size, color, alignment, spacing, decoration, etc. For example, the following CSS rule sets the font family, size, and weight of all headings to Arial, 24px, and bold, respectively:

```css
h1, h2, h3, h4, h5, h6 {
  font-family: Arial;
  font-size: 24px;
  font-weight: bold;
}
```

- **Background properties**: These properties control the background of HTML elements, such as color, image, position, size, repeat, etc. For example, the following CSS rule sets the background color of the body element to light gray, and the background image of the header element to a URL, with no repeat and center alignment:

```css
body {
  background-color: lightgray;
}

header {
  background-image: url("logo.png");
  background-repeat: no-repeat;
  background-position: center;
}
```

- **Border properties**: These properties control the border of HTML elements, such as width, style, color, radius, etc. For example, the following CSS rule sets the border of all images to 5px solid black, and the border radius to 10px:

```css
img {
  border: 5px solid black;
  border-radius: 10px;
}
```

- **Box model properties**: These properties control the dimensions and spacing of HTML elements, such as width, height, margin, padding, etc. For example, the following CSS rule sets the width of the main element to 80% of the parent element, and the margin and padding to 20px:

```css
main {
  width: 80%;
  margin: 20px;
  padding: 20px;
}
```

- **Layout properties**: These properties control the layout and positioning of HTML elements, such as display, position, float, clear, etc. For example, the following CSS rule sets the display of the nav element to block, the position to fixed, the top and left to 0, and the width to 100%:

```css
nav {
  display: block;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
}
```

- **Animation properties**: These properties control the animation of HTML elements, such as transition, transform, animation, etc. For example, the following CSS rule sets the transition of the button element to 0.5s, and the transform to rotate 90 degrees when hovered:

```css
button {
  transition: 0.5s;
}

button:hover {
  transform: rotate(90deg);
}
```

## Syntax and Rules of CSS Properties

The syntax and rules of CSS properties are as follows:

- CSS properties are case-insensitive, but it is a good practice to use lowercase letters for consistency and readability.
- CSS properties are separated by semicolons (;) and enclosed by curly braces ({}) in a CSS rule.
- CSS properties can be written in any order, but it is a good practice to group related properties together and follow a logical order.
- CSS properties can have one or more values, separated by commas (,) or spaces. For example, the `border` property can have three values: width, style, and color.
- CSS properties can have different units of measurement, such as pixels (px), percentages (%), ems (em), rems (rem), etc. For example, the `font-size` property can have a value of 16px or 1.5em.
- CSS properties can have different data types, such as colors, numbers, strings, URLs, etc. For example, the `color` property can have