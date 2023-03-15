Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of CSS Color for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing.

# CSS Color

- CSS color is a property that sets the color of an element's text, background, border, or other parts.
- CSS color can be specified by using a predefined color name, a hexadecimal value, an RGB value, an HSL value, or a color keyword.
- CSS color can also be modified by using the opacity property, which sets the transparency of an element or its color.
- CSS color can be applied to any element in HTML, such as headings, paragraphs, lists, tables, images, links, etc.

## CSS Color Syntax

- The syntax for CSS color is:

```css
selector {
  color: value;
}
```

- The selector is the HTML element that you want to style.
- The color property is the CSS property that sets the color of the element.
- The value is the color value that you want to apply to the element.

## CSS Color Values

- There are different ways to specify a color value in CSS, such as:

### Color Names

- CSS color names are predefined names that represent a specific color, such as red, blue, green, etc.
- There are 140 color names defined in CSS, which you can find here: https://www.w3schools.com/cssref/css_colors.asp
- To use a color name, simply write the name of the color as the value of the color property, for example:

```css
h1 {
  color: red;
}
```

### Hexadecimal Values

- CSS hexadecimal values are six-digit codes that represent a color, starting with a hash sign (#).
- Each digit can be a number from 0 to 9 or a letter from A to F, which corresponds to a value from 10 to 15.
- The first two digits represent the red component, the next two digits represent the green component, and the last two digits represent the blue component of the color.
- To use a hexadecimal value, write the hash sign (#) followed by the six-digit code as the value of the color property, for example:

```css
p {
  color: #FF0000;
}
```

### RGB Values

- CSS RGB values are numerical values that represent the amount of red, green, and blue in a color, using the rgb() function.
- Each value can be an integer from 0 to 255 or a percentage from 0% to 100%, where 0 means no color and 255 or 100% means full color.
- The rgb() function takes three parameters, separated by commas, which are the red, green, and blue values of the color.
- To use an RGB value, write the rgb() function with the three parameters as the value of the color property, for example:

```css
li {
  color: rgb(255, 0, 0);
}
```

### HSL Values

- CSS HSL values are numerical values that represent the hue, saturation, and lightness of a color, using the hsl() function.
- The hue is the degree of the color on a color wheel, from 0 to 360, where 0 is red, 120 is green, and 240 is blue.
- The saturation is the intensity of the color, from 0% to 100%, where 0% is gray and 100% is full color.
- The lightness is the brightness of the color, from 0% to 100%, where 0% is black and 100% is white.
- The hsl() function takes three parameters, separated by commas, which are the hue, saturation, and lightness values of the color.
- To use an HSL value, write the hsl() function with the three parameters as the value of the color property, for example:

```css
a {
  color: hsl(0, 100%, 50%);
}
```

### Color Keywords

- CSS color keywords are special words that represent a color, such as transparent, currentColor, or inherit.
- The transparent keyword sets the color to be fully transparent, which means it is invisible.
- The currentColor keyword sets the color to be the same as the current color of the element, which is usually inherited from its parent element.
- The inherit keyword sets the color to be the same as the color of the parent element, which can be useful for overriding other color values.
- To use a color keyword, simply write the keyword as the value of the color property, for example:

```css
div {