# Controlling Fonts

- Fonts are an important aspect of web design, as they affect the appearance and readability of the text content.
- CSS provides several properties to control the fonts of an element, such as `font-family`, `font-size`, `font-style`, `font-weight`, `font-variant`, and `font`.
- The `font-family` property specifies the name of the font to use for an element. It can take one or more comma-separated values, which are either generic names (such as `serif`, `sans-serif`, `monospace`, etc.) or specific font names (such as `Arial`, `Times New Roman`, `Courier New`, etc.).
- The `font-size` property specifies the size of the font to use for an element. It can take either an absolute value (such as `12px`, `16pt`, `1cm`, etc.) or a relative value (such as `small`, `medium`, `large`, `x-large`, etc.).
- The `font-style` property specifies the style of the font to use for an element. It can take one of the following values: `normal`, `italic`, or `oblique`.
- The `font-weight` property specifies the weight or boldness of the font to use for an element. It can take either a numeric value (from 100 to 900, where 400 is normal and 700 is bold) or a keyword value (such as `normal`, `bold`, `lighter`, or `bolder`).
- The `font-variant` property specifies whether the font to use for an element should be in small caps or not. It can take one of the following values: `normal` or `small-caps`.
- The `font` property is a shorthand property that combines the values of `font-family`, `font-size`, `font-style`, `font-weight`, and `font-variant` in one declaration. The order of the values is as follows: `font-style font-variant font-weight font-size/line-height font-family`. The `line-height` value is optional and specifies the height of a line of text. The `font-family` value is mandatory and must be the last value in the declaration. The other values are optional and can be omitted if the default values are desired.

- Example of using the `font` property:

```css
p {
  font: italic small-caps bold 20px/1.5 Arial, sans-serif;
}
```

- This declaration applies the following styles to the `<p>` elements:

  - The font style is italic.
  - The font variant is small caps.
  - The font weight is bold.
  - The font size is 20 pixels.
  - The line height is 1.5 times the font size.
  - The font family is Arial, or any sans-serif font if Arial is not available.