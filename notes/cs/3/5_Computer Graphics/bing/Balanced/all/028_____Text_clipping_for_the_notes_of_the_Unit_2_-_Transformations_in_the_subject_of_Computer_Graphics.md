# Text clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

Text clipping is a process of clipping the string. In this process, we clip the whole character or only some part of it depending on the requirement of the application. Text clipping is useful for removing text that is outside the viewing window or overlapping the window boundary.

There are three methods for text clipping which are listed below:

- All or none string clipping method: In this method, if the whole string is inside the clip window then we consider it. Otherwise, we discard the whole string. This method is simple but may result in loss of information.
- Text clipping method: In this method, we keep the characters of the string that lie inside the clip window and remove all the characters that lie outside the clip window. If a character overlaps the window boundary then we keep that part of the character that lies inside the window and discard that part that lies outside the clip window. This method is more flexible but may result in distorted characters.
- Character clipping method: In this method, we treat each character as a polygon and apply polygon clipping algorithms to clip the character. This method preserves the shape of the characters but may be computationally expensive.

The following diagram illustrates the three methods of text clipping:

![text clipping methods](text_clipping.png)

The text clipping methods can be implemented using various techniques such as scan-line algorithms, Cohen-Sutherland algorithm, Sutherland-Hodgman algorithm, etc. The choice of the technique depends on the methods used to generate characters and the requirements of a particular application.