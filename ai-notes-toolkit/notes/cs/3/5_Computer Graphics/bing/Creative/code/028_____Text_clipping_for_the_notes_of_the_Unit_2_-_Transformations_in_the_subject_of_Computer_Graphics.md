# Text clipping

Text clipping is a process of removing the characters or parts of characters that are outside the clipping window in computer graphics. It depends on the methods used to generate characters and the requirements of a particular application. There are three methods for text clipping which are listed below :

- **All or none string clipping method**: In this method, if the whole string is inside the clipping window, then it is displayed. Otherwise, the entire string is discarded. This method is simple and fast, but it may result in loss of information or incomplete text.

- **Text clipping method**: In this method, only the characters that are completely inside the clipping window are displayed. The characters that overlap the window boundary are partially clipped, meaning that only the portion that is inside the window is displayed. This method preserves more information than the previous one, but it may produce distorted or unreadable characters.

- **Precise character clipping method**: In this method, each character is treated as a polygon and clipped using a polygon clipping algorithm. This method produces the most accurate and readable text, but it is also the most complex and time-consuming one. This method is suitable for applications that require high-quality text rendering.