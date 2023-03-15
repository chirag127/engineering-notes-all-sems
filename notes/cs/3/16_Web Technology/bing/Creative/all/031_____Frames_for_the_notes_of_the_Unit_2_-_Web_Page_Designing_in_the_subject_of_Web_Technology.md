# Unit 2 - Web Page Designing

## Frames

- Frames are a way of dividing a web page into multiple sections, each with its own independent content and scrollbars.
- Frames can be used to create layouts that are more flexible and dynamic than using tables or CSS grids.
- Frames are created using the `<frameset>` tag, which replaces the `<body>` tag in the HTML document.
- The `<frameset>` tag can have one or more `<frame>` tags as its children, which specify the source, name, size, and border of each frame.
- The `<frameset>` tag can also have nested `<frameset>` tags to create more complex layouts with rows and columns of frames.
- The `<noframes>` tag can be used to provide alternative content for browsers that do not support frames or have frames disabled.
- Frames can be linked to each other using the `target` attribute in the `<a>` tag, which specifies the name of the frame to load the link in.
- Frames can also communicate with each other using JavaScript, by accessing the `window.frames` array or the `parent` and `top` properties of the `window` object.