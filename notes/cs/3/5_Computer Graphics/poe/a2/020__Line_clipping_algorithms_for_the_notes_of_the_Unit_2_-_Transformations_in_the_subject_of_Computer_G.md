 Here is the formal content in Markdown format without any emojis or external links for the topic "Line clipping algorithms for the notes of the Unit 2 - Transformations in the subject of Computer Graphics":

### Line Clipping Algorithms

1. Cohen–Sutherland Line Clipping Algorithm
- Classifies each point of the line into one of four regions based on x-max, x-min, y-max, y-min
- Repeatedly clips off the portion of the line that lies outside the viewport ( Clipping region ) until either:
- The entire line lies within the viewport
- The line is completely clipped away

2. Cyrus–Beck Line Clipping Algorithm
- Classifies each point of the line into one of nine regions based on x-max, x-min, y-max, y-min
- Clips the line in a single pass by finding the intersection of the line with the clipping rectangle borders
- Generally more efficient than Cohen–Sutherland algorithm but slightly more complex

3. Nicholl–Lee–Nicholl (NLN) Line Clipping Algorithm
- Clips lines, lines segments and polygons
- Uses a bouncing strategy which reflects clipped portions about the boundary until they lie within the viewport
- Generally more efficient than previous algorithms but complex implementation

This content summarizes three different line clipping algorithms with points in a formal tone for the given topic to be used as study notes. Let me know if you would like me to modify or expand the content.