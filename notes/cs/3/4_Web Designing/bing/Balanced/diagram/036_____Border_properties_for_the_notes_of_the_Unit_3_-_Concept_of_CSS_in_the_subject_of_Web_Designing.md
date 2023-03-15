Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write the content on border properties for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing. Here is the content I have written in markdown format:

# Border Properties

- The border properties in CSS are used to style the borders of an element.
- A border is a line that surrounds an element, separating it from other elements or the background.
- The border properties can be applied to any element that has a display value of block, inline-block, table, or table-cell.
- The border properties can be divided into three categories: border-width, border-style, and border-color.

## Border-width

- The border-width property specifies the width of the border of an element.
- The border-width can be specified in pixels, ems, rems, percentages, or other units of length.
- The border-width can also be specified using one of the following keywords: thin, medium, or thick.
- The border-width can be applied to all four sides of an element, or to each side individually using the properties border-top-width, border-right-width, border-bottom-width, and border-left-width.
- The border-width can also be specified using a shorthand syntax, where one, two, three, or four values can be given, separated by spaces.
- If one value is given, it applies to all four sides of the element.
- If two values are given, the first value applies to the top and bottom sides, and the second value applies to the right and left sides.
- If three values are given, the first value applies to the top side, the second value applies to the right and left sides, and the third value applies to the bottom side.
- If four values are given, they apply to the top, right, bottom, and left sides in that order.

## Border-style

- The border-style property specifies the style of the border of an element.
- The border-style can be specified using one of the following keywords: none, hidden, dotted, dashed, solid, double, groove, ridge, inset, or outset.
- The border-style can be applied to all four sides of an element, or to each side individually using the properties border-top-style, border-right-style, border-bottom-style, and border-left-style.
- The border-style can also be specified using a shorthand syntax, similar to the border-width property.
- If the border-style is none or hidden, the border-width is ignored and no border is drawn.

## Border-color

- The border-color property specifies the color of the border of an element.
- The border-color can be specified using a color name, a hexadecimal value, an RGB value, an RGBA value, an HSL value, an HSLA value, or a keyword such as currentColor or transparent.
- The border-color can be applied to all four sides of an element, or to each side individually using the properties border-top-color, border-right-color, border-bottom-color, and border-left-color.
- The border-color can also be specified using a shorthand syntax, similar to the border-width and border-style properties.
- If the border-color is not specified, the default value is the color of the element.

## Border Shorthand Property

- The border shorthand property is a convenient way to specify the border-width, border-style, and border-color properties in one declaration.
- The syntax of the border shorthand property is as follows:

```css
border: border-width border-style border-color;
```

- The order of the values does not matter, as long as they are valid values for the corresponding properties.
- If one of the values is omitted, the default value for that property is used.
- For example, the following declarations are equivalent:

```css
border: 5px solid red;
border: solid red 5px;
border: red 5px solid;
```

- The border shorthand property can also be applied to each side of an element using the properties border-top, border-right, border-bottom, and border-left.