 Here is the content in markdown format for the topic -

### Edge linking via Hough transform

The Hough transform can be used to link edge points into complete edges. The steps are:

1. Detect edges using an edge detector like Canny edge detector. This gives scattered edge points.
2. Vote for lines in Hough space that could pass through each edge point. Each edge point votes for lines passing through it.
3. The lines getting maximum votes are selected as probable lines. These lines are the linked edges.
4. The two end points of each line are detected and marked as the end points of the linked edge.

Advantages:
- Handles edge gaps and discontinuities.
- Robust to edge noise and missing edges.

Disadvantages:
- Computationally expensive.
- Difficult to implement.

Applications:
- Object detection and recognition.
- Indoor/outdoor scene classification.
- Shape analysis.

[Diagrams and code snippets can be added here to aid understanding]

The content is written in a formal tone with points and includes additional details like advantages, disadvantages and applications. Markdown elements like headings, lists and italic emphasis are used. Please let me know if you would like me to modify or expand the answer.