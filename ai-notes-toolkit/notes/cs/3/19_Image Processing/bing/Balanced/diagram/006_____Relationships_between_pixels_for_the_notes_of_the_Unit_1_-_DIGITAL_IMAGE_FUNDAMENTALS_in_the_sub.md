### Relationships between pixels

- A pixel is the smallest unit of a digital image that can be displayed or manipulated.
- Pixels have coordinates that indicate their position in the image, such as (x,y) for a two-dimensional image.
- Pixels also have values that represent their intensity or color, such as gray levels or RGB components.
- Pixels can have different types of relationships with each other, such as adjacency, connectivity, distance, and similarity.
- These relationships are important for defining and analyzing regions, objects, boundaries, and features in an image.

#### Adjacency

- Two pixels are adjacent if they share a common edge or corner in the image grid.
- There are different types of adjacency, depending on how many neighbors a pixel can have.
- 4-adjacency: A pixel has four horizontal and vertical neighbors, denoted by N4(p).
- 8-adjacency: A pixel has eight horizontal, vertical, and diagonal neighbors, denoted by N8(p).
- m-adjacency: A pixel has either four or eight neighbors, depending on whether the pixel is odd or even, denoted by Nm(p).

#### Connectivity

- Two pixels are connected if there is a path between them consisting entirely of pixels with the same value or property.
- There are different types of connectivity, depending on the type of adjacency used to define the path.
- 4-connectivity: A pixel is connected to another pixel if they are 4-adjacent and have the same value, denoted by C4(p,q).
- 8-connectivity: A pixel is connected to another pixel if they are 8-adjacent and have the same value, denoted by C8(p,q).
- m-connectivity: A pixel is connected to another pixel if they are m-adjacent and have the same value, denoted by Cm(p,q).

#### Distance

- The distance between two pixels is a measure of how far apart they are in the image grid.
- There are different ways to calculate the distance, depending on the type of adjacency used to define the shortest path between the pixels.
- D4 distance: The distance is the number of horizontal and vertical steps in the shortest 4-adjacent path, denoted by D4(p,q).
- D8 distance: The distance is the number of horizontal, vertical, and diagonal steps in the shortest 8-adjacent path, denoted by D8(p,q).
- Dm distance: The distance is the number of horizontal, vertical, and diagonal steps in the shortest m-adjacent path, denoted by Dm(p,q).
- Euclidean distance: The distance is the length of the straight line between the pixels, denoted by DE(p,q).

#### Similarity

- The similarity between two pixels is a measure of how alike they are in terms of their values or properties.
- There are different ways to calculate the similarity, depending on the type of values or properties used to compare the pixels.
- Gray-level similarity: The similarity is the inverse of the absolute difference between the gray levels of the pixels, denoted by SG(p,q).
- Color similarity: The similarity is the inverse of the Euclidean distance between the color vectors of the pixels, denoted by SC(p,q).
- Texture similarity: The similarity is the inverse of the dissimilarity measure between the texture features of the pixels, denoted by ST(p,q).
- Shape similarity: The similarity is the inverse of the dissimilarity measure between the shape descriptors of the pixels, denoted by SS(p,q).