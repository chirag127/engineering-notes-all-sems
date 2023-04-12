# CSS Properties

CSS properties are used to apply styles or behaviors to HTML elements, such as fonts, colors, spacing, layout, animation, and more. CSS properties are written as key-value pairs, separated by a colon and enclosed in a declaration block. For example:

```css
h1 {
  color: blue;
  font-size: 36px;
}
```

In this example, `color` and `font-size` are CSS properties, and `blue` and `36px` are their values. The declaration block is the part between the curly braces `{ }`.

There are hundreds of CSS properties available, and they can be grouped into different categories based on their function or the type of element they affect. Some of the most common categories are:

- **Text properties**: These properties control the appearance and formatting of text, such as font family, font size, font weight, text alignment, text decoration, text transform, line height, letter spacing, word spacing, text indent, text shadow, and more. For example:

```css
p {
  font-family: Arial, sans-serif;
  font-weight: bold;
  text-align: center;
  text-decoration: underline;
  text-transform: uppercase;
  line-height: 1.5;
  letter-spacing: 2px;
  word-spacing: 4px;
  text-indent: 20px;
  text-shadow: 2px 2px 5px gray;
}
```

- **Color and background properties**: These properties control the color and background of an element, such as background color, background image, background position, background size, background repeat, background attachment, background clip, background origin, background blend mode, border color, outline color, box shadow, and more. For example:

```css
div {
  background-color: yellow;
  background-image: url("flower.png");
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-clip: content-box;
  background-origin: border-box;
  background-blend-mode: multiply;
  border-color: green;
  outline-color: red;
  box-shadow: 10px 10px 20px black;
}
```

- **Box model properties**: These properties control the size and layout of an element, such as width, height, padding, border, margin, box sizing, display, position, top, right, bottom, left, float, clear, overflow, and more. For example:

```css
div {
  width: 300px;
  height: 200px;
  padding: 10px;
  border: 5px solid black;
  margin: 20px;
  box-sizing: border-box;
  display: block;
  position: relative;
  top: 50px;
  left: 100px;
  float: right;
  clear: both;
  overflow: hidden;
}
```

- **Flexbox properties**: These properties control the alignment and distribution of elements in a flexible container, such as flex-direction, flex-wrap, flex-flow, justify-content, align-items, align-content, order, flex-grow, flex-shrink, flex-basis, and more. For example:

```css
.container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  flex-flow: row wrap;
  justify-content: space-between;
  align-items: center;
  align-content: stretch;
}

.item {
  order: 1;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: 100px;
}
```

- **Grid properties**: These properties control the alignment and distribution of elements in a grid container, such as grid-template-columns, grid-template-rows, grid-template-areas, grid-template, grid-column-start, grid-column-end, grid-row-start, grid-row-end, grid-column, grid-row, grid-area, justify-items, align-items, place-items, justify-content, align-content, place-content, justify-self, align-self, place-self, grid-auto-columns, grid-auto-rows, grid-auto-flow, grid, and more. For example:

```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 100px 200px 100px;
  grid-template-areas: 
    "header header header"
    "main main sidebar"
    "footer footer footer";
  grid-template: 
    "header header header" 100px
    "main main sidebar

```
