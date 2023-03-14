 Here is the content in markdown format on the topic ### Frames in Web Page Designing:

### Frames in Web Page Designing

Frames are used to divide a web page into multiple sections where each section can load a separate HTML document. This allows multiple documents to be accessed through a single web page.

Advantages of using frames:

- It reduces bandwidth usage as the common header/footer etc needs to be downloaded only once and can be reused in all frames.
- It enhances the appearance of the web page and allows for a more structured layout.
- The navigation remains same while viewing different pages due to the persistent frame structure.

Disadvantages of using frames:

- It can create accessibility issues as frames may not work with some browsers or assistive technologies like screen readers.
- It can create bookmarking and linking issues as the whole frame set is treated as a single page by the browser.
- The page content can only be viewed if all the frames load properly, otherwise it leads to a broken page.
- Search engines may not index the content properly within frames.

Some tips for using frames:

- Use them only when necessary for appearance/navigation benefits.
- Ensure proper accessibility and linking.
- Keep the frame structure simple with minimal nesting of frames.
- Clearly specify the target frame for links using 'target' attribute.
- Use 'iframe' element instead of 'frameset' if embedding a single external page.

Examples of frame usage:

- A menu frame on left and content display frame on right.
- A header frame on top, footer frame at bottom and content frame in between.
- An iframe to embed an external map within a page.

Overall, frames should be used cautiously by considering the pros and cons for the specific use case. Alternative options like CSS layouts can be explored if frames are not suitable.