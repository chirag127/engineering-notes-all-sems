# Border properties for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- The border properties in CSS are used to style the borders of an element.
- The border properties can be applied to any element that can have a border, such as `<div>`, `<p>`, `<table>`, `<img>`, etc.
- The border properties can be specified individually for each side of the element, or for all sides at once.
- The border properties include:

  - `border-width`: Specifies the width of the border. It can be a length value (such as `5px`, `1em`, `0.5rem`, etc.), or one of the predefined keywords: `thin`, `medium`, or `thick`.
  - `border-style`: Specifies the style of the border. It can be one of the following values: `none`, `hidden`, `solid`, `dotted`, `dashed`, `double`, `groove`, `ridge`, `inset`, or `outset`.
  - `border-color`: Specifies the color of the border. It can be a color name (such as `red`, `blue`, `green`, etc.), a hexadecimal value (such as `#ff0000`, `#00ff00`, `#0000ff`, etc.), an RGB value (such as `rgb(255,0,0)`, `rgb(0,255,0)`, `rgb(0,0,255)`, etc.), an RGBA value (such as `rgba(255,0,0,0.5)`, `rgba(0,255,0,0.5)`, `rgba(0,0,255,0.5)`, etc.), an HSL value (such as `hsl(0,100%,50%)`, `hsl(120,100%,50%)`, `hsl(240,100%,50%)`, etc.), or an HSLA value (such as `hsla(0,100%,50%,0.5)`, `hsla(120,100%,50%,0.5)`, `hsla(240,100%,50%,0.5)`, etc.).
  - `border-radius`: Specifies the radius of the corners of the border. It can be a length value (such as `10px`, `2em`, `1rem`, etc.), or a percentage value (such as `50%`, `25%`, `10%`, etc.).
  - `border-image`: Specifies an image to be used as the border of the element. It can be a URL to an image file (such as `url("border.png")`), or a gradient function (such as `linear-gradient(to right, red, green, blue)`). The border-image property also accepts four values to specify how the image is sliced, repeated, and stretched along the border: `border-image-slice`, `border-image-repeat`, `border-image-width`, and `border-image-outset`.

- The border properties can be combined into a shorthand property: `border`. The syntax of the border property is:

  - `border: border-width border-style border-color;`
  - For example: `border: 5px solid red;`

- The border properties can also be combined into shorthand properties for each side of the element: `border-top`, `border-right`, `border-bottom`, and `border-left`. The syntax of these properties is the same as the border property.
- For example: `border-top: 5px solid red;`

- The border properties can be used to create various effects, such as:

  - A simple border around an element: `border: 5px solid black;`
  - A rounded border around an element: `border: 5px solid black; border-radius: 10px;`
  - A double border around an element: `border: 5px double black;`
  - A dotted border around an element: `border: 5px dotted black;`
  - A dashed border around an element: `border: 5px dashed black;`
  - A border with different colors for each side: `border-top: 5px solid red; border-right: 5px solid green; border-bottom: 5px solid blue; border-left: 5px solid yellow;`
  - A border with an image: `border: 5px solid transparent; border-image: url("border.png") 30 30 30 30 stretch stretch;`
  - A border with a gradient: `border: 5px solid transparent; border-image: linear-gradient(to right, red, green, blue