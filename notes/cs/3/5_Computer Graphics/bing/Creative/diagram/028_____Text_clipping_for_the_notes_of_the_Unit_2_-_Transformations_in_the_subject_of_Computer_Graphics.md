### Text clipping

Text clipping is a process of clipping the string. In this process, we clip the whole character or only some part of it depending on the requirement of the application. Text clipping is used to provide text display in a computer graphics system. It depends on the methods used to generate characters and the requirements of a particular application .

There are three methods for text clipping which are listed below:

- **All or none string clipping method**: In this method, if the whole string is inside the clip window then we consider it. Otherwise, we discard the whole string. This method is simple but it may result in loss of information if some characters are partially inside the clip window.
- **Text clipping method**: In this method, we keep the characters of the string which lie inside the clip window and remove all the characters which lie outside the clip window. If a character overlaps the window boundary then we keep that part of the character which lies inside the window and discard that part which lies outside the clip window. This method is more flexible but it may result in distorted characters if the clipping is done at arbitrary positions.
- **All or none character clipping method**: In this method, we keep the characters of the string which are completely inside the clip window and discard the characters which are partially or completely outside the clip window. This method is a compromise between the previous two methods. It preserves the shape of the characters but it may result in gaps in the string if some characters are partially inside the clip window.

The following diagram illustrates the three methods of text clipping:

![Text clipping methods](text_clipping.png)