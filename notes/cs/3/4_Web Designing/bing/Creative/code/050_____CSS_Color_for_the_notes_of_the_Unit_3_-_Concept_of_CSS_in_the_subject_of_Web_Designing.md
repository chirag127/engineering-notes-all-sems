Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Designing. Here are some notes on the topic of CSS Color for Unit 3 - Concept of CSS.

### CSS Color

- CSS color is a property that sets the color of an element's text, background, border, or other parts.
- CSS color can be specified by using predefined color names, hexadecimal values, RGB values, HSL values, or color keywords.
- CSS color can also be modified by using opacity, filters, gradients, or blending modes.

#### Predefined color names

- CSS supports 140 predefined color names, such as `red`, `green`, `blue`, `yellow`, `black`, `white`, etc.
- To use a predefined color name, simply assign it to the color property of an element, for example:

```css
p {
  color: red;
}
```

- This will make the text of all `<p>` elements red.

#### Hexadecimal values

- Hexadecimal values are six-digit codes that represent the amount of red, green, and blue in a color, prefixed with a `#` sign.
- Each digit can be a number from 0 to 9 or a letter from A to F, where 0 is the lowest intensity and F is the highest intensity.
- For example, `#FF0000` is pure red, `#00FF00` is pure green, `#0000FF` is pure blue, `#FFFFFF` is white, and `#000000` is black.
- To use a hexadecimal value, assign it to the color property of an element, for example:

```css
p {
  color: #FF0000;
}
```

- This will make the text of all `<p>` elements red.

#### RGB values

- RGB values are numerical values that represent the amount of red, green, and blue in a color, ranging from 0 to 255.
- To use an RGB value, use the `rgb()` function and pass the three values as parameters, separated by commas, for example:

```css
p {
  color: rgb(255, 0, 0);
}
```

- This will make the text of all `<p>` elements red.

- Alternatively, you can use percentage values instead of numbers, ranging from 0% to 100%, for example:

```css
p {
  color: rgb(100%, 0%, 0%);
}
```

- This will also make the text of all `<p>` elements red.

#### HSL values

- HSL values are numerical values that represent the hue, saturation, and lightness of a color, using the HSL color model.
- Hue is the degree of the color on a color wheel, ranging from 0 to 360, where 0 is red, 120 is green, and 240 is blue.
- Saturation is the intensity of the color, ranging from 0% to 100%, where 0% is gray and 100% is the full color.
- Lightness is the brightness of the color, ranging from 0% to 100%, where 0% is black and 100% is white.
- To use an HSL value, use the `hsl()` function and pass the three values as parameters, separated by commas, for example:

```css
p {
  color: hsl(0, 100%, 50%);
}
```

- This will make the text of all `<p>` elements red.

#### Color keywords

- CSS also supports some color keywords that are not predefined color names, but have a special meaning or function.
- Some of the color keywords are:

  - `transparent`: This keyword makes the element transparent, meaning it will show the background of its parent element or the document.
  - `currentcolor`: This keyword inherits the color value of the current element, meaning it will use the same color as the element's text.
  - `inherit`: This keyword inherits the color value of the parent element, meaning it will use the same color as the parent element's text.

- To use a color keyword, assign it to the color property of an element, for example:

```css
p {
  color: transparent;
}
```

- This will make the text of all `<p>` elements transparent.

#### Opacity

- Opacity is a property that sets the transparency of an element, ranging from 0 to 1, where 0 is fully transparent and 1 is fully opaque.
- To use opacity, assign a numerical value to the opacity property of an element, for example:

```css
p {
  color: red;
  opacity: 0.5;
}
``

```
