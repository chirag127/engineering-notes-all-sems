## Unit 1 - Introduction and Line Generation

1. **Introduction:** Computer graphics is the field of visual computing, where one utilizes computers both to generate visual images synthetically and to integrate or alter visual and spatial information sampled from the real world.

2. **Line Generation:** Line generation is the process of generating a line between two points in a computer graphics system. There are several algorithms for line generation, including the Digital Differential Analyzer (DDA) algorithm and the Bresenham's line algorithm.

    - **Digital Differential Analyzer (DDA) Algorithm:** The DDA algorithm is an incremental scan-conversion method for rasterizing lines. It calculates the intermediate points along the line path between the start and end points and rounds them to the nearest integer coordinates.

    - **Bresenham's Line Algorithm:** Bresenham's line algorithm is an efficient and accurate raster line-generating algorithm. It uses integer arithmetic to calculate the intermediate points along the line path between the start and end points, and it is faster than the DDA algorithm because it does not involve any floating-point calculations.