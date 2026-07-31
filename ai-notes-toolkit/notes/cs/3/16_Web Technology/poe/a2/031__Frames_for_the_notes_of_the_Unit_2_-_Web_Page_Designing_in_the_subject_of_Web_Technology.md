 Here is the content in markdown format without any emojis or external links and in formal tone:

### Frames for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

1. Introduction to Frames
- Frames are used to divide a web page into multiple sections where each section can load a separate HTML document.
- Each section is called a frame and behaves like a separate browser window.
- Frames make it easy to display multiple documents or web pages within a single web browser window.
- The main advantage of using frames is that it reduces the download time of a web page as the frame documents can be loaded parallelly.

2. Structure of a Frameset Document
- A frameset document defines the structure of frames using <frameset> tags.
- The <frameset> tag replaces the <body> tag in a frameset document.
- Attributes:
-- rows: defines the number of rows of frames.
-- cols: defines the number of columns of frames.
-- frameborder: specifies whether to show a border around the frames.

3. Nested Frames
- Frames can be nested to create multiple layers of frames.
- The nested frame will be loaded into one of the main frames.
- Nested frames help to organize the content in a better way and provide more control over the layout.

4. Frame Targeting
- The target attribute of <a> tag can be used to specify which frame the linked document should be opened in.
- This is called framing targeting and helps to control the display of linked documents.
- Values for target attribute:
-- _self: opens the link in the same frame (default)
-- _blank: opens the link in a new blank window
-- _parent: opens the link in the parent frame
-- _top: opens the link in the full body of the window
-- framename: opens the link in a frame named "framename"