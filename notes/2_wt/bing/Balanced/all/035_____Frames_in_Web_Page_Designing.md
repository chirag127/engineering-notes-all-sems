# Frames in Web Page Designing

- Frames are a feature of HTML that allows you, as the author, to control the layout of a Website in the user’s browser.
- Frames allow you to divide the browser window into rectangular sections that can be treated as if they were separate browser windows.
- They can be scrolled and resized, and loaded with different Web pages.
- A frames page, also called a frameset, is a Web page that is divided into two or more sections, each of which points to another Web page.
- A frame on a frames page can also point to another frames page.
- To use frames on a page, we use `<frameset>` tag instead of `<body>` tag.
- The `<frameset>` tag defines how to divide the window into frames.
- The `rows` attribute of `<frameset>` tag defines horizontal frames and `cols` attribute defines vertical frames.
- To specify the content of each frame, we use `<frame>` tag inside the `<frameset>` tag.
- The `<frame>` tag has a `src` attribute that specifies the URL of the Web page to be displayed in the frame.
- The `<frame>` tag can also have other attributes, such as `name`, `scrolling`, `noresize`, `marginwidth`, `marginheight`, etc.
- To create a link that targets a specific frame, we use the `target` attribute of the `<a>` tag.
- The `target` attribute can have the value of the `name` attribute of the frame, or one of the predefined values, such as `_blank`, `_self`, `_parent`, `_top`.
- Frames can be useful for creating consistent navigation menus, headers, footers, etc.
- Frames can also have some disadvantages, such as breaking the back button, bookmarking, printing, accessibility, etc .
- Frames are not supported by HTML5 and are considered obsolete .
- It is recommended to use other techniques, such as CSS, JavaScript, or server-side scripting, to create dynamic and responsive Web layouts .