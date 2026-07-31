### Border Properties

In CSS, the border properties allow you to specify the style, width, and color of an element's border. These properties are used to create a visual separation between the content of an element and its surroundings.

1. **border-style**: This property specifies the style of the border. The possible values are `none`, `dotted`, `dashed`, `solid`, `double`, `groove`, `ridge`, `inset`, and `outset`.
2. **border-width**: This property specifies the width of the border. The value can be specified in length units such as `px`, `em`, or `%`, or by using one of the predefined values: `thin`, `medium`, or `thick`.
3. **border-color**: This property specifies the color of the border. The value can be specified using a color name, a hexadecimal value, or an RGB value.
4. **border**: This is a shorthand property that allows you to specify the style, width, and color of the border in a single declaration. The values are specified in the order of style, width, and color.

For example, to create a solid red border with a width of 5 pixels, you can use the following CSS code:

```css
border: solid 5px red;
```

You can also specify different values for each side of the border using the `border-top`, `border-right`, `border-bottom`, and `border-left` properties. Each of these properties can take the same values as the `border` property.

For example, to create a dashed top border and a solid bottom border, you can use the following CSS code:

```css
border-top: dashed 3px black;
border-bottom: solid 5px black;
```

These border properties are commonly used in web design to create visually appealing layouts and to separate different sections of a page. They can be applied to any HTML element, including `div`, `p`, and `img` tags.