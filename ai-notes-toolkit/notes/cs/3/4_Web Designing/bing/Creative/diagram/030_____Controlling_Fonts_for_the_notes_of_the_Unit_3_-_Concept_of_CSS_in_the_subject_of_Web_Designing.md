Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write the content on the topic of Controlling Fonts for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing. Here is the content I have written in markdown format:

# Controlling Fonts

- Fonts are an important aspect of web design, as they affect the appearance and readability of the text on a web page.
- CSS provides various properties to control the fonts used on a web page, such as font-family, font-size, font-weight, font-style, and font-variant.
- The font-family property specifies the name of the font or a list of fonts to use for the text. The browser will try to use the first font in the list, and if it is not available, it will use the next one, and so on. For example:

```css
p {
  font-family: Arial, Helvetica, sans-serif;
}
```

- The font-size property specifies the size of the font in different units, such as pixels (px), points (pt), ems (em), or percentages (%). The default font size is 16px. For example:

```css
p {
  font-size: 18px;
}
```

- The font-weight property specifies the weight or boldness of the font. The possible values are normal, bold, bolder, lighter, or a number from 100 to 900. The default value is normal. For example:

```css
p {
  font-weight: bold;
}
```

- The font-style property specifies the style or slant of the font. The possible values are normal, italic, or oblique. The default value is normal. For example:

```css
p {
  font-style: italic;
}
```

- The font-variant property specifies whether the text should be displayed in small-caps or normal. The possible values are normal or small-caps. The default value is normal. For example:

```css
p {
  font-variant: small-caps;
}
```

- To apply multiple font properties at once, the font shorthand property can be used. The syntax is:

```css
font: font-style font-variant font-weight font-size/line-height font-family;
```

- The line-height property specifies the height of a line of text, which affects the vertical spacing between lines. The value can be a number, a length, or a percentage. For example:

```css
p {
  line-height: 1.5;
}
```

- The font property can also be used to set the font to a system font, such as caption, icon, menu, message-box, small-caption, or status-bar. For example:

```css
p {
  font: caption;
}
```

- To use a custom font that is not installed on the user's system, the @font-face rule can be used. The syntax is:

```css
@font-face {
  font-family: font-name;
  src: url(font-file);
}
```

- The font-name is the name that will be used to refer to the font in the CSS code. The font-file is the URL of the font file, which can be in different formats, such as TrueType (.ttf), OpenType (.otf), Web Open Font Format (.woff), or Scalable Vector Graphics (.svg).
- The @font-face rule should be placed at the top of the CSS file, before any other rules. For example:

```css
@font-face {
  font-family: MyFont;
  src: url(myfont.ttf);
}

p {
  font-family: MyFont, Arial, sans-serif;
}
```