### Dimension

- In CSS, dimension is a term that refers to a quantity that has both a number and a unit, such as `10px`, `2em`, `50%`, etc.
- Dimension is used to specify various properties in CSS, such as height, width, max-width, min-width, max-height, min-height, etc.
- Dimension can also be used to specify distances, durations, frequencies, resolutions, and other quantities in CSS.
- The syntax of dimension is a number immediately followed by a unit, which is an identifier. For example, `5rem`, `3s`, `12kHz`, `300dpi`, etc.
- The unit identifiers are case insensitive, meaning that `5rem` and `5REM` are equivalent.
- There are different types of units in CSS, such as absolute units, relative units, viewport units, etc. Each unit has a different meaning and use case.

#### Absolute units

- Absolute units are units that have a fixed and predefined length, regardless of the screen size, resolution, or font size.
- Absolute units are mainly used for print media, where the physical dimensions of the output are known.
- Absolute units include:

| Unit | Description | Example |
| ---- | ----------- | ------- |
| cm | Centimeters | `1cm` is roughly 37.8 pixels, or about 25.2/64 of an inch |
| mm | Millimeters | `1mm` is roughly 3.78 pixels, or 1/10th of a centimeter |
| in | Inches | `1in` is equal to 2.54 centimeters, or 96 pixels |
| px | Pixels | `1px` is the smallest unit of measurement that a screen can display |
| pt | Points | `1pt` is equal to 1/72 of an inch, or 1.33 pixels |
| pc | Picas | `1pc` is equal to 12 points, or 16 pixels |

#### Relative units

- Relative units are units that are relative to another value, such as the font size, the viewport size, or the parent element's size.
- Relative units are mainly used for responsive web design, where the layout and content should adapt to different screen sizes, resolutions, and font sizes.
- Relative units include:

| Unit | Description | Example |
| ---- | ----------- | ------- |
| em | Relative to the font size of the element | `1em` is equal to the current font size of the element, `2em` is twice the current font size, `0.5em` is half the current font size, etc. |
| rem | Relative to the font size of the root element | `1rem` is equal to the font size of the root element (usually the `<html>` element), `2rem` is twice the font size of the root element, `0.5rem` is half the font size of the root element, etc. |
| % | Relative to the parent element's size | `50%` is half the size of the parent element, `100%` is the same size as the parent element, `150%` is 1.5 times the size of the parent element, etc. |
| vw | Relative to 1% of the width of the viewport | `1vw` is equal to 1% of the width of the viewport, `50vw` is half the width of the viewport, `100vw` is the full width of the viewport, etc. |
| vh | Relative to 1% of the height of the viewport | `1vh` is equal to 1% of the height of the viewport, `50vh` is half the height of the viewport, `100vh` is the full height of the viewport, etc. |
| vmin | Relative to 1% of the smaller dimension of the viewport | `1vmin` is equal to 1% of the smaller dimension of the viewport, either the width or the height, whichever is smaller |
| vmax | Relative to 1% of the larger dimension of the viewport | `1vmax` is equal to 1% of the larger dimension of the viewport, either the width or the height, whichever is larger |

#### Other units

- There are also some other units in CSS that are used to specify durations, frequencies, resolutions, and angles.
- These units include:

| Unit | Description | Example |
| ---- | ----------- | ------- |
| s | Seconds | `1s` is equal to one