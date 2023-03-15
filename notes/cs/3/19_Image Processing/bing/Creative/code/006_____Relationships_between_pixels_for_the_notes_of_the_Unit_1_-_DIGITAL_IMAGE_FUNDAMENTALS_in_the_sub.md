### Relationships between pixels

- A pixel is the smallest unit of a digital image that can be displayed or manipulated.
- Pixels have coordinates that indicate their position in the image, usually starting from the top-left corner as the origin.
- Pixels have values that represent their intensity or color, depending on the image format and bit depth.
- Pixels can have different types of relationships with each other, such as adjacency, connectivity, distance, and similarity.
- Adjacency is the property of being next to each other in a certain direction or neighborhood. There are three common types of adjacency :
  - 4-adjacency: Two pixels are 4-adjacent if they share a horizontal or vertical edge. The 4-neighbors of a pixel p are denoted by N4(p) and have the coordinates (x+1,y), (x-1,y), (x,y+1), and (x,y-1), where (x,y) are the coordinates of p.
  - 8-adjacency: Two pixels are 8-adjacent if they share a horizontal, vertical, or diagonal edge. The 8-neighbors of a pixel p are denoted by N8(p) and have the coordinates (x+1,y), (x-1,y), (x,y+1), (x,y-1), (x+1,y+1), (x-1,y+1), (x+1,y-1), and (x-1,y-1), where (x,y) are the coordinates of p.
  - m-adjacency: Two pixels are m-adjacent if they are 8-adjacent but not 4-adjacent. The m-neighbors of a pixel p are denoted by Nm(p) and have the coordinates (x+1,y+1), (x-1,y+1), (x+1,y-1), and (x-1,y-1), where (x,y) are the coordinates of p.
- Connectivity is the property of being part of the same region or object in an image. There are different types of connectivity, depending on the type of adjacency used :
  - 4-connectivity: Two pixels are 4-connected if there is a path between them consisting of 4-adjacent pixels. A set of pixels that are 4-connected to a pixel p is called a 4-connected component of p.
  - 8-connectivity: Two pixels are 8-connected if there is a path between them consisting of 8-adjacent pixels. A set of pixels that are 8-connected to a pixel p is called an 8-connected component of p.
  - m-connectivity: Two pixels are m-connected if there is a path between them consisting of m-adjacent pixels. A set of pixels that are m-connected to a pixel p is called an m-connected component of p.
- Distance is the measure of how far apart two pixels are in an image. There are different ways to define distance, such as Euclidean, city-block, or chessboard distance:
  - Euclidean distance: The Euclidean distance between two pixels p and q with coordinates (x1,y1) and (x2,y2) is given by the formula: d(p,q) = sqrt((x1-x2)^2 + (y1-y2)^2)
  - City-block distance: The city-block distance between two pixels p and q with coordinates (x1,y1) and (x2,y2) is given by the formula: d(p,q) = |x1-x2| + |y1-y2|
  - Chessboard distance: The chessboard distance between two pixels p and q with coordinates (x1,y1) and (x2,y2) is given by the formula: d(p,q) = max(|x1-x2|, |y1-y2|)
- Similarity is the measure of how alike two pixels are in terms of their values or features. There are different ways to define similarity, such as correlation, mutual information, or histogram intersection:
  - Correlation: The correlation between two pixels p and q with values v1 and v2 is given by the formula: r(p,q) = (v1 - mean1) * (v2 - mean2) / (std1 * std2), where mean1 and mean2 are the mean values of the pixels in the regions containing p and q, and std1 and std2 are the standard deviations of