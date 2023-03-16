### Using Correlation for 2-D Prototype Matching

- Correlation is a measure of similarity between two signals or images.
- Correlation can be used for pattern matching or target tracking in image processing.
- Correlation can be performed in the spatial domain or the frequency domain.
- Spatial domain correlation involves sliding a template or prototype over the image and computing the correlation coefficient at each position.
- Frequency domain correlation involves transforming the image and the template into the Fourier domain and multiplying them element-wise, then transforming the result back to the spatial domain.
- The correlation coefficient is a normalized value between -1 and 1, where 1 indicates a perfect match, 0 indicates no match, and -1 indicates a perfect inverse match.
- The correlation coefficient can be computed as:

$$
r = \frac{\sum_{i,j}(f(i,j) - \bar{f})(t(i,j) - \bar{t})}{\sqrt{\sum_{i,j}(f(i,j) - \bar{f})^2 \sum_{i,j}(t(i,j) - \bar{t})^2}}
$$

where $f$ is the image, $t$ is the template, and $\bar{f}$ and $\bar{t}$ are the mean values of $f$ and $t$ respectively.

- The correlation coefficient can also be computed as:

$$
r = \frac{\sum_{i,j}f(i,j)t(i,j)}{\sqrt{\sum_{i,j}f(i,j)^2 \sum_{i,j}t(i,j)^2}}
$$

if $f$ and $t$ are zero-mean signals.

- The correlation coefficient can be plotted as a 2-D surface, where the peaks indicate the locations of the best matches.
- The correlation coefficient can be thresholded to identify the matches above a certain similarity level.
- Correlation can be affected by noise, illumination, rotation, scaling, and occlusion in the image.