Hello, I am Sydney, your AI assistant. I can help you with your notes for the Unit 2 - Web Page Designing in the subject of Web Technology. Here are some frames for the notes:

### Frames
- Frames are a way of dividing a web page into multiple sections, each with its own scroll bar and navigation.
- Frames can be used to create layouts that are consistent across multiple pages, such as a header, a footer, a sidebar, or a menu.
- Frames are created using the `<frameset>` tag, which replaces the `<body>` tag in the HTML document.
- The `<frameset>` tag can have one or more `<frame>` tags as its children, which specify the source, name, and size of each frame.
- The `<frameset>` tag can also have nested `<frameset>` tags to create more complex layouts with rows and columns of frames.
- The `<frame>` tag has the following attributes:
  - `src`: the URL of the document to display in the frame
  - `name`: a unique identifier for the frame, which can be used to target links and forms to the frame
  - `scrolling`: whether the frame has a scroll bar (`auto`, `yes`, or `no`)
  - `noresize`: whether the frame can be resized by the user (`noresize` or omitted)
  - `frameborder`: whether the frame has a border (`1` or `0`)
  - `marginwidth`: the width of the margin around the frame content in pixels
  - `marginheight`: the height of the margin around the frame content in pixels
- To link to a specific frame, the `<a>` tag or the `<form>` tag can use the `target` attribute, which specifies the name of the frame to display the link or the form result.
- To display a default document in a frame, the `<noframes>` tag can be used inside the `<frameset>` tag, which contains the HTML content for browsers that do not support frames.
- Frames have some advantages and disadvantages, such as:
  - Advantages:
    - Consistent layout and navigation across multiple pages
    - Reduced bandwidth and loading time by reusing common content
    - Flexibility and interactivity by allowing the user to resize and scroll different sections independently
  - Disadvantages:
    - Difficulty in bookmarking and printing individual pages
    - Incompatibility and accessibility issues with some browsers and devices
    - Confusion and distraction for the user by having multiple scroll bars and windows