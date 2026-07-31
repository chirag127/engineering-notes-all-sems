### Controlling Fonts

1. CSS allows you to control the font family, size, weight, style, and color of text.
2. The `font-family` property specifies the font for an element. You can specify a list of fonts separated by commas, and the browser will use the first font in the list that is installed on the user's computer.
3. The `font-size` property sets the size of the text. You can specify the size in pixels, ems, or percentages.
4. The `font-weight` property sets the weight of the font. Common values are normal and bold.
5. The `font-style` property sets the style of the font. Common values are normal, italic, and oblique.
6. The `color` property sets the color of the text. You can specify the color using a color name, a hexadecimal value, or an RGB value.

Example:
```css
p {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 16px;
  font-weight: bold;
  font-style: italic;
  color: #FF0000;
}
```
This example sets the font family, size, weight, style, and color for all `p` elements on a page. The text will be displayed in Arial if it is installed on the user's computer, otherwise, it will fall back to Helvetica or sans-serif. The text will be 16 pixels in size, bold, italic, and red in color.