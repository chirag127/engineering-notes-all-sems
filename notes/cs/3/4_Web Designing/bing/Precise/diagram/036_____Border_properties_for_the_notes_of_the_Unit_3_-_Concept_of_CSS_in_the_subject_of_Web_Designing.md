### Border Properties

In CSS, the border properties allow you to specify the style, width, and color of an element's border. Here are the main properties used to style borders:

1. `border-style`: This property specifies the style of the border. The values can be `none`, `dotted`, `dashed`, `solid`, `double`, `groove`, `ridge`, `inset`, or `outset`.
2. `border-width`: This property specifies the width of the border. The values can be specified in length units such as `px`, `em`, or `rem`, or by using one of the predefined values: `thin`, `medium`, or `thick`.
3. `border-color`: This property specifies the color of the border. The values can be specified using color names, hexadecimal values, RGB values, or HSL values.
4. `border`: This is a shorthand property that allows you to specify the style, width, and color of the border in a single declaration. The values are specified in the order of style, width, and color.

These properties can be applied to all four sides of an element's border, or to individual sides using the `border-top`, `border-right`, `border-bottom`, and `border-left` properties. Additionally, the `border-radius` property can be used to create rounded corners on an element's border.

Here is an example of how to use these properties to create a solid red border with a width of 5 pixels and rounded corners:

```css
.example {
  border-style: solid;
  border-width: 5px;
  border-color: red;
  border-radius: 10px;
}
```

This is a brief overview of the border properties in CSS. These properties are an important part of the concept of CSS and can be used to create visually appealing designs for web pages.