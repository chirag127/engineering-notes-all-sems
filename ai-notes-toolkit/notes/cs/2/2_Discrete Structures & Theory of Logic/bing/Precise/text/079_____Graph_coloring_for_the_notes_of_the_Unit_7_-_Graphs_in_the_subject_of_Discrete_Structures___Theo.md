### Graph Coloring

Graph coloring is a way of labeling graph components such as vertices, edges, and regions under some constraints. In a graph, no two adjacent vertices, adjacent edges, or adjacent regions are colored with the minimum number of colors .

- **Vertex Coloring**: A k-coloring of a graph G = (V,E) is a function c : V → C, where |C| = k. Vertices of the same color form a color class. A coloring is proper if adjacent vertices have different colors. A graph is k-colorable if there is a proper k-coloring. The chromatic number χ(G) of a graph G is the minimum k such that G is k-colorable .

- **Edge Coloring**: To show that we cannot color K7 with fewer than 7 colors, notice that because each of the 7 vertices can only be incident with one edge of a given color, there cannot be more than 3 edges colored with any given color (3 edges are already incident with 6 of the 7 vertices, and a fourth edge would have to be incident with two others) .

- **Four Color Theorem**: The Four Color Theorem states that if a graph is planar, then the chromatic number of the graph is less than or equal to 4. Thus, any map can be properly colored with 4 or fewer colors .

- **Applications**: Graph coloring has many applications, including scheduling problems. For example, it was used to color a graph of 75000 nodes to install updates in 8 passes .