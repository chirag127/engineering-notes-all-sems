 Here is the content in markdown format without any emojis or external links:

### Using Correlation for 2-D prototype matching

- Correlation is a technique for matching 2-D shapes and patterns without explicitly identifying features or key points.
- A prototype pattern is slid over the input image and the correlation between the prototype and the underlying image region is computed at each location.
- The location that produces the highest correlation is taken as the match location.
- Correlation is effective when the pattern to be located has a distinctive shape but its precise scale or rotation is unknown. It is also relatively inexpensive to compute.
- To perform correlation, the prototype pattern is digitized to form a 2-D array of numbers (e.g. 1s and 0s for a binary pattern). The input image is also digitized. Then the dot product between the prototype array and the corresponding array section of the image is computed, and summed to give the correlation value for that location.
- By sliding the prototype array over the image array and computing the correlation at each location, a correlation surface is constructed. The location of the peak in this surface corresponds to the most likely match location.
- The strength of the peak indicates how strong the match is. A correlation value close to the image size indicates a very strong match.
- To allow for rotation and size changes in the prototype, the correlation can be computed for multiple angles and scales, and the best overall match selected. This extends the technique to allow for shape classification rather than precise localization.