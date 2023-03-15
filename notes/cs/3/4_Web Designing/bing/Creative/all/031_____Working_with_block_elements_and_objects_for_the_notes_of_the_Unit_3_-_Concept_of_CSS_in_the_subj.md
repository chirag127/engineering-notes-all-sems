# Working with block elements and objects

- Block elements are HTML elements that occupy the entire width of their parent container and start on a new line. Examples of block elements are `<div>`, `<p>`, `<h1>`, `<ul>`, etc.
- Block elements can be styled using CSS properties such as `width`, `height`, `margin`, `padding`, `border`, `background`, `display`, `position`, etc.
- Block elements can be nested inside other block elements or inline elements, but not vice versa. For example, `<p><span>Some text</span></p>` is valid, but `<span><p>Some text</p></span>` is not.
- Objects are HTML elements that can contain multimedia content such as images, videos, audio, etc. Examples of objects are `<img>`, `<video>`, `<audio>`, `<canvas>`, `<svg>`, etc.
- Objects can be styled using CSS properties such as `width`, `height`, `margin`, `padding`, `border`, `background`, `display`, `position`, etc.
- Objects can be nested inside block elements or inline elements, depending on their display property. For example, `<div><img src="image.jpg"></div>` is valid, but `<img src="image.jpg"><div>Some text</div></img>` is not.
- Objects can also have attributes that specify their source, dimensions, alternative text, etc. For example, `<img src="image.jpg" alt="A picture" width="300" height="200">` is an object with attributes.