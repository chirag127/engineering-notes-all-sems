# Relationships between pixels

- A pixel is the smallest unit of a digital image that can be displayed or manipulated.
- Pixels have coordinates that indicate their position in the image, usually starting from the top-left corner as the origin (0,0).
- Pixels have values that represent their intensity or color, depending on the image format and color space.
- Pixels can have different types of relationships with each other, such as adjacency, connectivity, distance, and similarity.
- These relationships are useful for defining and analyzing regions, objects, boundaries, and features in an image.

## Adjacency

- Adjacency is the simplest relationship between pixels, which means that they are next to each other in a certain direction.
- There are three types of adjacency: 4-adjacency, 8-adjacency, and m-adjacency.
- 4-adjacency: Two pixels are 4-adjacent if they share a common side (horizontal or vertical). For example, the pixel p at (x,y) has four 4-neighbors: (x+1,y), (x-1,y), (x,y+1), and (x,y-1).
- 8-adjacency: Two pixels are 8-adjacent if they share a common side or a common vertex (diagonal). For example, the pixel p at (x,y) has eight 8-neighbors: (x+1,y), (x-1,y), (x,y+1), (x,y-1), (x+1,y+1), (x-1,y+1), (x+1,y-1), and (x-1,y-1).
- m-adjacency: Two pixels are m-adjacent if they are 8-adjacent but not 4-adjacent. For example, the pixel p at (x,y) has four m-neighbors: (x+1,y+1), (x-1,y+1), (x+1,y-1), and (x-1,y-1).

## Connectivity

- Connectivity is a more complex relationship between pixels, which means that there is a path between them that consists of pixels with the same property (such as value, color, or region).
- There are two types of connectivity: binary connectivity and grayscale connectivity.
- Binary connectivity: This applies to binary images, where pixels have only two possible values: 0 (background) or 1 (foreground). Two pixels are binary connected if they have the same value and are adjacent in a certain way. For example, two pixels are 4-connected if they are 4-adjacent and have the same value. Similarly, two pixels are 8-connected if they are 8-adjacent and have the same value.
- Grayscale connectivity: This applies to grayscale images, where pixels have a range of values from 0 (black) to 255 (white). Two pixels are grayscale connected if they are adjacent in a certain way and their values are within a specified threshold. For example, two pixels are 4-connected if they are 4-adjacent and their values differ by less than or equal to T, where T is a positive constant. Similarly, two pixels are 8-connected if they are 8-adjacent and their values differ by less than or equal to T.

## Distance

- Distance is a numerical measure of how far apart two pixels are in an image.
- There are different ways to calculate the distance between two pixels, depending on the type of adjacency and the image geometry.
- Some common distance metrics are: Euclidean distance, city-block distance, and chessboard distance.
- Euclidean distance: This is the most natural and intuitive way to measure the distance between two pixels, which is the length of the straight line that connects them. For example, the Euclidean distance between the pixel p at (x,y) and the pixel q at (s,t) is given by: d(p,q) = sqrt((x-s)^2 + (y-t)^2).
- City-block distance: This is also known as Manhattan distance, which is the sum of the horizontal and vertical distances between two pixels. For example, the city-block distance between the pixel p at (x,y) and the pixel q at (s,t) is given by: d(p,q) = |x-s| + |y-t|.
- Chessboard distance: This is also known as Chebyshev distance, which is the maximum of the horizontal and vertical distances between two pixels. For example, the chessboard distance between the pixel p