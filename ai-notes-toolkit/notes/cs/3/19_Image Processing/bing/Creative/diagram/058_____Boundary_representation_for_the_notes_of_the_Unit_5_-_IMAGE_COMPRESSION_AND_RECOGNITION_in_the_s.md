### Boundary representation

- Boundary representation (B-rep) is a method for representing a 3D shape by defining the limits of its volume.
- A solid is represented as a collection of connected surface elements, which define the boundary between interior and exterior points.
- A boundary representation of a model comprises topological components (faces, edges and vertices) and the connections between them, along with geometric definitions for those components (surfaces, curves and points, respectively).
- A face is a bounded portion of a surface; an edge is a bounded piece of a curve and a vertex lies at a point.
- Boundary representation is useful for image processing and computer-aided design, as it allows for efficient manipulation and analysis of 3D shapes.

#### Boundary extraction

- Boundary extraction is a process of obtaining the boundary of an image, which is the line or location dividing the two surfaces.
- Boundary extraction can help to gain information and understand the feature of an image, as it is the first process in preprocessing to present the image’s characteristics.
- Boundary extraction can be done by using morphological image processing operations, such as erosion, dilation, opening, closing, etc.
- Morphological image processing is a technique that deals with the shape and structure of an image, by applying a structuring element (a small binary image) to the input image.
- The basic idea of boundary extraction is to subtract the eroded image from the original image, which will result in the boundary pixels.
- The erosion operation shrinks the foreground pixels by removing the pixels at the boundary, while the dilation operation expands the foreground pixels by adding pixels at the boundary.
- The opening operation is a combination of erosion followed by dilation, which removes small objects and smooths the boundary.
- The closing operation is a combination of dilation followed by erosion, which fills small holes and gaps and smooths the boundary.

#### Boundary representation example

- Here is an example of boundary extraction using MATLAB:

```matlab
% Read the input image
img = imread('input.jpg');

% Convert the image to grayscale
img = rgb2gray(img);

% Convert the image to binary
img = imbinarize(img);

% Display the original image
subplot(2,2,1);
imshow(img);
title('Original Image');

% Perform erosion on the image
se = strel('disk',5);
eroded_img = imerode(img,se);

% Display the eroded image
subplot(2,2,2);
imshow(eroded_img);
title('Eroded Image');

% Perform boundary extraction by subtracting the eroded image from the original image
boundary_img = img - eroded_img;

% Display the boundary image
subplot(2,2,3);
imshow(boundary_img);
title('Boundary Image');
```

- The output of the code is shown below:

![Boundary extraction example](https://media.geeksforgeeks.org/wp-content/uploads/20201120121619/boundary-extraction-of-image-using-matlab.jpg)

- The boundary image shows the outline of the objects in the original image, which can be used for further analysis and processing.