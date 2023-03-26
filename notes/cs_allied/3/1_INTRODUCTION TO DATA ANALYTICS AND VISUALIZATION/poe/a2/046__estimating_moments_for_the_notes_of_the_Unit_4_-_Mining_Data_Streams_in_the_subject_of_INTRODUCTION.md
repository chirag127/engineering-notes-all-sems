 Here is the formal content in Markdown format without any emojis or external links for the given topic:

### Estimating Moments for the Notes of Unit 4 - Mining Data Streams

1. Mean - The average of a data stream can be estimated using an exponentially weighted moving average. This gives more weight to recent data points and can handle data streams efficiently.
2. Variance - The variance of a data stream can be estimated using an exponentially weighted moving average of the squared deviation from the mean. This is an efficient way to track the variance of a data stream.
3. Higher Moments - Higher moments such as skewness and kurtosis can also be estimated for data streams using similar exponentially weighted moving average techniques. These provide shortcuts to understand the shape of the distribution of a data stream without explicitly storing all data points.
4. Quantiles - Quantiles such as the median can be approximated using reservoir sampling which stores a random subset of data points that can be used to estimate quantiles. This uses limited storage but provides probabilistic guarantees on the approximation quality.

The above points cover the key techniques to estimate summary statistics and moments for data streams with limited storage. These provide useful insights into the behavior of data streams that can be used for further analytics tasks.