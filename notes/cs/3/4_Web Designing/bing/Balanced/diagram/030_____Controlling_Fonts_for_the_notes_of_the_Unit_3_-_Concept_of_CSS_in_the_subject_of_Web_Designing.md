### Controlling Fonts

- Fonts are an important aspect of web design, as they affect the appearance and readability of the text content.
- CSS provides several properties to control the fonts used in a web page, such as `font-family`, `font-size`, `font-weight`, `font-style`, `font-variant`, and `font`.
- The `font-family` property specifies the name of the font or a list of font names to use for the selected element. The browser will try to use the first font in the list that is available on the system. If none of the fonts are available, the browser will use a default font.
- The `font-size` property specifies the size of the font in various units, such as pixels, points, ems, percentages, etc. The default font size is 16 pixels, but it can be changed by the user or the browser settings.
- The `font-weight` property specifies the boldness or lightness of the font. The possible values are `normal`, `bold`, `bolder`, `lighter`, or a numeric value from 100 to 900, where 400 is normal and 700 is bold.
- The `font-style` property specifies the style of the font, such as `normal`, `italic`, or `oblique`. Italic fonts are slanted to the right, while oblique fonts are slanted to the left or right depending on the direction of the text.
- The `font-variant` property specifies whether the font should use small caps or normal caps. Small caps are uppercase letters that are smaller than the normal uppercase letters and have the same height as the lowercase letters.
- The `font` property is a shorthand property that combines the `font-family`, `font-size`, `font-weight`, `font-style`, and `font-variant` properties in one declaration. The order of the values is as follows: `font-style font-variant font-weight font-size/line-height font-family`. The `line-height` property specifies the height of a line of text, and it is optional. If any of the values are omitted, the default values are used.

- Example of using the `font` property:

```css
p {
  font: italic small-caps bold 20px/1.5 Arial, Helvetica, sans-serif;
}
```

- This declaration applies the following styles to the `<p>` elements:

  - The font style is italic.
  - The font variant is small caps.
  - The font weight is bold.
  - The font size is 20 pixels.
  - The line height is 1.5 times the font size.
  - The font family is Arial, Helvetica, or sans-serif, depending on the availability.