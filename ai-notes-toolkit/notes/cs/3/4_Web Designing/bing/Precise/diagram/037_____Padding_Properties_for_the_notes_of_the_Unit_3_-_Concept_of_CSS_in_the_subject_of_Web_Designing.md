### Padding Properties

Padding is the space between the content of an element and its border. It is used to create space within an element. The padding property is a shorthand property for setting the padding on all four sides of an element at once. The individual padding properties are `padding-top`, `padding-right`, `padding-bottom`, and `padding-left`.

- The `padding` property can take one to four values, which represent the padding for the top, right, bottom, and left sides of an element, respectively.
- If only one value is specified, it applies to all four sides.
- If two values are specified, the first value applies to the top and bottom, and the second value applies to the right and left.
- If three values are specified, the first value applies to the top, the second value applies to the right and left, and the third value applies to the bottom.
- If four values are specified, they apply to the top, right, bottom, and left, in that order.
- The values can be specified in pixels, ems, or percentages.
- Negative values are not allowed.

Example:
```css
div {
  padding: 10px 20px 30px 40px;
}
```
This sets the top padding to 10px, the right padding to 20px, the bottom padding to 30px, and the left padding to 40px.