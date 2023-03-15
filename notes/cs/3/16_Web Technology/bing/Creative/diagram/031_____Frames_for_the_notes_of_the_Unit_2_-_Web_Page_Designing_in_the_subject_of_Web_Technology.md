Hello, I am Sydney, your AI assistant. I can help you with your notes for the Unit 2 - Web Page Designing in the subject of Web Technology. Here is the content in markdown format:

### Frames
- Frames are a way of dividing a web page into multiple sections, each with its own independent content and scrollbars.
- Frames are created using the `<frameset>` tag, which replaces the `<body>` tag in a HTML document.
- The `<frameset>` tag can have one or more `<frame>` tags as its children, which specify the source, name, size, and border of each frame.
- The `<frameset>` tag can also have nested `<frameset>` tags to create more complex layouts of frames.
- Each `<frame>` tag can have a `src` attribute, which specifies the URL of the document to be displayed in the frame.
- Each `<frame>` tag can also have a `name` attribute, which assigns a name to the frame. This name can be used to target links or forms to a specific frame using the `target` attribute.
- Each `<frame>` tag can also have a `scrolling` attribute, which controls the appearance of scrollbars in the frame. The possible values are `yes`, `no`, or `auto`.
- Each `<frame>` tag can also have a `frameborder` attribute, which specifies whether to display a border around the frame. The possible values are `1` (default) or `0`.
- Each `<frame>` tag can also have a `noresize` attribute, which prevents the user from resizing the frame by dragging its border.
- Each `<frame>` tag can also have a `marginwidth` and `marginheight` attribute, which specify the size of the margins around the frame content in pixels.
- To create a default document to be displayed in case the browser does not support frames, the `<noframes>` tag can be used inside the `<frameset>` tag. The `<noframes>` tag can have any HTML content as its children.
- To access the properties and methods of a frame from another frame or the parent document, the `window.frames` collection can be used. The `window.frames` collection is an array of all the frames in the document, indexed by their name or position.
- To access the properties and methods of the parent document from a frame, the `window.parent` property can be used. The `window.parent` property refers to the window object of the parent document.
- To access the properties and methods of the top-level document from a frame, the `window.top` property can be used. The `window.top` property refers to the window object of the top-level document, which may or may not be the same as the parent document.