### Text clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Text clipping is a process of clipping the string, which means removing the characters or parts of characters that are outside the clipping window.
- Text clipping is dependent on the method of generation used for characters and the requirements of a particular application .
- There are three methods for text clipping which are listed below:

  - All or none string clipping method: In this method, if the whole string is inside the clip window then we consider it, otherwise we discard it . This method is simple but may result in loss of information.
  - Text clipping method: In this method, we keep the characters of the string which lie inside the clip window and remove all the characters which lie outside the clip window . If a character overlaps the window boundary then we keep that part of the character which lies inside the window and discard that part which lies outside the clip window. This method is more flexible but may result in distorted characters.
  - Character clipping method: In this method, we clip each character individually using the same algorithm as for line clipping. This method is more accurate but may result in more computation.

- An example of text clipping is shown below:

![Text clipping example](https://www.tutorialspoint.com/computer_graphics/images/text_clipping.jpg)

- The image shows a string "COMPUTER GRAPHICS" clipped by a window. The all or none string clipping method would discard the whole string, the text clipping method would keep the characters "PUTER GRAP" and clip the rest, and the character clipping method would clip each character partially.