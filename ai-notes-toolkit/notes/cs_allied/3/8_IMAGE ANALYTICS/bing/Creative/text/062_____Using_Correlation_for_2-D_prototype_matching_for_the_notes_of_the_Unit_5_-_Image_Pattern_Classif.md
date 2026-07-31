### Using Correlation for 2-D Prototype Matching

- Correlation is a measure of similarity between two signals or images.
- Correlation can be used for pattern matching, which is the process of finding a specific pattern or template in a larger image or signal.
- Correlation can be performed in the spatial domain or the frequency domain, depending on the application and the computational efficiency.
- 2-D correlation involves sliding a smaller template image over a larger input image and computing the correlation coefficient at each position.
- The correlation coefficient is a value between -1 and 1 that indicates how well the template matches the input image at that position.
- A high correlation coefficient means a good match, while a low correlation coefficient means a poor match.
- The correlation coefficient can be normalized to account for different scales and intensities of the images.
- Normalized cross-correlation is a common method for 2-D prototype matching, which uses the following formula:

![formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/6a8f6f0f6f3a6a9f7f9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9