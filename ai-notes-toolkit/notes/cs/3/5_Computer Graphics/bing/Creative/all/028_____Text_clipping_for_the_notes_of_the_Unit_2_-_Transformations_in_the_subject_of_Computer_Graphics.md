# Text clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

Text clipping is a process of clipping the string. In this process, we clip the whole character or only some part of it depending on the requirement of the application. Text clipping is useful for removing the text that is outside the viewing window or overlapping the window boundary.

There are three methods for text clipping which are listed below  :

- **All or none string clipping method**: In this method, if the whole string is inside the clip window then we consider it. Otherwise, we discard the whole string even if some part of it is inside the window. This method is simple but may result in loss of information.

- **Text clipping method**: In this method, we keep the characters of the string that lie inside the clip window and remove all the characters that lie outside the clip window. If a character overlaps the window boundary then we keep that part of the character that lies inside the window and discard that part that lies outside the clip window. This method is more accurate but may result in distorted characters.

- **All or none character clipping method**: In this method, we keep the characters of the string that are completely inside the clip window and discard the characters that are partially or completely outside the clip window. This method is a compromise between the previous two methods. It preserves the shape of the characters but may result in incomplete strings.

Text clipping can be implemented using various techniques such as scan-line algorithm, polygon clipping algorithm, or character generation algorithm . The choice of the technique depends on the methods used to generate characters and the requirements of a particular application.