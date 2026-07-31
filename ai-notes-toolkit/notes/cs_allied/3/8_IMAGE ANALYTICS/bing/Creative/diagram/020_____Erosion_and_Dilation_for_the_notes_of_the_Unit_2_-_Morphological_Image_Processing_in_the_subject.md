### Erosion and Dilation

- Erosion and dilation are basic morphological processing operations that produce contrasting results when applied to either gray-scale or binary images.
- Erosion involves the removal of pixels at the edges of the region, while dilation involves the addition of pixels to the boundaries of the region .
- The number of pixels added or removed from the objects in an image depends on the size and shape of the structuring element used to process the image .
- Erosion and dilation are often used in combination to implement image processing operations, such as opening, closing, top-hat, and bottom-hat.
- Erosion and dilation have a wide array of uses, such as removing noise, isolating individual elements, joining disparate elements, enhancing edges, and extracting features in an image.

#### Example of erosion and dilation

- Consider a binary image with a white object on a black background, and a 3x3 square structuring element.
- Erosion will shrink the object by one pixel on each side, as shown below:

```
Original image:

111111111
100000001
100000001
100000001
100000001
100000001
100000001
100000001
111111111

Eroded image:

000000000
000000000
010000010
010000010
010000010
010000010
010000010
000000000
000000000
```

- Dilation will expand the object by one pixel on each side, as shown below:

```
Original image:

111111111
100000001
100000001
100000001
100000001
100000001
100000001
100000001
111111111

Dilated image:

111111111
111111111
111111111
110000011
110000011
110000011
111111111
111111111
111111111
```