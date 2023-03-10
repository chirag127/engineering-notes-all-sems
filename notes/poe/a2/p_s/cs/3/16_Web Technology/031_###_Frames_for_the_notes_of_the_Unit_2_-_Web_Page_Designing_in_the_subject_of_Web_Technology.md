 Here is the content in Markdown format for the topic ### Frames for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology:

### Frames

Frames are used to divide a web page into multiple sections where each section can load a separate HTML document. This allows for easier maintenance of web pages as the entire web page need not be loaded again if one section needs to be updated.

Advantages of using frames:

- Easy maintenance as individual sections can be updated independently.
- Simulate a desktop like interface with separate panels for different information.
- Browser history list will contain the frameset document rather than individual pages.

Disadvantages of using frames:

- Creating bookmarks and linking to specific pages can be difficult.
- Search engines can face problems indexing framed content.
- Users can disable frames, in which case the frameset document will not appear properly.
- Each frame loads a separate HTML document, which can lead to increased load time.

Examples of using frames:

- A web page divided into a navigation frame on the left, a main content frame in the center and an advertisement frame on the right.
- A web mail service having a frame for the list of received emails and a separate frame to display the selected email.

Steps to create a web page using frames:

1. Create an HTML document for the frameset which defines the number of rows and columns of frames and their sizes.
2. Create separate HTML documents for content inside each frame.
3. The frameset document loads each frame's HTML document.
4. Use `<frameset>` and `<frame>` tags to define the frame structure.
5. Use `rows` attribute to specify number of rows and `cols` attribute to specify number of columns.
6. Use `src` attribute to specify the HTML document to load in each frame.

[Detailed ASCII diagrams and code snippets can be added here for more clarity.]