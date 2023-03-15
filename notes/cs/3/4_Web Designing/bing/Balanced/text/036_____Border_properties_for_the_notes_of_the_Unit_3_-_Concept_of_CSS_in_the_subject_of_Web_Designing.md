### Border properties for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- The border properties in CSS are used to style the borders of an element, such as its width, color, style, and radius.
- The border properties can be applied to any element that can have a border, such as `<div>`, `<p>`, `<table>`, `<img>`, etc.
- The border properties can be specified individually for each side of the element, or for all sides at once using the shorthand property `border`.
- The border properties are:

  - `border-width`: Specifies the width of the border, in pixels, ems, or other units. The default value is `medium`. The possible values are `thin`, `medium`, `thick`, or a numeric value.
  - `border-color`: Specifies the color of the border, using a color name, a hexadecimal value, an RGB value, or other color formats. The default value is the current color of the element.
  - `border-style`: Specifies the style of the border, such as solid, dashed, dotted, double, groove, ridge, inset, or outset. The default value is `none`, which means no border.
  - `border-radius`: Specifies the radius of the corners of the border, in pixels, ems, or other units. The default value is `0`, which means square corners. The value can be a single value for all corners, or four values for each corner in the order of top-left, top-right, bottom-right, and bottom-left.

- An example of using the border properties is:

```css
div {
  border-width: 5px;
  border-color: blue;
  border-style: solid;
  border-radius: 10px;
}
```

- This will create a blue solid border with rounded corners for all `<div>` elements.