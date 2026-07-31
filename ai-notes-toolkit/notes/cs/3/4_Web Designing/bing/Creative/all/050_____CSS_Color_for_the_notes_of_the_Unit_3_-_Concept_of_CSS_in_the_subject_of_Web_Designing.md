Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of CSS Color for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing.

# CSS Color

- CSS color is a property that sets the color of an element's text, background, border, or other parts.
- CSS color can be specified by using a predefined color name, a hexadecimal value, an RGB value, an HSL value, or a color keyword.
- CSS color can also be modified by using the opacity property, which sets the transparency of an element or its color.
- CSS color can be applied to any HTML element using a selector, such as an element selector, a class selector, an id selector, or a pseudo-class selector.

## Predefined color names

- CSS supports 140 predefined color names, such as `red`, `green`, `blue`, `yellow`, `pink`, `purple`, etc.
- Predefined color names are case-insensitive, meaning that `Red` and `red` are the same color.
- Predefined color names are easy to use and remember, but they have some limitations, such as not being able to create custom colors or shades.
- To use a predefined color name, simply assign it to the color property of an element, for example:

```css
p {
  color: red;
}
```

- This will make the text of all `<p>` elements red.

## Hexadecimal values

- Hexadecimal values are six-digit codes that represent the amount of red, green, and blue in a color, using the symbols 0-9 and A-F.
- Hexadecimal values start with a `#` sign, followed by three pairs of digits, each representing the red, green, and blue components of the color, in that order.
- Hexadecimal values can range from `#000000` (black) to `#FFFFFF` (white), and any color in between.
- Hexadecimal values are more precise and flexible than predefined color names, as they can create any color by adjusting the values of the three components.
- To use a hexadecimal value, assign it to the color property of an element, for example:

```css
p {
  color: #FF0000;
}
```

- This will make the text of all `<p>` elements red, but with a different shade than the predefined color name `red`.

## RGB values

- RGB values are numerical values that represent the amount of red, green, and blue in a color, using the format `rgb(red, green, blue)`.
- RGB values can range from 0 to 255 for each component, where 0 means no color and 255 means full color.
- RGB values are similar to hexadecimal values, but they use decimal numbers instead of hexadecimal symbols.
- RGB values are also precise and flexible, as they can create any color by adjusting the values of the three components.
- To use an RGB value, assign it to the color property of an element, for example:

```css
p {
  color: rgb(255, 0, 0);
}
```

- This will make the text of all `<p>` elements red, but with the same shade as the hexadecimal value `#FF0000`.

## HSL values

- HSL values are numerical values that represent the hue, saturation, and lightness of a color, using the format `hsl(hue, saturation%, lightness%)`.
- Hue is the degree of the color on a color wheel, ranging from 0 to 360, where 0 is red, 120 is green, and 240 is blue.
- Saturation is the intensity of the color, ranging from 0% (gray) to 100% (full color).
- Lightness is the brightness of the color, ranging from 0% (black) to 100% (white).
- HSL values are different from RGB and hexadecimal values, as they use a color model based on human perception rather than computer representation.
- HSL values are also precise and flexible, as they can create any color by adjusting the values of the three components.
- To use an HSL value, assign it to the color property of an element, for example:

```css
p {
  color: hsl(0, 100%, 50%);
}
```

- This will make the text of all `<p>` elements red, but with the same shade as the RGB value `rgb(255, 0, 0)`.

## Color keywords

- Color keywords are special words that represent a color or a shade of a color, such as `transparent`, `currentcolor`, or `inherit`.
- Transparent