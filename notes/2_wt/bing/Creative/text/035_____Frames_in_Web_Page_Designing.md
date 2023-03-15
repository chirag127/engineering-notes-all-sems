### Frames in Web Page Designing

- Frames are a feature of HTML that allows you, as the author, to control the layout of a Website in the user’s browser.
- Frames allow you to divide the browser window into rectangular sections that can be treated as if they were separate browser windows. They can be scrolled and resized, and loaded with different Web pages.
- A frames page, also called a frameset, is a Web page that is divided into two or more sections, each of which points to another Web page. A frame on a frames page can also point to another frames page.
- To use frames on a page, we use `<frameset>` tag instead of `<body>` tag. The `<frameset>` tag defines how to divide the window into frames. The `rows` attribute of `<frameset>` tag defines horizontal frames and `cols` attribute defines vertical frames.
- A frame is defined by using `<frame>` tag inside the `<frameset>` tag. The `<frame>` tag has a `src` attribute that specifies the URL of the Web page to be displayed in the frame. The `<frame>` tag can also have other attributes, such as `name`, `scrolling`, `noresize`, `marginwidth`, `marginheight`, etc.
- Frames can be useful for creating consistent navigation menus, headers, footers, etc. However, frames also have some disadvantages, such as :
  - Frames can disrupt the flow of the Web and make it difficult to bookmark, link, or print specific pages .
  - Frames can cause accessibility problems for some users, such as those using screen readers, text browsers, or mobile devices .
  - Frames can increase the loading time and bandwidth usage of a Web page, as each frame requires a separate HTTP request .
  - Frames can create compatibility issues with some browsers or devices that do not support frames or have different screen resolutions .